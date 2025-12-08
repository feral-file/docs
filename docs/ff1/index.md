# Getting Started with FF1

**FF1 is an art computer by Feral File.** It plays digital art on any screen. Plug it into a TV, projector, or monitor, scan a QR code, and your collection of art appears.

FF1 updates itself automatically over the air (OTA). For resets, troubleshooting, or experiments, you can also reinstall the OS manually. This guide covers the basics: what you need, installing the app, setting up hardware, (optionally) reinstalling the OS, and playing your first playlist.

---

## Before You Start

Make sure you have:

- An **FF1** unit and its power adapter
- An **HDMI cable** and a TV / monitor / projector
- A **phone** (iOS or Android) with internet access
- The **Feral File app** installed (see below)
- Your **Wi-Fi network name and password**

Once you have these, you’re ready to go.

---

## The FF1 Stack

| Component          | What it does                                | Why it matters                                            |
| ------------------ | ------------------------------------------- | --------------------------------------------------------- |
| **FF1 Hardware**   | Dedicated device for playing art on screens | Frees art from phones or laptops; works in shared spaces. |
| **FF OS** (open)   | Operating system that runs DP-1             | Open source – can be reflashed or customized.            |
| **Feral File App** | Mobile controller for pairing and playlists | Lets you pair your device and manage what plays.         |
| **DP-1 Protocol**  | Open format for art playlists               | Anyone can publish and share art feeds.                  |

---

## Step 1: Install the Feral File App

The app is your FF1’s remote control. Use it to pair, manage playlists, and adjust settings.

> These are **pre-release / test** builds, so you may need to accept TestFlight or testing terms.

- **Android** (testing link): <https://play.google.com/apps/testing/com.bitmark.autonomy_client>  
  (Use the same Google account you shared with us for testing.)
- **iPhone** (TestFlight): <https://testflight.apple.com/join/SBt1LsfR>  
  (You may need to install the TestFlight app first.)

Once installed, the Feral File app updates like any other app.

---

## Step 2: Plug In Your FF1 and Pair

### 2.1 Hook up the hardware

1. Connect **HDMI** from FF1 to your screen.
2. Plug in the **power adapter** to FF1 and to the wall.
3. Turn on your TV/monitor and choose the correct **HDMI input**.

### 2.2 What you should see

On a normal first boot (or after a good install), FF1 will:

1. Boot FF OS.
2. Show a **pairing screen with a QR code**.

If you see that QR code, the device is healthy and ready to pair.

### 2.3 Pair with your phone’s camera (recommended)

The fastest way for most people is to just use the phone’s camera app.

1. Open the **Camera** app on your phone.
2. Point it at the **QR code** on your TV.
3. Tap the notification or link that appears.

From here:

- If you already have the **Feral File app** installed, it should open and move straight into the pairing flow for this FF1.
- If you **don’t** have the app installed yet, you’ll be taken to the App Store / Play Store. Install the app, then open it — the pairing flow will resume using the same link (deferred deep link).

If this path doesn’t work on your device for any reason, you can always pair from inside the app instead.

### 2.4 Pair from inside the app (alternative path)

If the camera link doesn’t appear, or you prefer to start in the app:

1. Open the **Feral File app** on your phone.
2. Tap the **menu icon** (☰) in the corner to open the main menu.
3. Choose **“Scan QR”** or **“Add / Connect Device”** (wording may vary slightly between builds).
4. Use the in-app scanner to **scan the QR code** on your TV.
5. Follow the in-app steps to finish pairing.

This path is also how you’ll add additional FF1 devices later.

### 2.5 “You’re done” success state

You’re fully set up when:

- Your TV shows **artwork or a playlist UI** instead of just the QR code, and  
- The app shows that it’s **connected to your FF1** (you can select and control playlists).

If you’re already at this point, you **do not** need to reinstall the OS. The rest of this page is for advanced troubleshooting and testing.

---

## Step 3 (Advanced): Reinstall the OS from USB

Most people never need to do this. FF1 will keep itself updated automatically when it’s online.

Use this section only if:

- You’re doing **alpha testing** of a new build.
- The device is **stuck, unresponsive, or badly misconfigured**, and normal restarts don’t help.
- You want to **experiment with your own image** and know how to recover if something goes wrong.

If FF1 shows a QR code and plays art normally, skip this section.

### 3.1 Create a bootable USB

You’ll need a USB drive (at least 8 GB recommended). This process will erase the drive.

1. Download **BalenaEtcher**: <https://balena.io/etcher>
2. Download the latest FF1 system image on branch `release`: <https://ff1.feral-file.workers.dev>
3. Open Etcher and:
   - **Select image** → choose the file you downloaded (usually a `.zip` or `.img` file).
   - **Select target** → choose your USB drive carefully.
   - **Flash** → wait for Etcher to finish and validate.

If the flash fails, try again or use a different USB drive.

### 3.2 Install (fully automatic)

The install process is now completely hands-off. No BIOS changes or keyboard are needed once your devices are set up correctly.

1. **Power off FF1** (unplug the power cable).
2. Plug the **bootable USB drive** into a USB port on FF1.
3. Plug the **power cable back in**. FF1 will start and automatically boot from the USB.
4. **Wait until FF1 shuts itself down.**  
   - The screen may go blank or show progress messages.  
   - The install is finished when the device **turns itself off**.
5. **Unplug the USB drive.**
6. Plug the **power cable back in** again to turn FF1 on.
7. After booting, you should see the **pairing screen with a QR code**.

If you see the QR code after reinstalling, go back to **Step 2** to pair with the app.

---

## Troubleshooting

A few common issues and fixes:

- **App won’t pair?**  
  - Make sure your **phone and FF1 are on the same network** (when needed by that build).  
  - Toggle **Wi-Fi and Bluetooth** off and on.  
  - Quit and reopen the Feral File app.  
  - Power-cycle FF1 (unplug power, wait 5 seconds, plug in again).

- **No image on the screen?**  
  - Confirm the TV/monitor is on the **correct HDMI input**.  
  - Try a different HDMI cable or port.  
  - Try another screen if you have one.

- **Flash errors in Etcher?**  
  - Double-check you selected the **correct USB drive**.  
  - Try re-downloading the image.  
  - Try a different USB stick if errors persist.

- **Art not loading or playlists stuck?**  
  - Check that your network is up and not blocking outbound connections.  
  - Try reloading the playlist in the app.  
  - Restart FF1 and your router if needed.

- **OTA update seems stuck?**  
  - Wait a few minutes; some updates take time.  
  - Power-cycle FF1.  
  - If the device no longer reaches the QR screen after multiple restarts, then consider a **manual reinstall** as in Step 3.

If FF1 **shows the QR code and plays art**, your OS is healthy. In that case, focus on pairing, playlists, or network rather than reflashing.

Still stuck? Email **[FF1alpha@groups.feralfile.com](mailto:FF1alpha@groups.feralfile.com)** with a short description of what you see on the screen and what you’ve already tried.

---

## Next Steps

Once you’re paired and playing:

- Explore [How It Works](./how-it-works/life-cycle.md).  
- Build or subscribe to custom playlists.  
- Share feedback, ideas, or issues with the team.  
- (If you’re technical) check out the open-source pieces and DP-1 protocol on GitHub.

FF1 is meant to be a simple appliance for most people, but open and hackable for those who want to go deeper. Enjoy living with digital art every day.
