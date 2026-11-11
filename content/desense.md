---
title: Fixing desense issues with V/U satellites
date: 2025-10-10
---

[I recently upgraded my satellite ground station from eggbeaters to cross yagis](/leo-sat-ground-station-v3/). Everything seemed fine, but at first I didn’t realize I had a problem. This manifested itself in the fact that I sometimes heard myself very distorted on satellites with linear transponders and couldn’t hear anything at all on FM satellites when transmitting. Since I couldn’t find a solution myself, I asked the [International AMSAT Ops Telegram Group](https://t.me/amsatops) for help. There I first learned that this phenomenon is called “desense.” I would like to quote the very helpful page [“A Simple Desense Filter for Mode-J Satellites” on amsat.org](https://www.amsat.org/a-simple-desense-filter-for-mode-j-satellites/): “Desense is where your transmitter signal overloads your preamp (or receiver) causing it to become temporarily less sensitive. This overload condition may also be accompanied by white noise or intermodulation distortion where you hear distorted signals in your receiver, including possibly your own transmit signal, but only when you are transmitting.”

This post also explains how to fix this issue: By adding a diplexer between the 70cm preamp and the 70cm antenna. It should be installed so that the mix port of the diplexer is connected to the antenna and the 70cm port to the preamp. The diplexer will then act as a filter. You can of course also use a proper band pass or high pass filter but since I had a spare diplexer, I gave it a shot. The diplexer had BNC connecters which I needed for a previous project so I removed them and nstalled a new N connector to the 70cm port. To make it somewhat water proof, I sealed what I could with silicone:

![](/img/desense-02.jpg)

<br/>

The following diagram shows how the full configuration looks like with the newly added diplexer:

<br/>

![](/img/desense-04.png)

<br/>

Yes, that’s a lot of diplexers. Yes, using only one coax is not the best idea. Yes, I might upgrade to a two-coax configuration in the near future.

**Update 2025/10/17:** I removed the two regular diplexers and instead laid a second coaxial cable from the shack to the antennas:

<br/>

![](/img/desense-05.png)

<br/>

![](/img/desense-03.jpg)
