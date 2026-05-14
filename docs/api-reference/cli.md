# ff-cli: Start Here

ff-cli is a command-line tool that builds DP-1 playlists from NFT and feed data.

Use it when you want the shortest path from a prompt to visible playback on an Art Computer.

- What this is: the primary command workflow for building and sending playlists.
- Why use it: fastest route from prompt to play on the Art Computer.
- What to do next: run the first success flow below.

## Version note

Examples in this page align with current ff-cli behavior, which builds playlists with `dpVersion: 1.0.0`.

The canonical DP-1 specification is currently `v1.1.0` and adds multi-signature support via `signatures`.

ff-cli currently emits `dpVersion: 1.0.0` with legacy top-level `signature` behavior in its default playlist flow.

Use your toolchain's supported version and verify against the canonical spec before production use.

## First success in minutes

This path uses the canonical commands from `feral-file/ff-cli`.

```bash
# 1) Install (shortest path)
npm i -g ff-cli

# 2) Run guided setup
ff-cli setup

# 3) Build one playlist
ff-cli chat "Get 3 works from reas.eth" -o playlist.json

# 4) Play on your Art Computer
ff-cli play playlist.json
```

You are successful when the playlist builds and plays on your configured Art Computer.

`ff-cli chat` already performs playlist validation during the build flow, so a separate `validate` command is optional for this first run.

## Install options

### Primary

```bash
npm i -g ff-cli
```

### Alternate: prebuilt binary installer

```bash
curl -fsSL https://feralfile.com/ff-cli-install | bash
```

### Alternate: one-off with npx

```bash
npx ff-cli setup
npx ff-cli chat
```

### Manual configuration path (advanced)

If you are scripting setup or need direct config actions:

```bash
ff-cli config init
ff-cli config validate
```

## Commands by job

- Build playlist from natural language: `ff-cli chat [content]`
- Build playlist from deterministic params: `ff-cli build [params.json]`
- Validate a playlist file or URL: `ff-cli validate <file-or-url>`
- Sign a playlist: `ff-cli sign <file>`
- Play a playlist file, playlist URL, or media URL on the Art Computer: `ff-cli play <source>`
- Publish to feed server: `ff-cli publish <file>`
- Manage SSH access on the Art Computer: `ff-cli ssh <enable|disable>`
- List configured devices: `ff-cli device list`
- Add a device (with mDNS discovery): `ff-cli device add`
- Remove a device: `ff-cli device remove <name>`
- Configure and inspect setup: `ff-cli config <init|show|validate>`

## Copy-paste examples

### Build from natural language

```bash
ff-cli chat "Get 3 works from reas.eth" -o playlist.json
ff-cli chat "Get 3 works from einstein-rosen.tez" -o playlist.json
ff-cli chat "Get tokens 52932,52457 from Ethereum contract 0xb932a70A57673d89f4acfFBE830E8ed7f75Fb9e0" -o playlist.json
```

### Build from Feral File feed playlists

Legacy reference (archived `feral-file/dp1-feed`): use exhibition titles from:
<https://github.com/feral-file/dp1-feed/tree/main/playlists>

The current open-source feed implementation is [`display-protocol/dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2); see [Run your own Feed Server](../dp1-protocol/self-hosted-feed.md).

```bash
ff-cli chat "Get 3 from Unsupervised" -o playlist.json
ff-cli chat "Get 3 from Unsupervised and 2 from reas.eth" -o playlist.json
```

Feed playlist requests depend on configured feed servers and network reachability.

### Build without AI

```bash
ff-cli build ./params.json -o playlist.json
```

### Play on your configured Art Computer

```bash
# Local playlist file
ff-cli play playlist.json

# Hosted playlist URL
ff-cli play "https://cdn.example.com/playlist.json"

# Direct media URL
ff-cli play "https://example.com/video.mp4" --skip-verify
```

## Common failure points

- `config validate` fails: run `ff-cli config show`, fix model settings, then re-run validation. An LLM API key is optional and only required for `ff-cli chat`.
- `chat` fails with provider/auth errors: confirm provider API key env vars or `config.json` values.
- `play` cannot find device: check device host/name in config and make sure the Art Computer is reachable on your network.
- `play` version error: FF1 OS is below minimum supported version for that command; update FF1 OS and retry.
- Signature expectations differ by toolchain: many current CLI flows produce legacy top-level `signature` instead of `signatures[]`.

## Deeper references

- Full usage and workflow docs: <https://github.com/feral-file/ff-cli/blob/main/docs/README.md>
- Configuration reference: <https://github.com/feral-file/ff-cli/blob/main/docs/CONFIGURATION.md>
- Function-calling details: <https://github.com/feral-file/ff-cli/blob/main/docs/FUNCTION_CALLING.md>
- More examples: <https://github.com/feral-file/ff-cli/blob/main/docs/EXAMPLES.md>
- OpenClaw skill prompt: <https://github.com/feral-file/ff-cli/blob/main/skills/ff-control/SKILL.md>
- DP-1 protocol spec: <https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md>
- DP-1 validator behavior: <https://github.com/display-protocol/dp1-validator>

## Next step

Run the Art Computer bridge flow: [From valid DP-1 playlist to Art Computer playback](../dp1-protocol/art-computer-integration.md).
