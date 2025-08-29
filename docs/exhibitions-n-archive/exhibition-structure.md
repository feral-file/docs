# Exhibition Structure and Artwork Models

## Quick Start

**New to Feral File?** Start here:

1. **Choose exhibition type**: Solo (one artist) or Group (multiple artists + curator)
2. **Pick artwork model** for each work: Edition (identical copies), Series (variations), or 1 of 1 (unique)
3. **Review constraints**: Group shows can't use 1 of 1 model
4. **Consider your medium**: Generative code vs traditional media affects upload requirements

→ [Jump to decision guide](#choosing-your-model) | [See common scenarios](#common-scenarios)

## Overview

From a user's perspective, an exhibition is an event for viewing and collecting works. Technically, an exhibition is a container that holds artworks, their editions, and transactions. Each exhibition corresponds to a smart contract on Ethereum. 

## Exhibition types

The exhibition type controls configuration for artwork models, sale model, and peer-exchange rules. Types are based on how many artists participate:

- **Group** — more than one artist; a curator is required. 
- **Solo** — one artist; curator optional. 

## Artwork models

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

### What "Series" means (and doesn't)

Series = one artwork with multiple editions where each edition may render differently. All editions must share the same medium type (videos, images, software, etc.).

Series is not a container of multiple distinct artworks. You cannot nest: "series → artworks → each with its own editions."

**Series in practice:** 

If your work is a single concept that **varies per edition** (e.g., 30 different video cuts of the same piece), model it as **one work, Series of 30**. 

### Generative vs Non-Generative

Understanding whether your work is generative affects how you upload and structure your editions:

* **Generative** — Interactive software that creates unique visuals for each edition using code. You upload one code bundle that uses Feral File variables (like `artwork_number`, `token_id`, `contract_address`) or uses the [Artwork JS library](/../artwork-lib/install-basics) to produce a deterministic random seed to create different outputs. Each edition renders differently but consistently.
    - *Example*: A JavaScript artwork that uses `token_id` as a seed to generate different colors or patterns
    - *File requirement*: One HTML/JS bundle

* **Non-generative** — Fixed media or pre-rendered content. Each edition has its own specific file.
    - *Examples*: Video files, images, PDFs, or pre-made HTML files with fixed content
    - *File requirement*: One file per edition (if using Series model)

### Choosing your model

- Media that’s identical across copies → Edition (N).

- One software artwork that varies per edition → Series (N) with one HTML bundle (generative).

- Do these 30 videos represent **one conceptual artwork** with a different file per edition?  
  → **Series (30)** for **one** artwork.

- Are they **30 distinct artworks** (each stands alone with its own title/statement)?  
  → **30 artworks**, each **Edition** with your chosen edition size.

- **Mixed media in one artwork?** → **Not supported**. Split into separate artworks by medium type.

- **"Series" containing multiple distinct works?** → **Not supported**. Create multiple artworks instead.

### Common scenarios

**Traditional media:**

- **7 different video works, 10 copies each** → Create 7 artworks, each **Edition of 10**
- **One video concept with 7 different cuts/versions** → Create 1 artwork, **Series of 7** (all videos)
- **30 identical prints** → Create 1 artwork, **Edition of 30** (all images)

**Digital/Generative:**

- **One generative code, different output per edition** → Create 1 artwork, **Series** (generative software)
- **Multiple generative artworks for one show** → Create multiple artworks, each **Edition** or **Series**

**Mixed media scenarios:**

- **One concept: 5 videos + 5 images** → Split into 2 artworks: one for videos, one for images
- **Photo series with accompanying text files** → Choose primary medium or create separate artworks

**Not supported:**

- One "series container" holding multiple distinct artworks → Split into separate artworks instead
- Mixed medium types within a single artwork → Split by medium type

## Sale model (primary sale)

Exhibitions use a **fixed-price** (“shopping”) sale: collectors purchase at a listed price.

## Rules by type

### Group

- Curator required, and cannot also be an exhibiting artist.
- Curator’s Note is required.
- Artists may upload multiple works.
- A2P ("artist-to-peer" exchange): artists in a Group show may swap works with one another. Recommended practice is one edition to each artist and the curator, and one edition to Feral File for archive; artists receive the AP of their own work. A2P offers flexibility, as the system does not impose any constraints, but is documented as part of Group shows. 

### Solo

- Exhibition Note or Curator’s Note is required (at least one).
- For **Edition**/**Series** model: artists receive AP; Feral File receives one for archive (recommended, not enforced).
- For **1 of 1**: only one edition exists — no AP, no PP. 

## Frequently Asked Questions

**Q: Can I have a "series" that contains multiple different artworks?**
A: No. Series means one artwork with multiple variations. For multiple distinct artworks, create separate artwork entries.

**Q: What's the difference between Edition and Series?**
A: Edition = identical copies. Series = one artwork with variations per edition. Both must maintain the same medium type across all editions.

**Q: Can I mix videos and images in one artwork?**
A: No. Each artwork must have consistent medium type. Split mixed media into separate artworks.

**Q: How do I handle generative art?**
A: Use Series model with one code bundle. The code should use Feral File variables to create unique outputs per edition.

**Q: What if I have 50 different video works?**
A: Create 50 separate artworks, each as Edition model (not one Series of 50).

**Q: Can I have a photo series with accompanying audio files?**
A: No. Choose the primary medium or create separate artworks for photos and audio.

## Terms & Definitions

- **AP** — Artist Proof
- **PP** — Publisher Proof  
- **Edition** — Multiple identical copies of an artwork
- **Series** — One artwork with variations across editions
- **1 of 1** — Single unique edition
- **Generative** — Code-based artwork that creates unique visuals per edition
- **Archive rule** — Except for 1 of 1, one edition is reserved for Feral File archive