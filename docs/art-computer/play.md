# Play on Art Computer

Add a **Play on Art Computer** action to your product: someone selects works,
presses play, and the works appear on their Art Computer. It is for any
product where people encounter art — a marketplace, an artist's site, a
gallery app, an agent.

- What this is: a browser library that pairs your product with a visitor's Art
  Computer and plays a DP-1 playlist on it. It targets the web runtime —
  websites, web apps, Electron, web views inside native apps — and fully
  native clients can implement the documented protocol directly.
- Why use it: curation stays where it already happens, in your product;
  playback lands on the visitor's device. No backend changes, no API key, no
  registration.
- What to do next: mount the button, build a DP-1 playlist from the visitor's
  selection, and test against your own Art Computer.

## How it works for the visitor

1. They press **Play on Art Computer** on your site.
2. First time only, a pairing dialog opens:
   - **On a phone or tablet** it shows **Open the Feral File app**. They tap
     it, the app opens with the request, and they tap **Accept**.
   - **On a desktop or laptop** it shows a QR code. They scan it with the
     phone camera or the Feral File app, and tap **Accept** in the app.

   A six-digit code sits under the button or QR on both. A visitor can type it
   into the app instead: **Pair a site** in their Art Computer's settings. A
   code lasts five minutes; when it runs out the dialog shows a fresh one, up
   to twice.
3. The playlist plays. Later plays from your site skip pairing — the session
   is remembered per site origin until it expires or is removed.

Your site shows the request and the app, which holds the authority, accepts
it. The visitor never opens a settings page on the Art Computer or carries a
code from it to your site.

When approving, the owner can keep your site paired. That session does not
expire; it lasts until they remove it under **Paired sites** in the Art
Computer's settings in the app. Otherwise the session is short-lived. A site
on a library older than 0.3.0 gets a timed session even when the owner keeps
it paired.

Your site never receives device API keys or account credentials. It holds a
revokable browser session scoped to playback only. The mint request and the
returned session travel end-to-end encrypted between the visitor's browser and
their device, so the pairing broker never sees session tokens or playlist
content. The broker does see your site's origin, the browser metadata you
supply, and the pairing code it issues. The origin is attested, not claimed:
the broker reads it from the `Origin` header the visitor's browser sets, so
the approval prompt in the app names the site that actually asked.

## Mount the button

Install [`@feralfile/play`](https://www.npmjs.com/package/@feralfile/play)
(source lives in [`feral-file/play`](https://github.com/feral-file/play)):

```sh
npm i @feralfile/play
```

For a site with no build step, download `play.js` from the
[latest release](https://github.com/feral-file/play/releases/latest) — a
self-contained ESM bundle — host it next to your pages, and
`import { mountPlayOnArtComputerButton } from "./play.js"`.

```ts
import { mountPlayOnArtComputerButton } from "@feralfile/play";

mountPlayOnArtComputerButton({
  container: "#play-on-art-computer",
  playlist: () => buildDp1PlaylistFromSelection(),
  brokerBaseUrl: "https://handoff.feralfile.com",
  // Fallback when the session carries no relayer URL; see Network endpoints.
  relayerBaseUrl: "https://tv-cast-coordination.autonomy-system.workers.dev"
});
```

On click this checks for a stored browser session; when there is none it
opens the pairing dialog, waits for the Art Computer to join and the owner to
approve in the app, then plays the playlist. `playlist` accepts an async
function, so you can build the DP-1 document at click time from the visitor's
current selection.

The button, dialog copy, and styling are all overridable. `appLinkBaseUrl`
sets where the app link points; it defaults to
`https://link.feralfile.com/pair`, which opens the Feral File app when it is
installed and offers the install otherwise. For fully custom UI:

- `requestEphemeralSessionWithPairingUi` reuses a stored session or runs the
  pairing dialog; pass `createDialog` to replace the dialog entirely, or start
  from `createPairingDialog`.
- `requestEphemeralSession` is the headless core. It hands you the pairing
  material through `onPairingMaterial({ appLink, shortCode, expiresAt })`:
  open or encode `appLink` as a QR, show `shortCode`. The app link carries a
  single-use pairing token — show it to the visitor, never log it or send it
  to analytics.
- `displayDp1Playlist` sends the playlist on an approved session.

Errors are `PlayError` instances with a stable `code`: `pairing_code_expired`,
`mint_rejected`, `approval_timeout`, `session_rejected`, `pairing_canceled`,
`display_failed`, `display_rejected`. Match on the code, not the message. The
canonical reference for the full option surface, session lifecycle, and error
handling is the
[Integration Guide](https://github.com/feral-file/play/blob/main/docs/integration.md)
in the repo.

## Upgrading from 0.3.x

Sites on 0.3.x pair the other way — the Art Computer shows a code and the
visitor types it into the site — and keep working; the hosted broker still
serves that path. To move to 0.4.0:

- **Wrapped button:** no change. `appLinkBaseUrl` is optional.
- **`requestEphemeralSession`:** the `pairing` input (`{ shortCode }` /
  `{ qrPayload }`) is removed, along with `parsePairingQrPayload` and
  `pairingToResolved`. Pass `brokerBaseUrl` and `onPairingMaterial` instead.
- **Dialog:** `createPairingCodeDialog` is now `createPairingDialog`.
- **Errors:** drop matches on `pairing_code_not_found` and
  `pairing_code_used`; a site can no longer hit them.

## The playlist

The button takes a [DP-1](https://github.com/display-protocol/dp1) playlist
document. Each item points at a URL the Art Computer can render — artwork
pages, media files, generative works. Playlist content never travels through
Feral File pairing infrastructure: the device fetches the works directly from
the URLs in your playlist.

To hand-check a playlist before wiring up the button, use
[ff-cli](../ff-cli/index.md) (`ff-cli validate playlist.json`) or play it on
your own device with `ff-cli play`.

## Network endpoints

If your site sets a `Content-Security-Policy`, allow these in `connect-src`:

- `https://handoff.feralfile.com` — the pairing broker
- `https://tv-cast-coordination.autonomy-system.workers.dev` — the relayer
  that carries the play request. The approved session carries the base URL
  actually used (`session.relayerBaseUrl`); read it from there at runtime.

`https://link.feralfile.com` needs no entry: the app link is a navigation,
never a `fetch`, and the QR is drawn in the page by the library.

## Status

The library, hosted broker, mobile-app approval flow, and device playback work
end to end today; this page describes `@feralfile/play` 0.4.0. Joining a
site's channel needs Art Computer software 2.0.10 or later, and the app offers
**Pair a site** only for an Art Computer that has it. The integration surface
is pre-1.0, so expect additive API change between 0.x versions. API feedback is actively wanted — tell us what is
unclear, impractical, or missing by
[opening an issue](https://github.com/feral-file/play/issues)
on the repo.
