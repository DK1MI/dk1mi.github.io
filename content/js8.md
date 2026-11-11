---
title: Do one thing well: A 24/7 remote JS8 Station for 40m
date: 2026-05-21
---

## Introduction

As a longtime UNIX/Linux/BSD enthusiast, I also greatly appreciate the motto “Do one thing well” from the UNIX philosophy. I am recently also trying to keep things simple. It’s often better to have a little of something than too much. Here’s an example of the latter: Suppose I had a handheld game console on which every game ever released for any console was available - what would happen? I’d play a few of them briefly, never really diving into any of them, and put the console away after a short time. But what if I had nothing else to play but a Game Boy with a Pokémon cartridge? I would play that game for a long time and in great detail, probably even play through it multiple times.

Why am I writing this? Because I feel the same way about amateur radio. Especially on shortwave, I’ve always tried to have access to all bands. This has led to constant changes, to many successes, but also to the fact that I tended to scan bands for stations without ever making up my mind. That was all fine, especially since in recent years I’ve tended to focus on working as many rare DX stations as possible. But now I find myself longing more for good conversations than for quick 59
QSOs. Ragchewing isn’t exactly easy, though, if you don’t have a strong station - and especially not when you have a lot of local interference, which makes it harder to hear.

This frustration with interference has, among other things, led me to [set up a LEO satellite station](/leo-sat-ground-station-v3), which I enjoy a lot. However, QSOs are kept short, since an Earth-orbiting satellite doesn’t exactly hover over my house. Nevertheless, this already meets my needs for verbal communication via radio quite well, since you keep encountering the same stations and get to know each other a little better with every QSO.

Thanks to my satellite station, my shortwave station was suddenly available for experimentation. The idea arose to find a digital mode robust enough for my situation with the interference and offering true keyboard-to-keyboard communication. I’ve had quite a bit of success with FT8 so far, but it’s quite far from real QSOs. However, there’s JS8 with the accompanying software JS8Call. This digi mode is like FT8 but for real QSOs and has many other great features such as relaying messages, sending heartbeats, querying which other stations are able to hear, and more. After some research, it turned out that the main activity takes place on 40m. This is perfect because I have a 10-meter-long vertical antenna right behind the garden shed that is tuned to 40m.

## The Station

My idea was to build a JS8 station that’s as simple as possible, so it can also be operated remotely. I’ve already tried remote operation with the Hermes Lite 2, though back then I was still using a power amplifier and an antenna tuner - with only moderate success. The whole setup is far too complex, with too many variables. So I came up with the following setup:

- [QRP Labs QMX+](https://qrp-labs.com/qmxp.html) with the [10W mod](https://qrp-labs.com/qmxp/qmxpmod/pa0rdt.html) (putting out 7W on 40m)
- Raspberry Pi 5 running Debian Linux with JS8Call and a VNC server
- 10m long vertical antenna
- 40m band pass filter
- no antenna tuner
- no amplifier

I’ve already described the station’s setup here: <https://rz01.org/qmx>. To summarize the linked post, I've installed the QMX+ and the Raspberry Pi in a 19-inch rack inside the garden shed.

## Was it worth it?

In my view, the advantages of this station are as follows:

- It does exactly one thing, and it does it well
- The antenna cable is just 3m long, which greatly reduces signal loss
- The QMX+ is able to measure the SWR and output power which means that it protects itself when the SWR is too high and that I can query these values remotely
- Lightning protection - because the antenna cable stays outside the house
- Remote access to JS8Call via VPN and VNC
- I focus on one band and one mode and get the most out of that
- The station is available 24/7 and can therefore be used, for example, to relay messages for others using the store-and-forward principle

I’ve been running this station for a few weeks now and I’m very excited about it. While there’s not a crazy amount of activity on 40m except in the evenings and especially on weekends, there are a few stations that also run (unmanned) 24/7. This allows for asynchronous communication with other operators. No matter where I am in the world, I can connect to my home network via VPN and access the Raspberry Pi’s desktop via VNC. I’ve already made a few QSOs in JS8 and met some nice people along the way. The station will definitely keep running this way.

![](/img/js8-01.jpg)

## Future Plans

The idea is to make the whole station independent from the grid. To achieve this, I will most likely add a solar panel, MPPT charger and battery to the garden house. I have no idea if that makes sense because I wouldn't be able to access it via the network during a power outage but I will try to figure something out.
