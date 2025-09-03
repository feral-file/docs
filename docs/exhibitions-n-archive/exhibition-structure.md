# Exhibition Structure

## Overview

From a user's perspective, an exhibition is an event for viewing and collecting works. Technically, an exhibition is a container that holds artworks, their editions, and transactions. Each exhibition corresponds to a smart contract on blockchain.

## Exhibition Types

The exhibition type controls configuration for artwork models, sale model, and peer-exchange rules. Types are based on how many artists participate:

- **Group** — more than one artist; a curator is required. 
- **Solo** — one artist; curator optional.

### Rules by Type

#### Group Exhibitions

- Curator required, and cannot also be an exhibiting artist.
- Curator's Note is required.
- Artists may upload multiple works.
- A2P ("artist-to-peer" exchange): artists in a Group show may swap works with one another. Recommended practice is one edition to each artist and the curator, and one edition to Feral File for archive; artists receive the AP of their own work. A2P offers flexibility, as the system does not impose any constraints, but is documented as part of Group shows.
- **Constraint**: Cannot use 1 of 1 artwork model.

#### Solo Exhibitions

- Exhibition Note or Curator's Note is required (at least one).
- For **Edition**/**Series** model: artists receive AP; Feral File receives one for archive (recommended, not enforced).
- For **1 of 1**: only one edition exists — no AP, no PP.
- **Flexibility**: Can use all artwork models (Edition, Series, 1 of 1).

## Sale Model (Primary Sale)

Exhibitions use a **fixed-price** ("Buy Now") sale: collectors purchase at a listed price.

## Archive & Proofs

### Terminology

- **AP** — Artist Proof: Edition reserved for the artist
- **PP** — Publisher Proof: Edition reserved for Feral File
- **Archive rule** — Except for 1 of 1, one edition is typically reserved for Feral File archive

### Distribution Practices

**Group Exhibitions:**
- Each artist receives AP of their own work
- Recommended: One edition to curator, one to Feral File archive
- A2P exchanges allow flexible distribution among participants

**Solo Exhibitions:**
- Artist receives AP for Edition/Series models
- Recommended (not enforced): One edition to Feral File for archive
- 1 of 1 works: No AP/PP since only one edition exists

## Artwork Constraints

- All editions of an artwork must share the same medium type
- Cannot mix different artwork models within a single artwork entry
- Series cannot contain multiple distinct artworks

For detailed guidance on choosing artwork models, see [Modeling Your Work](modeling-work.md).
