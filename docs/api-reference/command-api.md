# Command API

The Command API has two sections:

- Command Parser (documented below)
- Relayer (documented below)

### Command Parser (v1)

- Base URL: `/api/v1`
- Auth: send `X-API-KEY` header
- Supports streaming via HTTP chunked `application/x-ndjson`

#### Overview

- Base URL: `/api/v1`
- Auth: send `X-API-KEY` header
- Content types: `application/json`, streaming `application/x-ndjson`

#### Authentication

- Include `X-API-KEY: <your key>` on every request.
- Unauthorized response example:

```json
{ "error": "Unauthorized", "message": "Valid X-API-KEY header is required for NL Parser endpoints" }
```

#### Endpoints

##### POST `/text`

- **Purpose**: Parse a natural language command, optionally disambiguate using device names, and return an intent and a playlist/display call.
- **Query parameters**:
  - `stream` (boolean): If true, return HTTP chunked NDJSON frames.
- **Request body** (JSON):
  - `command` (string, required): The natural language command.
  - `device_names` (string[], optional): Device names to help disambiguate.
- **Responses**:
  - 200 `application/json`: Non‑streaming response with `intent`, `response`, and `dp1_call`.
  - 200 `application/x-ndjson`: Streaming frames of `intent`, `dp1_call`, `response`, and `complete`.
  - 400: `{ "error": "Command is required" }` when the body is missing/invalid.
  - 401: As in Authentication section.

Example request (non‑streaming):

```bash
curl --location 'https://command-api.feral-file.workers.dev/api/v1/text' \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: ${X_API_KEY}' \
  --data '{
    "command": "show me unsupervised",
    "device_names": ["kitchen", "living_room", "bed room"]
  }'
```

Example 200 (non‑streaming):

```json
{
  "intent": {
    "action": "now_display",
    "quantity": 1,
    "random_playlist": true,
    "entities": [
      {
        "name": "Unsupervised — Data Universe — MoMA",
        "type": "artwork",
        "probability": 0.67082036,
        "ids": ["bmk--846a6e76b4364f63c16de8a30a264d28fd726bb2055b876052d95e91be0a4ffa"]
      }
    ]
  },
  "response": "I'll display a random selection of artworks matching 'Unsupervised' for you.",
  "dp1_call": {
    "dpVersion": "1.0.0",
    "id": "playlist-...",
    "created": "2025-08-14T07:37:01.562Z",
    "defaults": { "display": { "scaling": "fit", "background": "#111", "margin": "5%" } },
    "items": [ { "id": "0x..._f77cf9...", "duration": 360, "license": "open" } ],
    "title": "Featuring Unsupervised",
    "signature": "ed25519:0x..."
  }
}
```

Example 200 (streaming NDJSON, selected frames):

```ndjson
{"type":"intent","content":"Parsed intent: now_display","data":{"action":"now_display","quantity":1,"random_playlist":true}}
{"type":"dp1_call","content":"Generated DP1 call","data":{"dpVersion":"1.0.0","id":"playlist-...","items":[{"id":"0x...","duration":360}]}}
{"type":"response","content":"I'll display a random selection of artworks matching 'Unsupervised' for you."}
{"type":"complete","content":"Request completed successfully"}
```

##### POST `/voice`

- **Purpose**: Upload base64‑encoded audio for transcription and processing as a command.
- **Query parameters**:
  - `stream` (boolean): If true, return HTTP chunked NDJSON frames.
  - `skipCache` (boolean): Optional; bypass cache.
- **Request body** (JSON):
  - `audio` (string, required): Base64 audio (WAV/MP3/OGG; mono; ~16kHz recommended).
  - `device_names` (string[], optional)
- **Responses**:
  - 200: Same shape as `/text`.
  - 400: `{ "error": "Base64 audio data is required" }` when `audio` is missing.
  - 401: As in Authentication section.

#### Models

- **IntentObject**
  - `action` (string)
  - `quantity` (integer, optional)
  - `random_playlist` (boolean, optional)
  - `entities` (array of `Entity`, optional)

- **Entity**
  - `name` (string)
  - `type` (string; one of `artist`, `artwork`)
  - `probability` (number)
  - `ids` (string[])

- **DP1Call**
  - `dpVersion` (string)
  - `id` (string)
  - `created` (RFC3339 timestamp)
  - `title` (string, optional)
  - `defaults.display.scaling|background|margin`
  - `items` (array of `DP1Item`)
  - `signature` (string)

- **DP1Item**
  - `id` (string)
  - `duration` (integer seconds)
  - `license` (string)
  - `provenance.type` (e.g. `onChain`)
  - `provenance.contract.chain|standard|address|tokenId`

