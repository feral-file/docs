# DP-1 Protocol Overview

## Feral File's Implementation
DP-1 is an open protocol for blockchain-native digital art display, enabling interoperable playlists across devices. Feral File seeds this ecosystem with FF1 hardware as the reference implementation and hosts a production Feed Server at [feed.feralfile.com](https://feed.feralfile.com).

For the full vendor-neutral spec, see the [public DP-1 repo](https://github.com/display-protocol/dp1), including [design principles (raw)](https://github.com/display-protocol/dp1/main/docs/spec.md).

### Why DP-1 for Feral File
The digital display landscape faces challenges like fragmented standards and data integrity—DP-1 fixes that with unified validation and verifiable authenticity. For us, it powers seamless exhibitions: token-gated art on FF1s, AI-generated playlists, and global distribution.

## Core Components
Key DP-1 pieces in our ecosystem:

- **Feed Server**: Our hosted registry [](https://feed.feralfile.com) stores, validates, and signs playlists. See [Feed Server](feed-server.md).
- **Validator**: Ensures schema compliance and Ed25519 signatures. Use the open [DP-1 Validator](https://github.com/display-protocol/dp1-validator) CLI.
- **Schema**: Defines playlists with metadata, items, and display rules. Dive into [schemas.md](schemas.md) or the [OpenAPI spec (raw)](https://github.com/display-protocol/dp1/main/docs/feed-api.yaml).
- **Display Client**: FF1 renders these—optimized for provenance checks and OTA updates.

## Benefits of DP-1
- **Interoperability**: Content flows to FF1s, web players, and beyond.
- **Data Integrity**: Built-in validation prevents breaks.
- **Scalability**: Easy to scale exhibitions with new sources.
- **Trust**: On-chain provenance verifies NFTs.
- **Flexibility**: Supports open/token/subscription licenses.

## Key Feral Integrations
- **Exhibitions**: Model artworks as DP-1 playlists for token-gated displays (see [Exhibition Structure](../exhibitions-n-archive/exhibition-structure.md)).
- **AI Commands**: Generate playlists via natural language (see [Quickstart](../llm-agents/quickstart.md)).
- **FF1 Devices**: Render with hardware tweaks (see [Player Behavior](player-behavior.md)).

## Next Steps
- [Schemas](schemas.md) for Feral examples.
- Set up access to our [Feed Server](feed-server.md).