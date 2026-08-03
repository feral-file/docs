# Upgrading Memory and Storage

Most people never need this page. The Art Computer ships with enough memory and storage to play everything Feral File distributes, and it updates itself over the air.

This page is for owners who want more headroom: a large local library, or real-time generative work that leans on the GPU. Both the RAM and the SSD are user-serviceable, and both are reachable in one sitting with the case open.

!!! note "Upgrading does not void your warranty"
    Opening the Art Computer to change the memory or the SSD does not void its one-year hardware warranty. The device is built to be opened.

    Two ordinary limits apply. Damage caused during the upgrade itself is not covered, and parts you install are covered by their own manufacturer's warranty rather than ours.

---

## What you can change

| Component | Stock | Ceiling | Notes |
| :-- | :-- | :-- | :-- |
| **Memory** | 8 GB DDR5-4800 in one of two slots | 64 GB (2 × 32 GB) | Two SO-DIMM slots, one empty from the factory |
| **Storage** | 128 GB NVMe SSD | No practical limit | One M.2 2280 slot, PCIe 4.0 ×4 |

Nothing else inside is user-serviceable. The CPU and GPU are soldered, and the wireless card, antennas, and thermal assembly should be left alone.

The mesh end plates are a separate matter — those you can redesign and print yourself, and the CAD is published under an open license. See [Print Your Own Faceplates](./faceplates/index.md).

---

## What to buy

Buy to the requirements below. Any part that meets them will work — the specific products are known-good examples we have verified, not the only valid choices.

### Memory requirements

- **DDR5 SO-DIMM, 262-pin, 1.1 V, non-ECC, unbuffered**
- **DDR5-4800 or faster, but there is no benefit above 4800.** The Ryzen 7 7735U tops out at DDR5-4800. Faster modules work fine, they just run at 4800. Art Computers ship with either a DDR5-4800 or a DDR5-5600 module depending on what the factory had on hand, and both run at the same speed, so do not read the number on your existing module as a target. Buying a faster kit costs more and changes nothing.
- **Buy a matched two-module kit, not a single module.** The GPU is integrated, so system memory is also video memory. Filling both slots doubles memory bandwidth, and bandwidth — not capacity — is what limits real-time generative work. A single module gives up half of it.
- **Replace the stock module rather than pairing with it.** Mixed capacities break the matched pair. Keep the original in the box.

### Storage requirements

- **M.2 2280, PCIe 4.0 (Gen 4) or better, NVMe.** The slot is Gen 4 ×4. The drive fitted at the factory is a Gen 3 part, so a Gen 4 drive is the one upgrade here that uses capability the machine already has and is not currently using.
- **2280 only.** A 2242 or 2260 drive will seat but leaves the slot underused; a 22110 is too long to fit.
- **No heatsink.** The Art Computer moves heat through a 1 mm thermal pad into its finned aluminum lid. An SSD heatsink blocks that path and makes cooling worse, not better. Buy the bare version of whatever drive you choose — many drives ship in both, under nearly identical part numbers.

### Known-good parts

Verified August 2026. Confirm the part number at checkout: vendors list regional variants and heatsink versions under near-identical SKUs.

| Component | Product | Part number |
| :-- | :-- | :-- |
| Memory | Crucial 32 GB DDR5-4800 SO-DIMM kit (2 × 16 GB), CL40 | `CT2K16G48C40S5` |
| Memory (maximum) | Crucial 64 GB DDR5-4800 SO-DIMM kit (2 × 32 GB), CL40 | `CT2K32G48C40S5` |
| Storage | Samsung 990 EVO Plus 2 TB | `MZ-V9S2T0B/AM` |
| Storage (budget) | WD Blue SN5000 2 TB | `WDS200T4B0E` |

Two SKUs worth not confusing:

- `CT32G48C40S5` is a **single** 32 GB module. You want `CT2K16G48C40S5`, the two-module kit.
- `MZ-V9S2T0BW` is the same Samsung drive in international packaging. Either works; `/AM` is the US retail SKU.

---

## Why these drives, and why no heatsink

