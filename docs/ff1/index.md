# Getting Started with FF1

**FF1 is an art computer by Feral File.** It plays digital art on any screen. Plug it into a TV, projector, or monitor, scan a QR code, and your collection of art appears.

FF1 updates itself automatically over the air (OTA). For resets, troubleshooting, or experiments, you can also reinstall the OS manually. This guide covers the basics: what you need, plugging in FF1, pairing, and (optionally) reinstalling FF OS.

---

## Before You Start

Make sure you have:

- An **FF1** unit and its power adapter
- An **HDMI cable** and a TV / monitor / projector
- A **phone** (iOS or Android) with internet access
- Your **Wi-Fi network name and password**

---

## Step 1: Plug In Your FF1

1. Connect **HDMI** from FF1 to your screen.
2. Plug in the **power adapter** to FF1 and to the wall.
3. Turn on your TV/monitor and choose the correct **HDMI input**.
4. Turn FF1 on (just plug it in, it auto-powers).

On a normal first boot (or after a good install), FF1 will show a **pairing screen with a QR code**.

---

## Step 2: Pair (Scan the QR Code)

Pairing is done by scanning the QR code on the screen with your phone’s **camera app**.

1. Open your phone’s **Camera**.
2. Point it at the **QR code** on your TV.
3. Tap the link that appears.

What happens next:

- If you already have the **Feral File app**, it will open and continue pairing.
- If you don’t have the app yet, the link will take you to the App Store / Play Store. Install the app, then:
  - tap **Open** from the store page, or
  - re-scan the QR code if pairing doesn’t resume automatically.

### “You’re done” success state

You’re fully set up when:

- Your TV shows **artwork or a playlist UI** instead of just the QR code, and  
- The app shows that it’s **connected to your FF1** (you can select and control playlists).

---

## Official Apps (Optional Pre-Install)

You do **not** need to install the app ahead of time — scanning the QR code will guide you through it if needed.

- **Android:** <https://play.google.com/store/apps/details?id=com.feralfile.app>  
- **iPhone:** <https://apps.apple.com/us/app/feral-file-controller/id6755812386>

---

## Step 3 (Advanced): Reinstall FF OS from USB

Most people never need to do this. FF1 updates itself automatically when it’s online.

Use this section only if:

- The device is **stuck or misconfigured**, and normal restarts don’t help.
- You’re testing a new FF OS image.
- You need to recover a device for shipping / support.

### Create a bootable USB

1. Download **BalenaEtcher**: <https://balena.io/etcher>
2. Download the latest system image on branch `release`: <https://ff1.feral-file.workers.dev>
3. Use Etcher to flash the image onto a USB drive.

### Install (fully automatic)

1. **Power off FF1** (unplug the power cable).
2. Plug the **USB installer** into FF1.
3. Plug the **power cable back in**. FF1 will boot from the USB automatically.
4. **Wait until FF1 shuts itself down.** (The screen may go blank during install.)
5. Remove the USB.
6. **Power-cycle FF1** (unplug power, then plug it back in).

After booting, you should see the **pairing QR code** again. Go back to **Step 2** to pair.

---

## Troubleshooting

- **I don’t see a QR code.**  
  Confirm the TV is on the correct HDMI input. Try a different HDMI cable/port. Power-cycle FF1.

- **My phone camera doesn’t show a link.**  
  Try better lighting, hold the camera steady, and make sure you’re close enough for focus. Some phones require enabling QR scanning in Camera settings.

- **It sent me to the store, but pairing didn’t resume.**  
  Open the app, then **scan the QR code again** with your phone camera.

- **Art isn’t loading.**  
  Check your internet connection and try again.

Still stuck? Email **[support@feralfile.com](mailto:support@feralfile.com)**.

---

## Next Steps

- Explore [How It Works](./how-it-works/life-cycle.md).
- Build playlists and start living with art.
