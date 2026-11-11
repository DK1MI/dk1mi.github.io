---
title: What is M17? Why is it so great? And how do I get started?
date: 2025-08-02
---

I have recently [posted a lot about M17](/tags/m17/), and you may be wondering what it is all about, why I am so excited about it, and how you can get involved. Let’s start with what [M17](https://m17project.org/) is.

## What is M17? {#what-is-m17}

M17 is a **free and open-source** digital radio protocol for **voice and data**, built by and for amateur radio operators. This means that you can communicate with other hams worldwide using an M17-capable radio and a hotspot or repeater. This can be classic voice transmissions or data traffic. In contrast to other known digital modes, M17 is completely open source, offers **good voice quality** and is much **easier to handle**. **No code plugs** or registration are required. All you have to do is set your M17-capable radio to the frequency of the hotspot, enter your callsign in the radio and you’re ready to go. The desired reflector is set at the hotspot with little effort.

## Why is it so great? {#why-is-it-so-great}

While it is comparable with DMR, D-Star and System Fusion, the first big difference is, that it is open source. The codec used in M17 is [Codec 2](https://en.wikipedia.org/wiki/Codec_2) which is “a low-bitrate speech audio codec (speech coding) that is patent free and open source”. The aforementioned digital voice modes rely on closed source software and hardware.

The use of open source hardware and software is not only the best thing that can happen to amateur radio from an ethical point of view, it also allows the developers among us to develop new features, applications and devices themselves. The M17 specifications are of course freely available and can be found [here](https://spec.m17project.org/). So we don’t have to wait for some manufacturer to actually listen to their customers, we can either take the wheel ourselves or pass on our ideas to others in the community to have them developed.

M17 can also do **packet mode**, which I personally haven’t really explored. The only thing I’ve done here so far is **[send and receive text messages](/m17-sms)**. That alone is a great feature of M17. You can even see the messages on your hotspot dashboard (if the dashboard you are using supports it). DMR also supports text messaging but there are multiple implementations that are not compatible with each other. Many other applications are planned, e.g. the transmission of location information. Theoretically, even turn-based multiplayer games can be played via M17 without any problems.

I also have to admit that I sometimes think I’m too stupid for the established digital voice modes. Setting up the devices is often complicated and it usually requires proprietary software to program them in a complicated way. Furthermore, the devices (with the exception of DMR) are incredibly expensive, but still have various shortcomings that do not justify the price. Furthermore, updates are sparse in order to justify the sale of new devices.

But for me, **the most important aspect is the community**. Many radio amateurs from all over the world have come together to work on various projects related to M17. The [OpenRTX](https://openrtx.org) team, which has developed and published a completely open source firmware with M17 support for various radios, must be emphasized here. Apart from that, not only new software components are continuously being developed, e.g. for the operation of hotspots, but also great hardware like **the upcoming LinHT**, an “open-source hardware, Linux-based, SDR handheld transceiver. OpenHT successor with greatly simplified hardware - no FPGAs involved. This project offers a replacement board for the Retevis C62 radio, greatly expanding its capabilities.” This means that there will soon be a PCB available to buy or to build, which you can simply install in an inexpensive Retevis C62 handheld radio. This will give you a solid handheld radio with M17 (and many other things) at its heart.

I have been warmly welcomed into the M17 community and am currently developing software with other people I have never met before on a friendly and professional level.

If you want to know what is currently in development, you can find an overview on the following pages in the [M17 Wiki](https://wiki.m17foundation.org):

- [M17 Hardware Projects](https://wiki.m17foundation.org/index.php?title=Hardware_Projects)
- [M17 Software Projects](https://wiki.m17foundation.org/index.php?title=Software_Projects)
- [Projects that include M17 Support](https://wiki.m17foundation.org/index.php?title=Applications_with_M17_Support)

**To summarize:** M17 is just right for you if

- open source (in amateur radio) is important to you
- you are looking for a great, friendly community
- you are looking for an uncomplicated digital voice mode
- optional: you enjoy software and hardware development or want to learn it

## Ok…but now what? {#okbut-now-what}

The big question now, of course, is how to start with M17. Can I take part without a radio? What kind of radio do I need, what kind of hotspot? How can I talk to the M17 devs, where can I exchange information with other users?

## Can I participate without a radio? {#can-i-participate-without-a-radio}

Yes, and very easily. Android users have it the easiest here. The “DroidStar” app can be found and downloaded free of charge in the [Google Play Store](https://play.google.com/store/apps/details?id=org.dudetronics.droidstar&hl=en), for example. Once you have done this, you can connect directly to an M17 reflector after a few settings and make your first M17 QSO. You can find out how to do this in the [M17 Wiki](https://wiki.m17foundation.org/index.php?title=How_to_get_on_the_Air_-_Part_I:_Radio).

## I want the real thing, I want a radio! {#i-want-the-real-thing-i-want-a-radio}

If you want to use a real radio to transmit via M17, there are several possibilities. You can find more information on this in the [M17 Wiki](https://wiki.m17foundation.org/index.php?title=How_to_get_on_the_Air_-_Part_I:_Radio).

In the following I will concentrate on handheld radios and what options are available.

### I just want to buy a radio, I’m not a tinkerer {#i-just-want-to-buy-a-radio-im-not-a-tinkerer}

If this is the case, then Connect Systems has you covered. There are two radios available, the [CS7000 M17](https://www.connectsystems.com/products/top/radios/CS7000_M17.htm) and the [CS7000 M17 PLUS](https://www.connectsystems.com/products/top/radios/CS7000_M17_PLUS.htm). Both models are supported by OpenRTX and are actively used by M17 devs as well as by many operators.

### I love to build stuff myself {#i-love-to-build-stuff-myself}

There are some handheld radios you can convert by yourself to an M17 radio. The best option (in my opnion) is the modification of the inexpensive Baofeng DM-1701. The modification requires SMT soldering skills but is quite doable. Even I managed to do this mod with a bit of patience. You can read more about this [here in an articel I wrote](/m17-dm1701-mod/). The OpenRTX firmware for the DM-1701 is fully functional but it still lacks the persistent storage of radio settings made by the user. An improved firmware is already at the horizon.

### I don’t want to spend much money, don’t want to solder and can wait {#i-dont-want-to-spend-much-money-dont-want-to-solder-and-can-wait}

The OpenRTX team is developing a firmware for the Retevis C62 that can be flashed to the radio and be used without any hardware modifications.

### I want the ultimate radio and can wait {#i-want-the-ultimate-radio-and-can-wait}

[LinHT](https://github.com/M17-Project/LinHT-hw) is what you want. As described above, this will be a drop-in replacement mainboard for the inexpensive Retevis C62 radio. It will be an RF enabled Linux PC in a handheld radio and the perfect platform not only for M17 but for endless other radio related applications.

## What else do I need if I have a radio? {#what-else-do-i-need-if-i-have-a-radio}

As with all other digital voice modes, you either need a repeater nearby or a hotspot.

There are several options for the hotspot: Either you use a MMDVM based hotspot, which you may have already used for DMR, D-Star or System Fusion or you build a dedicated CC1200 based M17 hotspot.

### MMDVM Hotspot {#mmdvm-hotspot}

There are also various options here. The simplest option is to use our WPSD fork, which adds M17 to the popular WPSD hotspot distribution. You can find more information here: [WPSD-M17 Community Fork](/wpsd-m17/).

There is also an in-house development of the M17 community called [mspot](https://github.com/n7tae/mspot). An excerpt from the project description:

*This open-source project will build an M17-only repeater or hot-spot for amateur radio. The design goals for this project include:*

- *Easy to build: Because the mspot repeater is a single application and is complete. It includes a novel M17 gateway that can connect to both M17 and URF reflectors.*
- *Easy to configure: With a single, self contained application, there is just a single configuration file, and the project builds an additional program, inicheck, that will intelligently analyze your ini file and reports any problems it finds.*
- *Easy to use: mspot includes many RF-base commands to manage its connection state and responds to commands with voice messages, making mspot ideal for a mobile, smart-phone tethered repeater. I am hoping it is also useful to sight-impaired hams.*
- *Minimum executable size: mspot is tiny, especially when you compare it to the multi-mode alternatives.*
- *Excellent reliability: You’ll be the judge of that. Try it and find out.*

### CC1200 Hotspot {#cc1200-hotspot}

This hotspot does not use a MMDVM modem but the CC1200 M17 Hat developed by SP5WWP for the Raspberry Pi. For the CC1200, N1ADJ and I have recently released the software, which consists of the M17-gateway and a PHP based web application. While the M17 gateway does the actual work of the hotspot under the hood, the web application serves as a dashboard like you know it from other hotspots. Further information can be found at [this link](/cc1200-m17-hotspot/).

## I have more questions! {#i-have-more-questions}

Excellent! If you would like to get in touch with the devs or other users, you can join our Discord server or join the M17-Users group. Please visit <https://m17project.org/contact/> for more detailed information. The best starting point to reach others via radio or DroidStar is connecting to the reflector **M17-M17 C**.

Hope to meet you there!