The enclosure is designed around a sustained system load of roughly 15–28 W — CPU, GPU, and SSD together. That is the budget the whole device shares, so a drive that idles cool matters more than a drive that benchmarks fast.

Art playback is light sequential reading. In practice the drive sits at idle almost permanently, and idle power is where the difference shows up:

| Samsung 990 EVO Plus 2 TB | Power |
| :-- | :-- |
| Active read | 4.6 W |
| Active write | 4.2 W |
| Idle (APST on) | 60 mW |
| Idle (L1.2) | 5 mW |

*Source: Samsung 990 EVO Plus data sheet, rev. 1.0.*

Peak sequential speed is irrelevant here. A 4K video work streams at roughly 100 Mbps against a drive rated in the thousands. You would never see the speed difference, but you would feel thermal throttling — it shows up as playback stutter.

A flagship Gen 5 drive draws roughly twice the active power for performance this device cannot use, and pairs it with a heatsink that fights the enclosure. That is the combination to avoid.

---

## Before you start

You will need a small Phillips screwdriver and a USB drive of 8 GB or larger.

!!! warning "The end plates come loose when the lid does"
    The two mesh end plates are not screwed in. They slide into slots and the lid holds them captive, so expect both to fall out as you lift the lid off.

    One of them carries the Wi-Fi antennas, joined to the board by two fine coaxial leads. Support that plate instead of letting it drop and hang on them. A tugged antenna lead is the most common way an upgrade ends in a device that works but will not hold Wi-Fi.

**A replacement SSD arrives blank.** The stock drive ships with FF OS already imaged; yours will not. Reinstalling FF OS is a required step, not an optional one. Read [Step 3 of Getting Started](./index.md#step-3-advanced-reinstall-ff-os-from-usb) before you begin, and prepare the USB installer first — it is easier to do while the device is still running.

---

## Upgrade procedure

1. **Prepare the USB installer first**, following [Step 3 of Getting Started](./index.md#step-3-advanced-reinstall-ff-os-from-usb). Do this before opening the case.
2. **Unplug the power cable.** Wait a few seconds.
3. **Remove the four screws and lift off the finned lid.** The memory and the SSD are directly underneath. Both end plates will likely come loose as the lid clears — catch the one with the antenna leads rather than letting it hang.
4. **Swap the SSD.** Remove the retaining screw, lift the old drive out at a shallow angle, seat the new one the same way, and refit the screw. Do not overtighten.
5. **Swap the memory.** Release the clips on each side of the stock module; it will spring up. Lift it out, then seat each new module at roughly a 30° angle and press down until the clips latch. Fill both slots.
6. **Slide both end plates back into their slots**, refit the lid, and replace the four screws. The lid is what holds the plates in, so they will sit loose until it is back on.
7. **Reinstall FF OS** from the USB installer, following Getting Started Step 3.

When the install finishes, the Art Computer shuts itself down. Remove the USB drive, power-cycle, and you should land on the pairing QR code.

---

## After the upgrade

The Art Computer does not display its own memory or storage anywhere, so there is no number to check. Judge it by behaviour.

It worked if the device boots to the pairing QR code, pairs, and plays artwork.

**One failure stays quiet, so guard against it during the install rather than after.** A memory module can sit in its slot without latching. The machine then boots and runs normally on the other module, and nothing tells you that you are using half the memory bandwidth you just paid for. Press each module down until both clips snap in audibly, and tug gently on each one before closing the case.

Everything else fails loudly, and the troubleshooting below covers it.

---

## Troubleshooting

- **No QR code after the upgrade.** Confirm the TV is on the right HDMI input and the USB installer has been removed. If the screen stays dark, power down, reopen, and reseat the SSD and both memory modules.
- **No video at all after the upgrade.** Almost always a memory module that is not fully latched. Power down, remove both modules, and reseat them until the clips snap.
- **Wi-Fi will not connect after the upgrade.** Check the antenna leads where they meet the board. Pulling on the loose end plate is the usual cause.
- **The install never finishes.** Re-flash the USB installer with the current `release` image and try again.

Still stuck? Email **[support@feralfile.com](mailto:support@feralfile.com)**.
