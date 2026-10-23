# Hosted Feed (Feral File)

This page covers the hosted DP-1 feed operated by Feral File.

Use it when you want a managed endpoint instead of running your own feed server.

- What this is: hosted feed usage guidance for Feral File-managed infrastructure.
- Why use it: quickest managed path to publish and retrieve playlists and channels.
- What to do next: validate a payload, then POST to the hosted endpoint.

## What this is

The hosted feed accepts DP-1 playlists, playlist-groups, and channels, validates payloads, and serves them over HTTP APIs.

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

## Publish a channel

A channel is a signed, ordered list of playlist URLs under one publisher ([channel extension spec](https://github.com/display-protocol/dp1/blob/main/extensions/channels/channel.md)). The publisher signature covers those URLs, so publish the playlists first and sign the channel once they have their final URLs. One publisher key can sign several channels.

In a browser, [DP-1 Publisher](https://publisher.feralfile.com) publishes channels too, signing with your wallet as `publisher`. It strips any signatures already on a pasted document and signs again with the connected wallet.

From a terminal, [dp1-cli](https://github.com/display-protocol/dp1-cli/blob/main/docs/quickstart.md) signs with an Ed25519 key. This sequence was run end to end with dp1-cli v2.0.0-beta.3 against a local [dp1-feed-v2](https://github.com/display-protocol/dp1-feed-v2) v1.2.0:

1. Set up a signing key. The key that signs a channel as `publisher` owns it: only that key can replace or delete the channel, so keep a copy of it off this machine. Check for a saved key first:

    ```bash
    dp1-cli key show
    ```

    If it prints a `did:key`, use that key. If it reports no signing key, create one:

    ```bash
    dp1-cli key generate --save-config
    ```

    `--save-config` writes the private key to `~/.dp1/config.yaml`, replacing any key already saved there. If you keep the key elsewhere, pass `--private-key` or set `DP1_PRIVATE_KEY` when you sign.

2. Sign, verify, and publish each playlist. Start from an unsigned playlist with a `slug`. The feed requires the slug (`400 bad_request — slug is required`). `sign` keeps any signatures already in the file, so delete placeholder or stale ones first; the dp1-cli quickstart sample carries a placeholder.

    ```bash
    dp1-cli playlist sign playlist.json
    dp1-cli playlist verify playlist.json
    dp1-cli playlist publish playlist.json --feed-url https://feed.feralfile.com
    ```

    The playlist's URL is `https://feed.feralfile.com/api/v1/playlists/<slug>`; its ID works in place of the slug.

3. Write `channel.json`, listing the playlist URLs in the order you want them:

    ```json
    {
      "id": "<UUID v4>",
      "slug": "my-channel",
      "title": "My Channel",
      "version": "1.0.0",
      "created": "2026-10-22T00:00:00Z",
      "summary": "One or two sentences about the channel.",
      "publisher": {
        "name": "My Organization",
        "key": "<your did:key>",
        "url": "https://example.com"
      },
      "playlists": [
        "https://feed.feralfile.com/api/v1/playlists/<slug>"
      ]
    }
    ```

    `version` is the channel extension version, `1.0.0`, not a version number for your channel. Give each channel its own `id` and `slug`: `publish` creates, and reusing either returns `409 conflict`.

4. Sign, verify, and publish the channel:

    ```bash
    dp1-cli channel sign channel.json
    dp1-cli channel verify channel.json
    dp1-cli channel publish channel.json --feed-url https://feed.feralfile.com
    ```

    The feed adds its own `feed` signature and serves the channel at `https://feed.feralfile.com/api/v1/channels/<slug>`.

Before you publish:

- `--feed-url` takes the host only. dp1-cli appends `/api/v1/...` itself, so a URL ending in `/api/v1` returns 404.
- The feed rejects any field it does not recognize (`400 bad_request — json: unknown field`), even when `dp1-cli channel validate` or `dp1-cli playlist validate` passes. Remove the field, sign again, and publish.
- `feed.feralfile.com` is production, and there is no staging feed. To rehearse, run [dp1-feed-v2](https://github.com/display-protocol/dp1-feed-v2#quick-start) locally and point `--feed-url` at it.

A published channel appears in the Feral File app once Feral File lists it.

## API reference source

- Canonical feed server OpenAPI: <https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml>

## Notes

- DP-1 is protocol-first and vendor-neutral; the hosted feed is one deployment option.
- The open-source reference operator repo is not the same thing as Feral File's hosted production feed service.
- If you need deployment details, storage model, or infrastructure tuning, use the open implementation docs in [`display-protocol/dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2).

## Next step

If you want your own deployment, follow [run your own using `dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2#quick-start).
