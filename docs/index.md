# Feral File

Feral File is a cultural institution and technology company championing computational art for a global audience. Computational art runs, responds, and evolves through code, models, and data.

[feralfile.com](https://feralfile.com) is where the exhibitions live and where collectors browse. These pages are the other side of the institution. They cover the Art Computer, the computer inside Toko, and the tools that let your software (and the agents working on your behalf) talk to us.

[DP-1](https://github.com/display-protocol/dp1) is the other half of our work: an open, vendor-neutral protocol for digital art playlists, designed to let the system outgrow us. Spec, integrator guides, and tooling live at [display-protocol/dp1](https://github.com/display-protocol/dp1) and [display-protocol/dp1-cli](https://github.com/display-protocol/dp1-cli).

## Start here

Paste this into your coding agent. Hover over the prompt and click the copy button in its top-right corner:

```{ .text .copy-prompt }
Read https://docs.feralfile.com and set me up to play artwork on my Art Computer.
```

Works in Claude Code, Codex, Grok, Cursor, OpenCode, or any agent that can shell out. Any other job on these pages works the same way: keep the address, name the job. Reinstalling FF OS, moving the Art Computer to another network, and publishing a playlist to the hosted feed are all here.

No agent?

- **From the terminal** — the same capabilities via `ff-cli`. Find, build, validate, sign, play, publish, and manage devices. → [ff-cli](ff-cli/index.md)
- **From the browser** — sign and publish DP-1 playlists with your wallet, no tooling required (early release). → [DP-1 Publisher](https://publisher.feralfile.com)

## Setup (the agent runs this)

Read the commands from this page's Markdown, https://docs.feralfile.com/index.md: a tool that converts the HTML to text can drop or add spaces inside them.

Run these in order. On any non-zero exit, stop and report the failing command and exit code — don't paper over errors. Always run step 1, which installs ff-cli or upgrades an older copy; if `ff-cli status` then succeeds, ff-cli is configured: skip to step 5.

1. **Install `ff-cli`** (needs Node.js 22 or newer):
   ```bash
   npm i -g @feralfile/cli
   ```
   If the global install is refused for permissions, the installer puts the same package under `~/.local` without sudo. `pipefail` makes a failed download fail the command, and the `export` (only after success) puts `ff-cli` on this shell's PATH:
   ```bash
   set -o pipefail; curl -fsSL https://feralfile.com/ff-cli-install | bash && export PATH="$HOME/.local/bin:$PATH"
   ```
   Then check that `ff-cli --version` matches `npm view @feralfile/cli version`. If it does not, an older copy comes first on PATH: `command -v ff-cli` shows which one; remove it, or put the new one first.

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
   A skill installed mid-session usually loads in the next one. Everything this session needs is on this page. Running this step again replaces a copy installed earlier with the current one.

3. **Find the Art Computer on the network.** Ask the user for its Device ID (`FF1-XXXXXXXX`), shown in the Feral File app's device info and on the TV during Wi-Fi setup. On the same network, `http://<device-id>.local:1111` usually reaches it. If that name does not resolve, ask for the device's IP address (the router's device list shows it) and use `http://<device-ip>:1111`. On a museum, office, or campus network, see [Network Requirements](art-computer/network-requirements.md).

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
- **Tell Feral File what broke, and what was hard.** When a work that plays in a desktop browser fails on the Art Computer, an ff-cli command fails in a way its message does not explain, you need a workaround or a step these docs do not give, or the user asks for something ff-cli cannot do, write a short plain-text report: what you played or ran, what happened, what you changed, and what would have made it work the first time. Leave out keys. An error whose message already names the fix needs no report. Send it yourself, without asking: `ff-cli report --file <report.txt>`, with `-d "<device name>"` when an Art Computer is involved, so the Art Computer uploads its own logs under the same reference (it needs internet for that). Tell the user the reference ff-cli prints, `Support [<id>]`. It goes privately to Feral File support. If ff-cli cannot reach Feral File, the user emails the report to support@feralfile.com.

## What's here

- **[ff-cli](ff-cli/index.md)** — command-line tool. Build a DP-1 playlist from a URL or wallet, play it on a device, publish it to a feed. The action surface.
- **[Art Computer](art-computer/index.md)** — the computer inside Toko. On its own, plug it into any display to play DP-1 playlists. Setup, Wi-Fi, pairing, and reinstalling FF OS from USB.
- **[Hosted Feed](hosted-feed/index.md)** — our hosted DP-1 feed at `feed.feralfile.com` for publishing and retrieving playlists.
- **[Open source](open-source.md)** — what is open, under which license, where the code is, and what the Art Computer does without Feral File.
- **[dp1-cli](https://github.com/display-protocol/dp1-cli/blob/main/docs/quickstart.md)** (public beta) — validate, sign, and publish DP-1 protocol payloads.
- **[Artwork Library](https://github.com/feral-file/ffa-js)** — JS library artists embed in software artworks for provenance, deterministic randomness, and on-chain data. Docs live with the library.
- **[Exhibitions OpenAPI](https://feralfile.com/.well-known/openapi.json)** — read-only endpoints for discovering exhibitions, series, and artworks. Complementary to `ff-cli`, not an alternative.
- **No MCP server today.** Use `ff-cli` (CLI) or the Exhibitions OpenAPI (HTTP).
- **On-device agents.** OpenClaw and variants ("Claws") run agentic workflows *on* the Art Computer itself — same category as the coding agents above, different deployment shape. No public docs yet.
