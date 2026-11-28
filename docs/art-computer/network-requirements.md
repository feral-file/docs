# Network Requirements

On a home network there is nothing to configure. This page is for IT teams putting an Art Computer on a managed network (a museum, gallery, office, or campus) with a firewall, VLANs, or wireless isolation.

What keeps working when none of these hosts can be reached is on [Open source](../open-source.md#running-without-feral-file).

## Outbound access

The Art Computer needs outbound connections only. It hosts nothing publicly and needs no inbound rules from the internet.

Allow outbound **TCP 443** (HTTPS and WSS) to:

| Host | Purpose |
| :-- | :-- |
| `relayer.feralfile.io` | Control from the Feral File app on another network, and display requests from websites. Display and control on the local network do not depend on it |
| `ffos.feralfile.com`, `ffos.feralfile.io` | FF OS updates. A new Art Computer checks its version here before it shows the pairing code |
| `feed.feralfile.com` | Playlists and channels from Feral File's hosted feed |
| `indexer-v2.feralfile.com`, `indexer.feralfile.com`, `catalog.feralfile.io` | Artwork metadata |
| `customer-vt0p8j34ppjv1kd4.cloudflarestream.com` | Video for works Feral File hosts |
| `*.r2.cloudflarestorage.com` | Files for works Feral File hosts |
| `feralfile-remote-configs.pages.dev` | Remote configuration |
| `raw.githubusercontent.com` | Release notes and legal documents |
| `handoff.feralfile.com` | Pairing a website for [Display on Art Computer](./display.md) |
| `link.feralfile.com` | The address in the pairing code on screen. The phone that pairs opens it, so allow it for the phone as well |
| `ingest-metrics.feralfile.com` | Device metrics and crash reports |
| `support-logs.feralfile.com` | Log upload when the owner sends logs to support. The device posts here, receives a presigned upload address, and uploads the logs to that address, so allow that address too |
| `rpc.feralfile.com`, `ethereum-rpc.publicnode.com`, `eth.drpc.org`, `mainnet.base.org`, `base-rpc.publicnode.com`, `base.drpc.org`, `mainnet.smartpy.io`, `rpc.tzkt.io` | Reading works whose files are stored on Ethereum, Base, or Tezos |
| `ipapi.co`, `ipinfo.io`, `geoip.chrisdown.name`, `worldtimeapi.org`, `ipwho.is`, `reallyfreegeoip.org`, `api.ipbase.com` | Time zone lookup. Any one is enough |
| `8.8.8.8`, `8.8.4.4`, `223.5.5.5`, `1.12.12.12` | The online check. The device decides it is online when it can open a connection to port 443 on any one of these addresses |
| `1.1.1.1` (ports 443 and 53) and `connectivitycheck.gstatic.com` (port 80) | Network diagnostics the device runs when it believes it is offline. Support reads the result |

Works are fetched from wherever the playlist points (artist sites, IPFS gateways, CDNs), so a network that allows hosts by name also needs to allow the hosts of the works on display.

Also allow:

- **DNS** (UDP and TCP 53, or your network's resolvers)
- **NTP** (UDP 123) to `pool.ntp.org` and `time.cloudflare.com`

!!! warning "NTP is not optional"
    The Art Computer sets its clock over NTP before it validates TLS certificates. With NTP blocked, every HTTPS connection fails, and the errors look like certificate problems.

## Wi-Fi and Ethernet

- **Supported Wi-Fi:** password-protected (WPA personal) and open networks, including hidden ones. **Enterprise Wi-Fi (802.1X, with a username or certificate) is not supported.** Use Ethernet on those networks.
- **Ethernet:** the Gigabit port is behind the removable side panels. A wired Art Computer skips Wi-Fi setup. There is a [printable side panel](./faceplates/index.md) that leaves the port exposed. Wired interfaces are armed for Wake-on-LAN on adapters that support it.
- **Wi-Fi setup happens from a phone**, over a temporary hotspot named `FF1-<device id>` that the Art Computer broadcasts. The phone is off your network for that step, and a phone managed so it cannot join unknown networks cannot do it.
- **A hotspot that keeps coming back on a new Art Computer** means it joined your network and could not reach the internet. Check the outbound rules above before the Wi-Fi password.
- **Pairing:** pair from a phone on the same Wi-Fi as the Art Computer, by scanning the code on its screen.

## What the Art Computer exposes on the local network

None of this needs to be reachable from the internet.

| Port | Protocol | Purpose |
| :-- | :-- | :-- |
| TCP **1111** | HTTP and WebSocket | The device API: commands, status, a notification stream, and Prometheus `/metrics`. It is up whenever the device has a link, with or without internet |
| UDP **5353** | mDNS | Advertises `_ff1._tcp` (multicast `224.0.0.251`) so the app and `ff-cli` can find the device |
| TCP **80** | HTTP | The Wi-Fi setup page, only while the setup hotspot is up |
| TCP **9431** | HTTP | The local metrics agent |
| TCP **22** | SSH | Only while the owner has turned SSH on with `ff-cli ssh enable` |

!!! note "Who can control it from the local network"
    Any host on the local network can send display and playback commands, read status, and change volume, rotation, and sleep, without a key. The owner can turn that off in the app under **Guest control**. Commands that change the device itself (SSH access, factory reset, Wi-Fi setup, updates, shutdown) are accepted only when signed by a key the owner has registered. Put the Art Computer on a network segment whose clients you trust to change what is on display.

## Control from the app, ff-cli, or an agent

- **The Feral File app** reaches the Art Computer through the relayer from any network, and directly on port 1111 when the phone is on the same network. Both the phone and the device connect outbound.
- **[ff-cli](../ff-cli/index.md) and coding agents** run on a computer that talks directly to the Art Computer on **TCP 1111**. The two must be able to reach each other: the same VLAN, or routed with port 1111 allowed. **Client isolation must be off** between them.
- **Discovery is optional.** It uses mDNS, which needs multicast on a shared broadcast domain. Where multicast is blocked, register the Art Computer by address:

```bash
ff-cli device add --host http://<device-ip>:1111 --name "Gallery 1"
```

A small dedicated network for the Art Computers and the operator's computer, with isolation off, is enough when the main network cannot allow this.

## What usually breaks

- **TLS inspection.** Interception breaks the relayer's WebSocket connection, so app control fails while normal browsing works. Exempt the device.
- **A captive portal that asks again.** The device's connections drop when the portal expires the session. Use a network that does not ask again, or allow the device's MAC address.
- **Client isolation.** ff-cli times out. Turn isolation off between the computer and the Art Computer.

Support: **[support@feralfile.com](mailto:support@feralfile.com)**, with a description of the network. **Send logs** in the app uploads the device's logs, its network diagnostics among them.
