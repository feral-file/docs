# DP-1 Schemas

This page explains the DP-1 object model in plain language and links the canonical schema sources.

## Version note

Canonical DP-1 specification is currently `v1.1.0`.

The minimal example on this page uses `dpVersion: 1.0.0` for compatibility with current FF1 CLI output in the first-run flow.

For production behavior, follow the canonical spec version your toolchain supports.

Ecosystem tooling is transitional. Do not assume full `v1.1.0` end-to-end parity across all adjacent repos unless explicitly verified there.

## Canonical sources

- DP-1 specification and schema rules: <https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md>
- Feed server OpenAPI (operator API): <https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml>

## Object model at a glance

- `playlist`
  - Top-level container with `dpVersion`, identity fields, display defaults, and `items`.
- `defaults`
  - Optional baseline values inherited by items (for example display settings, license, duration).
- `items[]`
  - The ordered media entries a player can render.
- `display`
  - Rendering preferences such as scaling, background, and margin.
- `provenance`
  - Optional source-of-truth metadata (for example on-chain contract context).
- `signature` or `signatures`
  - Integrity and trust metadata defined by the DP-1 spec version in use.

## Minimal playlist shape

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

Use this as a shape reference only. For authoritative field behavior and version rules, use the canonical spec.

## Next step

Run [Validator Quickstart](validator.md) on your own payload.
