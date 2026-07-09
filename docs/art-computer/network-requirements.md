# Network Requirements

On a home network, there is nothing to configure. Plug the Art Computer in, pair with the app, and it works.

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

Also allow:

- **DNS** (UDP/TCP 53, or your network's resolvers)
- **NTP** (UDP 123)

!!! warning "NTP is not optional"
    The Art Computer uses NTP to set its clock before validating TLS certificates. If NTP is blocked, every HTTPS connection fails, and the errors look like certificate problems rather than a time problem.

---

## Controlling with the Feral File app (default)

The phone never connects to the Art Computer over your LAN. Both the phone and the device open outbound WebSocket connections to the cloud relayer, which brokers commands between them.

- Initial pairing uses **Bluetooth LE** (physical proximity only, no network requirements).
- Ongoing control is **WSS over TCP 443** to the relayer.
- The phone and the device do **not** need to be on the same network.
- The app does not use mDNS.

If the device egress rules above are in place, the app path needs nothing further.

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

- **Client / AP isolation on.** The laptop cannot reach the device at all; ff-cli times out. Turn isolation off between the two, or use a dedicated SSID.
- **Multicast / mDNS blocked.** Discovery fails but nothing else is wrong. Register the device by IP as shown above.
- **TLS inspection / MITM proxy.** Interception on the WSS path breaks the relayer's WebSocket upgrade, so app control fails even though normal browsing works. Exempt the device from inspection.
- **Captive portal with periodic re-authentication.** The device's relayer connection drops silently when the portal expires the session. Use a network that does not re-prompt, or whitelist the device's MAC address.
- **NTP blocked.** All TLS fails with misleading certificate errors. Allow UDP 123.

Still stuck? Email **[support@feralfile.com](mailto:support@feralfile.com)** with a description of your network setup.
