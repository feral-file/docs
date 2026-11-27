# Conservation

Displaying a work made with code means running it. Keeping the work means being able to run it again, years later, after the servers it depended on have closed.

A work made with code has two sides to keep: what it is made of (its code, libraries, media, and inputs such as a token's seed) and what draws it (a browser engine). A preservation capsule is one file that holds the work and names the exact engine it was checked in. With the capsule and that engine, anyone can run the work offline and check that it still renders as it did.

Capsules are built and checked with [dp1c](https://github.com/display-protocol/dp1-capsule), a prototype, open source under MPL 2.0. The capsule starts from section 9 of the [DP-1 specification](https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md). The engine layer, the reference frame, and the tolerance are proposals, written out in the repository's `SPEC-PROPOSAL.md`.

## How a work stops displaying

Casey Reas's *There's No Distance #1* (2023) was released on fxhash, and its files are stored on Ethereum. The token's metadata, the indexers, and the players all reached those files through fxhash's servers. When fxhash closed in August 2026, the files were intact on chain and the work stopped displaying everywhere.

The repository's `tools/onchfs-read.py` reads the work's five files directly from the contract and checks each one against its on-chain address, and `dp1c.py build` packs them into a capsule. The work renders again from the capsule, offline, with no fxhash server involved.

## What a capsule holds

| Part | What it is |
| :-- | :-- |
| The work | Every file the work loads, each listed by its SHA-256 |
| The engine's name | The SHA-256 of an image that holds one exact Chromium and its fonts. The image itself is a separate file, kept beside the capsule |
| The render settings | Viewport size, time zone, a fixed clock, and the token's seed when the work has one |
| The reference frame | The frame the work rendered when the capsule was packed, with its hashes |
| The tolerance | How far a later render may differ from the reference frame and still pass |
| Provenance | The contract and token, when the work has them, as the DP-1 playlist item carries them |

A signature travels in a file beside the capsule. It shows which key signed the capsule and that nobody changed it after.

The tolerance is the artist's to set: a distance, from 0 to 64, between a perceptual hash of the fresh render and of the reference frame. 0 asks for exact pixels. The default passes the small differences one engine shows against another on the example works, and fails a blank frame or another work. It is a measure of the hash, and it does not say how alike two images look to a person.

## Check a capsule

On Linux with Python 3 (and its `zstandard` and `Pillow` packages), bubblewrap, and Chromium:

```bash
git clone https://github.com/display-protocol/dp1-capsule
cd dp1-capsule
python3 dp1c.py verify examples/theres-no-distance-1.dp1c --host
```

The check runs with the network off and uses no Feral File service. It reports three things separately:

- **The files** are exactly what was packed: nothing missing, extra, or changed.
- **The reference frame** agrees with itself across the playlist, its record, and the image's own pixels.
- **A fresh render** lands within the capsule's tolerance of the reference frame.

`--host` renders in your computer's own Chromium. A render within tolerance reads `reproducedOnDifferentEngine`, and the command exits 2. The verdict `reproduced`, exit 0, needs the engine image the capsule names. That image is not published for the example capsules; `engine/build-engine.sh` in the repository builds an engine image from the Arch Linux package archive.

## Where a capsule's files come from

| Source | Example in the repository |
| :-- | :-- |
| A contract that generates the work on chain | Tyler Hobbs, *Fidenza #503*, read from the Art Blocks generator |
| Files stored on chain (`onchfs://`) | Casey Reas, *There's No Distance #1* |
| A contract call that returns the work (`web3://`) | Han, *Digital Soul* and *Prodigy* |
| What an Art Computer saved when it displayed the work | Driessens & Verstappen, *E-volved Formula #22 #1* |
| A directory of files | A browser work whose files you have |

## On the Art Computer

An Art Computer saves the works it displays so they stay on display offline, and dp1c builds a capsule from that saved copy. Building and checking a capsule happens on a computer with dp1c. The Art Computer does not build or check capsules.

The check reports a work that uses a web worker or a cross-process iframe as a render problem. CSS animations, transitions, and video run on a clock the engine does not control, so a work whose picture depends on them may not reproduce. The repository's [README](https://github.com/display-protocol/dp1-capsule#readme) and `SPEC-PROPOSAL.md` have every command, the measurements, and what the tool does not catch.
