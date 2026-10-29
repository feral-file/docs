# Open source

Everything that plays the work is open source: the protocol, the operating system, the player, the tools that send a playlist, the feed server, and this documentation. You can read it, change it, build on it, and pass it on. The Art Computer you own is yours: you have root access, Secure Boot is off, and you can install what you like.

Two things are not open source: the Feral File app and the relayer. An Art Computer that has been paired once plays art without either (one that was never paired is not yet tested); [What is not open](#what-is-not-open) says what each does and what takes its place.

## What is open, and under which license

| Component | What it is | Code | License |
| :-- | :-- | :-- | :-- |
| DP-1 | The playlist protocol: anyone can publish a playlist, any player that speaks DP-1 can play it | [display-protocol/dp1](https://github.com/display-protocol/dp1) | CC BY 4.0 |
| FF OS | The Art Computer's operating system: the image build and the system services | [feral-file/ffos](https://github.com/feral-file/ffos), [feral-file/ffos-user](https://github.com/feral-file/ffos-user) | Apache 2.0 |
| FF Player | The player FF OS runs; it plays each work | [feral-file/ff-player](https://github.com/feral-file/ff-player) | MPL 2.0 |
| ff-cli | Build a playlist, play it on an Art Computer on your network, publish it to a feed | [feral-file/ff-cli](https://github.com/feral-file/ff-cli) | MIT |
| DP-1 feed server | The feed server; Feral File's hosted feed runs it, and you can run your own | [display-protocol/dp1-feed-v2](https://github.com/display-protocol/dp1-feed-v2) | MPL 2.0 |
| DP-1 tools and SDKs | Validation tool, publisher, Go and JavaScript SDKs | [dp1-cli](https://github.com/display-protocol/dp1-cli), [dp1-publisher](https://github.com/display-protocol/dp1-publisher), [dp1-go](https://github.com/display-protocol/dp1-go), [dp1-js](https://github.com/display-protocol/dp1-js) | MPL 2.0 |
| Play on Art Computer | The browser library and pairing broker behind [Play on Art Computer](art-computer/play.md) | [feral-file/play](https://github.com/feral-file/play) | Apache 2.0 |
| Indexer | Artwork metadata from Ethereum and Tezos | [feral-file/ff-indexer-v2](https://github.com/feral-file/ff-indexer-v2) | MPL 2.0 |
| Faceplates | The CAD files for the Art Computer's faceplate | [Print Your Own Faceplates](art-computer/faceplates/index.md) | CC BY-SA 4.0 |
| This documentation | docs.feralfile.com | [feral-file/docs](https://github.com/feral-file/docs) | CC BY 4.0 |

Every license here lets you use, change, and redistribute the work, and each asks that you keep its copyright notice and credit. Beyond that:

- **Apache 2.0 and MPL 2.0 both grant a patent license** with the code. Apache 2.0 asks that a copy you redistribute carries the license and its notices, and marks the files you changed.
- **MPL 2.0** asks that when you ship its files in a product, you make the source of those files available under MPL 2.0 and tell people how to get it. Your own files, the ones with no MPL code in them, stay under whatever terms you choose. Nothing is sent to Feral File.
- **CC BY 4.0 and CC BY-SA 4.0** ask that you link the license and say what you changed. CC BY-SA 4.0 also asks that a faceplate design you adapt and share stays under CC BY-SA 4.0 or a compatible license.

Contributions come in under the repository's license. There is no contributor agreement, and no other license on request: the same terms for everyone. A license is never withdrawn from a released version.

## What is not open

- **The Feral File app.** The phone app: browse the art Feral File publishes, keep your collection, pair an Art Computer to your account, and control it. Without it, you put the Art Computer on Wi-Fi by joining the setup hotspot it broadcasts and opening its setup page ([Getting Started](art-computer/index.md)), and you control it from [ff-cli](ff-cli/index.md), or from any program on the same network, over the LAN API: the command interface the Art Computer serves on your local network. Pairing to an account needs the app and Feral File's cloud.
- **The relayer.** The cloud service that carries commands to an Art Computer from the app when the phone is on another network, and from [Play on Art Computer](art-computer/play.md) in a browser. Without it, control over the LAN API on the same network still works.

Feral File also runs services: the hosted feed at feed.feralfile.com, the hosting for the works it publishes, and the catalog behind feralfile.com. The hosted feed runs the open feed server listed above; you can run your own feed, use another one, or send a playlist to the Art Computer directly, and a work can be hosted anywhere. What keeps working when none of Feral File's servers can be reached, and what stops, is on [Running without Feral File](art-computer/without-feral-file.md).
