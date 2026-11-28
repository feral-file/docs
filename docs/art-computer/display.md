# Display on Art Computer

Add a **Display on Art Computer** button to your website. A visitor selects works, presses the button, and the works go on display on their Art Computer. It is for any product where people encounter art: a marketplace, an artist's site, a gallery's site.

The button is a browser library. Your site builds a [DP-1](https://github.com/display-protocol/dp1) playlist, and the library pairs with the visitor's Art Computer and sends it. The first time, the visitor approves your site in the Feral File app. It needs no backend changes, no API key, and no registration.

## Mount the button

```sh
npm i @feralfile/display
```

```ts
import { mountDisplayOnArtComputerButton } from "@feralfile/display";

mountDisplayOnArtComputerButton({
  container: "#display-on-art-computer",
  playlist: () => buildDp1PlaylistFromSelection(),
  brokerBaseUrl: "https://handoff.feralfile.com",
  relayerBaseUrl: "https://tv-cast-coordination.autonomy-system.workers.dev"
});
```

`playlist` can be an async function, so you can build the playlist when the visitor clicks. To check a playlist before wiring the button, run `ff-cli validate playlist.json`, or display it on your own Art Computer with [ff-cli](../ff-cli/index.md).

The [Integration Guide](https://github.com/feral-file/ff-send/blob/main/docs/integration.md) in the library's repository has the rest: what the visitor sees, a build with no bundler, custom buttons and dialogs, error codes, what Feral File's servers can and cannot see, and the hosts to allow in a `Content-Security-Policy`.

## Declare your page's playlist

A page that presents a set of works can name the DP-1 playlist that carries
them. Put one line in the page's `<head>`:

```html
<link rel="alternate" type="application/json" href="https://example.com/show/playlist.json" title="DP-1 playlist">
```

A client given the page's address can then find the playlist without the
visitor hunting for it. The page stays the thing people share; the playlist is
what goes on display.

- `rel` includes `alternate`, and `title` is exactly `DP-1 playlist`. The title
  is what marks the link, because `application/json` alone does not say DP-1.
- `href` is the playlist's `http(s)` address. It may be relative to the page.
- The address serves the playlist as JSON to any client, with no login. Sign
  the playlist: a client verifies it the same way it verifies any hosted
  playlist, and being linked from your page grants it nothing.
- Declare one playlist per page. A client uses the first matching link.

[ff-cli](../ff-cli/index.md) follows this line:

```bash
ff-cli display "https://feralfile.com/exhibitions/e-volved-formulae-8an"
```

That displays the exhibition's works, not the page. Feral File exhibition
pages declare their playlists this way. If the declared playlist does not
load, `display` stops with an error and sends nothing; `ff-cli display --web`
displays the page itself.

This works alongside the button: the button serves a visitor in the browser,
and the declared playlist serves anyone, or any agent, holding the page's
address.

## Feedback

Tell us what is unclear or missing by [opening an issue](https://github.com/feral-file/ff-send/issues).
