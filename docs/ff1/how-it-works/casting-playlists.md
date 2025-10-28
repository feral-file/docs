# Casting DP-1 Playlists to FF1

Preview and test your DP-1 playlists on FF1 devices. This allows you to see how your artworks will display and ensure everything works correctly.

## Prerequisites

- FF1 device on your network
- FF1 device IP address
- DP-1 playlist (URL or JSON data)

## Quick Commands

### Cast from URL
```bash
curl --request POST "http://$ff1-ip:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{"command": "displayPlaylist","request":{"playlistUrl":"$playlist_url", "intent": {"action": "now_display"}}}'
```

### Cast from JSON data
```bash
curl --request POST "http://$ff1-ip:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{"command": "displayPlaylist","request":{"playlist":{ $actual_playlist_json }, "intent": {"action": "now_display"}}}'
```

> 💡 **That's it!** Just replace the variables (`$ff1-ip`, `$playlist_url`, `$actual_playlist_json`) with your values and run the command.

### Variable Reference

Replace these placeholders in the commands above:

- **`$ff1-ip`** → Your FF1 device IP address (e.g., `192.168.1.100`)
- **`$playlist_url`** → URL to your DP-1 playlist JSON file (e.g., `https://my-feed.example.com/playlists/playlist-ID`)
- **`$actual_playlist_json`** → Your complete DP-1 playlist JSON content (see examples below)

## Complete Examples

### Example 1: Cast from URL
```bash
# Replace with your actual FF1 IP and playlist URL
curl --request POST "http://192.168.1.100:1111/api/cast" \
  --header "content-type:application/json" \
  --data '{"command": "displayPlaylist","request":{"playlistUrl":"https://feed.example.com/my-playlist.json", "intent": {"action": "now_display"}}}'
```

### Example 2: Cast from JSON data
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
            "duration": 15,
            "license": "open",
            "provenance": {
              "type": "onChain",
              "contract": {
                "chain": "ethereum",
                "standard": "ERC-721",
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

### 1. Find Your FF1 Device IP Address

You need the local IP address of your FF1 device to send cast commands.

**How to find the IP address (on FF1 device or Linux-based systems):**

1. Open a terminal or command prompt on your FF1 device (or the device running FF1).
2. Run:
   ```bash
   ip a
   ```
3. Look for an entry like `inet 192.168.x.x` or `inet 10.x.x.x` under your active network interface (commonly `eth0`, `wlan0`, or similar).
   - The number after `inet` (e.g., `192.168.1.100`) is your device’s IP address on the local network.


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
