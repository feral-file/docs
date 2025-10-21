### Overview

FF1 CLI builds and validates DP‑1 (Display Protocol 1) playlists from NFT data using either natural language (AI‑orchestrated function calling) or deterministic parameters. For the DP‑1 spec, see [DP-1 Specification](https://github.com/display-protocol/dp1).

**Key characteristics:**

- Deterministic by design: tool outputs are validated against DP‑1 before send.

- Optional Ed25519 signing with canonical JSON via `dp1-js`.

### Install

Use the Node.js workflow provided by the project:

```bash
npm install
```

Initialize and validate configuration:

```bash
npm run dev -- config init
npm run dev -- config validate
```

Optional build for production:

```bash
npm run build
node dist/index.js chat
```

### Quick start

Natural language (AI‑orchestrated):

```bash
npm run dev chat
npm run dev -- chat "Get tokens 1,2,3 from Ethereum contract 0xabc" -o playlist.json
```

Deterministic (no AI):

```bash
npm run dev -- build examples/params-example.json -o playlist.json
```

### Commands and flags

- `chat [content]` – AI‑driven natural language playlists
  - Options: `-o, --output <file>`, `-m, --model <name>`, `-v, --verbose`
- `build [params.json]` – Deterministic build from JSON file or stdin
  - Options: `-o, --output <file>`, `-v, --verbose`
- `validate <file>` / `verify <file>` – Validate a DP‑1 playlist file
- `sign <file>` – Sign playlist with Ed25519
  - Options: `-k, --key <base64>`, `-o, --output <file>`
- `send <file>` – Send playlist to an FF1 device
  - Options: `-d, --device <name>`, `--skip-verify`
- `config <init|show|validate>` – Manage configuration

Models are configured in `config.json` and can be switched at runtime via `--model`.

### Examples

Setup:

```bash
npm install
npm run dev -- config init
npm run dev -- config validate
```

Natural language:

```bash
# Interactive chat
npm run dev chat

# One‑shot requests
npm run dev -- chat "Get tokens 1,2,3 from Ethereum contract 0xabc" -o playlist.json
npm run dev -- chat "Get token 42 from Tezos contract KT1abc"
npm run dev -- chat "Get 3 items from Social Codes and 2 from 0xdef" -v

# Switch model
npm run dev -- chat "your request" --model grok
npm run dev -- chat "your request" --model chatgpt
npm run dev -- chat "your request" --model gemini
```

Deterministic build (no AI):

```bash
# From file
npm run dev -- build examples/params-example.json -o playlist.json

# From stdin
cat examples/params-example.json | npm run dev -- build -o playlist.json
```

AI‑orchestrated deterministic flow (prompts):

```bash
# Show tool‑call progress and validation
npm run dev -- chat "Build a playlist of my Tezos works from address tz1... plus 3 from Social Codes" -v -o playlist.json

# Switch model if desired
npm run dev -- chat "Build playlist from Ethereum address 0x... and 2 from Social Codes" --model chatgpt -v
```

One‑shot complex prompt:

```bash
# Combine sources, shuffle, set per‑item duration, and send to a device
npm run dev -- chat "Get tokens 1,2 from contract 0xabc and token 42 from KT1xyz; shuffle; 6 seconds each; send to 'Living Room Display'." -o playlist.json -v
```

Validate / sign / send:

```bash
# Validate playlist
npm run dev -- validate playlist.json

# Sign playlist
npm run dev -- sign playlist.json -o signed.json

# Send to device (verifies by default)
npm run dev -- send playlist.json -d "Living Room Display"
```

### Troubleshooting

Configuration and diagnostics:

```bash
# Show current configuration
npm run dev -- config show

# Reinitialize config
npm run dev -- config init

# Validate config and surface actionable errors
npm run dev -- config validate
```

Notes and constraints:
- Max 20 items total across all requirements
- Duration per item defaults to 10s (configurable)
- Device selection: omit `-d` to use the first configured device, or pass exact `--device <name>`

### Configuration reference

See [Configuration Guide](https://github.com/feral-file/ff1-cli/blob/main/docs/CONFIGURATION.md) for all fields, environment variables, feed settings, and FF1 device selection rules. Minimal `config.json` and environment variable helpers are provided there.

### Function calling architecture

For how the model orchestrates tool calls, schemas, and the deterministic pipeline, see [Function Calling Details](https://github.com/feral-file/ff1-cli/blob/main/docs/FUNCTION_CALLING.md). In short: parse intent → call tools to fetch/build → verify DP‑1 → optionally sign → optionally send.

### See also

- [Command API reference](../api-reference/command-api.md)
- [General CLI README](https://github.com/feral-file/ff1-cli/blob/main/docs/README.md)
- [Examples](https://github.com/feral-file/ff1-cli/blob/main/docs/EXAMPLES.md)
- [Configuration](https://github.com/feral-file/ff1-cli/blob/main/docs/CONFIGURATION.md)
- [Function calling details](https://github.com/feral-file/ff1-cli/blob/main/docs/FUNCTION_CALLING.md)
- [DP‑1 specification](https://github.com/display-protocol/dp1)