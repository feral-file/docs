# Channels

A **channel** is a persistent, signed collection of playlists with a publisher
identity. People follow a channel on their Art Computer; when you add or update
its playlists, their devices pick up the change. A playlist is a one-time
selection — a channel is something you keep.

Use a channel when you want an ongoing, followable presence (a gallery, a
curator, a platform) rather than a single hand-off.

!!! note "Playlists come first"
    A channel references playlists, it doesn't contain artworks directly. Build
    your playlists first — see **[ff-cli](../ff-cli/index.md)** or the
    **[Hosted Feed](../hosted-feed/index.md)** — then add them to a channel.

## Two ways to make one

=== "No-code (web)"

    [**publisher.feralfile.com**](https://publisher.feralfile.com) is the
    no-code way to create and run a channel. Sign in, create a channel, give it
    a title and description, add your playlists in the order you want them, and
    publish. Publishing signs the channel under your publisher identity so
    devices can verify it.

    This is the right path for curators and partners — no API keys, no JSON.

=== "API (programmatic)"

    Channels are first-class on the hosted DP-1 feed. Read operations are
    public; writes need a Bearer API key.

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
    `coverImage`, and `curators`. The feed signs the channel server-side on
    write. For the authoritative field list and every endpoint
    (`GET`/`POST`/`PUT`/`PATCH`/`DELETE` on `/channels` and
    `/channels/{id}`), see the feed
    [OpenAPI](https://github.com/display-protocol/dp1-feed-v2/blob/main/api/openapi.yaml)
    and the [channel extension schema](https://github.com/display-protocol/dp1/tree/main/extensions/channels).

## How following works

A channel carries at least one **feed** signature and one **publisher**
signature; conforming players verify both before they trust it. Once a device
follows your channel, the playlists you add or reorder propagate to it — that's
the difference between a channel and a one-off playlist hand-off.

## See also

- **[Agents Quickstart](../agents/index.md)** — set up a coding agent to build the playlists a channel points at.
- **[Hosted Feed](../hosted-feed/index.md)** — the managed endpoint channels and playlists live on.
- **[ff-cli](../ff-cli/index.md)** — build and publish the playlists.
