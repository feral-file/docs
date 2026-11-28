# Conservation

Displaying a work made with code means running it. Keeping the work means being able to run it again after the servers it depended on have closed.

Storing a work's files on chain does not by itself keep it on display. Players often reach those files through a marketplace's servers, and when those servers close the work stops displaying while its files are intact.

A preservation capsule is one file that holds every file a work loads and names the exact browser engine it was checked in. With the capsule and that engine, the work renders offline, and the render can be compared with the frame recorded when the capsule was packed.

Capsules are built and checked with [dp1c](https://github.com/display-protocol/dp1-capsule), open source under MPL 2.0. The capsule starts from section 9 of the [DP-1 specification](https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md). The engine layer, the reference frame, and the tolerance are proposals, written out in the repository's `SPEC-PROPOSAL.md`.

## Check a capsule

On Linux with Python 3 (and its `zstandard` and `Pillow` packages), bubblewrap, and Chromium:

```bash
git clone https://github.com/display-protocol/dp1-capsule
cd dp1-capsule
python3 dp1c.py verify examples/theres-no-distance-1.dp1c --host
```

The check runs with the network off and uses no Feral File service. It reports three things separately:

- **The files** are exactly what was packed: nothing missing, extra, or changed.
- **The reference frame** is the same frame in the playlist, in the capsule's record, and in the image file.
- **A fresh render** lands within the capsule's tolerance of the reference frame.

`--host` renders in your computer's own Chromium. A render within tolerance reads `reproducedOnDifferentEngine`, and the command exits 2. The verdict `reproduced`, exit 0, needs the engine image the capsule names. That image is not published for the example capsules; `engine/build-engine.sh` in the repository builds an engine image from the Arch Linux package archive.

## What a capsule holds

| Part | What it is |
| :-- | :-- |
| The work | Every file the work loads, each listed by its SHA-256 |
| The engine's name | The SHA-256 of an image that holds one exact Chromium and its fonts. The image itself is a separate file, kept beside the capsule |
| The render settings | Viewport size, time zone, a fixed clock, and the token's seed when the work has one |
| The reference frame | The frame the work rendered when the capsule was packed, with its hashes |
| The tolerance | How far a later render may differ from the reference frame and still pass. The artist sets it, from exact pixels to a looser match |
| Provenance | The contract and token, when the work has them, as the DP-1 playlist item carries them |

A signature travels in a file beside the capsule. It shows which key signed the capsule and that nobody changed it after.

## Where a capsule's files come from

- A contract that generates the work on chain
- Files stored on chain (`onchfs://`)
- A contract call that returns the work (`web3://`)
- The copy an Art Computer saved when it displayed the work
- A directory of files

The repository has an example capsule for each of the first four.

## What it does not do

The Art Computer does not build or check capsules. That happens on a computer with dp1c, which can start from the copy an Art Computer saved.

The check does not cover every work. CSS animations, transitions, and video run on a clock the engine does not control, so a work whose picture depends on them may not reproduce. The repository's [README](https://github.com/display-protocol/dp1-capsule#readme) has every command, the measurements, and what the check does not catch.
