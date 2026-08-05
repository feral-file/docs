# Browser Integration

Add a **Play on Art Computer** action to your website: a visitor selects works
on your site, presses play, and the works appear on their Art Computer.

- What this is: a browser library that pairs your site with a visitor's Art
  Computer and plays a DP-1 playlist on it.
- Why use it: curation stays on your site; playback lands on the visitor's
  device. No backend changes, no API key, no registration.
- What to do next: mount the button, build a DP-1 playlist from the visitor's
  selection, and test against your own Art Computer.

## How it works for the visitor

1. They press **Play on Art Computer** on your site.
2. First time only: a popup asks for a pairing code. They turn on **Browser
   Pairing** for their Art Computer in the Feral File mobile app
   (Settings → Art Computers → select the device), enter the code shown on its
   display, and approve the browser session in the app.
3. The playlist plays. Later plays from your site skip pairing — the session
   is remembered per site origin until it expires or is revoked.

Your site never receives device API keys or account credentials. It holds a
short-lived, revokable browser session scoped to playback only. The mint
request and the returned session travel end-to-end encrypted between the
visitor's browser and their device, so the pairing broker never sees session
tokens or playlist content. The broker does see the pairing code, your site's
origin, and the browser metadata sent at channel join.

## Mount the button

The library lives in
[`feral-file/ff-art-computer-handoff`](https://github.com/feral-file/ff-art-computer-handoff)
under `clients/session-recipient/js` (`@feral-file/mint-pairing-requester-js`,
consumed from the repo — not yet on npm).

```ts
import { mountPlayOnArtComputerButton } from "@feral-file/mint-pairing-requester-js";

mountPlayOnArtComputerButton({
  container: "#play-on-art-computer",
  playlist: () => buildDp1PlaylistFromSelection(),
  brokerBaseUrl: "https://handoff.feralfile.com"
});
```

On click this checks for a stored browser session, runs the pairing popup only
when there is none, waits for approval in the mobile app, then plays the
playlist. `playlist` accepts an async function, so you can build the DP-1
document at click time from the visitor's current selection.

The button, popup copy, and styling are all overridable, and a headless API
(`requestEphemeralSession` / `displayDp1Playlist`) is available for fully
custom UI. The canonical reference for the full option surface, session
lifecycle, and error handling is the
[Third-Party Integration Guide](https://github.com/feral-file/ff-art-computer-handoff/blob/main/docs/third-party-integration.md)
in the repo.

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
- the relayer that carries the play request — its base URL is delivered in the
  approved session (`session.relayerBaseUrl`)

## Status

The library, hosted broker, mobile-app approval flow, and device playback work
end to end today. The integration surface is pre-1.0: the library is consumed
from the repo rather than npm, and API feedback is actively wanted. Tell us
what is unclear, impractical, or missing —
[open an issue](https://github.com/feral-file/ff-art-computer-handoff/issues)
on the repo.
