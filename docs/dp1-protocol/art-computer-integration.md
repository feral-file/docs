# From DP-1 Playlist to Art Computer Playback

DP-1 is the open protocol.

The Art Computer is Feral File's reference hardware for playback.

This page is the shortest bridge from a valid DP-1 playlist to visible playback on the Art Computer.

Version note: this bridge accepts any playlist that validates for your toolchain. Current ff-cli examples in these docs emit `dpVersion: 1.0.0`; canonical DP-1 spec is `v1.1.0`.

Use [dp1-cli](dp1-cli.md) (**public beta**) for DP-1 validation and signing; it uses [dp1-go](https://github.com/display-protocol/dp1-go) for schema checks and signature semantics. **dp1-cli** is the **actively maintained** successor to the legacy **dp1-validator** release line in the [same GitHub repository](https://github.com/display-protocol/dp1-cli) (different tags; the legacy line is frozen).

## Shortest path

1. Validate your playlist: [DP-1 CLI quickstart](dp1-cli.md)
2. Send playlist to the Art Computer:

```bash
curl --request POST "http://$DEVICE_ID.local:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{"command":"displayPlaylist","request":{"playlistUrl":"$PLAYLIST_URL","intent":{"action":"now_display"}}}'
```

Replace:

- `$DEVICE_ID` with your Art Computer device id (the manufacturer-assigned hostname, e.g. `ff1-441s8sp2`)
- `$PLAYLIST_URL` with your hosted DP-1 playlist URL

## If you prefer CLI

Use [ff-cli: Start Here](../api-reference/cli.md) and end with `ff-cli play`.

## Common failure points

- Device not reachable on local network.
- Playlist URL is not publicly reachable by the device.
- Playlist did not pass validation before send.
- Signature model mismatch across tools: legacy `signature` vs spec `signatures[]` expectations.

## Next step

Tune playback behavior in [Player Behavior](player-behavior.md).
