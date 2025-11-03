# Display DP-1 Playlists on FF1

Preview and test how your DP-1 playlists render on your FF1 device — a quick way to verify scaling, timing, and transitions before publishing.

## Prerequisites

- FF1 device on your network
- FF1 device ID, visible in the Feral File mobile app after your device is connected
- DP-1 playlist (URL or JSON data)

## Run your first Commands

You can send a playlist either by URL or by sending the full JSON payload.

### Send from URL
```bash
curl --request POST "http://$device_ID.local:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{"command": "displayPlaylist","request":{"playlistUrl":"$playlist_url", "intent": {"action": "now_display"}}}'
```

### Send from JSON data
```bash
curl --request POST "http://$device_ID.local:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{"command": "displayPlaylist","request":{"playlist":{ $actual_playlist_json }, "intent": {"action": "now_display"}}}'
```

> 💡 **That's it!** Just replace the variables (`$device_ID`, `$playlist_url`, `$actual_playlist_json`) with your values and run the command.

### Variable Reference

Replace these placeholders in the commands above:

- **`$device_ID`** → The unique device ID for your FF1. You can [find it](#1-locate-your-ff1-device-id) in the Feral File mobile app after your FF1 is connected.
- **`$playlist_url`** → URL to your DP-1 playlist JSON file (e.g., `https://my-feed.example.com/playlists/playlist-ID`)
- **`$actual_playlist_json`** → Your complete DP-1 playlist JSON content (see examples below)

## Complete Examples

### Example 1: Send from URL
```bash
# Replace with your actual FF1 IP and playlist URL
curl --request POST "http://192.168.1.100:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{"command": "displayPlaylist","request":{"playlistUrl":"https://feed.example.com/my-playlist.json", "intent": {"action": "now_display"}}}'
```

### Example 2: Send from JSON data
```bash
# Replace with your actual FF1 IP and playlist JSON
curl --request POST "http://192.168.1.100:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{
    "command": "displayPlaylist",
    "request": {
      "playlist": {
        "dpVersion": "1.0.0",
        "title": "Test Artwork Display",
        "defaults": {
          "display": {
            "scaling": "contain",
            "background": "#000000",
            "margin": 0
          }
        },
        "items": [
          {
            "source": "https://example.com/artwork.html",
            "duration": 300,
            "license": "open",
            "provenance": {
              "type": "onChain",
              "contract": {
                "chain": "evm",
                "standard": "erc721",
                "address": "0x1234567890123456789012345678901234567890",
                "tokenId": "1"
              }
            }
          }
        ]
      },
      "intent": {"action": "now_display"}
    }
  }'
```

## Step-by-Step Guide

### 1. Locate Your FF1 Device ID

To send a playlist, you'll need your unique FF1 Device ID:

1. Open the Feral File mobile app.
2. Tap the menu icon (☰) in the upper right corner.
3. Go to `FF1 Settings`.
4. Scroll down to `Device Information`.
5. Copy the `Device Id`—you'll use this to direct commands to your FF1.

Having the correct Device ID ensures your playlist is sent to the right FF1 device.

### 2. Prepare Your Playlist
Choose one method:

**Option A: Use a playlist URL**
- Host your DP-1 playlist JSON file on a web server—this can be your own self-hosted [Feed Server](../../dp1-protocol/self-hosted-feed.md)
- Use the public URL where your playlist is served (e.g., `https://your-server.com/playlists/playlist-ID`)

**Option B: Use inline JSON**
- Prepare your complete DP-1 playlist JSON
- Replace `$actual_playlist_json` with the entire DP-1 JSON format, see [DP-1 Specification](https://github.com/display-protocol/dp1)

### 3. Execute the Command
Copy the appropriate example above, replace the variables, and run it in your terminal.

## Troubleshooting

- **Connection refused**: Check if FF1 device IP is correct and device is powered on
- **Invalid JSON**: Validate your DP-1 playlist format
- If the FF1 doesn’t respond, check that it’s on the same network.
