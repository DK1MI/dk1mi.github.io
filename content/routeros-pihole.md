---
title: MikroTik: Forcing DNS through Pi-hole with automatic failover
date: 2026-11-26
---

Like many other people, I run a [Pi-hole](https://pi-hole.net/) server at home to filter out the ever-increasing amount of 
junk (such as trackers and ads) from my network traffic. Unfortunately, however, there are some devices 
that ignore the DNS servers configured via DHCP and simply use their own. Examples include smart TVs, 
streaming sticks, and some IoT devices.

In this post I document how to make a MikroTik router running RouterOS 7 catch those queries and redirect
them to the Pi-hole anyway, and how to fall back to a public resolver automatically if the
Pi-hole goes down. I started out with just the firewall rules that force all devices to use Pi-hole
but then quickly realized that I basically have no internet access anymore as soon as the Pi-hole server
is down.

## My network

You need to know two things about my network to understand this post:

| Network | Subnet | Notes |
|---|---|---|
| LAN | `192.168.88.0/24` | Router `192.168.88.1`, **Pi-hole `192.168.88.39`** (same subnet!) |
| Other internal networks (guest Wi-Fi, DMZ, ...) | e.g. `192.168.55.0/24` | Routed through the router, isolated from the LAN by firewall rules |

The router's interface list `WAN` contains all internet-facing interfaces (PPPoE, the
physical WAN port, an LTE backup etc.).

That the Pi-hole sits **in the same subnet as the LAN clients** is important for two things: once for
the redirect (hairpin NAT) and also for the failover implementation.

## Step 1: Point DHCP at the Pi-hole

```
/ip dhcp-server network
set [find address=192.168.88.0/24] dns-server=192.168.88.39,192.168.88.1
set [find address=192.168.55.0/24] dns-server=192.168.88.39
```

The second LAN entry (the router itself) is for the failover (which I explained later). The router
doesn't answer DNS itself: the redirect in step 2 sends those queries to the Pi-hole too.

Don't use a public resolver like `8.8.8.8` as the secondary DNS entry in DHCP. It looks harmless, because the
router would redirect its port 53 queries to the Pi-hole as well. But it gives clients a known
provider that offers *encrypted* DNS, and some of them switch to it on their own (see step 5).

I know that it's maybe not a good idea to use 8.8.8.8 since it's from Google and therefore 
not really privacy friendly but I wanted something that is only used in rare situations and 
that will work with a high probability.

## Step 2: Redirect every other DNS query to the Pi-hole

```
/ip firewall nat
add chain=dstnat action=dst-nat protocol=udp dst-port=53 in-interface-list=!WAN \
    src-address=!192.168.88.39 dst-address=!192.168.88.39 to-addresses=192.168.88.39 \
    comment="DNS-PIHOLE udp"
add chain=dstnat action=dst-nat protocol=tcp dst-port=53 in-interface-list=!WAN \
    src-address=!192.168.88.39 dst-address=!192.168.88.39 to-addresses=192.168.88.39 \
    comment="DNS-PIHOLE tcp"
```

Any port 53 packet the router receives is rewritten to be redirected to Pi-hole. Connection
tracking rewrites the reply's source back, so a client that asked `8.8.8.8` sees an answer
"from `8.8.8.8`" and would therefore not try any dirty tricks....

- `src-address=!192.168.88.39`: the Pi-hole's **own** upstream queries must not be
  redirected back to itself.
- `dst-address=!192.168.88.39`: queries that already go to the Pi-hole need no rewriting.
- `in-interface-list=!WAN`: **don't skip this.** Without it, a DNS query from the internet
  to your public IP is redirected to the Pi-hole too. The default "drop all from WAN not
  DSTNATed" firewall rule then lets it through, because it *was* dst-natted. That turns your
  Pi-hole into an open resolver on the internet, ready for DNS amplification abuse. For the
  same reason, make sure *every* internet-facing interface really is in the `WAN` list.
- UDP **and** TCP: DNS can fall back to TCP.

Queries addressed to the router itself (for example, if a DMZ system uses the router as its DNS
server) are caught by the same rules, because the redirect happens before the router's input
chain sees the packet.

## Step 3: Hairpin NAT

The redirect alone breaks LAN clients with hard-coded DNS. Here's why:

