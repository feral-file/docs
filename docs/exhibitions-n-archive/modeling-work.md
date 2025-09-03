# Modeling Your Work

## Quick Start

**New to Feral File?** Start here:

1. **Choose exhibition type**: Solo (one artist) or Group (multiple artists + curator)
2. **Pick artwork model** for each work: Edition (identical copies), Series (variations), or 1 of 1 (unique)
3. **Review constraints**: Group shows can't use 1 of 1 model
4. **Consider your medium**: Single-Source Generative vs Per-Edition Source affects your workflow

→ [Jump to decision guide](#choosing-your-model) | [See common scenarios](#common-scenarios)

## Artwork Models Overview

An artwork model sets the supply and the display behavior. **Important**: All editions of an artwork must share the same concept and medium type (video, image, software, etc.).

- **Edition** — multiple identical editions (all the same).
- **Series** — multiple editions with edition-specific display, unique editions (all different).
- **1 of 1** — a single edition.

**Allowed artwork models by exhibition type:**

| Exhibition Type | Edition | Series | 1 of 1 |
|-----------------|---------|--------|--------|
| **Group**       | ✅ Yes  | ✅ Yes | ❌ No  |
| **Solo**        | ✅ Yes  | ✅ Yes | ✅ Yes |

> **Important**: Group exhibitions cannot use the **1 of 1** model - this is only available for Solo shows.

## What "Series" means (and doesn't)

Series = one artwork with multiple editions where each edition may render differently. All editions must share the same medium type (videos, images, software, etc.).

Series is not a container of multiple distinct artworks. You cannot nest: "series → artworks → each with its own editions."

**Series in practice:** 

If your work is a single concept that **varies per edition** (e.g., 30 different video cuts of the same piece), model it as **one work, Series of 30**.

## Single-Source Generative vs Per-Edition Source

This distinction affects how your artwork creates different editions:

* **Single-Source Generative** — Upload one software bundle that reads Feral File variables (`token_id`, `edition_number`, `contract_address`, ...) and deterministically renders a unique output for each edition.
    - *How it works*: Same source code + different URL parameters = different visual output
    - *Example*: JavaScript artwork that reads `?token_id=123` and generates unique patterns based on that value
    - *Key requirement*: Must be deterministic - same parameters always produce the same result
    - *File requirement*: One HTML/JS bundle
    - *Artwork model*: Typically **Series** (one codebase, multiple unique outputs)

* **Per-Edition Source** — Upload one file per edition. Use this for media or software where each edition ships its own file.
    - *How it works*: Separate files for each edition, no parameters involved
    - *Examples*: Video files, images, PDFs, pre-rendered animations
    - *File requirement*: One file per edition (if using Series model)
    - *Artwork model*: Can be **Edition** (identical copies) or **Series** (different files per edition)

## Choosing your model

- Media that's identical across copies → Edition (N).

- One software artwork that varies per edition → Series (N) with one HTML bundle (Single-Source Generative).

- Do these 30 videos represent **one conceptual artwork** with a different file per edition?  
  → **Series (30)** for **one** artwork.

- Are they **30 distinct artworks** (each stands alone with its own title/statement)?  
  → **30 artworks**, each **Edition** with your chosen edition size.

- **Mixed media in one artwork?** → **Not supported**. Split into separate artworks by medium type.

- **"Series" containing multiple distinct works?** → **Not supported**. Create multiple artworks instead.

## Common scenarios

**Traditional media:**

- **7 different video works, 10 copies each** → Create 7 artworks, each **Edition of 10**
- **One video concept with 7 different cuts/versions** → Create 1 artwork, **Series of 7** (all videos)
- **30 identical prints** → Create 1 artwork, **Edition of 30** (all images)

**Digital/Single-Source Generative:**

- **One codebase, different output per edition via parameters** → Create 1 artwork, **Series** (Single-Source Generative)
- **Multiple Single-Source Generative artworks for one show** → Create multiple artworks, each **Edition** or **Series**

**Mixed media scenarios:**

- **One concept: 5 videos + 5 images** → Split into 2 artworks: one for videos, one for images
- **Photo series with accompanying text files** → Choose primary medium or create separate artworks

**Not supported:**

- One "series container" holding multiple distinct artworks → Split into separate artworks instead
- Mixed medium types within a single artwork → Split by medium type

## Frequently Asked Questions

**Q: Can I have a "series" that contains multiple different artworks?**
A: No. Series means one artwork with multiple variations. For multiple distinct artworks, create separate artwork entries.

**Q: What's the difference between Edition and Series?**
A: Edition = identical copies. Series = one artwork with variations per edition. Both must maintain the same medium type across all editions.

**Q: Can I mix videos and images in one artwork?**
A: No. Each artwork must have consistent medium type. Split mixed media into separate artworks.

**Q: How do I handle Single-Source Generative art?**
A: Use Series model with one code bundle. The software should read Feral File variables from URL query parameters to create unique outputs per edition.

**Q: Can I have a photo series with accompanying audio files?**
A: No. Choose the primary medium or create separate artworks for photos and audio.

## Terms & Definitions

- **AP** — Artist Proof
- **PP** — Publisher Proof  
- **Edition** — Multiple identical copies of an artwork
- **Series** — One artwork with variations across editions
- **1 of 1** — Single unique edition
- **Single-Source Generative** — One piece of software that creates unique visuals per edition using Feral File variables from URL query parameters
- **Per-Edition Source** — Each edition has its own specific file or content, created before minting
- **Archive rule** — Except for 1 of 1, one edition is reserved for Feral File archive
