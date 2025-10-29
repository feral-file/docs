# Self-Hosting a DP-1 Feed
This guide walks you through setting up a DP-1 feed server so you can publish your own playlists for [FF1](../ff1/index.md).

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

## 2. Choose Your Setup Method

You can run the DP1 feed server in two ways:

### 🐳 **Method A: Full Docker Setup (Recommended)**
Everything runs in Docker - dependencies and server. No `.env` file needed.

### ⚙️ **Method B: Manual Node.js Development**  
Server runs directly with Node.js. Requires `.env` setup.
Run dependencies (etcd and NATS) using Docker (recommended), or set them up manually if you prefer.

---

## Method A: Full Docker Setup

### Run Everything with Docker
```bash
# Start all services (etcd, NATS, and dp1-feed server)
docker compose up -d

# → Server runs at http://localhost:8787
```

**That's it!** Docker Compose includes pre-configured development secrets (`test-api-secret`, `test-ed25519-private-key`).

> **Security note:** The provided secrets are for development only. **Never use these values in production.** Always generate strong, unique secrets for any publicly accessible deployment.  
> See [Security note](#5-security-notes) below for details.

Health check:
```bash
curl http://localhost:8787/api/v1/health
# {"status":"ok"}
```

Skip to [Post Your First Playlist](#3-post-your-first-playlist) →

---

## Method B: Manual Node.js Development

### B.1. Start Dependencies Only

Option a. Docker Compose. Start only etcd and NATS in Docker
```bash
docker compose up -d etcd nats
```

Option b. Manual setup

```bash
# Start etcd (terminal tab no.1)
etcd --listen-client-urls http://0.0.0.0:2379 --advertise-client-urls http://localhost:2379

# Start NATS with JetStream (terminal tab no.2)
nats-server -js

# Open terminal tab no.3 to run server
```

### B.2. Configure Environment
Create your development `.env` file:

```bash
cp .env.sample .env
```

Edit `.env` to set secrets. See [Security note](#5-security-notes) below for details.

### B.3. Run Node.js Server
```bash
# Start dev server with live reload
npm run node:dev

# Or start production build
npm run node:build
npm run node:start

# → http://localhost:8787
```

Health check:
```bash
curl http://localhost:8787/api/v1/health
# {"status":"ok"}
```

## 3. Post Your First Playlist

Both methods use the same API. Use the development secret `test-api-secret`:

```bash
curl -H "Authorization: Bearer test-api-secret" \
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

_For more endpoints and request/response details, visit the [API Reference](feed-server.md#api-reference)._

### Generate Playlists from Your NFT Collection

Instead of manually creating playlist JSON, you can use the **FF1 CLI** to automatically generate playlists from your existing NFT data:

```bash
# Generate playlist from specific NFT tokens
ff1-cli$ npm run dev -- chat "Get tokens 1,2,3 from Ethereum contract 0xabc" -o playlist.json

# Generate from your wallet address
ff1-cli$ npm run dev -- chat "Build a playlist from my Ethereum address 0x..." -o playlist.json
```

Then post the generated playlist to your feed server:
```bash
curl -H "Authorization: Bearer test-api-secret" \
     -H "Content-Type: application/json" \
     -X POST http://localhost:8787/api/v1/playlists \
     -d @playlist.json
```

→ **[Learn more about FF1 CLI](../api-reference/cli.md)** - Generate playlists from NFT data using AI or deterministic parameters

## 4. Troubleshooting

- **401 Unauthorized** → Missing or incorrect `Authorization: Bearer test-api-secret` header
- **No signatures[]** → Server signing not configured. Check your setup (see [Security Notes](#5-security-notes))
- **Port in use**: Another process may be running on port 8787. You can:
    - Change the `PORT` variable, e.g. `PORT=8788 npm run dev`, then restart the server.
    - Or stop the existing process using port 8787 (`npx kill-port 8787` or by killing it in your task manager).
    - On Windows, you can check with `netstat -ano | findstr :8787` to identify and terminate the process.
    - On macOS/Linux, use `lsof -i :8787` and `kill <PID>`.
    - Verify Docker or other services aren’t conflicting with your chosen port.
    - Restart your computer if you're unsure what's using the port.

## 5. Security Notes

### Development vs Production Secrets

**For local testing**: The provided placeholder values (`test-api-secret`, `test-ed25519-private-key`) are fine.

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


---

## 6. (Optional) Cloudflare Worker Deploy

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

Once your feed server is running, try to:

→ **[Cast Playlists to FF1](../ff1/how-it-works/casting-playlists.md)** - Preview your playlists on FF1 devices before tokenizing
