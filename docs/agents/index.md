# Agents Quickstart

## Paste this into your coding agent

Hover over the prompt and click the copy button in its top-right corner:

```{ .text .copy-prompt }
Read https://docs.feralfile.com/agents/ and set me up to play artwork on my Art Computer.
```

Your agent runs the setup below. Works in Claude Code, Codex, Grok, Cursor, OpenCode, or any agent that can shell out.

## Setup (the agent runs this)

Run these in order. On any non-zero exit, stop and report the failing command and exit code — don't paper over errors. Always run step 1, which installs ff-cli or upgrades an older copy; if `ff-cli status` then succeeds, ff-cli is configured: skip to step 5.

1. **Install `ff-cli`** (needs Node.js 22 or newer):
   ```bash
   npm i -g @feralfile/cli
   ```
   If the global install is refused for permissions, the installer puts the same package under `~/.local` without sudo. `pipefail` makes a failed download fail the command, and the `export` puts `ff-cli` on this shell's PATH:
   ```bash
   set -o pipefail; curl -fsSL https://feralfile.com/ff-cli-install | bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

2. **Install the `ff-control` skill**, so the agent knows these commands in its next session.
   For Claude Code and Grok (Grok also reads `~/.claude/skills`):
   ```bash
   d="$(mktemp -d)" && git clone --depth=1 https://github.com/feral-file/ff-cli "$d" \
     && mkdir -p ~/.claude/skills && cp -r "$d/skills/ff-control" ~/.claude/skills/
   ```
   For Codex:
   ```bash
   d="$(mktemp -d)" && git clone --depth=1 https://github.com/feral-file/ff-cli "$d" \
     && mkdir -p ~/.codex/skills && cp -r "$d/skills/ff-control" ~/.codex/skills/
   ```
   A skill installed mid-session usually loads in the next one. Everything this session needs is on this page.

3. **Find the Art Computer on the network.** Ask the user for its Device ID (`FF1-XXXXXXXX`), shown in the Feral File app's device info and on the TV during Wi-Fi setup. On the same network, `http://<device-id>.local:1111` usually reaches it. If that name does not resolve, ask for the device's IP address (the router's device list shows it) and use `http://<device-ip>:1111`. On a museum, office, or campus network, see [Network Requirements](../art-computer/network-requirements.md).

4. **Configure** (no prompts; ff-cli needs no LLM API key):
   ```bash
   ff-cli setup --non-interactive --device-host http://<device-id>.local:1111 --device-name "<name>"
   ```
   This registers the device, and makes a signing key when none is configured (an existing key is kept). Setup refuses to replace a signing key that is already configured, because that key owns the user's published playlists; never add `--force` unless the user asks to replace it. Add more devices later with `ff-cli device add --host http://<address>:1111 --name "<name>"`.

5. **Run what the user asked for:**

    | The user gives you | Run |
    | :-- | :-- |
    | An artwork or collection link (Art Blocks, Objkt, fxhash, OpenSea, SuperRare, Feral File, Neort, Verse, Raster), or `ethereum:0x…:tokenId` / `tezos:KT1…:tokenId` | `ff-cli find "<link>" --play -y` (add `-l <n>` to cap a large series) |
    | A web page or media file | `ff-cli play "<url>"` |
    | A page on one of those marketplace sites, shown as a page | `ff-cli play --web "<url>"` |
    | A wallet, for what it owns | `ff-cli build` with a `query_address` requirement; `ff-cli build --help` shows the format |
    | A playlist file or playlist URL | `ff-cli play "<file-or-url>"` |

    Add `-d "<device name>"` to `play`, or to `find --play`, to pick a device other than the first.

### Rules that keep agents on track

- **Pass `-y` to `find`.** Without a terminal, a question fails with exit 1 and names the flag that answers it. With `-y` and no `-o`, `find` plays the playlist; add `--no-play` to only save it.
- **Read the exit code, then the output.** Non-zero means what was asked did not happen, including a send to an unreachable device and a `build` that lost a requirement or a named token. A zero exit can still carry a partial result: `find` and `build` print how many items they saved and which tokens could not be resolved, so report those.
- **`find` on a wallet address plays one work by the artist at that address**, not what the wallet owns. For holdings, use `build` with `query_address`.
- **`play` refuses a URL that does not exist** (HTTP 404 or 410, or a host that does not resolve), so a typo is never cast as an error page.

## What's actually here

- **[ff-cli](../ff-cli/index.md)** — build playlists, play artwork, publish feeds. The action surface.
- **[dp1-cli](https://github.com/display-protocol/dp1-cli/blob/main/docs/quickstart.md)** (public beta) — validate, sign, and publish DP-1 protocol payloads.
- **Exhibitions OpenAPI** — `https://feralfile.com/.well-known/openapi.json`. Read-only endpoints for discovering exhibitions, series, and artworks. Complementary to `ff-cli`, not an alternative.
- **No MCP server today.** Use `ff-cli` (CLI) or the Exhibitions OpenAPI (HTTP).

## Owner remote maintenance

An optional FFOS integration lets an owner's existing agent computer reach an
FF1 over the owner's Tailscale network. It requires firmware containing
`feral-tailscale` and explicit enrollment of that computer and its SSH public key. Owner access
persists until revocation or factory reset, including when controld needs repair.
Follow the procedure’s full-image installation checks. If support is absent,
check the normal firmware release channel for availability; enrollment waits
until a version containing owner access is published and installed.

Follow the [owner-access procedure](https://github.com/feral-file/ffos/blob/36e25cec84505271a7232d6936bb46a19fab5cfd/docs/OWNER_TAILSCALE.md)
for enrollment, diagnostics, disconnect and access verification. Use
the existing `ff-control` skill and explicit FF1 Tailscale IPv4 address. Tailscale
must run on the computer executing the agent; a connected phone does not give a
cloud agent access. Required pairing approvals still belong to the owner.

## On-device agents

OpenClaw and variants ("Claws") run agentic workflows *on* the Art Computer itself — same category as the coding agents above, different deployment shape. Public docs for OpenClaw will land here as it matures.
