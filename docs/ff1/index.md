# Getting Started with FF1

**FF1 is an art computer by Feral File.** It plays digital art on any screen. Plug it into a TV, projector, or monitor, scan a QR code, and your collection of art appears.

FF1 updates itself automatically over the air (OTA). For resets, troubleshooting, or experiments, you can also reinstall the OS manually. This guide covers the basics: installing the app, setting up hardware, updating the OS, and playing your first playlist.

---

## The FF1 Stack

| Component          | What it does                                | Why it matters                                            |
| ------------------ | ------------------------------------------- | --------------------------------------------------------- |
| **FF1 Hardware**   | Dedicated device for playing art on screens | Frees art from phones or laptops; works in shared spaces. |
| **FF OS** (open)   | Operating system that runs DP-1             | Open source—can be reflashed or customized.               |
| **Feral File App** | Mobile controller for pairing and playlists | Lets you pair your device and manage what plays.          |
| **DP-1 Protocol**  | Open format for art playlists               | Anyone can publish and share art feeds.                   |

---

## Step 1: Install the Feral File App

The app is your FF1’s remote control. Use it to pair, manage playlists, and adjust settings.

* [Android](https://play.google.com/apps/testing/com.bitmark.autonomy_client)
* [iPhone](https://testflight.apple.com/join/SBt1LsfR)

Once installed, the app updates like any other.

---

## Step 2: Set Up Your FF1

1. **Connect power and HDMI.** Use the adapter and connect to your screen.
2. **Turn it on.** If your unit is pre-flashed, you’ll see a pairing prompt right away.

Need a fresh install? Jump to Step 3.

---

## Step 3: Install or Update the OS

FF1 normally updates itself when online. But you can also re-install manually if you’re troubleshooting or testing.

### When to reinstall

* During alpha testing (major updates).
* If the device becomes unresponsive or slow.
* If you want to experiment with your own build.

### Create a bootable USB

1. Download [BalenaEtcher](https://balena.io/etcher).
2. Download the latest system image on branch `release`: [ff1.feral-file.workers.dev](https://ff1.feral-file.workers.dev).
3. Use Etcher to flash the `.zip` onto a USB drive.

### Install

1. Plug the USB into FF1.
2. Power on and press **F7** repeatedly until the boot menu appears.
3. Select the USB drive.
4. Follow the on-screen instructions. The device will shut down when finished.
5. Remove the USB and power on again. You’ll see the pairing screen.

---

## Troubleshooting

* **App won’t pair?** Check Wi-Fi and Bluetooth, restart both devices.
* **Flash errors?** Confirm the right USB target in Etcher; try another drive.
* **Art not loading?** Check internet connection and reload playlists.
* **OTA update not working?** Reinstall manually as above.

Still stuck? Email **[FF1alpha@groups.feralfile.com](mailto:FF1alpha@groups.feralfile.com)**.

---

## Next Steps

* Explore [How It Works](./how-it-works/life-cycle.md).
* Build custom playlists.
* Contribute code or ideas on GitHub.

---
