# Reinstall FF OS

The Art Computer updates itself when it is online. Reinstall FF OS from a USB drive when the Art Computer is stuck and a restart does not help, or after you replace its SSD.

## Create a bootable USB

1. Download the latest system image on branch `release`: <https://ffos.feralfile.com>
2. Download **BalenaEtcher**: <https://balena.io/etcher>
3. Use Etcher to flash the image onto a USB drive.

**With a coding agent**, paste `Read https://docs.feralfile.com and reinstall FF OS on my Art Computer.` and the agent does this half for you. What it runs: `https://ffos.feralfile.com/api/latest/release` redirects (follow it with `curl -L`) to JSON with `latest_version` and `image_url`, a path on the same host; the image's signature is at the same path with `.sig` appended. It downloads both, then checks the image against the FF1 release public key, the same check the Art Computer runs before an update:

```bash
curl -fsSLO https://raw.githubusercontent.com/feral-file/ffos/release/archiso-ff1/airootfs/root/.ff1-release-public-key.pem
openssl dgst -sha256 -verify .ff1-release-public-key.pem -signature <image>.iso.sig <image>.iso
```

Then it asks you which disk is the USB drive before writing anything (a wrong disk erases your computer), writes the image to that disk, and hands you the steps below. Those stay by hand.

## Install

1. **Power off the Art Computer** (unplug the power cable).
2. Plug the **USB installer** into the Art Computer.
3. Plug the **power cable back in**. The Art Computer will boot from the USB automatically.
4. **Wait until the Art Computer shuts itself down.** (The screen may go blank during install.)
5. Remove the USB.
6. **Power-cycle the Art Computer** (unplug power, then plug it back in).

After booting, the Art Computer shows its setup screen again.
