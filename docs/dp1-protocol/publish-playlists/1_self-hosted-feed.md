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

## 2. Start local deps

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

### Option A: Docker Compose Setup (Recommended for Testing)

- The `docker-compose.yml` file includes pre-configured development values (Uses placeholder secrets: `dev-api-secret` and `dev-ed25519-private-key`)
- No .env file needed for local testing

⚠️ **For production**: Replace these placeholder values with real secrets (see [Security Notes](#security-notes) below).

### Option B: Manual Setup (without Docker)

Create a `.env` file in the project root:
```typescript
# Security (replace with real values for production)
API_SECRET=dev-api-secret                     # protects write endpoints
ED25519_PRIVATE_KEY=dev-ed25519-private-key   # server signing key

# Dependencies
ETCD_ENDPOINT=http://localhost:2379
NATS_ENDPOINT=nats://localhost:4222
NATS_STREAM_NAME=DP1_WRITE_OPERATIONS
NATS_SUBJECT_NAME=dp1.write.operations

# Optional
ENVIRONMENT=development
```

⚠️ **For production**: Replace `dev-api-secret` and `dev-ed25519-private-key` with real secrets (see [Security Notes](#security-notes) below).

## Security Notes

### Development vs Production Secrets

**For local testing**: The provided placeholder values (`dev-api-secret`, `dev-ed25519-private-key`) are fine.

**For production**: You MUST replace these with real secrets:

### Generate Production Secrets

**API_SECRET** - Protects write endpoints from unauthorized access:
```bash
openssl rand -hex 32
# Use this entire string as your API_SECRET
```

**ED25519_PRIVATE_KEY** - Signs playlists cryptographically:
```bash
openssl genpkey -algorithm ED25519 -outform DER | xxd -p -c 256
# Use this entire hex string as your ED25519_PRIVATE_KEY
```

### Security Best Practices

- Generate fresh secrets.
- Store them in a secrets manager (Vault, AWS Secrets Manager, Cloudflare secrets, etc.).
- Never commit .env files with real keys to GitHub.

## 4. Run the server

```bash
# build once
npm run node:build

# dev server (auto-reload)
npm run node:start:dev

# → http://localhost:8787
```

Health check:

```bash
curl http://localhost:8787/api/v1/health
# {"status":"ok"}
```

## 5. Post your first playlist

To post and retrieve playlists, you'll use the DP-1 Feed server's REST API.

**POST** `/playlists`

Submit a new one—we validate, sign, and store it.

```bash
curl -H "Authorization: Bearer your-api-key-here" \
     -H "Content-Type: application/json" \
     -X POST http://localhost:8787/api/v1/playlists \
     -d @playlist.json
```

**Request Body Example:**
```json
{
  "dpVersion": "1.0.0",
  "title": "Digital Art Showcase",
  "defaults": {
    "display": {
      "scaling": "contain",
      "background": "#000000",
      "margin": 0
    }
  },
  "items": [
    {
      "duration": 30,
      "license": "open",
      "source": "ipfs://cid",
      "provenance": {
        "type": "onChain",
        "contract": {
          "chain": "ethereum",
          "standard": "ERC-721",
          "address": "0x...",
          "tokenId": "1"
        }
      }
    }
  ]
}
```

_For more endpoints and request/response details, visit the [API Reference](../../dp1-protocol/feed-server.md#api-reference)._

## 6. Troubleshooting

- **401 Unauthorized** → Missing or incorrect `Authorization: Bearer <API_SECRET>` header

- **No signatures[]** → Server signing not configured. Check your `ED25519_PRIVATE_KEY` is set correctly (see [Security Notes](#security-notes))

- **Port in use** → set PORT=8788 and restart.

- **Deps not up** → docker compose ps (you should see etcd + NATS running).

---
## (Optional) Cloudflare Worker Deploy

For public deployment, you can use [Cloudflare Workers](https://github.com/display-protocol/dp1-feed/blob/main/DEVELOPMENT.md#cloudflare-workers-development)

```bash
# Set secrets (use real values from Security Notes section)
npm run worker:setup:secrets

# Start with live reload
npm run worker:dev

# Deploy
npm run worker:deploy
```

## What's Next?

Once your feed server is running, proceed to:

→ [Add Your Feed in FF1 App](2_add-feed-in-app.md) - Connect your feed URL so FF1 can fetch and play your playlists

→ [Get Starred by Curators](3_curator-stars-playlist.md) - Learn about curator endorsements