1. Client `192.168.88.50` sends a query to `8.8.8.8`; the router rewrites it to `192.168.88.39`.
2. The Pi-hole sees source `192.168.88.50`, which is in its own subnet, so it replies **directly**
   to the client instead of going through the router.
3. The client receives an answer from `192.168.88.39`, but it asked `8.8.8.8` and therefore drops the reply.

The fix is to masquerade redirected queries, so the Pi-hole thinks the router asked and
sends the reply back through it:

```
/ip firewall address-list
add list=pihole-clients address=192.168.88.0/24 comment=LAN
add list=pihole-clients address=192.168.55.0/24 comment=Guest

/ip firewall nat
add chain=srcnat action=masquerade protocol=udp dst-port=53 dst-address=192.168.88.39 \
    src-address-list=pihole-clients comment="DNS to Pi-hole (udp)"
add chain=srcnat action=masquerade protocol=tcp dst-port=53 dst-address=192.168.88.39 \
    src-address-list=pihole-clients comment="DNS to Pi-hole (tcp)"
```

LAN clients that use the Pi-hole directly (via DHCP) talk to it inside the switch and never
pass through the router, so they keep showing up with their own IP in the Pi-hole log.

For **routed** networks like the guest Wi-Fi, the masquerade isn't strictly needed for the
traffic to flow. It does make the queries look local to the Pi-hole. This helps if Pi-hole's
interface setting is "Allow only local requests", which would otherwise refuse
queries from other subnets.

## Step 4: Allowing isolated networks reach Pi-hole

If your guest or DMZ networks are isolated from the LAN, add an exception for DNS **above**
the isolation rules. Forward rules see the packet *after* the dst-nat, so matching on the
Pi-hole's address covers both direct and redirected queries.

```
/ip firewall filter
add chain=forward action=accept protocol=udp dst-port=53 dst-address=192.168.88.39 \
    src-address-list=pihole-clients comment="DNS to Pi-hole (udp)" place-before=<first isolation rule>
add chain=forward action=accept protocol=tcp dst-port=53 dst-address=192.168.88.39 \
    src-address-list=pihole-clients comment="DNS to Pi-hole (tcp)" place-before=<first isolation rule>
```

## Step 5: Block encrypted DNS on port 853

The redirect only catches plain DNS on port 53. DNS-over-TLS (DoT, TCP 853) and DNS-over-QUIC
(DoQ, UDP 853) go straight past it. This isn't just about exotic devices: **Android's "Private
DNS" is set to "Automatic" by default.** Android then checks whether its DNS servers offer DoT
and uses it if they do. The Pi-hole doesn't offer it, but `8.8.8.8` does. Once an Android phone
had `8.8.8.8` as its secondary DNS server, it quietly sent encrypted queries to Google: no ad
blocking, and no internal names. That one took me a long time to figure out...

Reject port 853, and clients fall back to plain DNS, which the redirect catches:

```
/ip firewall filter
add chain=forward action=reject reject-with=tcp-reset protocol=tcp dst-port=853 \
    in-interface-list=!WAN comment="Block DoT" place-before=[find comment="DNS to Pi-hole (udp)"]
add chain=forward action=reject reject-with=icmp-port-unreachable protocol=udp dst-port=853 \
    in-interface-list=!WAN comment="Block DoQ" place-before=[find comment="DNS to Pi-hole (udp)"]
```

Use `reject`, not `drop`: clients give up right away instead of waiting for a timeout.

A phone with a fixed Private DNS hostname (for example `dns.google`) refuses to fall back, so
DNS stops working on it entirely. Set it to "Automatic" or "Off" on such devices.

At this point, all DNS goes through the Pi-hole. The rest of this post makes sure the network
survives when it doesn't.

## Step 6: Failover when the Pi-hole is down

Forcing everything through one box creates a single point of failure. If the Pi-hole
dies, nothing resolves DNS queries anymore. The goal is to switch to a public resolver 
**only when the Pi-hole is really unavailable**, and switch back when it returns.

### 6a. A second pair of redirect rules

