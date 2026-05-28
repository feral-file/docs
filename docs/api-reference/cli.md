# ff-cli: Start Here

ff-cli is a command-line tool that builds DP-1 playlists from NFT and feed data.

Use it when you want the shortest path from a prompt to visible playback on an Art Computer.

- What this is: the primary command workflow for building and sending playlists.
- Why use it: fastest route from prompt to play on the Art Computer.
- What to do next: run the first success flow below.

## Version note

ff-cli builds playlists at `dpVersion: 1.1.0` with the multi-signature `signatures[]` envelope, matching the canonical DP-1 specification.

Use your toolchain's supported version and verify against the canonical spec before production use.

## First success in minutes

This path uses the canonical commands from `feral-file/ff-cli`.

```bash
# 1) Install (shortest path)
npm i -g @feralfile/cli

# 2) Run guided setup
ff-cli setup

# 3) Build one playlist
ff-cli chat "Get 3 works from reas.eth" -o playlist.json

# 4) Play on your Art Computer
ff-cli play playlist.json
```

You are successful when the playlist builds and plays on your configured Art Computer.

`ff-cli chat` already performs playlist validation during the build flow, so a separate `validate` command is optional for this first run.

**Already have a URL or address?** Skip the LLM setup and use `ff-cli find` instead:

```bash
ff-cli find https://www.artblocks.io/collection/ringers-by-dmitri-cherniak -o playlist.json
ff-cli play playlist.json
```

See [Find from a URL or address](#find-from-a-url-or-address) below for the full input list.

## Install options

### Primary

```bash
npm i -g @feralfile/cli
```

### Alternate: prebuilt binary installer

```bash
curl -fsSL https://feralfile.com/ff-cli-install | bash
```

### Alternate: one-off with npx

```bash
npx @feralfile/cli setup
npx @feralfile/cli chat
```

### Manual configuration path (advanced)

If you are scripting setup or need direct config actions:

```bash
ff-cli config init
ff-cli config validate
```

## Commands by job

- Build playlist from natural language: `ff-cli chat [content]`
- Build playlist from a URL, on-chain coords, or wallet address: `ff-cli find <input>`
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

### Find from a URL or address

`ff-cli find` takes a marketplace URL, raw on-chain coordinates, or a wallet address and builds a playlist directly. No LLM API key required.

```bash
# Marketplace URL — paste from the artwork or collection page
ff-cli find https://www.artblocks.io/collection/ringers-by-dmitri-cherniak -o playlist.json
ff-cli find https://objkt.com/tokens/hicetnunc/111068 -o playlist.json
ff-cli find https://feralfile.com/exhibitions/artwork/{id} -o playlist.json

# Raw on-chain coordinates
ff-cli find ethereum:0xababababab20053426ad1c782de9ea8444358070:5001410 -o playlist.json
ff-cli find tezos:KT1RJ6PbjHpwc3M5rw5s2Nbmefwbuwbdxton:111068 -o playlist.json

# Wallet address — picks an artwork from the address's catalog
ff-cli find 0xf3860788d1597cecf938424baabe976fac87dc26 -o playlist.json
ff-cli find tz1fQTvvcCy5PTt8HcUSQTu64dH9mJjjDudi -o playlist.json
```

Supported sources: Objkt, fxhash (`/gentk/...`, `/iteration/{slug}`, `/project/{slug}`, `/generative/{slug}`), Art Blocks, OpenSea, SuperRare, Feral File, Neort, plus raw `ethereum:` / `tezos:` coords and `0x…` / `tz1.../tz2.../tz3...` addresses.

Combine with `--play`, `--publish`, or `--output` to skip straight to delivery; see `ff-cli find --help` for the full flag set.

### Build from Feral File feed playlists

Legacy reference (archived `feral-file/dp1-feed`): use exhibition titles from:
<https://github.com/feral-file/dp1-feed/tree/main/playlists>

The current open-source feed implementation is [`display-protocol/dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2); see its [Quick Start](https://github.com/display-protocol/dp1-feed-v2#quick-start) to run your own.

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
- Signature shape across the ecosystem: ff-cli emits the spec-current `signatures[]`, but some other tools still emit the legacy top-level `signature`. If you integrate with multiple tools, verify both forms validate as expected.

## Deeper references

- Full usage and workflow docs: <https://github.com/feral-file/ff-cli/blob/main/docs/README.md>
- Configuration reference: <https://github.com/feral-file/ff-cli/blob/main/docs/CONFIGURATION.md>
- Function-calling details: <https://github.com/feral-file/ff-cli/blob/main/docs/FUNCTION_CALLING.md>
- More examples: <https://github.com/feral-file/ff-cli/blob/main/docs/EXAMPLES.md>
- OpenClaw skill prompt: <https://github.com/feral-file/ff-cli/blob/main/skills/ff-control/SKILL.md>
- DP-1 protocol spec: <https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md>
- DP-1 CLI (**public beta**; validate, sign, verify, publish): <https://github.com/display-protocol/dp1-cli> — **dp1-cli** is the **actively maintained** successor to the legacy **dp1-validator** tag line in that **same repository** (legacy tags are frozen).

## Next step

Run the Art Computer bridge flow: [From valid DP-1 playlist to Art Computer playback](../dp1-protocol/art-computer-integration.md).
