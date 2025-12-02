# Change logs

## Dec 2

### FF OS 0.15.0 — OTA Firmware Upgrade Support

**OTA Firmware Components**

System components like BlueZ now update over the air. Future firmware releases install normally without requiring a manual reflash.

**Bluetooth Connection Recovery**

Fixed a rare handshake failure that could break communication between the mobile app and your FF1 while artwork continued to play. Connection recovery is now reliable.

**Manual Reflash Required**

This release needs a manual reflash ([flashing guide](https://docs.feralfile.com/ff1/#step-3-install-or-update-the-os)). OTA resumes for future releases.

### Feral File Mobile App 0.66.8 — Interface Refinements

**Smoother Navigation**

Animations, transitions, and visuals have been updated for a more consistent experience.

**Optional Explore Bar**

The Explore bar is now hidden by default. Enable it under **Preferences → Settings** if you want quick access to search and discovery tools.

**Clearer Bluetooth Pairing**

Pairing and reconnecting now show clearer progress states and error messages, making setup more transparent.

---

## Nov 25

### FF OS 0.14.0 — Bluetooth Connection Improvements

**More Reliable Pairing**

We've fixed pairing failures and dropped sessions that required multiple reconnect attempts. Connections should now work reliably from the first attempt. If you still encounter issues, let us know through in-app support.

### Mobile App 0.65.0 — Major UI Refresh

**Redesigned From the Ground Up**

New navigation patterns, refined typography, updated color palette, and streamlined flows throughout. This is the first phase of the redesign, with more polish coming in future releases.

---

## Nov 11

### FF OS 0.13.0 — Vulkan Rendering & iOS Bluetooth

**Vulkan Rendering for AMD Devices**

Artworks now play correctly on AMD-based FF1 units. This update activates the Vulkan graphics pipeline on AMD hardware, fixing visual glitches and video playback issues.

**iOS Bluetooth Optimization**

Pairing with iOS devices is smoother and faster. Connection stability and command response have both improved.

**Manual Reflash Required**

This release needs a manual reflash ([flashing guide](https://docs.feralfile.com/ff1/#step-3-install-or-update-the-os)).

### Mobile App 0.64.0 — Rebuilt Art Indexer

**Faster, More Accurate Collections**

Your collection data is now accurate and near-instant. The new indexer rewrites how artworks are tracked and updated:

- Collections sort by token acquisition time
- Wallet transfers appear within seconds
- Art Blocks metadata pulled directly from source for greater accuracy
- Reliable thumbnails through redundant IPFS gateways

**Objkt Playlists Return Soon**

Now that the indexer is stable, Objkt playlists re-enable later this week using the same new data pipeline.

**Indexer Stability Note**

This is a complete rewrite of the indexing system. If you see missing metadata or broken thumbnails, please report them through in-app support.

---

## Nov 4

### FF OS 0.12.0 — Enhanced Observability

**Real-Time Performance Metrics**

Your FF1 now reports performance and stability metrics in real time. This deeper visibility helps us spot regressions quickly and focus fixes where they matter most.

**OTA Compatibility Guard**

If your FF1 encounters a version gap that prevents a direct upgrade, it now guides you with clear instructions—usually a one-time manual flash. This keeps devices from getting stuck mid-update.

### Mobile App 0.63.4 — Launch Screen Fix

**App Launch Fixed**

Resolved an issue where the app could freeze during its first launch. If the problem persists, contact us through in-app support.

---

## Oct 28

### FF OS 0.11.0 — Security Hardening & Bug Fixes

**OTA Security Hardening**

Your FF1 now cryptographically verifies every OTA update before installation. No payload can be altered or tampered with in transit.

**Automated Error Reporting**

Crash logs and runtime exceptions are captured and sent automatically, helping us find and fix rare bugs faster.

**Objkt Playback Fixed**

Resolved a playback issue affecting certain Objkt artworks. All supported Objkt works now play normally through DP-1 playlists.

**Manual Reflash Required**

This release needs a manual reflash ([flashing guide](https://docs.feralfile.com/ff1/#step-3-install-or-update-the-os)). OTA is not supported for 0.10.0 → 0.11.0. OTA resumes for future releases.

### Mobile App — Content Update

**Objkt Playlists Temporarily Hidden**

We've paused visibility for most Objkt playlists in the mobile app while rebuilding the indexing pipeline. Two selective playlists remain available for demo purposes. Objkt artworks play normally on your FF1, but the mobile app couldn't load thumbnails or some artworks reliably. The feature returns once the new indexer is stable.

---

## Oct 21

### FF OS 0.10.0 — Prompt-to-Playlist & Security

**Prompt-to-Playlist Tool**

We've published [ff1-cli](https://github.com/feral-file/ff1-cli), an open-source command-line tool that turns prompts into DP-1 playlists. Type a phrase, generate a playlist, and play it on your FF1—no web UI required. See the [ff1-cli documentation](https://docs.feralfile.com/api-reference/cli/).

**OTA Security Update**

Improved verification in the OTA update process for better reliability, file integrity, and source authority.

**Manual Reflash Required**

This release needs a manual reflash ([flashing guide](https://docs.feralfile.com/ff1/#step-3-install-or-update-the-os)). Future updates return to over-the-air delivery.

### Mobile App 0.63.3 — Collection Sync Fixes

**Personal Collections Refresh Reliably**

Collections now refresh correctly after adding new works.

**Now Playing Thumbnails Load**

Thumbnails appear consistently in the footer bar.

**Objkt Search Works**

Search results now show up properly in the Prompt Bar.

**Plays Works Without Provenance**

Artworks missing provenance fields in DP-1 playlists now play as expected.

**Smoother Animations**

Collection views and playback flows run with less visual stutter.

---

## Oct 14

### FF OS 0.9.0 — Hardware-Backed Security

**TPM Identity**

Your FF1 now stores its DeviceKey in the TPM (Trusted Platform Module). Hardware-backed identity that can't be copied or spoofed.

**Manual Reflash Required**

This release needs a one-time manual reflash ([flashing guide](https://docs.feralfile.com/ff1/#step-3-install-or-update-the-os)). Future updates return to over-the-air delivery.

### Mobile App 0.63.1 — Objkt Playlists

**Play Objkt**

Browse and play Objkt playlists directly from the app.

---

## Oct 10

### FF OS 0.8.1 — Ownership Tracking Fixed

**Collections Sync Correctly**

Transferred artworks now disappear from playlists as ownership changes. No stale items lingering after you've sold or moved a piece.

### Mobile App 0.63.1 — Fixes for Smoother Daily Use

**Now Playing Controls Restored**

Rotate and fit/fill controls are back in the Now Playing bar.

**Duplicate Items Removed**

Fixed an issue where the same artwork appeared twice in Now Playing.

**Navigation Scrolls to Current Work**

Opening Now Playing now jumps directly to what's on screen.

**Collection Reflects Transfers**

Works you've transferred now disappear from your personal Collection properly.

---

## Sep 30

### FF OS 0.8.0 — Your Collection, Always Current

**Play Your Personal Collection**

Your FF1 now plays your personal collection as a playlist that updates as your collection changes over time.

### Mobile App 0.63.0 — Easier Control, Smarter Curation

**Factory Reset via Bluetooth**

Reset your FF1 directly from the app.

**What's Playing Next**

The Now Playing bar now shows which artwork is coming up.

**Add Your Addresses**

Add your Ethereum or Tezos addresses in the Collection tab to sync art you own.

**Search & Add with the Prompt Bar**

Use natural language in the Prompt Bar to search playlists or add addresses.

<details>
<summary>Developer Notes</summary>

- QEMU build support (see QEMU instructions)
</details>

---

## Sep 19

### FF OS 0.7.0 — More Reliable Updates, Better Monitoring

**Redesigned Updates & Resets**

OTA updates are now more robust and reliable. Factory resets restore your system to a clean snapshot more effectively.

**System Monitoring**

Your device now includes a built-in tracker to monitor system metrics.

**Cleaner Logs**

Reduced excessive Chromium logs for better performance and cleaner system output.

---

## Sep 9

### FF OS 0.6.0 — Smoother Setup, Clearer Errors

**Improved Setup Flow**

Fixed an issue where the device sometimes stayed stuck on a screen instead of returning to the QR code page.

**Better Service Monitoring**

Your device now keeps a closer eye on essential background services, showing clear error messages when something goes wrong.

**Screen Rotation Fix**

Screen rotation now works correctly in landscape and portrait.

<details>
<summary>Developer Notes</summary>

- Run FF OS in QEMU for testing without physical hardware
</details>

---

## Aug 22

### FF OS 0.5.0 — Faster Support, Quieter Alerts

**Improved Error Detection**

Upgraded how your device detects and reports errors behind the scenes.

**Focused Alerts**

Fine-tuned error alerts to focus on critical issues, reducing unnecessary notifications.

**Send Logs from the App**

Share device logs directly from the FF1 mobile app.

**Better Log Management**

Improved how your device stores and manages logs for better performance.

---

## Aug 18

### FF OS 0.4.0 — Cleaner Code, Consistent Identity

**Reorganized Open Source**

Split the original repository into two separate repos: [ffos](https://github.com/feral-file/ffos) for OS builds and [ffos-user](https://github.com/feral-file/ffos-user) for services. The original [feralfile-device](https://github.com/feral-file/feralfile-device/) repository has been archived.

**FF1 Name Finalized**

The device is now officially FF1 (formerly FFX1).