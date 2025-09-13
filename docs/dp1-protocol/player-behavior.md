# Player Behavior

DP-1 players like FF1 interpret playlists via a standardized lifecycle. For core rules, see [DP-1 spec](https://github.com/display-protocol/dp1/blob/main/docs/spec.md).

## FF1-Specific Behavior
FF1 (Feral's reference hardware) renders DP-1 content with these optimizations:

### Render Hints
- **Scaling/Margins**: Defaults to "fit" with 5% margins; overrides per item take precedence.
- **Backgrounds**: Supports hex colors; falls back to black (#000) for unstyled items.
- **Transitions**: 1s fade between items; disabled for "instant" license types (e.g., subscription previews needing quick loads).

### Asset Locators
FF1 resolves sources via:
- **URLs**: Direct fetch (e.g., HTTPS/IPFS); caches for OTA updates (see [FF1 OTA](../ff1/how-it-works/ota.md)).
- **Provenance Checks**: Verifies on-chain token ownership before token-gated renders.
- **Fallbacks**: If source fails, displays static thumbnail from `ref` (IPFS manifest).

### Lifecycle
1. Fetch playlist from Feed Server.
2. Validate signature.
3. Loop items indefinitely (or until interrupted, e.g., new playlist via OTA), respecting durations.
4. Handle errors: Log to console; skip to next item.
   - **Power Cycle?** FF1 retries fetches on boot; check logs via SSH for provenance fails.

Example FF1 config in playlist:
```json
{
  "defaults": {
    "display": { "scaling": "fit", "margin": "5%" }
  }
}
```

For QEMU testing, see [FF1 QEMU](../ff1/qemu/macOS.md).

.

