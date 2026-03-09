# From DP-1 Playlist to FF1 Playback

DP-1 is the open protocol.

FF1 is Feral File's art computer and the reference hardware for playback.

This page is the shortest bridge from a valid DP-1 playlist to visible playback on FF1.

Version note: this bridge accepts any playlist that validates for your toolchain. Current FF1 CLI examples in these docs emit `dpVersion: 1.0.0`; canonical DP-1 spec is `v1.1.0`.

Validator quickstart in this docs path focuses on structure checks and legacy top-level signature verification.

## Shortest path

1. Validate your playlist: [Validator Quickstart](validator.md)
2. Send playlist to FF1:

```bash
curl --request POST "http://$DEVICE_ID.local:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{"command":"displayPlaylist","request":{"playlistUrl":"$PLAYLIST_URL","intent":{"action":"now_display"}}}'
```

Replace:

- `$DEVICE_ID` with your FF1 device id
- `$PLAYLIST_URL` with your hosted DP-1 playlist URL

## If you prefer CLI

Use [FF1 CLI: Start Here](../api-reference/cli.md) and end with `ff1 send`.

## Common failure points

- Device not reachable on local network.
- Playlist URL is not publicly reachable by the device.
- Playlist did not pass validation before send.
- Signature model mismatch across tools: legacy `signature` vs spec `signatures[]` expectations.

## Next step

Tune playback behavior in [Player Behavior](player-behavior.md).
