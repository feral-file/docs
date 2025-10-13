# Self-Hosting a DP-1 Feed
This guide walks you through setting up a DP-1 feed server so you can publish your own playlists for FF1.

> Goal: run a feed on http://localhost:8787, protect write endpoints with API_SECRET, and server-sign playlists with an Ed25519 private key.

## 0. Prerequisites

- Node.js 22+
- Git
- Docker Desktop (recommended, for dependencies etcd + NATS JetStream)

```bash
node -v
docker -v
```

Optional: Cloudflare Workers account if you want to deploy publicly.

## 1. Clone and install

```bash
git clone https://github.com/display-protocol/dp1-feed.git
cd dp1-feed
npm install
```

> Most users should clone. Fork only if you plan to modify and publish your version

## 2. Start local deps (1 command)

### Option A: Docker Compose (recommend)
```bash
docker compose up -d etcd nats
```

### Option B: Manual setup (without Docker)
```bash
# Start etcd
etcd --listen-client-urls http://0.0.0.0:2379 --advertise-client-urls http://localhost:2379

# Start NATS with JetStream
nats-server -js
```

## 3. Configure Environment (one-time setup)
Before running `dp1-feed`, you need to configure environment variables. These tell the server how to authenticate, sign playlists, and connect to its dependencies.

You can run dp1-feed with either Docker Compose (pre-set dev values) or manual .env setup.

### Option A: Docker Compose Setup

- The `docker-compose.yml` file includes pre-configured environment variables for development

- No .env file needed.

⚠️ For production, edit `docker-compose.yml` to replace secrets with real values.

### Option B: Manual Setup (without Docker)

Create a `.env` file in the project root:
```typescript
# Required
API_SECRET=dev-api-secret                     # protects write endpoints
ED25519_PRIVATE_KEY=dev-ed25519-private-key   # server signing key

# etcd configuration
ETCD_ENDPOINT=http://localhost:2379

# NATS JetStream configuration
NATS_ENDPOINT=nats://localhost:4222
NATS_STREAM_NAME=DP1_WRITE_OPERATIONS
NATS_SUBJECT_NAME=dp1.write.operations

# Optional
ENVIRONMENT=development
```

### How to generate keys

**API_SECRET** → any strong random string. Example:

```bash
openssl rand -hex 32
# Use this value in place of dev-api-secret.
```

**ED25519_PRIVATE_KEY** → generate an Ed25519 keypair. Example:

```bash
openssl genpkey -algorithm ED25519 -outform DER | xxd -p -c 256
```

**⚠️ Important:**
Use the provided dev values only for local testing. For production:

- Generate fresh secrets.
- Store them in a secrets manager (Vault, AWS Secrets Manager, Cloudflare secrets, etc.).
- Never commit .env files with real keys to GitHub.

## 4. Run the server

```bash
# build once
npm run node:build

# dev server (auto-reload)

npm run node:start:dev
# or config with .env manually
npm run node:start:dev:with-env

# → http://localhost:8787
```

Health check:

```bash
curl http://localhost:8787/api/v1/health
# {"status":"ok"}
```

## 5. Post your first playlist (signed by the server)

Create `playlist.json`:

```json
{
  "dpVersion": "1.0.0",
  "title": "my-first-playlist",
  "items": [
    { "source": "https://example.com/art.html", "kind": "html", "duration": 300 }
  ]
}
```

POST (note the Bearer token):

```bash
curl -X POST http://localhost:8787/api/v1/playlists \
  -H "Authorization: Bearer $API_SECRET" \
  -H "Content-Type: application/json" \
  -d @playlist.json | jq .
```

Fetch all playlists (should now include a signatures[] entry the server added):

```bash
curl -s http://localhost:8787/api/v1/playlists | jq .
```

## 6. Troubleshooting

- **401 Unauthorized** → you didn’t send the header: `Authorization: Bearer <API_SECRET>`.

- **No signatures[]** → server signing isn’t configured. Ensure one of:
    * `SIGNING_PRIVATE_KEY_PATH=/path/to/dp1_signer` or
    * `SIGNING_PRIVATE_KEY_PEM='-----BEGIN PRIVATE KEY----- …'`

- **Port in use** → set PORT=8788 and restart.

- **Deps not up** → docker compose ps (you should see etcd + NATS running).

---
## (Optional) Cloudflare Worker deploy
If you support Workers in your doc, give the 3-step path:

```bash
# set secrets once
npx wrangler secret put API_SECRET
npx wrangler secret put SIGNING_PRIVATE_KEY_PEM   # paste PEM

# deploy
npm run worker:deploy
```

## What's Next?

Once your feed server is running, proceed to:

→ [Add Your Feed in FF1 App](2_add-feed-in-app.md) - Connect your feed URL so FF1 can fetch and play your playlists

→ [Get Starred by Curators](3_curator-stars-playlist.md) - Learn about curator endorsements
