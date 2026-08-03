# Print Your Own Faceplates

The two mesh plates on the ends of the Art Computer are the one part of the enclosure you can reasonably make yourself. The CAD is published here under an open license so you can print the stock parts, or design your own.

The obvious reason to make one is a port. The board inside carries far more I/O than the product shows — Ethernet, DisplayPort, extra USB — and the stock plate deliberately hides all of it. Earlier designs exposed more, and people could not tell what plugged into what. Simplicity is the default, not the limit. If you want Ethernet, take the plate off and make one that has it.

---

## Download

| File | What it is |
| :-- | :-- |
| **faceplate-mesh** · [STEP](faceplate-mesh.stp) · [3MF](faceplate-mesh.3mf) · [STL](faceplate-mesh.stl) | The plain plate. No openings. This is the one carrying the Wi-Fi antennas. |
| **faceplate-ports** · [STEP](faceplate-ports.stp) · [3MF](faceplate-ports.3mf) · [STL](faceplate-ports.stl) | The plate as shipped: power, HDMI, and USB-C. |
| **faceplate-ports-ethernet** · [STEP](faceplate-ports-ethernet.stp) · [3MF](faceplate-ports-ethernet.3mf) · [STL](faceplate-ports-ethernet.stl) | The same plate with an Ethernet opening added. Not a shipping part. |

Take **STEP** if you want to modify the design — it is the real solid model, and every CAD tool reads it. Take **3MF** or **STL** if you only want to print it.

Licensed **[CC BY-SA 4.0](LICENSE.txt)**. Print them, sell them, change them — just credit Feral File and share your changes under the same license.

---

## Which plate is which

Look at your device. One end has the ports; the other is plain mesh. They are not interchangeable, and the difference matters more than it looks.

| | Plain mesh plate | Ported plate |
| :-- | :-- | :-- |
| **Cooling** | Air **intake** | Air **exhaust**, directly in front of the heatsink fins |
| **Radio** | Both Wi-Fi antennas are stuck to the inside of this plate | — |

The ported plate is the more dangerous one to restyle. Intake is diffuse and forgiving. Exhaust is directed: air leaves the fin stack in a band, and a plate that blocks that band traps heat even if its total open area looks fine.

---

## Design rules

Three things constrain the design. Break any one of them and the device still boots, which is what makes them worth stating.

### 1. It has to breathe

The mesh is the airflow path, not decoration. Venting through the plates rather than piercing the aluminum extrusion was a deliberate choice, so there is no second vent path to fall back on. A solid or heavily stylised plate suffocates the machine.

The stock plates measure **roughly 25% open area** — 912 mm² on the ported plate and 982 mm² on the plain one, out of a 3,698 mm² face. Keep at least that much, and keep it in the same region of the plate. On the ported plate that means keeping the mesh band where the stock plate has it; the three port cutouts sit off to one side precisely so they stay out of the way of the fins.

These numbers are measured from the stock parts, not derived from a thermal model. Treat them as "match the factory plate," not as a validated threshold.

### 2. It has to let the radio through

Both Wi-Fi antennas are adhesive flexible-circuit strips stuck to the **inside face of the plain plate**. They radiate straight through it. So:

- **No carbon-fill, glass-fill, or metal-fill filament.** These will kill Wi-Fi. Plain ABS, ASA, or PETG only.
- **Leave flat, solid areas at both ends of the inner face** — roughly the outer third at each end. That is where the antennas land. Do not run mesh edge to edge.

There is no mounting geometry to reproduce. No bosses, no clips, no recesses. The antennas are peel-and-stick, applied by hand.

### 3. It has to fit

The plates are not screwed in. They slide into slots in the extrusion, and the lid screws down to hold them captive. That makes two dimensions critical:

| | |
| :-- | :-- |
| Outline | **108.76 × 34.00 mm** |
| Thickness | **2.50 mm**, uniform |
| Slide-fit tolerance | **±0.2 mm** |

A slide fit is the least forgiving thing to hit on an FDM printer. Two failure modes account for nearly all of it:

- **Elephant's foot.** First-layer squish flares the bottom edge and the plate will not enter the slot. Chamfer the edges or tune your first-layer compensation.
- **Warping.** A 108.76 × 34 × 2.5 mm part curls at the ends, and a curled plate does not slide. Print it flat on the bed, and use a brim.

---

## Material

The factory parts are **ABS**, produced by injection moulding.

For home printing, **PETG is the better choice.** It prints flat and true without an enclosure, and its ~80 °C glass transition is comfortable where the plate sits — at the periphery, in the airflow, on a machine that targets under 75 °C at the CPU. ABS and ASA match the stock material and have more heat headroom, but need an enclosed printer to come out straight at this size.

**PLA is not suitable.** It softens around 60 °C, which is inside this device's normal operating range.

---

## Before you print

Pull a plate off and look at it. Removing the lid's four screws frees both plates — see the [upgrade guide](../upgrades.md) for the disassembly, and note the warning there about the antenna leads.

Nothing here is sealed and none of it voids your warranty. Damage you cause is on you, as always, but opening the machine is not damage.

---

Made something good? We would like to see it — **[support@feralfile.com](mailto:support@feralfile.com)**.
