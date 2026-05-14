# DP-1 Validator Quickstart

Validation is the fastest way to confirm your integration is on the right track.

This page shows a minimal first run with the open-source DP-1 validator.

- What this is: a practical first trust check for playlist inputs.
- Why use it: catch payload and signature issues before feed/player debugging.
- What to do next: validate one playlist now, then align schema details.

## Version note

Canonical DP-1 specification is currently `v1.1.0`.

This quickstart uses a minimal `dpVersion: 1.0.0` payload to match current ff-cli output and validator examples.

Use the version your integration emits, and validate it against the canonical spec rules.

Current validator behavior is strongest for structure checks and legacy top-level `signature` verification (`--pubkey`).

Do not assume this CLI verifies full DP-1 `v1.1.0` `signatures[]` chain semantics end-to-end unless confirmed upstream.

## What this is

The DP-1 validator checks playlist shape and signature validity.

## Why use it first

If validation fails, playback and distribution issues usually follow. Validate early before feed or player debugging.

## Minimal first run

1) Save a minimal playlist as `playlist.json`:

```json
{
  "dpVersion": "1.0.0",
  "id": "385f79b6-a45f-4c1c-8080-e93a192adccc",
  "title": "Minimal DP-1 Playlist",
  "created": "2025-10-17T07:02:03Z",
  "items": [
    {
      "id": "item-1",
      "title": "Example Item",
      "source": "https://example.com/artwork.html",
      "duration": 30,
      "license": "open"
    }
  ]
}
```

2) Validate from base64 payload:

```bash
PLAYLIST_B64="$(cat playlist.json | base64 | tr -d '\n')"
dp1-validator playlist --playlist "$PLAYLIST_B64"
```

If your flow includes a legacy top-level `signature`, pass `--pubkey` with the expected Ed25519 public key.

## Canonical validator source

- Validator repository: <https://github.com/display-protocol/dp1-validator>

## Common failure points

- Wrong `dpVersion` for your toolchain.
- Missing required fields such as `title`, `items`, or item `source`.
- Signature mismatch caused by payload changes after signing.
- `signatures[]` chain expectations: verify against canonical DP-1 spec and upstream validator status.

## Next step

Read [Schemas](schemas.md) and align your payload model.
