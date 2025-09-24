# DP-1 Schemas

For authoritative definitions, refer to the [DP-1 JSON schemas](https://github.com/display-protocol/dp1/blob/main/docs/spec.md) and [Feed API spec](https://github.com/display-protocol/dp1-feed/blob/main/openapi.yaml) in the public repo.

## Feral File Examples
Feral workflows often extend core schemas with exhibition metadata. Example for an FF1-bound artwork:

```json
{
  "dpVersion": "1.0.0",
  "id": "feral-exhibit-001",
  "slug": "generative-sunset",
  "title": "Generative Sunset",
  "created": "2025-09-13T00:00:00Z",
  "defaults": {
    "display": { "scaling": "fit", "background": "#000" }
  },
  "items": [
    {
      "id": "item-001",
      "slug": "sunset-loop",
      "source": "https://cdn.feralfile.com/art/sunset.html",
      "duration": 300,
      "license": "token",
      "ref": "ipfs://manifest-for-exhibition",  // Feral extension for token metadata
      "provenance": {
        "type": "onChain",
        "contract": { "chain": "evm", "standard": "erc721", "address": "0x...", "tokenId": "123" }
      }
    }
  ],
  "signature": "ed25519:<hex>"
}
```

## Quick Validation
Use the open-source [DP-1 Validator](https://github.com/display-protocol/dp1-validator) to check your playlist:
```bash
./dp1-validator playlist --playlist "https://your-url/playlist.json" --pubkey "your-pubkey-hex"
```
It verifies signatures, schemas, and assets—essential for Feral submissions.

Validate with the open [DP-1 Validator](https://github.com/display-protocol/dp1-validator). For Feral-specific validation in exhibitions, see [Token Metadata](../exhibitions-n-archive/token-metadata.md).

See also: Full field list in the [DP-1 spec](https://github.com/display-protocol/dp1/blob/main/docs/spec.md).
