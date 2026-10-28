# Open source

Everything that plays the work is open source: the protocol, the operating system, the player, the tools that send a playlist, the feed server, and this documentation. You can read, change, build on and redistribute all of it. The Art Computer you own is yours: you have a root shell on it, Secure Boot is off, and you can install what you like. What keeps working with none of Feral File's servers reachable is on [Running without Feral File](art-computer/without-feral-file.md).

What Feral File keeps is where it chooses: the Feral File app, which is how we curate and publish our own channels, and the services we run. None of them is needed to play art on an Art Computer.

## What is open, and under which license

| Component | What it is | Code | License |
| :-- | :-- | :-- | :-- |
| DP-1 | The playlist protocol: anyone can publish a playlist, any player that speaks DP-1 can play it | [display-protocol/dp1](https://github.com/display-protocol/dp1) | CC BY 4.0 |
| FF OS | The Art Computer's operating system: the image build and the system services | [feral-file/ffos](https://github.com/feral-file/ffos), [feral-file/ffos-user](https://github.com/feral-file/ffos-user) | Apache 2.0 |
| FF Player | The player FF OS runs; it plays each work | [feral-file/ff-player](https://github.com/feral-file/ff-player) | MPL 2.0 |
| ff-cli | Build a playlist, play it on an Art Computer on your network, publish it to a feed | [feral-file/ff-cli](https://github.com/feral-file/ff-cli) | MIT |
| DP-1 feed server | The reference feed server; run your own | [display-protocol/dp1-feed-v2](https://github.com/display-protocol/dp1-feed-v2) | MPL 2.0 |
| DP-1 tools and SDKs | Validation tool, publisher, Go and JavaScript SDKs | [dp1-cli](https://github.com/display-protocol/dp1-cli), [dp1-publisher](https://github.com/display-protocol/dp1-publisher), [dp1-go](https://github.com/display-protocol/dp1-go), [dp1-js](https://github.com/display-protocol/dp1-js) | MPL 2.0 |
| Play on Art Computer | The browser library and pairing broker behind [Play on Art Computer](art-computer/play.md) | [feral-file/play](https://github.com/feral-file/play) | Apache 2.0 |
| Indexer | Artwork metadata from Ethereum and Tezos | [feral-file/ff-indexer-v2](https://github.com/feral-file/ff-indexer-v2) | MPL 2.0 |
| Faceplates | The Art Computer's faceplate CAD | [Print Your Own Faceplates](art-computer/faceplates/index.md) | CC BY-SA 4.0 |
| This documentation | docs.feralfile.com | [feral-file/docs](https://github.com/feral-file/docs) | CC BY 4.0 |

Apache 2.0 and MPL 2.0 include a patent license. MPL 2.0 asks one thing of a product that ships a changed copy of one of these files: whoever receives the product receives that file's source too. The product's own code stays its own, and nothing has to be sent to Feral File.

Contributions come in under the repository's license. There is no contributor agreement, and the same license applies to everyone. A license is never withdrawn from a released version.

## What Feral File keeps

| Component | What it is | What works without it |
| :-- | :-- | :-- |
| The Feral File app | How we curate and publish our channels, and one way to control an Art Computer | Wi-Fi setup from the Art Computer's own hotspot page, and control from ff-cli or any program on the same network, over the LAN API. Pairing an Art Computer to an account is the app's. |
| The relayer | The cloud link between the app and an Art Computer on a different network | Direct control over the LAN API |
| Video and asset hosting | Where Feral File keeps the files of the works it publishes | Works hosted anywhere else |
| The hosted feed at feed.feralfile.com | One DP-1 feed server among any number | Your own feed server, from the open-source code above |
| The catalog and exhibitions API | Feral File's own record of its exhibitions | Playlists from anywhere else |
