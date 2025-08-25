# FF1 Over-the-Air (OTA) Update

## Overview

The FF1 device implements a comprehensive OTA update system that can perform both full system image updates and incremental package updates. The system is designed to be robust, with automatic rollback capabilities and progress reporting through the device's display.

## Architecture Components

### 1. Core Components

- **`feral-setupd`** - Rust daemon that handles device pairing, Wi-Fi setup, and OTA update orchestration
- **Update Scripts** - Bash scripts that perform the actual system updates
- **Systemd Services** - Service units that manage the update process
- **Configuration** - JSON configuration file containing update endpoints and credentials

### 2. Key Files

| Component | Path | Purpose |
|-----------|------|---------|
| Setup Daemon (setupd) | `components/feral-setupd/` | Rust daemon handling orchestration, version checking, BLE communication |
| Main Updater | `scripts/feral-updater.sh` | Entry point script that determines update type |
| System Update | `scripts/feral-system-update.sh` | Full system image update via Btrfs snapshots |
| Service Update | `scripts/feral-service-update.sh` | Package-only updates via pacman |
| Configuration | `/home/feralfile/ff1-config.json` | Update endpoint and authentication config |

## Update Flow

### 1. Update Detection

The update process can be triggered in three ways:

#### A. Automatic Detection (setupd main flow)
When the device boots and has internet connectivity, setupd automatically checks for updates before proceeding with normal operation. If an update is required, it immediately triggers the update process instead of showing the normal display interface.

#### B. BLE-Triggered Update (during Wi-Fi setup)
When a user connects the device to Wi-Fi through the mobile app setup process, setupd checks for updates after establishing internet connectivity. If an update is needed, it starts the update process and returns a specific error code to the mobile app indicating the device is updating.

#### C. Scheduled Automatic Updates
The device runs a systemd timer that automatically checks for and applies updates at a configured time (typically 3:00 AM local time, but configurable). This scheduled update runs daily and includes a randomized delay of up to 2 hours to distribute server load. The timer uses the same update logic as the other triggers but runs unattended without user interaction.

### 2. Version Comparison Logic

The system fetches version information from a remote API endpoint using authenticated credentials. Rather than simply comparing against the latest available version, it compares the current device version against a minimum supported version threshold. This design allows the system to enforce mandatory updates when devices fall below the minimum supported version, ensuring security and compatibility requirements are met.

### 3. Update Process Orchestration

#### 3.1 Interactive Updates (setupd-triggered)

When an update is required during interactive flows (boot or Wi-Fi setup), setupd performs several coordinated actions:

1. **Shows update UI** - Immediately switches the display to show update progress screen to inform the user
2. **Spawns updater** - Launches a background systemd service with a unique identifier to handle the actual update process
3. **Tails progress logs** - Continuously monitors the update log file for progress updates and error messages
4. **Updates display** - Processes log messages and updates the display with progress percentages and status messages in real-time

The system generates a unique random identifier for each update process to distinguish log messages from concurrent or overlapping update attempts.

#### 3.2 Scheduled Automatic Updates (3:00 AM)

For the scheduled automatic updates that run at 3:00 AM daily, the process operates differently:

1. **Timer activation** - The systemd timer triggers at the configured time with a randomized delay
2. **Silent operation** - Updates run without any display changes since the device may be displaying artwork
3. **Background processing** - The same update logic executes but logs only to files without UI updates
4. **Service restart** - For package updates, affected services are restarted automatically
5. **System reboot** - For full system updates, the device reboots automatically to apply changes
6. **Resume operation** - After updates complete, the device returns to normal artwork display

The automatic updates are designed to be completely transparent to users, with the device appearing to simply restart if a full system update was applied.

### 4. Update Decision Tree

The main update script determines what type of update to perform by comparing the current device version against the latest available version from the remote API:

If the versions differ, it executes a full system image update. If the image version is current, it instead checks for and applies any available package updates to individual software components. This two-tier approach allows for both major system changes and minor incremental updates.

## Update Types

### 1. Full System Update (`feral-system-update.sh`)

For major system changes, the device performs a complete system image update:

