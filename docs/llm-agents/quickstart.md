# LLM & Agents Quickstart

This page is for developers using coding agents — **Claude Code, Codex, Cursor, OpenCode** — who want to drive Feral File from a chat.

If you're integrating an autonomous backend service, the same surfaces apply; the recipes below just use a coding agent because that's the shortest path to seeing it work.

## TL;DR

- Install `ff-cli`. Your agent already knows how to call CLIs — that's the whole integration.
- Most useful first command: `ff-cli find <URL or wallet>` — **no LLM key required**.
- For deterministic flow, paste the [ff-control skill](https://github.com/feral-file/ff-cli/blob/main/skills/ff-control/SKILL.md) into your agent's system prompt.

## Pick the right surface

| You want to... | Use |
|---|---|
| Make a playlist and play it on an Art Computer | [**ff-cli**](../api-reference/cli.md) |
| Validate, sign, or publish DP-1 protocol payloads | [**dp1-cli**](../dp1-protocol/dp1-cli.md) (public beta) |
| Wire a custom HTTP client (Python, Go, your own agent) | **OpenAPI schema** (below) |

## Five-minute first win

In your terminal:

```bash
npm i -g @feralfile/cli
ff-cli setup
```

Then in **Claude Code, Codex, Cursor, or any coding agent**, paste:

> Use ff-cli to make a playlist from <https://www.artblocks.io/collection/ringers-by-dmitri-cherniak> and play it on my Art Computer.

The agent will run `ff-cli find` → `ff-cli play`. That's the integration.

For more `find` inputs (wallets, on-chain coords, other marketplaces), see [Find from a URL or address](../api-reference/cli.md#find-from-a-url-or-address).

## Tighter control: drop in the ff-control skill

If you want the agent to follow a deterministic flow and report failures concisely, give it the ff-control prompt:

<https://github.com/feral-file/ff-cli/blob/main/skills/ff-control/SKILL.md>

How to install:

- **Claude Code** — drop the skill directory into your user skills:
  ```bash
  git clone --depth=1 https://github.com/feral-file/ff-cli /tmp/ff-cli \
    && mkdir -p ~/.claude/skills \
    && cp -r /tmp/ff-cli/skills/ff-control ~/.claude/skills/
  ```
  Claude Code will surface it automatically when you ask about playlists, Art Computer playback, or publishing.
- **Codex** — paste the body of `SKILL.md` into your project's `AGENTS.md`. Codex reads `AGENTS.md` natively.
- **Cursor / OpenCode** — paste the body into `.cursor/rules/` or the equivalent system-prompt slot for your tool.
- **Any other agent** — use it as the system prompt for that conversation.

It validates config, builds, validates the playlist, and sends or publishes — surfacing the failing command + exit code on any error. See [`SKILL.md`](https://github.com/feral-file/ff-cli/blob/main/skills/ff-control/SKILL.md) for the exact prompt.

## OpenAPI schema (for custom HTTP clients)

If you're not using `ff-cli` — e.g. you're writing a Python integration, wiring an HTTP tool into a custom agent, or generating a client — import:

```
https://feralfile.com/.well-known/openapi.json
```

Most agent frameworks accept an OpenAPI URL as a tool spec; feed it in and the model gets typed call signatures. Keep requests scoped and explicit, and validate generated DP-1 payloads with [dp1-cli](../dp1-protocol/dp1-cli.md) before publishing.

## What about MCP?

There is **no Feral File MCP server today**. Use `ff-cli` (CLI calls — which any coding agent handles natively) or the OpenAPI schema (HTTP) instead.

## What people build

- **"Play this URL"** — paste a marketplace URL, get playback: `ff-cli find <url> --play`
- **"Make a playlist from this wallet"** — `ff-cli find <address>`
- **Daily auto-curated exhibition** — agent + `ff-cli chat` + `ff-cli publish` on a cron
- **Pre-publish validation** — `dp1-cli validate` in CI before signing a feed payload

## Guardrails

- Keep agent prompts small and scoped — large prompts produce unstable outputs.
- Don't duplicate DP-1 schemas or feed-operation docs into your agent prompt; link to them.
- Keep protocol operations in DP-1 pages, command workflows in `ff-cli` pages.
- Don't claim end-to-end DP-1 `v1.1.0` parity unless verified in the upstream repos.

## Next step

- Hands-on with the CLI: [ff-cli first run](../api-reference/cli.md)
- Protocol-side integration: [DP-1 start here](../dp1-protocol/overview.md)
- Validate before publishing: [dp1-cli quickstart](../dp1-protocol/dp1-cli.md)
