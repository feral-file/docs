# LLM & Agents Quickstart

This section is for teams building LLM or agent tooling around Feral File APIs.

It is a support layer, not a separate product track.

- What this is: a thin setup guide for tool-calling with Feral File APIs.
- Why use it: connect an agent safely without duplicating protocol or CLI logic.
- What to do next: choose ff-cli or DP-1 as your primary execution path.

## What this is for

- Connect an LLM tool to OpenAPI endpoints.
- Keep calls deterministic and small.
- Route execution to the right primary docs path.

## Use these primary paths

- Playlist generation and playback workflows: [ff-cli: Start Here](../api-reference/cli.md)
- Protocol correctness, schemas, dp1-cli (validation and signing; public beta), and feeds: [DP-1: Start Here](../dp1-protocol/overview.md)

## Minimal setup

1. Import OpenAPI schema:
   - `https://feralfile.com/.well-known/openapi.json`
2. Add system instructions that keep requests scoped and explicit.
3. Keep request limits small to avoid oversized context and unstable outputs.
4. Validate generated playlist payloads with [DP-1 CLI quickstart](../dp1-protocol/dp1-cli.md) (**public beta**).

If your agent should run ff-cli directly, use this ready prompt as your starting point:

- <https://github.com/feral-file/ff-cli/blob/main/skills/ff-control/SKILL.md>

This keeps the flow simple: status -> config validate -> build -> validate -> send/publish, and reports failing command + code when a step breaks.

## Guardrails

- Do not treat this section as a replacement for CLI docs.
- Do not duplicate DP-1 schema or feed operation docs in agent prompts.
- Keep protocol operations in DP-1 pages and command workflows in ff-cli pages.
- Do not claim end-to-end DP-1 `v1.1.0` parity across all tools unless verified in upstream repos.

## Next step

Choose your execution path: [ff-cli first run](../api-reference/cli.md) or [DP-1 integrator start](../dp1-protocol/overview.md).
