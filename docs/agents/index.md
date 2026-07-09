# Agents Quickstart

## Paste this into your coding agent

Hover over the prompt and click the copy button in its top-right corner:

```{ .text .copy-prompt }
Read https://docs.feralfile.com/agents/ and set me up to play artwork on my Art Computer.
```

Your agent runs the setup below. Works in Claude Code, Codex, Cursor, OpenCode, or any agent that can shell out.

## Setup (the agent runs this)

Run these in order. On any non-zero exit, stop and report the failing command and exit code — don't paper over errors.

1. **Install `ff-cli`:**
   ```bash
   curl -fsSL https://feralfile.com/ff-cli-install | bash
   ```
   Use `npm i -g @feralfile/cli` instead if the user prefers a Node-managed install.

2. **Install the `ff-control` skill so the agent surfaces it automatically next time.**
   For Claude Code:
   ```bash
   git clone --depth=1 https://github.com/feral-file/ff-cli /tmp/ff-cli \
     && mkdir -p ~/.claude/skills \
     && cp -r /tmp/ff-cli/skills/ff-control ~/.claude/skills/
   ```
   For Codex:
   ```bash
   git clone --depth=1 https://github.com/feral-file/ff-cli /tmp/ff-cli \
     && mkdir -p ~/.codex/skills \
     && cp -r /tmp/ff-cli/skills/ff-control ~/.codex/skills/
   ```

3. **Configure:**
   ```bash
   ff-cli setup
   ```
   Interactive, and quick — ff-cli needs no LLM API key. Setup just configures the signing key and the user's Art Computer.

4. **Add the user's Art Computer.** Ask the user for the device's IP address or hostname, then register it directly:
   ```bash
   ff-cli device add --host http://<device-ip>:1111 --name "<name>"
   ```
   Bare `ff-cli device add` attempts mDNS discovery instead, but mDNS is unreliable across subnets and often blocked on managed networks — prefer the explicit host. Setting up on a museum, office, or campus network? See [Network Requirements](../art-computer/network-requirements.md).

5. **Run what the user asked for.** Most common starting point:
   ```bash
   ff-cli find <url-or-wallet-from-user> --play
   ```
   `ff-cli find` accepts marketplace URLs (Art Blocks, Objkt, fxhash, OpenSea, SuperRare, Feral File, Neort), raw on-chain coords (`ethereum:0x…:tokenId`, `tezos:KT1…:tokenId`), and wallet addresses.

## What's actually here

- **[ff-cli](../ff-cli/index.md)** — build playlists, play artwork, publish feeds. The action surface.
- **[dp1-cli](https://github.com/display-protocol/dp1-cli/blob/main/docs/quickstart.md)** (public beta) — validate, sign, and publish DP-1 protocol payloads.
- **Exhibitions OpenAPI** — `https://feralfile.com/.well-known/openapi.json`. Read-only endpoints for discovering exhibitions, series, and artworks. Complementary to `ff-cli`, not an alternative.
- **No MCP server today.** Use `ff-cli` (CLI) or the Exhibitions OpenAPI (HTTP).

## On-device agents

OpenClaw and variants ("Claws") run agentic workflows *on* the Art Computer itself — same category as the coding agents above, different deployment shape. Public docs for OpenClaw will land here as it matures.
