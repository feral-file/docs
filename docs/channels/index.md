# Channels

A channel is a persistent, signed collection of playlists with a publisher
identity. People follow a channel on their Art Computer, and the playlists you
add or reorder show up on their device. A playlist is a one-time selection; a
channel is something you keep.

Reach for a channel when you want an ongoing, followable presence — a gallery, a
curator, a platform — rather than a single hand-off.

!!! note "Build your playlists first"
    A channel references playlists, not artworks. Make the playlists first with
    [ff-cli](../ff-cli/index.md) or the [Hosted Feed](../hosted-feed/index.md),
    then point a channel at them.

## Make a channel

=== "No-code (web)"

    [publisher.feralfile.com](https://publisher.feralfile.com) creates and
    publishes channels with no API keys and no JSON. Sign in, assemble your
    playlists into a channel, and publish. Publishing signs the channel under
    your publisher identity so devices can verify it.

    This is the path for curators and partners.

=== "API"

    Channels are first-class on the hosted feed. Reads are public; writes need a
    Bearer API key.

    Base URL: `https://feed.feralfile.com/api/v1`

    ```bash
    # Create a channel (write — needs your API key)
    curl -H "Authorization: Bearer your-api-key-here" \
      -H "Content-Type: application/json" \
      -X POST https://feed.feralfile.com/api/v1/channels \
      -d @channel.json

    # List channels (public)
    curl https://feed.feralfile.com/api/v1/channels
    ```

    `channel.json` is a DP-1 channel: `title`, `slug`, a `publisher` identity,
    and an ordered `playlists` array of playlist URLs, plus optional `summary`,
    `coverImage`, and `curators`. The feed signs the channel on write. For the
    full field list and every endpoint, see the canonical
    [feed OpenAPI](https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml)
    and [channel extension schema](https://github.com/display-protocol/dp1/tree/main/extensions/channels).

## Reach followers

A channel carries at least one **feed** signature and one **publisher**
signature; conforming players verify both before they trust it. Once a device
follows your channel, every playlist you add or reorder propagates to it — that
is what a channel gives you over a one-off playlist.

## Next step

Build the playlists your channel will point at — see [ff-cli](../ff-cli/index.md).
