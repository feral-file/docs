# Art Computer Over-the-Air (OTA) Update

## Overview

The Art Computer implements a comprehensive OTA update system that can perform both full system image updates and incremental package updates. The system is designed to be robust, with a one-shot trial boot for new images, a factory snapshot kept on disk for recovery, and progress reporting through the device's display.

## Architecture Components

### 1. Core Components

- **`feral-controld`** — the Go device daemon ([`ffos-user`](https://github.com/feral-file/ffos-user)) that owns connectivity, command routing, and device setup. Its `otagate` package decides when an update is required, starts the updater, and narrates progress on screen.
- **Update Scripts** — Bash scripts (in the [`ffos`](https://github.com/feral-file/ffos) image) that perform the actual system updates
- **Systemd Services** — service units and timers that run the update process
- **Configuration** — JSON configuration file containing the update branch, current version, and update endpoint

### 2. Key Files

| Component | Path | Purpose |
|-----------|------|---------|
| OTA gate | `components/feral-controld/otagate/` (`ffos-user`) | Version checking, single-flight update orchestration, log tailing, on-screen progress |
| Main Updater | `feral-updater.sh` (`ffos`) | Entry point script that determines update type |
| System Update | `feral-system-update.sh` (`ffos`) | Full system image update via Btrfs snapshots |
| Service Update | `feral-service-update.sh` (`ffos`) | Package-only updates via pacman |
| Configuration | `/home/feralfile/ff1-config.json` | Update branch, current version, and update endpoint (read-only for the daemons; only the updater scripts write it) |

## Update Flow

### 1. Update Detection

The update process can be triggered four ways. All of them run through the same single-flight gate in `feral-controld`: concurrent callers join the one in-flight update rather than starting a second one.

#### A. Boot-time check (claimed devices)
When a device that is already paired boots and reaches the internet within 30 minutes of booting (wide on purpose: after a site-wide power cut the network often comes back minutes after the device), `feral-controld` runs a *required* version check. If the fleet's minimum version is above the running build, it starts the update immediately instead of waiting for the nightly timer. A failed version check (typically DNS still converging after a power restore) is retried on a bounded backoff (up to 8 attempts, about 20 minutes); if it never succeeds, the nightly timer is the fallback. A daemon restart mid-exhibition does not trigger this check — only a real boot does.

#### B. Pre-claim gate (during setup)
After a device joins Wi-Fi through the setup hotspot (or boots online but unclaimed), `feral-controld` runs the same *required* check **before** it shows the pairing QR code. If an update is needed, the screen switches to the update progress view and the QR code is withheld until the device has rebooted on the new version. A device cannot be paired while it is below the minimum version.

#### C. Scheduled automatic updates
A system timer (`feral-updater@03:00.timer`) runs the updater daily at 03:00 local time. This is the silent path: it runs unattended without user interaction and applies any available image or package update. A second timer, `feral-recovery-update@5:30.timer`, runs the recovery updater script (`feral-recovery-update.sh`) at 05:30 as a further safety net.

#### D. User-triggered update
The `updateToLatestVersion` command (from the app over the relayer, or over the LAN hub) runs an *available* check — update to any newer version, not just a mandatory one. The command is acknowledged immediately; a successful update ends in a reboot, so the result is visible only through the on-screen narration and the version reported after the reboot.

### 2. Version Comparison Logic

The device fetches the version manifest for its branch from the update endpoint (`{endpoint}/api/latest/{branch}`, read from `ff1-config.json`). The manifest carries:

| Field | Meaning |
|-------|---------|
| `latest_version` | The newest build on the branch |
| `min_runtime_version` | The floor below which a device **must** update before it may pair or keep running normally |
| `min_upgradeable_version` (optional) | The floor below which a device is too old to update itself over the air and has to be reflashed from USB |
| `flashing_guide` (optional) | A link to the reflashing instructions for that case |

Two check modes exist:

- **Required** (boot-time and pre-claim checks): update only if the current device version is below `min_runtime_version`. This enforces mandatory updates when devices fall below the floor, ensuring security and compatibility requirements are met.
- **Available** (user-triggered): update if `latest_version` is newer than the current one.

A device below `min_upgradeable_version` is reported as too old to auto-upgrade; the fix is a [USB reinstall](../index.md#step-3-advanced-reinstall-ff-os-from-usb).

The version check itself is retried up to 3 times with a 2-second wait and a 10-second per-request cap, so an unstable connection fails fast rather than hanging the setup flow.

### 3. Update Process Orchestration

#### 3.1 Interactive Updates (controld-triggered)

When an update is required during an interactive flow (boot, setup, or a user command), `feral-controld` performs several coordinated actions:

1. **Spawns updater** — starts a transient systemd unit (`feral-updater-run@<id>.service`) with a unique identifier to handle the actual update process. `feral-watchdog` is paused for the duration so a slow update is not mistaken for a hang.
2. **Tails progress logs** — continuously monitors `/var/log/updaterd.log` for lines tagged with this run's id
3. **Shows update UI** — on the first progress line, pushes the `updating` state to the on-screen setup overlay (via the player's `setupDisplay` CDP contract) so the user sees progress
4. **Updates display** — parses progress percentages and status messages and repaints the overlay in real time

The unique random identifier per run distinguishes log messages from concurrent or overlapping update attempts. Spawning the updater is itself retried up to 3 times with a short backoff; if every attempt fails, the gate records a failure and the overlay reports it (during setup, as a failed step with a retry path; on a paired device, by hiding the stuck progress view).

#### 3.2 Scheduled Automatic Updates (03:00)

For the scheduled automatic updates, the process operates differently:

1. **Timer activation** — the systemd timer triggers at the configured time
2. **Silent operation** — updates run without any display changes since the device may be displaying artwork
3. **Background processing** — the same update logic executes but logs only to files without UI updates
4. **Service restart** — for package updates, affected services are restarted automatically
5. **System reboot** — for full system updates, the device reboots automatically to apply changes
6. **Resume operation** — after updates complete, the device returns to normal artwork display

The automatic updates are designed to be completely transparent to users, with the device appearing to simply restart if a full system update was applied.

### 4. Update Decision Tree

The main update script determines what type of update to perform by comparing the current device version against the latest available version from the remote API:

If the versions differ, it executes a full system image update. If the image version is current, it instead checks for and applies any available package updates to individual software components. This two-tier approach allows for both major system changes and minor incremental updates.

## Update Types

### 1. Full System Update (`feral-system-update.sh`)

For major system changes, the device performs a complete system image update:

#### Process Flow:
1. **Create Btrfs Snapshot** — prepare a candidate subvolume for the new system
2. **Download New Image** — fetch compressed system image with progress tracking
3. **Extract and Mount** — extract ISO and mount SquashFS filesystem
4. **Selective Rsync** — sync new files while preserving user data and configs
5. **Update Bootloader** — install new kernel, initramfs, and boot entries
6. **One-Shot Candidate Boot** — arm a single trial boot of the new system (`bootctl set-oneshot`); if its kernel fails to boot, the next power cycle lands back on the previous system automatically
7. **Reboot** — restart into the candidate to apply changes

#### Key Features:
- **Progress Tracking** — download progress with speed calculation and real-time updates
- **Selective Sync** — preserves user data, configurations, and sensitive files
- **One-Shot Candidate Boot** — the new system gets exactly one trial boot before it is promoted; the Btrfs default subvolume is only switched after that boot succeeds
- **Atomic Updates** — uses Btrfs snapshots to ensure system consistency

#### Critical Exclusions:
The sync process carefully excludes system directories, temporary files, user configurations, network settings, SSH keys, and device-specific data to preserve the device's identity and user customizations while updating the core system.

#### Boot Configuration:
The system maintains two permanent boot entries, plus a temporary one during an update:
- **arch.conf** — normal boot
- **factory_reset.conf** — factory reset (restores the factory system)
- **arch-candidate.conf** — one-shot trial boot of a freshly downloaded update; removed once the update is promoted

There is no previous-version rollback entry: once an update's trial boot succeeds, the new system is promoted and the previous version is deleted. Recovery from a bad update is a [factory reset](../factory-reset.md).

### 2. Package Update

For minor updates, only specific packages are updated using the system package manager. The process updates only Feral File specific software components and restarts the affected services if any packages were actually updated. If no updates are available, the process completes without making any changes.

Note that the device daemons ship as packages, but the systemd unit files and user-session scripts ship only with a full image — so a change that touches both is always released as a full image update.

## Configuration Structure

The device uses a JSON configuration file (`/home/feralfile/ff1-config.json`) that contains the update branch, the current version, and the endpoint for fetching updates. The daemons read it; only the updater scripts write it. The same file is the source of the `branch` and `version` shown in the pairing QR code and on the LAN status API, so those can never disagree with what the updater sees.

## Progress Reporting

### Log Format
All update processes use structured logging with unique identifiers, timestamps, log levels, and structured message fields to enable parsing and monitoring.

### Progress Tracking
`feral-controld` continuously monitors these structured logs, extracts progress percentages and status messages, and forwards this information to the on-screen overlay in real time. Transient and permanent failures are told apart by matching the updater's messages, so a bad signature fails fast while a dropped download is retried.

## Error Handling and Recovery

### 1. Recovery
- **One-Shot Candidate Boot** — a downloaded update gets exactly one trial boot; if its kernel fails to start, the next power cycle automatically returns to the previous system and the failed update is discarded
- **Factory Reset** — the recovery path for a system that boots but misbehaves: from the app, or with the keyboard-free [power-cord gesture](../factory-reset.md) when the app cannot reach the device
- There is no automatic rollback to the previous version after an update has been promoted

### 2. Error Propagation
- **On-screen narration** — during setup, a failed update is shown on the display with a retry; the pairing QR code stays withheld until an update succeeds
- **Structured Logging** — all errors logged with context and unique IDs
- **Bounded retries** — version checks and updater launches are each retried a fixed number of times, then the gate gives up for that round and retries on a backoff

### 3. Network Resilience
- **Connection Checking** — verifies internet connectivity before starting
- **Bounded retries** — a dropped download is retried (up to three full attempts per round) before the round is given up
- **Timeout Handling** — appropriate timeouts for different operations

## Security Features

### 1. Source of truth
- **Configured endpoint** — the version manifest and update artifacts are fetched only from the distribution endpoint configured in `ff1-config.json`, which is read-only for the device daemons

### 2. Integrity
- **Signed Packages** — pacman packages are cryptographically signed; full images are signature-verified before installation
- **Atomic Operations** — Btrfs snapshots ensure consistency
- **Recovery Path** — the factory system is kept on disk and reachable without a keyboard, so a bad state is recoverable in the field

## Systemd Integration

### Services
- **`feral-updater-run@.service`** — transient, run-specific update unit started by `feral-controld` for interactive updates (one instance per run id)
- **`feral-updater@.timer`** — scheduled update check; the device enables `feral-updater@03:00.timer` at startup
- **`feral-recovery-update@.timer`** — second scheduled safety net; the device enables `feral-recovery-update@5:30.timer` at startup

### Logging
All update processes log to `/var/log/updaterd.log` with structured format for monitoring and debugging.

## Setup Integration

Setup is done over the device's own Wi-Fi hotspot and a captive portal (there is no Bluetooth path — see [Life Cycle](./life-cycle.md)). Once the device joins a network and reaches the internet, the pre-claim gate runs **before** the pairing QR code is shown:

- **No update needed** → the QR code is painted and pairing continues.
- **Update needed** → the screen shows update progress; the device reboots on the new version and re-enters setup from a cold boot, where the QR code then appears.
- **Version check failed** → nothing changes on screen (it stays on the "finalizing" step); the device retries quickly on a backoff.
- **Update failed** → the screen reports the failure; the device retries more slowly. Either way the QR code is not shown until an update succeeds.

This prevents pairing while an update is in progress and gives the user clear feedback on the display itself.

## Summary

The Art Computer OTA system provides:
- **Dual Update Modes** — full system images for major changes, packages for minor updates
- **Four triggers** — boot-time check, pre-claim gate, nightly timer, and an explicit app/LAN command, all through one single-flight gate
- **Recovery** — atomic snapshot-based updates, a one-shot trial boot for new images, and a keyboard-free [factory reset](../factory-reset.md) as the field recovery path
- **Progress Visibility** — real-time progress reporting through the device display
- **Network Resilience** — handles connection issues gracefully
- **Security** — a single configured distribution endpoint, signature-verified images, and signed packages
- **Integration** — the pairing QR code is withheld until the device is on a supported version

The system is designed to minimize the risk of bricking devices while providing comprehensive update capabilities for both the underlying system and individual software components.
