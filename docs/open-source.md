# Open source

Everything that plays the work is open source: the protocol, the operating system, the player, the tools that send a playlist, the feed server, and this documentation. You can read it, change it, build on it, and pass it on. The Art Computer you own is yours, down to root access. And the work plays without Feral File: [what that means, from a test](#running-without-feral-file), and [what still needs Feral File](#what-needs-feral-file).

## What is open, and under which license

| Component | What it is | Code | License |
| :-- | :-- | :-- | :-- |
| DP-1 | The playlist protocol: anyone can publish a playlist, any player that speaks DP-1 can play it | [display-protocol/dp1](https://github.com/display-protocol/dp1) | CC BY 4.0 |
| FF OS | The Art Computer's operating system: the image build and the system services | [feral-file/ffos](https://github.com/feral-file/ffos), [feral-file/ffos-user](https://github.com/feral-file/ffos-user) | Apache 2.0 |
| FF Player | The player FF OS runs; it plays each work | [feral-file/ff-player](https://github.com/feral-file/ff-player) | MPL 2.0 |
| ff-cli | Build a playlist, play it on an Art Computer on your network, publish it to a feed | [feral-file/ff-cli](https://github.com/feral-file/ff-cli) | MIT |
| DP-1 feed server | The server that holds playlists and channels for players to fetch; Feral File's hosted feed runs it | [display-protocol/dp1-feed-v2](https://github.com/display-protocol/dp1-feed-v2) | MPL 2.0 |
| DP-1 tools and SDKs | Validation tool, publisher, Go and JavaScript SDKs | [dp1-cli](https://github.com/display-protocol/dp1-cli), [dp1-publisher](https://github.com/display-protocol/dp1-publisher), [dp1-go](https://github.com/display-protocol/dp1-go), [dp1-js](https://github.com/display-protocol/dp1-js) | MPL 2.0 |
| Play on Art Computer | The browser library behind [Play on Art Computer](art-computer/play.md), and the pairing broker that connects a web page to an Art Computer | [feral-file/play](https://github.com/feral-file/play) | Apache 2.0 |
| Indexer | Artwork metadata from Ethereum and Tezos | [feral-file/ff-indexer-v2](https://github.com/feral-file/ff-indexer-v2) | MPL 2.0 |
| Faceplates | The CAD files for the Art Computer's faceplate | [Print Your Own Faceplates](art-computer/faceplates/index.md) | CC BY-SA 4.0 |
| This documentation | docs.feralfile.com | [feral-file/docs](https://github.com/feral-file/docs) | CC BY 4.0 |

Every license here lets you use, change, and redistribute the work, and each asks that you keep its copyright notice and credit. Beyond that:

- **Apache 2.0 and MPL 2.0 both grant a patent license** with the code. Apache 2.0 asks that a copy you redistribute carries the license and its notices, and marks the files you changed.
- **MPL 2.0** asks that when you ship its files in a product, you make the source of those files available under MPL 2.0 and tell people how to get it. Your own files, the ones with no MPL code in them, stay under whatever terms you choose. Nothing is sent to Feral File.
- **CC BY 4.0 and CC BY-SA 4.0** ask that you link the license and say what you changed. CC BY-SA 4.0 also asks that a faceplate design you adapt and share stays under CC BY-SA 4.0 or a compatible license.

Contributions come in under the repository's license. There is no contributor agreement, and no other license on request: the same terms for everyone. A license is never withdrawn from a released version.

## Running without Feral File

In the test, every Feral File host was blocked on an Art Computer for ten minutes and its open connections to them were cut. Two things were checked:

- **The playlist it was playing kept playing**, and it loaded the next work from the host the playlist points to, a third-party site.
- **A work sent from a computer on the same network played.** `ff-cli play` on a laptop sent it to the LAN API, the command interface the Art Computer serves on your local network, signed with the laptop's own key.

A playlist keeps playing as long as its media stays reachable or is in the Art Computer's offline cache. So a playlist whose media Feral File hosts stops with Feral File once the cache runs out, and one whose media is anywhere else does not.

The test Art Computer had been paired with the app once. Whether a never-paired Art Computer plays from the LAN with Feral File unreachable is not yet tested; an unpaired Art Computer that cannot reach the internet re-opens its setup hotspot for a few cycles.

So an institution can run its own [DP-1 feed server](https://github.com/display-protocol/dp1-feed-v2), sign its own playlists, and play them on its Art Computers from its own network with [ff-cli](ff-cli/index.md):

```bash
ff-cli sign playlist.json            # signs with the key in your ff-cli config
ff-cli play playlist.json -d <name>  # over the LAN API; play refuses an unsigned file
```

`ff-cli build` signs what it writes when a key is configured, and `ff-cli publish` sends a signed playlist to a feed.

## What needs Feral File

Two things are not open source: the Feral File app and the relayer. The rest of this table is services Feral File runs; their hosts are on [Network Requirements](art-computer/network-requirements.md). Each row says what stops when that thing is missing: the app not installed, or the service unreachable.

| Feral File's | What it is | What stops without it |
| :-- | :-- | :-- |
| The Feral File app | The phone app: browse the art Feral File publishes, keep your collection, pair an Art Computer to your account, and control it | Pairing to an account, and control from your phone. Wi-Fi setup from the Art Computer's own setup hotspot keeps working, and so does control from ff-cli, or any program on the same network, over the LAN API. |
| The relayer | The cloud service that carries commands to an Art Computer from the app on another network, and from a web page using Play on Art Computer | Control from the app when the phone is on another network, and play requests from a browser. The LAN API keeps working. |
| Pairing | Binding an Art Computer to an account, over the local network or by the QR code; both paths go through Feral File's cloud | Pairing a new Art Computer. One paired before stays paired, and control over the LAN API needs no pairing step after that. |
| The hosted feed | feed.feralfile.com, Feral File's own DP-1 feed | Feral File's channels, Daily among them. Playlists from any other feed, or sent directly, keep working. |
| The indexer | Artwork metadata for works found through Feral File | Metadata for those works. A playlist that carries its own metadata keeps working. |
| Hosting of works | The video and files of the works Feral File publishes | Those works, once the offline cache runs out. Works hosted anywhere else keep playing. |
| Remote configuration | Settings the player reads when it starts | Nothing within a session; the player keeps the copy it read. After a restart with the source unreachable it runs on its built-in defaults. |
| Software updates | FF OS updates, which come only from Feral File's signed channel | Updates. The Art Computer keeps running the version it has. |
| The browser pairing broker | `handoff.feralfile.com`, which pairs a web page with an Art Computer for [Play on Art Computer](art-computer/play.md), even on the same network | Pairing a new site. A site already paired keeps sending play requests through the relayer until its session expires. |
| Support logs and telemetry | Log upload when you send logs to support, and the metrics Feral File reads | Sending logs to support, and the metrics. |

## What is yours

- **Root access.** `ff-cli ssh enable --pubkey <key.pub> --ttl 30m -d <name>` opens SSH on the local network until the time runs out; without `--ttl` it stays open until `ff-cli ssh disable`. On firmware that includes Tailscale, a VPN, owner access over it stays open once enrolled ([ff-cli](ff-cli/index.md#owner-remote-maintenance)).
- **The operating system.** FF OS can be reinstalled from a USB stick ([Getting Started](art-computer/index.md)), and Secure Boot is off.

## Updates without Feral File

Not yet. Feral File's own FF OS image pipeline needs Feral File's storage credentials and signing key. Whether someone outside can build an image from the open source with their own keys and point an Art Computer at their own update channel is untested. Until it is, playing survives Feral File and updating does not.