```
/ip firewall nat
add chain=dstnat action=dst-nat protocol=udp dst-port=53 in-interface-list=!WAN \
    src-address=!192.168.88.39 to-addresses=8.8.8.8 comment="DNS-FALLBACK udp" disabled=yes
add chain=dstnat action=dst-nat protocol=tcp dst-port=53 in-interface-list=!WAN \
    src-address=!192.168.88.39 to-addresses=8.8.8.8 comment="DNS-FALLBACK tcp" disabled=yes
```

Note the missing `dst-address=!192.168.88.39`. In fallback mode, queries sent to the
(dead) Pi-hole from routed networks are redirected to `8.8.8.8` too. Guest and DMZ clients
don't even notice the switch: they keep sending to the same address, and the router decides
where it goes. The normal WAN masquerade handles the source NAT.

### 6b. Why the LAN needs a secondary DNS server

The router can't redirect a LAN client's query to `192.168.88.39`: it never sees it, because
client and Pi-hole talk directly through the switch. That's why the LAN DHCP from step 1
hands out the router (`192.168.88.1`) as a **secondary** server. Queries to it always pass
through the router's NAT:

- **Pi-hole up:** `DNS-PIHOLE` redirects them to the Pi-hole, so blocking still applies.
- **Pi-hole down:** the client's resolver gives up on the primary and asks the secondary.
  `DNS-FALLBACK` now sends those queries to `8.8.8.8`.

The router has no DoT/DoH service, so clients find nothing encrypted to switch to. A public
secondary like `8.8.8.8` invites clients to switch:
- **Android:** upgrades to DoT, as described in step 5.
- **Chrome and Windows 11:** can switch to DNS-over-HTTPS automatically when the system's
  DNS server is a known provider. DoH runs on port 443, so the port-853 block doesn't catch it.

A router IP isn't on their lists.

Routed networks (guest, DMZ) need no change to their DHCP settings.

### 6c. The health check

A script asks the Pi-hole for a name **it answers itself** for a local DNS record.
This checks the DNS service itself, not just whether the host answers a ping. And an internet
outage, where the Pi-hole is fine but can't reach its upstream, doesn't trigger a (then) pointless
failover.

The script only switches after three checks in a row agree, 10 seconds apart, in both
directions. It doesn't keep any state between runs: it reads the current mode from the NAT
rules, so it also survives reboots.

```
/system script add name=pihole-check policy=read,write,test source={
:local pihole 192.168.88.39
:local checkName "localserver.lan"
:local tries 3
:local pause 10s
:local verbose false

:local check do={
    :local ok false
    :do {
        :local a [:resolve domain-name=$name server=$server]
        :if ([:typeof [:toip $a]] = "ip") do={ :set ok true }
    } on-error={}
    :return $ok
}

:local fallbackOn ([/ip firewall nat get [find comment="DNS-FALLBACK udp"] disabled] = false)
:local up [$check name=$checkName server=$pihole]
:if ($verbose) do={ :log info "pihole-check: up=$up fallback=$fallbackOn" }

:if ($up = $fallbackOn) do={
    :local confirmed true
    :for i from=2 to=$tries do={
        :if ($confirmed) do={
            :delay $pause
            :if ([$check name=$checkName server=$pihole] != $up) do={ :set confirmed false }
            :if ($verbose) do={ :log info "pihole-check: confirm $i/$tries confirmed=$confirmed" }
        }
    }
    :if ($confirmed) do={
        :if ($up) do={
            /ip firewall nat disable [find comment~"^DNS-FALLBACK"]
            /ip firewall nat enable [find comment~"^DNS-PIHOLE"]
            /ip firewall connection remove [find dst-address~":53\$"]
            :log warning "DNS failover: Pi-hole back ($tries good checks for $checkName)"
        } else={
            /ip firewall nat disable [find comment~"^DNS-PIHOLE"]
            /ip firewall nat enable [find comment~"^DNS-FALLBACK"]
            /ip firewall connection remove [find dst-address~":53\$"]
            :log warning "DNS failover: Pi-hole down ($tries failed checks for $checkName), using 8.8.8.8"
        }
    }
}
}

/system scheduler add name=pihole-check interval=30s \
    start-date=[/system clock get date] start-time=[/system clock get time] \
    on-event="/system script run pihole-check" policy=read,write,test
```

The `connection remove` line clears existing DNS entries from connection tracking, so no
client keeps talking to the dead Pi-hole through an old NAT mapping.

