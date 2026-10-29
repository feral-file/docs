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
2. Scan the QR code with your phone's camera, then follow your phone's prompt to connect. Scanning proposes the connection; it may not join automatically.
3. If Wi-Fi settings opens, tap the **`FF1-XXXXXXXX` setup network**. Prompts vary by phone and may say **Join**, **Connect**, or **Sign in to network**. You can also join by hand with the numeric password on the TV. If your phone warns that this network has no internet, choose the option that keeps it connected; the warning is expected.
4. A setup page opens automatically. If it does not, stay connected to the `FF1-…` network, open your browser, and enter the numeric setup-page address shown on the TV. If the address still does not open, temporarily turn off mobile data and any VPN, then try it again.
5. **Pick the Wi-Fi network your Art Computer should use** and enter that network's password. The numeric password on the TV is only for the temporary `FF1-…` setup network. Hidden network? Type its name in the manual field.
6. Watch the TV. The setup hotspot switches off while the Art Computer joins your network. If the password was wrong, the hotspot comes back — join it again and retry.

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

1. Download the latest FF OS image: <https://ffos.feralfile.com/download/release/latest.iso>. Every build, by branch and version, is listed at <https://ffos.feralfile.com>.
2. Download **BalenaEtcher**: <https://balena.io/etcher>
3. Use Etcher to flash the image onto a USB drive.

**With a coding agent**, paste `Read https://docs.feralfile.com and reinstall FF OS on my Art Computer.` and the agent does this half for you. What it runs: `https://ffos.feralfile.com/api/latest/release` returns the version, `image_url` and `image_signature_url` as JSON. It downloads both, then checks the image against the FF1 release public key, the same check the Art Computer runs before an update:

```bash
curl -fsSLO https://raw.githubusercontent.com/feral-file/ffos/release/archiso-ff1/airootfs/root/.ff1-release-public-key.pem
openssl dgst -sha256 -verify .ff1-release-public-key.pem -signature <image>.iso.sig <image>.iso
```

Then it asks you which disk is the USB drive before writing anything (a wrong disk erases your computer), writes the image to that disk, and hands you the steps below. Those stay by hand.

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
  Stay close to the Art Computer. After scanning, follow your phone's prompt to connect; if it opens Wi-Fi settings, tap the `FF1-…` setup network. Prompts vary and may say **Join**, **Connect**, or **Sign in to network**. If your phone warns that the network has no internet, choose the option that keeps it connected. If the page still does not open, enter the numeric setup-page address shown on the TV. If your phone still cannot reach it, temporarily turn off mobile data and any VPN, then try the address again. Some work phones are managed so they cannot join unknown networks — use another phone, or an Ethernet cable.

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
