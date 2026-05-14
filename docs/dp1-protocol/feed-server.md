# Hosted Feed (Feral File)

This page covers the hosted DP-1 feed operated by Feral File.

Use it when you want a managed endpoint instead of running your own feed server.

- What this is: hosted feed usage guidance for Feral File-managed infrastructure.
- Why use it: quickest managed path to publish and retrieve playlists.
- What to do next: validate a payload, then POST to the hosted endpoint.

## What this is

The hosted feed accepts DP-1 playlists, validates payloads, and serves playlist data over HTTP APIs.

Base URL:

`https://feed.feralfile.com/api/v1`

## Hosted vs self-hosted

- Hosted (this page): managed endpoint at `feed.feralfile.com`
- Self-hosted: run your own open-source reference feed operator ([`display-protocol/dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2)) in your infrastructure

If you need full control, use [Run your own Feed Server](self-hosted-feed.md).

## Minimal hosted flow

1. Build or prepare a valid DP-1 playlist.
2. Validate first with [dp1-cli](dp1-cli.md) (public beta).
3. POST to hosted feed.
4. Retrieve by ID or slug.

Example POST:

```bash
curl -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json" \
  -X POST https://feed.feralfile.com/api/v1/playlists \
  -d @playlist.json
```

## API reference source

- Canonical feed server OpenAPI: <https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml>

## Notes

- DP-1 is protocol-first and vendor-neutral; the hosted feed is one deployment option.
- The open-source reference operator repo is not the same thing as Feral File's hosted production feed service.
- If you need deployment details, storage model, or infrastructure tuning, use the open implementation docs in [`display-protocol/dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2).

## Next step

If you want your own deployment, follow [Run your own Feed Server](self-hosted-feed.md).
