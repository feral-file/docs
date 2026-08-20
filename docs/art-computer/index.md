# Getting Started with the Art Computer

**The Art Computer is Feral File's instrument for digital art.** It plays digital art on any screen. Plug it into a TV, projector, or monitor, put it on your Wi-Fi from your phone, pair it with the app, and your collection of art appears.

The Art Computer updates itself automatically over the air (OTA). For resets, troubleshooting, or experiments, you can also reinstall the OS manually. This guide covers the basics: what you need, plugging it in, Wi-Fi setup, pairing, and (optionally) reinstalling FF OS.

---

## Before You Start

Make sure you have:

- An **Art Computer** and its power adapter
- An **HDMI cable** and a TV / monitor / projector
- A **phone** (iOS or Android) with internet access
- Your **Wi-Fi network name and password** — or an **Ethernet cable** to a network with internet (see [Network Requirements](./network-requirements.md) for how to reach the port)

Setting up on a managed network (museum, office, campus)? See [Network Requirements](./network-requirements.md) for the firewall and Wi-Fi policies your IT team will ask about.

---

## Step 1: Plug In Your Art Computer

1. Connect **HDMI** from the Art Computer to your screen.
2. Plug in the **power adapter** to the Art Computer and to the wall.
3. Turn on your TV/monitor and choose the correct **HDMI input**.
4. Turn the Art Computer on (just plug it in, it auto-powers).

On a normal first boot (or after a good install), the Art Computer shows a **Wi-Fi setup screen** — or, if it is already on a network with internet (Ethernet, or a Wi-Fi it already knows), it goes straight to the **pairing screen**.

---

## Step 2: Connect and Pair

### Connect to Wi-Fi

The Art Computer has no keyboard, so you give it your Wi-Fi password from your phone, through a small hotspot the Art Computer broadcasts itself. Skip this step if you plugged in an Ethernet cable.

1. On the TV you will see a network name like **`FF1-XXXXXXXX`**, a numeric password, and a QR code.
2. On your phone, **join that network** — scan the QR code with your camera, or open Wi-Fi settings and join it by hand with the password on screen. (Your phone has no internet while it is on this network; that is expected.)
3. A setup page opens automatically. If it does not, open your browser and go to **`http://ff1.config`**.
4. **Pick your Wi-Fi network** from the list and enter its password. Hidden network? Type its name in the manual field.
5. Watch the TV. The setup hotspot switches off while the Art Computer joins your network. If the password was wrong, the hotspot comes back — join it again and retry.

Once the Art Computer is online it checks for a required update (it may install one and restart — leave it powered), then shows the **pairing screen**.

### Pair with the app

The pairing screen gives you two ways in; either works.

**Let the app find it (same Wi-Fi).** Open the **Feral File app** on a phone connected to the same Wi-Fi as the Art Computer. The app discovers the device on the local network and offers to pair it. Confirm, and you are done.

**Or scan the QR code.** Open your phone’s **Camera**, point it at the **QR code** on the TV, and tap the link that appears.

- If you already have the **Feral File app**, it opens and continues pairing.
- If you don’t have the app yet, the link takes you to the App Store / Play Store. Install the app, then tap **Open** from the store page, or re-scan the QR code if pairing doesn’t resume automatically.

### “You’re done” success state

You’re fully set up when:

- Your TV shows **artwork or a playlist UI** instead of the pairing screen, and  
- The app shows that it’s **connected to your Art Computer** (you can select and control playlists).

---

## Official Apps (Optional Pre-Install)

You do **not** need to install the app ahead of time — scanning the QR code will guide you through it if needed.

- **Android:** <https://play.google.com/store/apps/details?id=com.feralfile.app>  
- **iPhone:** <https://apps.apple.com/us/app/feral-file-controller/id6755812386>

The Feral File app is Feral File's proprietary product shell. For the open protocol and developer tooling, see the [DP-1 specification](https://github.com/display-protocol/dp1) and [ff-cli](../ff-cli/index.md).

---

## Step 3 (Advanced): Reinstall FF OS from USB

Most people never need to do this. The Art Computer updates itself automatically when it’s online.

Use this section only if:

- The device is **stuck or misconfigured**, and normal restarts don’t help.
- You’re testing a new FF OS image.
- You need to recover a device for shipping / support.

### Create a bootable USB

1. Download **BalenaEtcher**: <https://balena.io/etcher>
2. Download the latest system image on branch `release`: <https://ffos.feralfile.com>
3. Use Etcher to flash the image onto a USB drive.

### Install (fully automatic)

1. **Power off the Art Computer** (unplug the power cable).
2. Plug the **USB installer** into the Art Computer.
3. Plug the **power cable back in**. The Art Computer will boot from the USB automatically.
4. **Wait until the Art Computer shuts itself down.** (The screen may go blank during install.)
5. Remove the USB.
6. **Power-cycle the Art Computer** (unplug power, then plug it back in).

After booting, you should see the **Wi-Fi setup screen** again. Go back to **Step 2** to connect and pair.

---

## Troubleshooting

- **I don’t see a setup screen or QR code.**  
  Confirm the TV is on the correct HDMI input. Try a different HDMI cable/port. Power-cycle the Art Computer.

- **My phone can’t see the `FF1-…` network, or the setup page doesn’t open.**  
  Stay close to the Art Computer and make sure you joined the `FF1-…` network (not your home Wi-Fi). If the page does not pop up, open a browser and go to `http://ff1.config`. Some work phones are managed so they cannot join unknown networks — use another phone, or an Ethernet cable.

- **The Art Computer says it couldn’t join my Wi-Fi.**  
  Join the `FF1-…` network again and re-enter the password. Enterprise Wi-Fi that asks for a username (offices, campuses) cannot be entered here — use Ethernet, or see [Network Requirements](./network-requirements.md).

- **The app doesn’t find the Art Computer.**  
  Make sure the phone is on the same Wi-Fi as the Art Computer, then wait a few seconds. If it still does not appear, scan the QR code on the TV instead.

- **The Art Computer seems to restart over and over (boot loop).**  
  A failing HDMI cable can look exactly like a boot loop: the screen drops and re-syncs while the Art Computer itself is running fine. Swap in a known-good HDMI cable before assuming the device is faulty.

- **My phone camera doesn’t show a link.**  
  Try better lighting, hold the camera steady, and make sure you’re close enough for focus. Some phones require enabling QR scanning in Camera settings.

- **It sent me to the store, but pairing didn’t resume.**  
  Open the app, then **scan the QR code again** with your phone camera.

- **Art isn’t loading.**  
  Check your internet connection and try again. If the Art Computer has lost its Wi-Fi entirely (the password changed, or the network is gone), it brings the setup hotspot back on its own after a few minutes — repeat Step 2. If it is on Wi-Fi but you want to move it to a different network, use the app to start Wi-Fi setup again (unplug any Ethernet cable first).

- **The `FF1-…` hotspot disappeared while I was setting up.**  
  While it is waiting, the Art Computer briefly switches the hotspot off every few minutes to look for your network, then brings it back. Wait a minute and join it again — nothing is broken.

Still stuck? Email **[support@feralfile.com](mailto:support@feralfile.com)**.

---

## Next Steps

- Explore [How It Works](./how-it-works/life-cycle.md).
- Build playlists and start living with art.
