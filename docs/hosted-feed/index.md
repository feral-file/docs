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

If you need full control, use [run your own using `dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2#quick-start).

## Authentication

Reads (retrieve a playlist by ID or slug) require no authentication.

Writes authenticate one of two ways, per the [feed OpenAPI spec](https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml):

- **Signed playlist (the public path).** A request whose body carries a non-empty, verifiable `signatures[]` array is accepted on its signatures alone — no API key needed. The server verifies the signatures before persisting anything.
- **API key** (`Authorization: Bearer <key>`). On the hosted feed this key is preconfigured server infrastructure; Feral File does not issue API keys. Use the signed-playlist path instead, or run your own feed where you configure your own key.

DELETE and registry operations always require the API key, so they are not publicly available on the hosted feed.

## Minimal hosted flow

1. Build and sign a DP-1 playlist (`ff-cli sign`, or [dp1-cli](https://github.com/display-protocol/dp1-cli/blob/main/docs/quickstart.md), public beta).
2. Validate it with dp1-cli.
3. POST it to the hosted feed — the signatures authenticate the request.
4. Retrieve by ID or slug.

Example POST:

```bash
curl -H "Content-Type: application/json" \
  -X POST https://feed.feralfile.com/api/v1/playlists \
  -d @signed-playlist.json
```

## API reference source

- Canonical feed server OpenAPI: <https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml>

## Notes

- DP-1 is protocol-first and vendor-neutral; the hosted feed is one deployment option.
- The open-source reference operator repo is not the same thing as Feral File's hosted production feed service.
- If you need deployment details, storage model, or infrastructure tuning, use the open implementation docs in [`display-protocol/dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2).

## Next step

If you want your own deployment, follow [run your own using `dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2#quick-start).
