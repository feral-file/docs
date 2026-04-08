# Run Your Own Feed Server

This page is for running your own DP-1 feed operator using the open-source reference implementation.

- What this is: a practical operator path for self-hosted DP-1 feeds.
- Why use it: full control over deployment, auth secrets, and signing keys.
- What to do next: run a local operator and complete one create/fetch cycle.

## Operator source of truth

- Reference operator repo: <https://github.com/display-protocol/dp1-feed-v2>
- Canonical OpenAPI: <https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml>

This page covers operator usage only. It is separate from Feral File's hosted production feed service.

## Version and compatibility note

- Canonical DP-1 protocol spec is currently `v1.1.0`: <https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md>
- The `dp1-feed-v2` quick start uses `dpVersion: 1.1.0` in its example request.
- Other tooling in the ecosystem may still emit `dpVersion: 1.0.0`; align to what your stack produces and validate.

## Quick local run (Docker Compose)

Prerequisites:

- Docker + Docker Compose
- Go 1.25+ is only required if you prefer `go run` instead of containers (see the repository README).

```bash
git clone https://github.com/display-protocol/dp1-feed-v2.git
cd dp1-feed-v2
cp config/.env.example config/.env
# Edit config/.env: set DP1_FEED_API_KEY and DP1_FEED_SIGNING_KEY_HEX (see below)
docker compose up --build
```

The API is available at `http://localhost:8787`.

Signing key: generate a 64-character hex string (32 bytes), for example:

```bash
openssl rand -hex 32
```

Put the value in `DP1_FEED_SIGNING_KEY_HEX` in `config/.env`.

## First trust-building cycle

Use the same API key you set as `DP1_FEED_API_KEY` in `config/.env` (export it in your shell as `DP1_FEED_API_KEY` for the commands below).

1. Health check

```bash
curl http://localhost:8787/health
```

2. Create playlist

```bash
curl -X POST http://localhost:8787/api/v1/playlists \
  -H "Authorization: Bearer ${DP1_FEED_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "dpVersion": "1.1.0",
    "title": "My First Playlist",
    "items": [{
      "source": "https://example.com/video.mp4",
      "duration": 30000,
      "license": "open"
    }]
  }'
```

3. Fetch created playlist

```bash
curl http://localhost:8787/api/v1/playlists/<playlist-id-or-slug>
```

If you need to generate playlists quickly, use [FF1 CLI: Start Here](../api-reference/cli.md), then post the result to your operator.

## Security essentials

- Keep `DP1_FEED_API_KEY` and `DP1_FEED_SIGNING_KEY_HEX` out of source control.
- Use generated secrets for any non-local deployment.
- Rotate secrets when moving from local dev to shared environments.

## Next step

Compare self-hosted and managed usage in [Hosted Feed (Feral File)](feed-server.md).