### Relayer (v1)

- Base URL: `https://artwork-info.feral-file.workers.dev`
- Auth: send `API-KEY` header, or use `apiKey` query parameter as an alternative when headers are not supported.

#### Shared parameters

- `topicID` (query, string, required for most endpoints): Topic identifier that binds a portal and its notification subscribers.
- `apiKey` (query, string, optional): Alternative to the `API-KEY` header.

#### Endpoints

##### POST `/api/connection`

- **Purpose**: Establish a portal WebSocket connection or generate a new `topicID`.
- **Behaviors**:
  - With a global API key: No `topicID` required; returns 200 with a freshly generated `topicID`.
  - With a provisioned API key: Requires `topicID`; upgrades to WebSocket for portal clients (HTTP 101).
- **Query parameters**:
  - `topicID` (required for provisioned keys)
  - `apiKey` (optional)
- **Auth**: `API-KEY` header or `apiKey` query param.
- **Responses**:
  - 101: WebSocket protocol switch (portal client)
  - 200: `{ "topicID": "..." }` when generating a topic with a global key
  - 400: Bad request (missing `topicID` for provisioned keys, or invalid data)
  - 401: Unauthorized (invalid API key)

Examples:

- Generate a `topicID` (global key):

```bash
curl -X POST 'https://artwork-info.feral-file.workers.dev/api/connection' \
  -H 'API-KEY: ${GLOBAL_API_KEY}'
```

- Portal WebSocket upgrade (provisioned key):

```bash
wscat -c 'wss://artwork-info.feral-file.workers.dev/api/connection?topicID=${TOPIC_ID}' \
  -H 'API-KEY: ${PROVISIONED_API_KEY}'
```

##### POST `/api/cast`

- **Purpose**: Send a cast command to all connected portal clients for a `topicID`.
- **Query parameters**:
  - `topicID` (required)
  - `apiKey` (optional)
- **Auth**: `API-KEY` header or `apiKey` query param.
- **Request body**: JSON object (arbitrary command payload).
- **Responses**:
  - 200: `{ "message": { ... } }` — response from the portal client(s)
  - 400: Bad request (no portal clients or invalid data)
  - 401: Unauthorized (invalid API key)

Example:

```bash
curl -X POST 'https://artwork-info.feral-file.workers.dev/api/cast?topicID=${TOPIC_ID}' \
  -H 'Content-Type: application/json' \
  -H 'API-KEY: ${API_KEY}' \
  --data '{
    "type": "display",
    "payload": { "mode": "now", "artworkId": "0x..." }
  }'
```

##### GET `/api/notification`

- **Purpose**: Subscribe to notifications for a `topicID` via WebSocket.
- **Query parameters**:
  - `topicID` (required)
  - `apiKey` (optional)
- **Auth**: `API-KEY` header or `apiKey` query param.
- **Responses**:
  - 101: WebSocket protocol switch (notification client)
  - 400: Bad request (missing `topicID` or not a WebSocket upgrade)
  - 401: Unauthorized (invalid API key)

Examples:

- Using `wscat` with header:

```bash
wscat -c 'wss://artwork-info.feral-file.workers.dev/api/notification?topicID=${TOPIC_ID}' \
  -H 'API-KEY: ${API_KEY}'
```

- Using query param if headers are not supported:

```bash
wscat -c 'wss://artwork-info.feral-file.workers.dev/api/notification?topicID=${TOPIC_ID}&apiKey=${API_KEY}'
```

##### OPTIONS (CORS preflight)

- All endpoints support `OPTIONS` and return 204 with appropriate CORS headers.

#### Examples

- Non-streaming request:

```bash
curl --location 'https://command-api.feral-file.workers.dev/api/v1/text' \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: ${X_API_KEY}' \
  --data '{
    "command": "show me unsupervised",
    "device_names": ["kitchen", "living_room", "bed room"]
  }'
```

- Streaming request:

```bash
curl --location 'https://command-api.feral-file.workers.dev/api/v1/text?stream=true&summary=true' \
  --header 'Content-Type: application/json' \
  --header 'X-API-KEY: ${X_API_KEY}' \
  --data '{"command": "show me random artworks"}'
```

Notes

- 401 shape (no/invalid key): `{ "error": "Unauthorized", "message": "Valid X-API-KEY header is required for NL Parser endpoints" }`
- 400 shape (/text missing body): `{ "error": "Command is required" }`
- 400 shape (/voice missing body): `{ "error": "Base64 audio data is required" }`
