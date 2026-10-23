# ff-cli: Start Here

ff-cli is a command-line tool that builds DP-1 playlists from NFT and feed data and plays them on an Art Computer.

Use it when you want the shortest path from a URL, wallet, or set of tokens to visible playback on an Art Computer.

- What this is: the primary command workflow for building, signing, and playing playlists.
- Why use it: fastest route from a link to play on the Art Computer. No LLM API key required.
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

# 3) Build one playlist from an artwork or collection URL (or on-chain coords)
ff-cli find https://www.artblocks.io/collection/ringers-by-dmitri-cherniak -o playlist.json

# 4) Play on your Art Computer
ff-cli play playlist.json
```

You are successful when the playlist builds and plays on your configured Art Computer.

`ff-cli find` validates the playlist as part of the build, so a separate `validate` command is optional for this first run. To build and play in one step, add `--play`:

```bash
ff-cli find https://objkt.com/tokens/hicetnunc/111068 --play
```

**Want natural language?** ff-cli has no built-in chat. Drive it conversationally from a coding agent — Claude Code, Codex, or Cursor — using the `ff-control` skill; the agent translates your request into `ff-cli` commands. See [Agents](../agents/index.md).

## Install options

### Primary

```bash
npm i -g @feralfile/cli
```

### Alternate: installer (no sudo)

Installs the same npm package under `~/.local` and links `ff-cli` into `~/.local/bin`. Use it when a global npm install is refused for permissions. Needs Node.js 22 or newer.

```bash
set -o pipefail; curl -fsSL https://feralfile.com/ff-cli-install | bash && export PATH="$HOME/.local/bin:$PATH"
```

### Alternate: one-off with npx

```bash
npx @feralfile/cli setup
npx @feralfile/cli find https://www.artblocks.io/collection/ringers-by-dmitri-cherniak --play
```

### Manual configuration path (advanced)

If you are scripting setup or need direct config actions:

```bash
ff-cli setup --non-interactive --device-host http://<device-ip>:1111 --device-name "Living Room"
ff-cli config validate
```

Setup runs without prompts whenever stdin is not a terminal. It generates a signing key when none is configured and keeps one that is. `--generate-key`, `--key`, and `--key-file` refuse to replace a configured key, because it owns the playlists you published; `--force` replaces it.

## Commands by job

- Build playlist from an artwork or collection URL, on-chain coords, or an artist's address: `ff-cli find <input>`
- Build playlist from deterministic params, including what a wallet owns: `ff-cli build [params.json]` (`ff-cli build --help` lists the requirement types)
- Validate a playlist file or URL: `ff-cli validate <file-or-url>`
- Sign a playlist: `ff-cli sign <file>`
- Play a playlist file, playlist URL, media URL, or any web page on the Art Computer: `ff-cli play <source>` (`--web` plays a page on a marketplace site as a page)
- Publish to feed server: `ff-cli publish <file>`
- Replace the playlist already stored under this document id, instead of creating a new one: `ff-cli publish <file> --replace`
- Save a published playlist from a feed server (the starting point for `--replace`): `ff-cli fetch <id-or-url>`
- Delete a playlist from a feed server (signed delete; owner key required): `ff-cli unpublish <id-or-url>`
- Manage SSH access on the Art Computer: `ff-cli ssh <enable|disable>`
- List configured devices: `ff-cli device list`
- Add a device: `ff-cli device add --host http://<device-ip>:1111 --name "<name>"` (bare `ff-cli device add` tries mDNS discovery)
- Remove a device: `ff-cli device remove <name>`
- Configure and inspect setup: `ff-cli config <init|show|validate>`

Every command that takes a signing key with `-k, --key <privateKey>` also takes `--key-file <path>`, which reads the same key material from a file instead of the command line. Pass one or the other, not both.

## Owner remote maintenance

For an explicitly enrolled FF1 with firmware containing `feral-tailscale`, `ff-cli` can use the FF1's
Tailscale IPv4 address as its explicit host. Preserve its physical device ID and
existing name when replacing the configured host; there is no automatic
LAN/Tailscale failover. Persistent owner SSH uses port 2222 and remains separate
from `ff-cli ssh`, which manages temporary support access on port 22.