#### Process Flow:
1. **Create Btrfs Snapshot** - Backup current system state for rollback
2. **Download New Image** - Fetch compressed system image with progress tracking
3. **Extract and Mount** - Extract ISO and mount SquashFS filesystem
4. **Selective Rsync** - Sync new files while preserving user data and configs
5. **Update Bootloader** - Install new kernel, initramfs, and boot entries
6. **Configure Rollback** - Set up boot entries for factory reset and OTA rollback
7. **Reboot** - Restart to apply changes

#### Key Features:
- **Progress Tracking** - Download progress with speed calculation and real-time updates
- **Selective Sync** - Preserves user data, configurations, and sensitive files
- **Rollback Support** - Creates multiple boot entries for different rollback scenarios
- **Atomic Updates** - Uses Btrfs snapshots to ensure system consistency

#### Critical Exclusions:
The sync process carefully excludes system directories, temporary files, user configurations, network settings, SSH keys, and device-specific data to preserve the device's identity and user customizations while updating the core system.

#### Boot Configuration:
The system creates three boot entries:
- **arch.conf** - Normal boot
- **factory_reset.conf** - Factory reset rollback
- **ota_prev.conf** - Previous version rollback

### 2. Package Update

For minor updates, only specific packages are updated using the system package manager. The process updates only Feral File specific software components and restarts the affected services if any packages were actually updated. If no updates are available, the process completes without making any changes.

## Configuration Structure

The device uses a JSON configuration file that contains the update branch, current version, authentication credentials for the distribution server, and the base endpoint URL for fetching updates.

## Progress Reporting

### Log Format
All update processes use structured logging with unique identifiers, timestamps, log levels, and structured message fields to enable parsing and monitoring.

### Progress Tracking
The setupd daemon continuously monitors these structured logs using regular expressions to extract progress percentages and status messages, then forwards this information to update the device display in real-time.

## Error Handling and Recovery

### 1. Automatic Rollback
- **Btrfs Snapshots** - System can roll back to previous working state
- **Boot Menu Options** - Multiple rollback scenarios available at boot
- **Factory Reset** - Complete system reset option

### 2. Error Propagation
- **BLE Error Codes** - Specific error codes sent to mobile app during setup
- **Structured Logging** - All errors logged with context and unique IDs
- **Progress Interruption** - Update can be cancelled or fails gracefully

### 3. Network Resilience
- **Connection Checking** - Verifies internet connectivity before starting
- **Resume Capability** - Can handle network interruptions during downloads
- **Timeout Handling** - Appropriate timeouts for different operations

## Security Features

### 1. Authentication
- **Basic Auth** - Username/password for update endpoint access
- **Secure Endpoints** - Updates fetched from authenticated distribution server

### 2. Integrity
- **Signed Packages** - Pacman packages are cryptographically signed
- **Atomic Operations** - Btrfs snapshots ensure consistency
- **Rollback Protection** - Multiple recovery options prevent bricking

## Systemd Integration

### Services
- **`feral-updater@.service`** - Template service for update instances
- **`feral-updater-run@.service`** - Run-specific update service with unique ID
- **`feral-updater@.timer`** - Periodic update checking (weekly)

### Logging
All update processes log to `/home/feralfile/.logs/updaterd.log` with structured format for monitoring and debugging.

## BLE Integration

During initial setup, the device can trigger updates when connecting to Wi-Fi:

### Error Codes
- `BLE_ERR_CODE_DEVICE_UPDATING = 5` - Device is currently updating
- `BLE_ERR_CODE_VERSION_CHECK_FAILED = 6` - Failed to check for updates

This prevents setup completion while an update is in progress and provides clear feedback to the mobile app.

## Summary

The FF1 OTA system provides:
- **Dual Update Modes** - Full system images for major changes, packages for minor updates
- **Robust Recovery** - Multiple rollback options and atomic operations
- **Progress Visibility** - Real-time progress reporting through device display
- **Network Resilience** - Handles connection issues gracefully
- **Security** - Authenticated downloads and signed packages
- **Integration** - Seamless integration with setup process and mobile app

The system is designed to minimize the risk of bricking devices while providing comprehensive update capabilities for both the underlying system and individual software components.
