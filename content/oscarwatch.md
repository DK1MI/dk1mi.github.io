---
title: The OscarWatch Multiplatform Satellite Tracking System
date: 2026-07-31 14:00
summary: I've been using MM9SQL's OscarWatch for some time now, but now that version 1.0.0 has been released, it's time to write about it. This open-source software is a satellite tracker for amateur radio operators. It has helped me finally say goodbye to SATPC32. Not that SATPC32 is bad, but for one thing, it’s a bit outdated, and for another, it unfortunately only runs on Windows. As someone who even forces his kids to use Linux on their computers, OscarWatch was just what I needed. So far, I’ve successfully used it on an AMD64 system running Debian Trixie and on a Raspberry Pi 5 (also running Trixie)...
---

I've been using [MM9SQL's OscarWatch](https://github.com/magicbug/OscarWatch-Tracker) for some time now, but now that version 1.0.0 has been released, it's time to write about it. This open-source software is a satellite tracker for amateur radio operators. It has helped me finally say goodbye to [SATPC32](https://www.dk1tb.de/indexeng.htm). Not that SATPC32 is bad, but for one thing, it’s a bit outdated, and for another, it unfortunately only runs on Windows. As someone who even forces his kids to use Linux on their computers, OscarWatch was just what I needed. So far, I’ve successfully used it on an AMD64 system running Debian Trixie and on a Raspberry Pi 5 (also running Trixie).

![](/img/oscarwatch-01.jpg)

Here’s the complete setup I’m using in my shack together with OscarWatch:

- ICOM IC-910 as a VHF/UHF transceiver
- Yaesu G-5500 rotor and control unit
- RTC-200 computer interface for the G-5500
- Raspberry Pi 5

OscarWatch offers everything I need in a single program. It provides me with

- a world map showing the amateur radio satellites I’ve selected and their orbits
- a list of upcoming satellite passes, including pass duration and maximum elevation
- widgets with information on the status of my radio and rotator
- a sky plot that visualizes the pass in relation to my QTH
- automatic updates of the TLEs and the transponder database
- fully automatic control of my radio
- fully automatic control of my rotor

This app has even more features, but I either don't need them or haven't discovered them yet.

## OscarWatch in Daily Use

My Raspberry Pi runs 24/7 with OscarWatch open the whole time. Whenever I want to operate the radio, I connect to the Pi via VNC. OscarWatch is also forgiving if you turn the rotor controller and radio off and on again in between. The TLEs and transponder database are kept up to date in the background. So far, I’ve never had to manually add a transponder. Unlike some other SAT trackers, my IC-910 is fully supported, as is the rotor controller. I just have to select the desired satellite from the list of upcoming passes, and the entire system is activated and gets going as soon as the pass begins. All I have to do then is push PTT and make QSOs. After the QSO, I click “standby” again, and my rotor rotates back to the customizable parking position.

## Conclusion

OscarWatch is stable, cross-platform, visually appealing, easy to use, and integrates perfectly into my shack. If you are a SAT operator with the same or a similar/supported setup, I highly recommend this application!