See the [owner-access procedure](https://github.com/feral-file/ffos/blob/36e25cec84505271a7232d6936bb46a19fab5cfd/docs/OWNER_TAILSCALE.md).
Follow the procedure’s full-image installation checks first. If support is
absent, check the normal firmware release channel for availability; enrollment
waits until a version containing owner access is published and installed.

## Copy-paste examples

### Find from a URL or address

`ff-cli find` takes a marketplace URL, raw on-chain coordinates, or an artist's address and builds a playlist directly. No LLM API key required.

```bash
# Marketplace URL — paste from the artwork or collection page
ff-cli find https://www.artblocks.io/collection/ringers-by-dmitri-cherniak -o playlist.json
ff-cli find https://objkt.com/tokens/hicetnunc/111068 -o playlist.json
ff-cli find https://feralfile.com/exhibitions/artwork/{id} -o playlist.json

# Raw on-chain coordinates
ff-cli find ethereum:0xababababab20053426ad1c782de9ea8444358070:5001410 -o playlist.json
ff-cli find tezos:KT1RJ6PbjHpwc3M5rw5s2Nbmefwbuwbdxton:111068 -o playlist.json

# Artist address — plays one work by the artist at that address
# (for what a wallet owns, see "Build from structured params" below)
ff-cli find 0xf3860788d1597cecf938424baabe976fac87dc26 -o playlist.json
ff-cli find tz1fQTvvcCy5PTt8HcUSQTu64dH9mJjjDudi -o playlist.json
```

Supported sources: Objkt, fxhash (`/gentk/...`, `/iteration/{slug}`, `/project/{slug}`, `/generative/{slug}`), Art Blocks, OpenSea, SuperRare, Feral File, Neort, Verse, Raster, plus raw `ethereum:` / `tezos:` coords and `0x…` / `tz1.../tz2.../tz3...` addresses.

Combine with `--play`, `--publish`, or `--output` to skip straight to delivery; see `ff-cli find --help` for the full flag set. In scripts and agents, add `-y`: without a terminal, a question fails with exit 1 and names the flag that answers it.

### Build from structured params

`ff-cli build` takes a JSON parameters file (or stdin) and builds a playlist deterministically — no network guessing, no LLM. It exits 1 when a requirement finds nothing, named `tokenIds` do not all resolve, or the send to `playlistSettings.deviceName` fails. The playlist is still saved when anything was collected.

```bash
ff-cli build ./params.json -o playlist.json
```

What a wallet owns:

```bash
echo '{"requirements":[{"type":"query_address","ownerAddress":"0xf3860788d1597cecf938424baabe976fac87dc26","quantity":5}],"playlistSettings":{"title":"My collection"}}' \
  | ff-cli build -o wallet.json
```

A minimal `params.json` for specific tokens from a contract:

```json
{
  "requirements": [
    {
      "type": "build_playlist",
      "blockchain": "ethereum",
      "contractAddress": "0xb932a70A57673d89f4acfFBE830E8ed7f75Fb9e0",
      "tokenIds": ["52932", "52457"]
    }
  ]
}
```

### Build from Feral File feed playlists

Feed playlists are fetched by name via a `fetch_feed` requirement. Pipe params straight to `ff-cli build`:

```bash
echo '{"requirements":[{"type":"fetch_feed","playlistName":"Unsupervised","quantity":3}]}' \
  | ff-cli build -o playlist.json
```

Feed playlist requests depend on configured feed servers and network reachability. The current open-source feed implementation is [`display-protocol/dp1-feed-v2`](https://github.com/display-protocol/dp1-feed-v2); see its [Quick Start](https://github.com/display-protocol/dp1-feed-v2#quick-start) to run your own.

### Play on your configured Art Computer

```bash
# Local playlist file
ff-cli play playlist.json

# Hosted playlist URL
ff-cli play "https://cdn.example.com/playlist.json"

# Direct media URL
ff-cli play "https://example.com/video.mp4"

# Any web page
ff-cli play "https://example.com/"

# A page on a marketplace site, as a page (play otherwise sends these to find)
ff-cli play --web "https://feralfile.com/"
```

`play` refuses a URL that answers 404 or 410, or whose host does not resolve, so a typo is never cast as an error page.

## Common failure points

- `config validate` fails: run `ff-cli config show`, fix the reported values, then re-run validation.
- `play` cannot find device: check device host/name in config and make sure the Art Computer is reachable on your network. On managed networks (museums, offices), see [Network Requirements](../art-computer/network-requirements.md).
- `play` version error: FF OS is below the minimum supported version for that command; update FF OS and retry.
- Signature shape across the ecosystem: ff-cli emits the spec-current `signatures[]`, but some other tools still emit the legacy top-level `signature`. If you integrate with multiple tools, verify both forms validate as expected.

## Deeper references

- Full usage and workflow docs: <https://github.com/feral-file/ff-cli/blob/main/docs/README.md>
- Configuration reference: <https://github.com/feral-file/ff-cli/blob/main/docs/CONFIGURATION.md>
- More examples: <https://github.com/feral-file/ff-cli/blob/main/docs/EXAMPLES.md>
- Agent skill prompt (`ff-control`): <https://github.com/feral-file/ff-cli/blob/main/skills/ff-control/SKILL.md>
- DP-1 protocol spec: <https://github.com/display-protocol/dp1/blob/main/core/v1.1.0/spec.md>
- DP-1 CLI (**public beta**; validate, sign, verify, publish): <https://github.com/display-protocol/dp1-cli> — **dp1-cli** is the **actively maintained** successor to the legacy **dp1-validator** tag line in that **same repository** (legacy tags are frozen).
