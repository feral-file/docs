# Network Requirements

On a home network, there is nothing to configure. Plug the Art Computer in, join its setup hotspot from your phone, pick your Wi-Fi, pair with the app, and it works.

This page is for IT teams putting an Art Computer on a managed network — a museum, gallery, office, or campus — where firewalls, VLANs, and wireless isolation policies are in play. It lists exactly what the device and its controllers need, and the policies that most often break them.

---

## Device internet access (required)

The Art Computer needs outbound HTTPS. It hosts nothing publicly and needs no inbound rules from the internet.

Allow outbound **TCP 443** (HTTPS and WSS) to:

| Host | Purpose |
| :-- | :-- |
| `tv-cast-coordination.autonomy-system.workers.dev` | Cloud relayer for app control (critical) |
| `dp1-feed-operator-api-prod.autonomy-system.workers.dev` | Playlists and channels |
| `customer-vt0p8j34ppjv1kd4.cloudflarestream.com` | Video assets (HLS) |
| `indexer-v2.feralfile.com` | Artwork metadata |
| `feralfile-remote-configs.pages.dev` | Remote configuration |
| `raw.githubusercontent.com` | Release notes and legal documents |
| `*.r2.cloudflarestorage.com` | Asset storage |
| `ingest-metrics.feralfile.com` | Device telemetry. The analytics toggle in the app stops periodic metrics collection, but the device still pushes a few events (watchdog crash reports) over this connection, so keep the host allowed |
| `support-logs.feralfile.com` | Log upload when you send logs to support from the app. The upload is two steps: the device posts to this host, which hands back a presigned upload URL, and the device then PUTs the log archive to that URL. Allow the presigned upload URL as well, or the upload gets a submission id and no logs |
| `handoff.feralfile.com` | Browser pairing broker for [Play on Art Computer](./play.md) |
| `link.feralfile.com` | Pairing QR target. The QR code on screen encodes a `link.feralfile.com` address that the owner's phone opens, so allow it for the phone doing the pairing, not only for the device |
| `8.8.8.8` and `8.8.4.4` | Internet-reachability check. The device decides whether it is online by opening a TCP connection to port 443 on these two addresses |
| `1.1.1.1` | Neutral reachability probe used by the network diagnostics the device runs when it believes it is offline |

Artworks themselves are fetched from wherever the playlist points — artist sites, IPFS gateways, CDNs — so a network that allow-lists hosts will also need to allow whatever the collection references.

Also allow:

