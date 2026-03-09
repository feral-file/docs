# FF1 CLI: Start Here

FF1 CLI is a command-line tool that builds DP-1 playlists from NFT and feed data.

Use it when you want the shortest path from a prompt to visible playback on an FF1 art computer.

- What this is: the primary command workflow for building and sending playlists.
- Why use it: fastest route from prompt to play on FF1 reference hardware.
- What to do next: run the first success flow below.

## Version note

Examples in this page align with current FF1 CLI behavior, which builds playlists with `dpVersion: 1.0.0`.

The canonical DP-1 specification is currently `v1.1.0` and adds multi-signature support via `signatures`.

FF1 CLI currently emits `dpVersion: 1.0.0` with legacy top-level `signature` behavior in its default playlist flow.

Use your toolchain's supported version and verify against the canonical spec before production use.

## First success in minutes

This path uses the canonical commands from `feral-file/ff1-cli`.

```bash
# 1) Install (shortest path)
npm i -g ff1-cli

# 2) Run guided setup
ff1 setup

# 3) Build one playlist
ff1 chat "Get tokens 1,2,3 from Ethereum contract 0xabc" -o playlist.json

# 4) Validate playlist
ff1 validate playlist.json

# 5) If your device is configured, play on FF1
ff1 send playlist.json -d "Living Room Display"
```

You are successful when `playlist.json` validates and, if a device is available, the playlist plays on FF1.

## Install options

### Primary

```bash
npm i -g ff1-cli
```

### Alternate: prebuilt binary installer

```bash
curl -fsSL https://feralfile.com/ff1-cli-install | bash
```

### Alternate: one-off with npx

```bash
npx ff1-cli setup
npx ff1-cli chat
```

### Manual configuration path (advanced)

If you are scripting setup or need direct config actions:

```bash
ff1 config init
ff1 config validate
```

## Commands by job

- Build playlist from natural language: `ff1 chat [content]`
- Build playlist from deterministic params: `ff1 build [params.json]`
- Validate a playlist file or URL: `ff1 validate <file-or-url>`
- Sign a playlist: `ff1 sign <file>`
- Send a playlist to FF1: `ff1 send <file-or-url>`
- Play a direct media URL: `ff1 play <url>`
- Publish to feed server: `ff1 publish <file>`
- Configure and inspect setup: `ff1 config <init|show|validate>`

## Copy-paste examples

### Build from natural language

```bash
ff1 chat "Get token 42 from Tezos contract KT1abc" -o playlist.json
```

### Build without AI

```bash
ff1 build ./params.json -o playlist.json
```

### Validate, then play

```bash
ff1 validate playlist.json
ff1 send playlist.json -d "Living Room Display"
```

## Common failure points

- `config validate` fails: run `ff1 config show`, fix API keys and model settings, then re-run validation.
- `chat` fails with provider/auth errors: confirm provider API key env vars or `config.json` values.
- `send` cannot find device: check device host/name in config and make sure FF1 is reachable on your network.
- `send` version error: FF1 OS is below minimum supported version for that command; update FF1 OS and retry.
- Signature expectations differ by toolchain: many current CLI flows produce legacy top-level `signature` instead of `signatures[]`.

## Deeper references

- Full usage and workflow docs: <https://github.com/feral-file/ff1-cli/blob/main/docs/README.md>
- Configuration reference: <https://github.com/feral-file/ff1-cli/blob/main/docs/CONFIGURATION.md>
- Function-calling details: <https://github.com/feral-file/ff1-cli/blob/main/docs/FUNCTION_CALLING.md>
- More examples: <https://github.com/feral-file/ff1-cli/blob/main/docs/EXAMPLES.md>
- DP-1 protocol spec: <https://github.com/display-protocol/dp1/blob/main/docs/spec.md>
- DP-1 validator behavior: <https://github.com/display-protocol/dp1-validator>

## Next step

Run the FF1 bridge flow: [From valid DP-1 playlist to FF1 playback](../dp1-protocol/ff1-integration.md).
