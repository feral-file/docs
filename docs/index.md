# Feral File

Feral File is a cultural institution and technology company championing computational art for a global audience. Computational art runs, responds, and evolves through code, models, and data.

[feralfile.com](https://feralfile.com) is where the exhibitions live and where collectors browse. These pages are the other side of the institution. They cover the Digital Art System (the Art Computer and the Art Panel) and the tools that let your software (and the agents working on your behalf) talk to us.

[DP-1](https://github.com/display-protocol/dp1) is the other half of our work: an open, vendor-neutral protocol for digital art playlists, designed to let the system outgrow us. Spec, integrator guides, and tooling live at [display-protocol/dp1](https://github.com/display-protocol/dp1) and [display-protocol/dp1-cli](https://github.com/display-protocol/dp1-cli).

## Start here

- **In conversation** — through Claude Code, Codex, Cursor, or OpenCode. Find artworks, build playlists, play them on your Art Computer, publish to a feed, all in chat. → [Agents](agents/index.md)
- **From the terminal** — same capabilities via `ff-cli`. Find, build, validate, sign, play, publish, and manage devices. → [ff-cli](ff-cli/index.md)
- **From the browser** — sign and publish DP-1 playlists with your wallet, no tooling required (early release). → [DP-1 Publisher](https://publisher.feralfile.com)

## What's here

- **[ff-cli](ff-cli/index.md)** — command-line tool. Build a DP-1 playlist from a URL or wallet, play it on a device, publish it to a feed.
- **[Art Computer](art-computer/index.md)** — the computational engine of the Digital Art System. Plug it into any screen, or pair it with the Art Panel, to play DP-1 playlists.
- **[Hosted Feed](hosted-feed/index.md)** — our hosted DP-1 feed at `feed.feralfile.com` for publishing and retrieving playlists.
- **[Agents](agents/index.md)** — for coding agents (off-device) and OpenClaw runtimes (on-device).
- **[Artwork Library](https://github.com/feral-file/ffa-js)** — JS library artists embed in software artworks for provenance, deterministic randomness, and on-chain data. Docs live with the library.
- **[Exhibitions OpenAPI](https://feralfile.com/.well-known/openapi.json)** — read-only endpoints for discovering exhibitions, series, and artworks. Complementary to `ff-cli`.