- **DNS** (UDP/TCP 53, or your network's resolvers)
- **NTP** (UDP 123)

!!! warning "NTP is not optional"
    The Art Computer uses NTP to set its clock before validating TLS certificates. If NTP is blocked, every HTTPS connection fails, and the errors look like certificate problems rather than a time problem.

!!! warning "The reachability check dials IP addresses, not names"
    The device does not decide it is online by reaching a Feral File host. It opens a TCP connection to `8.8.8.8:443` and `8.8.4.4:443`. If your firewall allows every host in the table above but blocks those two addresses on port 443, the device reports itself offline even when it is not, and anything keyed on that verdict follows the wrong answer. Blocking `1.1.1.1:443` does not put the device offline, but it removes one of the signals in the diagnostics support reads, so a filtered network is harder to tell from a real outage.

---

## Wi-Fi setup (the setup hotspot)

The Art Computer is put on Wi-Fi from a phone, through a hotspot the device itself broadcasts — there is no Bluetooth step.

- The device raises an access point named **`FF1-<device id>`** (WPA2, 8-digit numeric password). The SSID, password, and a join QR code are shown on the screen.
- The phone joins that hotspot. Scanning the QR code may still require the user to follow a connection prompt; labels vary by phone and may include **Join**, **Connect**, or **Sign in to network**. Some phones open Wi-Fi settings and leave the `FF1-…` network unselected. If the phone warns that the hotspot has no internet, the user should choose the option that keeps it connected. Captive-portal detection then opens the setup page automatically; if it does not, the TV shows the hotspot's direct numeric address as a DNS-independent browser fallback. If the browser remains on cellular despite the Wi-Fi connection, temporarily disabling mobile data and any VPN makes the on-link address deterministic on Android and iOS.
- The setup page lists the networks the device can see, excluding its own temporary `FF1-…` setup network, and starts with no destination selected. It also provides a manual field for hidden networks.
- The user picks the network the Art Computer should use and enters that network's password, not the numeric setup password shown on the TV. The hotspot goes down while the device joins; if the join fails it comes back so the user can retry.

What this means for a managed network:

- **Supported networks:** password-protected (personal / PSK) and open Wi-Fi, including hidden SSIDs. **Enterprise Wi-Fi (802.1X / WPA-Enterprise with usernames or certificates) cannot be entered through the setup page** — on those networks, use Ethernet.
- The phone is off your network for the minute it is on the setup hotspot. Nothing on your network is involved in that step; MDM policies that block joining unknown SSIDs will block it.
- The hotspot is raised on first boot, and again when a paired device has had **no link at all** (no cable, no Wi-Fi association) for about five minutes — a changed Wi-Fi password, a retired SSID — or boots somewhere none of its saved networks are in range. A **paired** device that is associated but has no internet (upstream outage) keeps its network connection and does not re-enter setup; the app can put it back into setup mode on demand (not while an Ethernet cable is connected).
- An **unpaired** device that gets onto a network but cannot reach the internet — the classic "got an IP, firewalled from the relayer" case on a managed network — reopens its setup hotspot after about five minutes, for a few cycles, so setup can be redone. If you see the `FF1-…` hotspot keep reappearing on a new device, check the egress rules above rather than the Wi-Fi credentials.
- While the hotspot is up, the device periodically drops it for up to a few minutes to scan for the user's network, then brings it back. A setup screen that disappears and returns on its own is not a fault.
- A device with working Ethernet skips Wi-Fi setup entirely.

---

## Wired Ethernet

The Art Computer has a Gigabit Ethernet port behind its removable side panels (see the [specification](./specification.md)). On networks where wireless policy is the sticking point — enterprise Wi-Fi, wireless isolation, MDM restrictions on the phone — wiring the device is the simplest fix: the egress rules above still apply, but Wi-Fi setup, captive portals, and wireless isolation drop out of the picture.

Wired interfaces are armed for **Wake-on-LAN** (magic packet) at startup, on adapters that support it.

The stock enclosure ships sealed for simplicity. If you want the port permanently accessible, there is a [3D-printable side panel](./faceplates/index.md) with the LAN port exposed.

---

## What the device exposes on the LAN

The Art Computer listens on the local network for its own controllers. None of this needs to be reachable from the internet.

| Port | Protocol | Purpose |
| :-- | :-- | :-- |
| TCP **1111** | HTTP / WebSocket | Device API: commands (`POST /api/cast`), status (`GET /api/status`, `/api/v2/status`), screenshot, notification stream, Prometheus `/metrics`. Up whenever the device has a link, internet or not. |
| UDP **5353** | mDNS | Service advertisement `_ff1._tcp` (multicast `224.0.0.251`), so the app and `ff-cli` can find the device. |
| TCP **80** | HTTP | Captive portal — served only while the setup hotspot is up. |
| TCP **9431** | HTTP | Local metrics agent (vmagent): status UI and its metrics import endpoint. |

!!! note "The LAN is the trust boundary"
    The port 1111 API is **unauthenticated** in the current release: any host that can reach the device on the local network can drive it (and any host can push metrics into the agent on port 9431). That is the deliberate, release-scoped design — LAN presence is the authorization — and the reason to put the device on a network segment where local clients are trusted. Screen-anchored LAN pairing, where the device stores authorized controller keys, is the planned end state.

---

## Controlling with the Feral File app (default)

The app reaches the Art Computer two ways:

- **Over the cloud relayer.** Both the phone and the device open outbound WebSocket connections (WSS over TCP 443) to the relayer, which brokers commands between them. The phone and the device do **not** need to be on the same network, and nothing inbound is required.
- **Over the LAN.** When the phone and the device are on the same network, the app discovers the device with mDNS (`_ff1._tcp`) and can talk to it directly on port 1111. This is the primary path for first-time pairing (the app finds the device and offers to pair it; the QR code on screen is the backup when discovery is blocked) and for local recovery such as re-running Wi-Fi setup.

If the device egress rules above are in place, the relayer path needs nothing further. If your network blocks multicast or isolates clients, pairing still works by scanning the QR code — the phone then binds the device through the cloud.

---

## Controlling with ff-cli or a coding agent

The [ff-cli](../ff-cli/index.md) and [agent](../agents/index.md) workflows run on a laptop that talks **directly to the Art Computer over the local network**:

- The laptop sends commands to the device over **HTTP on TCP 1111**.
- The laptop and the device must be able to reach each other — same VLAN, or routed with port 1111 allowed between them.
- **Client / AP isolation must be off** between the laptop and the device. Enterprise Wi-Fi often enables isolation by default, and it is the most common thing that breaks this path.

Device discovery uses mDNS / Bonjour, but it is optional:

- Discovery: service type `_ff1._tcp`, UDP 5353, multicast group `224.0.0.251`. Requires the laptop and device to share a broadcast domain with multicast allowed.
- If your network blocks multicast, skip discovery and register the device by address:

```bash
ff-cli device add --host http://<device-ip>:1111 --name "Gallery 1"
```

If neither reachability nor a static address is workable on the main network, a small dedicated SSID/VLAN for the device and the operator's laptop — isolation off, mDNS allowed — is enough. Even a single access point works.

---

## Common failure modes on managed networks

- **Enterprise (802.1X) Wi-Fi only.** The setup page cannot take enterprise credentials. Use Ethernet, or a PSK guest SSID with the egress rules above.
- **Phone cannot join the setup hotspot.** MDM or a policy blocking unknown SSIDs. Use a personal phone for the one-minute setup step, or wire the device.
- **Client / AP isolation on.** The laptop cannot reach the device at all; ff-cli times out. Turn isolation off between the two, or use a dedicated SSID.
- **Multicast / mDNS blocked.** Discovery fails but nothing else is wrong. The app falls back to the QR code for pairing; register the device by IP for ff-cli as shown above.
- **TLS inspection / MITM proxy.** Interception on the WSS path breaks the relayer's WebSocket upgrade, so app control fails even though normal browsing works. Exempt the device from inspection.
- **Captive portal with periodic re-authentication.** The device's relayer connection drops silently when the portal expires the session. Use a network that does not re-prompt, or whitelist the device's MAC address.
- **NTP blocked.** All TLS fails with misleading certificate errors. Allow UDP 123.
- **Reachability addresses blocked.** Everything the device needs is allowed, and it still says it is offline. Allow TCP 443 to `8.8.8.8` and `8.8.4.4`, which is how the device answers the question.

Still stuck? Email **[support@feralfile.com](mailto:support@feralfile.com)** with a description of your network setup. From the app, **Send logs** uploads the device's logs — including its network flight recorder — so support can see what the device saw.
