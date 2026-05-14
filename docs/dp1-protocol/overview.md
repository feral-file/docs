# DP-1: Start Here (Integrators)

DP-1 is an open, vendor-neutral protocol for signed digital art playlists.

Use DP-1 when you want portable playback across compatible players, with validation and signature checks as the trust baseline.

- What this is: the protocol entry point for integrators.
- Why use it: one playlist format that can be validated and played across compatible systems.
- What to do next: validate one minimal playlist first.

## Version note

Canonical DP-1 specification is currently `v1.1.0`.

In this first-run flow, some examples use `dpVersion: 1.0.0` for compatibility with current CLI/operator tooling in the ecosystem.

Treat the spec as authoritative and choose the version your toolchain supports.

Do not assume blanket end-to-end `1.1.0` parity across CLIs, and feed operator unless explicitly verified in those repos.

## First success flow

1. Validate one minimal playlist with [dp1-cli](dp1-cli.md) (public beta).
2. Review the core object model (`playlist`, `items`, `display`, `provenance`).
3. Publish or host the validated playlist.
4. Play it on the Art Computer (Feral File's reference hardware) or another compatible player.

## Canonical references

- DP-1 specification (authoritative, currently v1.1.0): <https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md>
- DP-1 repository: <https://github.com/display-protocol/dp1>
- Feed server implementation (OpenAPI + server): <https://github.com/display-protocol/dp1-feed-v2>
- **dp1-cli** (validate, sign, verify, publish; **public beta**; **actively maintained** successor to legacy **dp1-validator** tags in the **same repo**): <https://github.com/display-protocol/dp1-cli>

## Fast links for this site

- Validate first: [DP-1 CLI quickstart](dp1-cli.md) (public beta)
- Understand object model: [Schemas](schemas.md)
- Hosted feed guidance (Feral File): [Hosted Feed](feed-server.md)
- Run your own feed: [Self-Hosted Feed](self-hosted-feed.md)
- Short Art Computer bridge: [From DP-1 to Art Computer playback](art-computer-integration.md)

## Notes on roles

- **DP-1** is the protocol.
- **The Art Computer** is Feral File's reference hardware (model designation: FF1).
- You can integrate DP-1 without the Art Computer.

## Next step

Run [DP-1 CLI quickstart](dp1-cli.md) and validate one playlist.
