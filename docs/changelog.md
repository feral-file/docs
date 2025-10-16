# Change logs

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