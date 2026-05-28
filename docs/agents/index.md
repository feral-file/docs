# Agents Quickstart

## Paste this into your coding agent

> Read https://docs.feralfile.com/agents/ and set me up to play artwork on my Art Computer.

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
   For Codex, target `~/.codex/skills/` with the same `cp` command.

3. **Configure:**
   ```bash
   ff-cli setup
   ```
   Interactive. An LLM API key is only required for `ff-cli chat` — skip it if the user just wants to play URLs or wallets.

4. **Add the user's Art Computer:**
   ```bash
   ff-cli device add
   ```
   Discovers via mDNS. If discovery fails, ask the user for the device hostname or IP.

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
