# Running without Feral File

The Art Computer is built so that the work plays without Feral File. This page says what that means today, from a test, and what still depends on Feral File's servers.

## What keeps working

Tested on 2026-10-28 on an Art Computer running FF OS 2.0.11, with every Feral File host blocked on the device for ten minutes and its open connections to them cut:

- **The playlist it was playing kept playing**, and it loaded the next work from the host the playlist points to (a third-party site).
- **A work sent from a computer on the same network played.** `ff-cli play` on a laptop sent it to the LAN API on port 1111, signed with the laptop's own key.

The device had been paired with the app once before the test. Whether a never-paired Art Computer plays from the LAN without the pairing step is not yet tested.

So an institution can run its own [DP-1 feed server](https://github.com/display-protocol/dp1-feed-v2), publish playlists signed with its own key, and play them on its Art Computers from its own network with [ff-cli](../ff-cli/index.md). First setup needs no app: the Art Computer raises its own Wi-Fi hotspot with a setup page, or takes an Ethernet cable ([Getting Started](index.md)).

## What needs Feral File's servers

From the host list on [Network Requirements](network-requirements.md):

| Needs Feral File | What stops without it |
| :-- | :-- |
| The relayer | Control from the Feral File app when the phone is on another network. The LAN API keeps working. |
| The hosted feed | Feral File's channels and Daily. Playlists from any other feed, or sent directly, keep working. |
| The indexer | Artwork metadata for works found through Feral File. A playlist that carries its own metadata keeps working. |
| Remote configuration | Settings every Art Computer downloads at boot. The device keeps its last copy. |
| Software updates | FF OS updates come only from Feral File's signed channel. The device keeps running the version it has. |
| Support logs and telemetry | Sending logs to support, and the metrics Feral File reads. |
| The pairing link | The QR code on the pairing screen opens a Feral File address. Pairing over the LAN works without it. |

## What is yours

- **A root shell.** `ff-cli ssh enable` opens SSH on the local network for a set time; owner access over Tailscale persists ([ff-cli](../ff-cli/index.md#owner-remote-maintenance)).
- **The operating system.** FF OS can be reinstalled from a USB stick ([Getting Started](index.md)). Secure Boot is off, so another operating system boots too.
- **The code.** Everything that plays the work is open source: [Open source](../open-source.md).

## Still owed

Two things are not yet true, and they are the work in front of us:

- **Updates without Feral File.** Building an FF OS image needs Feral File's build secrets and signing key, and an Art Computer takes updates only from Feral File's signed channel. Playing survives Feral File; updating does not yet.
- **Signing a playlist file for `ff-cli play`.** `ff-cli build` writes an unsigned playlist, and `ff-cli play` refuses an unsigned file. A playlist you host yourself must be signed with the DP-1 tooling first ([dp1-cli](https://github.com/display-protocol/dp1-cli)), or published to a feed with `ff-cli publish`, which signs it.
