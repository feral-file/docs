# Running without Feral File

The Art Computer is built so that the work plays without Feral File. This page says what that means today, from a test, and what still depends on Feral File's servers.

## What keeps working

Tested on 2026-10-28 on an Art Computer running FF OS 2.0.11, with every Feral File host blocked on the device for ten minutes and its open connections to them cut:

- **The playlist it was playing kept playing**, and it loaded the next work from the host the playlist points to (a third-party site).
- **A work sent from a computer on the same network played.** `ff-cli play` on a laptop sent it to the LAN API on port 1111, signed with the laptop's own key.

A playlist keeps playing as long as its media stays reachable or is in the device's offline cache. A playlist whose media Feral File hosts stops with Feral File; one whose media is anywhere else does not.

The test device had been paired with the app once. Wi-Fi setup needs no app (the Art Computer's own hotspot page, or an Ethernet cable: [Getting Started](index.md)), and pairing with the app binds the device to an account through Feral File's cloud, over the local network or by the QR code. A device that has never been paired re-opens its setup hotspot on its own from time to time. Whether a never-paired Art Computer plays from the LAN with Feral File unreachable is not yet tested.

So an institution can run its own [DP-1 feed server](https://github.com/display-protocol/dp1-feed-v2), sign its own playlists, and play them on its Art Computers from its own network with [ff-cli](../ff-cli/index.md):

```bash
ff-cli sign playlist.json            # signs with the key in your ff-cli config
ff-cli play playlist.json -d <name>  # over the LAN API; play refuses an unsigned file
```

`ff-cli build` signs what it writes when a key is configured, and `ff-cli publish` sends a signed playlist to a feed.

## What needs Feral File's servers

From the host list on [Network Requirements](network-requirements.md):

| Needs Feral File | What stops without it |
| :-- | :-- |
| The relayer | Control from the Feral File app when the phone is on another network. The LAN API keeps working. |
| Pairing | Both pairing paths bind the device to an account through Feral File's cloud. A device paired before stays paired, and control over the LAN API needs no pairing step after that. |
| The hosted feed | Feral File's channels and Daily. Playlists from any other feed, or sent directly, keep working. |
| The indexer | Artwork metadata for works found through Feral File. A playlist that carries its own metadata keeps working. |
| Video and asset hosting | Works whose video or files Feral File hosts. Works hosted anywhere else, or already in the offline cache, keep playing. |
| Remote configuration | Settings the player reads when it starts. Within a session it keeps the copy it read; after a restart with the source unreachable it runs on its built-in defaults. |
| Software updates | FF OS updates come only from Feral File's signed channel. The device keeps running the version it has. |
| The browser pairing broker | [Play on Art Computer](play.md) from a browser, which pairs through `handoff.feralfile.com` even on the same network. |
| Support logs and telemetry | Sending logs to support, and the metrics Feral File reads. |

## What is yours

- **A root shell.** `ff-cli ssh enable --pubkey <key.pub> --ttl 30m -d <name>` opens SSH on the local network until the time runs out; without `--ttl` it stays open until `ff-cli ssh disable`. Owner access over Tailscale persists on firmware that carries `feral-tailscale`, after enrollment ([ff-cli](../ff-cli/index.md#owner-remote-maintenance)).
- **The operating system.** FF OS can be reinstalled from a USB stick ([Getting Started](index.md)), and Secure Boot is off.
- **The code.** Everything that plays the work is open source: [Open source](../open-source.md).

## Still owed

**Updates without Feral File.** Feral File's own FF OS image pipeline needs Feral File's storage credentials and signing key, and an Art Computer takes updates only from Feral File's signed channel. Whether someone outside can build an image from the open source with their own keys and point a device at their own update channel is untested. Until it is, playing survives Feral File and updating does not.
