# Run Your Own Feed Server

This page is for running your own DP-1 feed operator using the open-source reference implementation.

- What this is: a practical operator path for self-hosted DP-1 feeds.
- Why use it: full control over deployment, auth secrets, and signing keys.
- What to do next: run a local operator and complete one create/fetch cycle.

## Operator source of truth

- Reference operator repo: <https://github.com/display-protocol/dp1-feed>
- Canonical OpenAPI: <https://github.com/display-protocol/dp1-feed/blob/main/openapi.yaml>

This page covers operator usage only. It is separate from Feral File's hosted production feed service.

## Version and compatibility note

- Canonical DP-1 protocol spec is currently `v1.1.0`: <https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md>
- Current operator examples are often centered on `dpVersion: 1.0.0`.
- Treat those examples as practical implementation baselines, not blanket ecosystem parity claims.

## Quick local run (Node + Docker)

Prerequisites:

- Node.js 22+
- Docker + Docker Compose

```bash
git clone https://github.com/display-protocol/dp1-feed.git
cd dp1-feed
npm install
docker compose up -d
```

The API is available at `http://localhost:8787`.

## First trust-building cycle

1. Health check

```bash
curl http://localhost:8787/api/v1/health
```

2. Create playlist

```bash
curl -X POST http://localhost:8787/api/v1/playlists \
  -H "Authorization: Bearer dev-api-secret" \
  -H "Content-Type: application/json" \
  -d @playlist.json
```

3. Fetch created playlist

```bash
curl http://localhost:8787/api/v1/playlists/<playlist-id-or-slug>
```

If you need to generate playlists quickly, use [FF1 CLI: Start Here](../api-reference/cli.md), then post the result to your operator.

## Security essentials

- Keep `API_SECRET` and `ED25519_PRIVATE_KEY` out of source control.
- Use generated secrets for any non-local deployment.
- Rotate secrets when moving from local dev to shared environments.

## Next step

Compare self-hosted and managed usage in [Hosted Feed (Feral File)](feed-server.md).
