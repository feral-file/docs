# Player Behavior

This page explains how players consume DP-1 playlists at runtime.

- What this is: runtime behavior guidance for playback clients.
- Why use it: helps debug validation, fetch, and playback issues.
- What to do next: confirm your player behavior against the canonical DP-1 spec.

## Version and compatibility note

- Canonical DP-1 spec is currently `v1.1.0`.
- Some adjacent tooling still centers `dpVersion: 1.0.0` payloads and legacy top-level `signature` behavior.
- Do not assume blanket end-to-end `1.1.0` parity across CLI, validator, and feed operator unless explicitly verified in those repos.

## Runtime sequence (player view)

1. Load playlist from URL or feed endpoint.
2. Validate playlist structure for the toolchain version in use.
3. Verify trust metadata (`signature` or `signatures`) according to implemented verifier capabilities.
4. Render items in order with item/default display settings.
5. On failure, surface a clear error and continue according to player policy.

## The Art Computer as reference hardware

The Art Computer is Feral File's reference hardware path for DP-1 playback.

Use Art Computer behavior as one implementation path, not as the protocol definition.

## Next step

Use the bridge flow: [From DP-1 playlist to Art Computer playback](art-computer-integration.md).
