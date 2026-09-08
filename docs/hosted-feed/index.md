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

Reads (retrieve a playlist, playlist-group, or channel by ID or slug) require no authentication.

Writes are authenticated by the cryptographic signatures in the request body. There is no API key: the feed removed it, and neither sends nor accepts an `Authorization` header. The server verifies the signatures before persisting anything, per the [feed OpenAPI spec](https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml).

- **Create (`POST`)** is open to anyone. The body must carry a non-empty, verifiable `signatures[]` array, and at least one signature must come from the document's owner acting in the owner role — `curator` for playlists and playlist-groups, `publisher` for channels. The `curators[]` / `publisher` fields are optional; a document that declares neither must carry exactly one owner-role signature, and that key becomes the owner.

    Prefer a browser to a terminal? [DP-1 Publisher](https://publisher.feralfile.com) handles this flow for you: sign a playlist with your wallet and publish it to the hosted feed. It is an early release — feedback to [support@feralfile.com](mailto:support@feralfile.com) is welcome.
- **Update (`PUT`)** replaces the whole document. The body pairs the full re-signed document with a signed `authorization` intent that binds the change to this resource and expires, so a previously published document cannot be replayed to roll a resource back. There is no `PATCH`.
- **Delete (`DELETE`)** takes a signed delete-intent from an owner. Deleted IDs are tombstoned and cannot be recreated under the same ID.

Only an owner can update or delete a resource: a key the stored document names in `curators[]` / `publisher`, or — when it declares neither — its single owner-role signer.

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
