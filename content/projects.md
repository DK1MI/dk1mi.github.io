---
title: Projects
---

Below is a list of selected software and hardware projects that I have worked on in the past, sorted by category and listed newest first within each one:

- [Software](#software)
- [Radio & Electronics Builds/Projects](#builds)
- [Antennas & Ground Stations](#antennas)
- [Mods & Repairs](#mods)
- [3D Prints](#3d-prints)
- [Other](#other)

## Software {#software}

| Project | Description | Blog Post | Code / Download |
|---|---|---|---|
| 10W QMX Transceiver | Build of a QMX Transceiver with the PA0RDT 10W mod | [Post](/qmx-10w/) | - |
| COZYDOOM.WAD | A Doom WAD that replaces monsters in Doom, plus a web based builder to create your own variant | [Post](/cozydoom-post/) | [WAD v1.1](/files/COZYDOOM_v1.1.WAD), [Builder](https://cozydoom.rz01.org) |
| Backupkrake | Self-hosted, centrally monitored backup solution for my home and remote servers | [Post](/backupkrake-post/) | [GitHub](https://github.com/DK1MI/backupkrake) |
| rz01.org SSG | Dependency-free static site generator in Python 3 that builds this website | [Post](/ssg/) | [GitHub](https://github.com/DK1MI/dk1mi.github.io) |
| Web SDR → Radio Sync | Chrome extension that syncs a WebSDR with my radio, shows POTA/SOTA/WWFF spots and logs to Cloudlog/Wavelog | [Post](/websdr-radio-sync/), [Update](/websdr-radio-sync-store/) | [GitHub](https://github.com/DK1MI/websdr-radio-sync), [Chrome Web Store](https://chromewebstore.google.com/detail/web-sdr-%E2%86%92-radio-sync/ijdhjmmjgenlhgceppmhopmajkjigfhh) |
| OscarWatch Notifier | Listens to the OscarWatch WebSocket and sends push notifications for upcoming satellite passes | [Post](/oscarwatch-notifier/) | [GitHub](https://github.com/DK1MI/oscarwatch-notifier) |
| js8notifier | Python script that forwards incoming JS8Call messages via Pushover | [Post](/js8notifier/) | [js8notifier.py](/files/js8notifier.py) |
| Micro ADIF Syntax | ADIF syntax highlighting for the Micro editor | [Post](/micro-adif/) | in the post |
| SAT-Cloudlog-Bridge | Forwards QSOs logged on a CSN Technologies S.A.T. directly to Cloudlog/Wavelog | [Post](/sat-cloudlog-bridge/) | [GitHub](https://github.com/DK1MI/SAT-Cloudlog-Bridge) |
| satpasses | Generates a static HTML page with upcoming passes of your favorite satellites (N2YO API) | [Post](/satpasses/) | [GitHub](https://github.com/DK1MI/satpasses) |
| CC1200 Hotspot Installer | Bash script that installs all software needed for the CC1200 M17 hotspot on a Raspberry Pi | [Post](/cc1200-install-script/) | [GitHub](https://github.com/DK1MI/cc1200-hotspot-installer) |
| bear2hugo.py | Small Python script to migrate a Bear Blog export to Hugo | [Post](/bear2hugo/) | in the post |
| Retro Color Schemes for Quisk | Two dark, retro console inspired color themes for the Quisk SDR software | [Post](/retro-console-color-schemes-for-quisk/) | in the post |
| Hardrock-50 Widget for Quisk | Shows power, SWR, band and temperature of the Hardrock-50 in Quisk and follows the band of the Hermes Lite 2 (fork of OE6HKE's widget) | [Post](/quisk-hardrock-50/), [Improved](/improved-quisk-hardrock-50/) | [HR50-Quisk-Widget.tar.gz](/files/HR50-Quisk-Widget.tar.gz) |
| Cloudlog Rotator Control | Tampermonkey script that turns the antenna rotator straight from Cloudlog | [Post](/cloudlog-tampermonkey-antenna-rotator/) | [hygain-ir-controller.tar.gz](/files/hygain-ir-controller.tar.gz) |
| CloudlogOffline2QRZ | Pretends to be a Cloudlog instance and forwards QSOs from CloudlogOffline to the QRZ.com logbook | [Post](/cloudlogoffline-to-qrz/) | [CloudlogOffline2QRZ.tar.gz](/files/CloudlogOffline2QRZ.tar.gz) |
| vim-fle-syntax | Vim syntax plugin for Fast Log Entry (FLE) log files | [Post](/vim-fle-syntax/) | [vim-fle-syntax.tar.gz](/files/vim-fle-syntax.tar.gz) |
| DXPager | Watches the DX cluster and pages you via DAPNET when a new DXCC entity shows up | [Post](/dxpager/) | [dxpager.tar.gz](/files/dxpager.tar.gz) |
| ColorSpot | Command line DX cluster client with country, continent, LotW and needed-entity highlighting | [Post](/colorspot/) | [colorspot.tar.gz](/files/colorspot.tar.gz) |
| Hardrock-50 Remote Display | Python API and physical remote display for the Hardrock-50 amplifier | [Post](/hardrock50-remote-display/) | [hr50-remote-display.tar.gz](/files/hr50-remote-display.tar.gz) |
| qrzlogger | Command line application to log QSOs directly into the QRZ.com logbook | [Post](/qrzlogger/) | [qrzlogger.tar.gz](/files/qrzlogger.tar.gz) |
| qrz.sh | Command line tool to query the QRZ.com callsign database | [Post](/qrz-sh/) | [qrz.sh.tar.gz](/files/qrz.sh.tar.gz) |
| nsd-dyndns | Adds dynamic DNS functionality to the NSD authoritative name server | [Post](/dynamic-dns-for-nsd/) | [nsd-dyndns.tar.gz](/files/nsd-dyndns.tar.gz) |
| esm2markdown | Converts McAfee SIEM correlation rule exports to Markdown documentation | [Post](/correlation-rule-documentation-generator-for-mcafee-siem/) | [esm2markdown.tar.gz](/files/esm2markdown.tar.gz) |
| pass Patch | Patch for the pass password manager to show passwords hidden (red on red) via SSH | [Post](/patch-for-the-cli-password-manager-pass/) | in the post |
| Nmap SQLite Output | NSE script that stores Nmap scan results in an SQLite database | [Post](/nse-script-sqlite-output-for-nmap/) | [nmap-sqlite-output.tar.gz](/files/nmap-sqlite-output.tar.gz) |

## Radio & Electronics Builds/Projects {#builds}

| Project | Description | Blog Post | Code / Download |
|---|---|---|---|
| TS-570 Low Power Carrier Plug | Plug for the TS-570's tuner port that sends a low power carrier for tuning a remote ATU | [Post](/ts570-dummy-atu/) | – |
| Hadley Telescope | 3D printable Newtonian telescope for my kids (and me) | [Post](/hadley-telescope/) | – |
| CC1200 M17 Hotspot | Hot plate soldered Raspberry Pi hat acting as an M17 hotspot | [Post](/cc1200/) | [Upstream](https://github.com/M17-Project/CC1200_HAT-hw) |
| Remote ATU-100 | ATU-100 automatic antenna tuner with DG4SN's firmware, operated remotely at the antenna | [Post](/remote-atu-100/) | – |
| QubeDX v3 | Remote controlled CubeSat style QRP digi mode transceiver, merging QubeDX and QubeDX S | [v3](/when-two-become-one/), [v1](/qubedx/), [S](/qubedx-s/) | – |
| USB-C Charger for MD-380/RT3S/GD-77 | USB-C powered charging cradle for several DMR handhelds | [Post](/usb-c-charger-for-md380-rt3s-gd-77/) | – |
| Hy-Gain AR-500X Remote Control | Network remote control for the Hy-Gain AR-500X antenna rotator | [Post](/remote-control-hygain-antenna-rotator/) | [hygain-ir-controller.tar.gz](/files/hygain-ir-controller.tar.gz) |
| Hermes Lite 2 to Hardrock-50 Interface | Arduino based interface between Hermes Lite 2 and Hardrock-50 that keeps the amp from freezing | [V2](/hermes-lite-2-to-hardrock-50-interface-v2/), [V1](/hl2-hr50-interface/) | [hl2-interface.tar.gz](/files/hl2-interface.tar.gz) |
| SHARI AllStarLink Node | Compact, USB powered AllStarLink node for mobile use | [Post](/shari-asl-node/) | – |
| Remote Power/SWR Meter | WT32/ESP32 based power and SWR meter with a web interface | [Post](/remote-power-meter/) | [wt32powermeter.tar.gz](/files/wt32powermeter.tar.gz) |
| Battery Packs | Two battery packs spot welded from inherited cells | [Post](/battery-pack-building/) | – |
| AllStarLink Node | Stationary AllStarLink node | [Post](/allstarlink-node-build/) | – |
| Hardrock-50 | Build of the Hardrock-50 HF amplifier kit | [Post](/building-the-hardrock50/) | – |
| Remote Antenna Switch | Raspberry Pi controlled antenna switch that picks the antenna by band | [Post](/antenna-switch/) | – |
| The AntennaPi | Raspberry Pi based remote antenna switch for the attic | [Post](/the-antennapi/) | – |
| Heated Trackball | A trackball with a USB powered heating wire | [Post](/heated-trackball/) | – |
| One Button Audiobook Player | Raspberry Pi audiobook player with a single button for a visually impaired 90-year-old | [Post](/the-one-button-audiobook-player/) | [theonebuttonaudiobookplayer.tar.gz](/files/theonebuttonaudiobookplayer.tar.gz) |
| The Laundruino | Arduino with a web server that tells me when the washing machine is done | [Post](/the-arduino-enabled-washing-machine/) | [laundruino.tar.gz](/files/laundruino.tar.gz) |

## Antennas & Ground Stations {#antennas}

| Project | Description | Blog Post | Code / Download |
|---|---|---|---|
| Random Wire Vertical | 13m long vertical on a Spiderbeam mast, tunable from 160m to 10m | [Post](/random-wire-vertical/) | – |
| M0PLK Delta Loop | Multiband delta loop with 3D printed insulators and spacers | [Post](/m0plk-delta-loop/) | [End Cap](/files/M0PLK_14mm_End_Cap.stl), [Spacer](/files/M0PLK_65mm_Ladder_Line_Spacer.stl), [Insulator](/files/M0PLK_Middle_Insulator.stl) (STL) |
| 70cm Eggbeater | My first eggbeater antenna for LEO satellites | [Post](/70cm-eggbeater-antenna/) | – |
| Dual Band Slim Jim | 2m/70cm travel antenna made from 240 Ohm cable | [Post](/dual-band-slim-jim/) | – |
| Shortened 30m Dipole | 9.5m long loaded dipole for the attic | [Post](/30m-dipole/) | – |

## Mods & Repairs {#mods}

| Project | Description | Blog Post | Code / Download |
|---|---|---|---|
| Game Boy Classic | Backlight mod and recapping of a Game Boy (DMG) | [Post](/dmg/) | – |
| Baofeng DM-1701 M17 Mod | Hardware mod and OpenRTX firmware to use the DM-1701 for M17 | [Post](/m17-dm1701-mod/) | – |
| Logitech MX Ergo | Replacing worn out button microswitches | [Post](/mx-ergo/) | – |
| AEG Lavatherm Dryer | Fixing error EH0 by reflowing dry solder joints on the main board | [Post](/dryer-repair/) | – |
| mAT-1500Pro | How I destroyed and repaired a brand-new automatic antenna tuner (twice) | [Post](/mat-1500pro/) | – |
| uBitx | AGC, S-meter, VFO knob, firmware changes and PTT control for a linear amplifier | [PTT](/ubitx-linear-amplifier-ptt-control/), [AGC](/ubitx_agc/), [S-Meter](/ubitx_smeter/), [VFO](/ubitx_vfo_knob/) | [ubitxv6.tar.gz](/files/ubitxv6.tar.gz) |
| Xiegu X5105 LCD Swap | Replacing the faulty display of a second-hand X5105 | [Post](/xiegu-x5105-lcd-swap/) | – |
| TP5100 Charger Mod | Making the MD-380/RT3S/GD-77 charger reliable with a TP5100 module | [Post](/tp5100-charger-mod/) | – |
| MX-P50M | BNC sockets and a dedicated PTT jack for the MX-P50M amplifier | [Post](/mx-p50m-mod/) | – |
| Xiegu G90 | Collection of mods for the Xiegu G90 | [Post](/g90-mods/) | – |

## 3D Prints {#3d-prints}

| Project | Description | Blog Post | Code / Download |
|---|---|---|---|
| Spiderbeam HD 12m Mount | Mount for the Spiderbeam HD 12m fiberglass mast | [Post](/spiderbeam-hd-12m-mount/) | [STL](/files/spiderbeam-hd-12m-mount.stl) |
| CX600 Coax Relay Wall Mount | Snap-on wall mount for CX600 coaxial relays | [Post](/coax-relay-wall-mount/) | [Printables](https://www.printables.com/de/model/488366-cx-600-coaxial-relay-wall-mount) |
| MX-P50M Protection Covers | Protection covers for the MX-P50M amplifier | [Post](/mx-p50m-covers/) | [Printables](https://www.printables.com/de/model/488369-mx-p50m-amplifier-protection-covers) |
| Miady PowerPole Lid | PowerPole lid for the Miady 7.2Ah LiFePO4 battery | [Post](/miady-powerpole-lid/) | [Printables](https://www.printables.com/de/model/488370-miady-128v-72ah-lifepo4-power-pole-lid) |

## Other {#other}

| Project | Description | Blog Post | Code / Download |
|---|---|---|---|
| Paper Logbook | Printable A5 logbook template for amateur radio QSOs | [Post](/paper-logging/) | [PDF](/files/logbook_a5_v2.pdf), [ODS](/files/logbook_a5_v2.ods) |
| Doom WAD Logbook | The Doom WADs I have played and what I think of them | [Page](/doom-wad-logbook/) | – |
| Little Helper | A replica of Gyro Gearloose's Little Helper with a light bulb head | [Post](/little-helper/) | – |