Keep `(tries - 1) × pause` below the scheduler interval, so runs don't overlap. With
these values, the switch happens 20–50 seconds after the Pi-hole goes down.

### Things that took me way to long to realize

- **`:resolve` doesn't throw an error when the server is down.** In my tests on RouterOS 7.25,
  it just returned an empty result, so an `on-error` block never fired and the check always
  "succeeded". The script therefore only treats an actual IP address as success.
- **Global variables didn't survive between scheduler runs** in my setup, so a "3 failures
  in a row" counter never went past 1. I didn't find out why. The script above sidesteps this
  completely by doing all checks within one run.
- **My first secondary DNS server was `8.8.8.8`.** The failover worked, but my Android phone
  stopped using the Pi-hole altogether: Private DNS "Automatic" had found DoT at Google (my guess at least). 
  With the router as the secondary and port 853 blocked, it's back on the Pi-hole.
- **Set `verbose true` while testing.** It logs every check and makes debugging much easier.

### Testing it

1. Stop the Pi-hole's DNS service: `sudo systemctl stop pihole-FT` or `docker compose down`
2. Watch the router log: `/log print follow where message~"pihole-check|DNS failover"`
3. After 20–50 s you should see "Pi-hole down". `/ip firewall nat print where comment~"DNS-"`
   shows the FALLBACK rules enabled.
4. From a client: `nslookup example.com` should work again, maybe with a short delay (see below).
5. Start the Pi-hole again and wait for "Pi-hole back".

To check that the redirect works at all, ask Google for a name only the Pi-hole knows:
`nslookup internalserver.lan 8.8.8.8`. An answer means the Pi-hole intercepted it.

## Limitations

This setup catches a lot, but it's no complete enforcement. What it can't do:

- **DNS-over-HTTPS (DoH) bypasses it completely.** Browsers (Firefox, Chrome "Secure DNS"),
  some apps and Android's Private DNS can send DNS inside normal HTTPS on port 443. The router
  can't tell it apart from other web traffic. What could help:
  - blocking known DoH endpoints with an address list or the Pi-hole's own blocklists
  - Pi-hole's built-in `use-application-dns.net` canary domain, which tells Firefox to turn
    its DoH off
  - not handing out public resolvers via DHCP (step 6b), so automatic upgrades have nothing
    to upgrade to
- **Encrypted DNS on port 853 is only blocked, not redirected** (step 5). Devices that insist
  on it, such as an Android phone with a fixed Private DNS hostname, lose DNS instead of
  falling back.
- **IPv6.** Everything here is IPv4. If your clients have IPv6, DNS over IPv6 bypasses these
  rules, and DHCPv6/RA may hand out other DNS servers. You need equivalent IPv6 rules, or
  you have to keep IPv6 DNS under control.
- **VPNs on clients** tunnel their DNS past the router, and nothing on the router can change that.
- **Redirected clients lose their identity in the Pi-hole log.** Because of the masquerade,
  their queries show up as coming from the router (`192.168.88.1`). Per-client statistics
  and per-client group rules only work for devices that use the Pi-hole directly.
  - To find out which devices have hard-coded DNS, temporarily add a
    `chain=dstnat action=log` rule above the redirect. Log rules don't stop the packet.
- **During a failover, there's no blocking and less privacy.** All queries go straight to the
  fallback resolver. If that bothers you, pick a privacy-friendlier one than Google (for
  example `9.9.9.9`), or run a second Pi-hole.
- **The failover isn't instant.** For up to a minute after the Pi-hole dies, DNS fails until the
  script has confirmed the outage. After the switch, LAN clients still first wait for a timeout
  from the dead primary before they ask the secondary. That's about 1 second on Windows and up
  to 5 seconds per lookup with a plain Linux `resolv.conf`. systemd-resolved and macOS move to
  the working server and stay there.

## Summary

This was far from easy to build but it runs now and is solid. The cool thing is that other family
members don't need to change anything on their devices since everything is handled centrally. I had this
setup running for a while without the failover functionality and it was fine until we had some 
power outages which led to issues with the pi-hole server. 

In case you want to implement the same, I highly recommnend to backup your RouterOS config before 
and ideally in between the changes. At one point I was very happy to be able to roll everything back...
