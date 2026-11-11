---
title: LEO SAT ground station v3: Upgrading from eggbeaters to a cross yagi setup
date: 2025-09-21
---

After [having lots of fun experimenting with eggbeaters](/leo-sat-ground-station-v2), I decided to invest some serious money and make a huge upgrade to my LEO ground station. The result is a much more capable setup that lets me also work linear-transponder satellites (RS-44, JO-97, etc.) with much lower RF power. It also allows me to work satellites during lower elevation passes.

This is the new setup:

- Radio: [Icom IC-910H](https://www.rigpix.com/icom/ic910h.htm)
- Antennas: [Cross RHCP 2m/70cm LEO satellite kit from YU1CF](https://antennas-amplifiers.com/leo-satellites-kit-cross-rhcp-antennas/)
- Pre-amps: Mast-head 2m and 70cm LNAs
- Rotor: [Yaesu G-5500 DC rotor](https://www.yaesu.com/product-detail.aspx?Model=G-5500DC&CatName=Rotators) + [RTC-200 computer interface](https://www.cgantenna.be/product_rtc200.html)
- PC control & tracking: [SatPC32](https://www.dk1tb.de/indexeng.htm) (rotor + CAT + doppler control)
- Logging: [Wavelog](https://www.wavelog.org/) + [Cloudlog Aurora](https://aurora.cloudlog.org/) (SatPC32 → Aurora → Wavelog)

With this new setup, I now have a system that moves the antennas fully automatically and directs them at the satellite, and which not only sets the frequencies in the radio initially, but also continuously adjusts them to correct the doppler effect. Furthermore, a lot of data is already set automatically in the logging software for me, such as the satellite name, RX/TX band and frequency, and the propagation mode.

My main radio is now an Icom IC-910H instead of an SDR receiver and an HT for TX. I chose this radio purely for cost reasons. Of course, I would have preferred an IC-9700, but it was too expensive for me. Apart from the lack of a waterfall display (which I would really like to have) and the simple USB connection option for digimodes, the IC-910H offers everything you need for satellite operation. A big plus of this older device is a dedicated control knob for the output power. SatPC32 supports this radio out of the box.

![](/img/leo-sat-ground-station-v3-02.jpg)

I replaced the eggbeaters with a cross RHCP 2m/70cm satellite antenna kit from antennas-amplifiers.com. These RHCP circularly-polarized antennas provide significant gain compared to omnidirectional eggbeaters and allows working satellites also during low-elevation passes. To improve the received signal and to compensate cable losses, I installed mast-head preamps for both 2m and 70cm.

![](/img/leo-sat-ground-station-v3-01.jpg)

SatPC32 is the central control element on the shack PC. It handles TLE-based tracking, computes doppler shifts, and drives both the G-5500 rotor (via the RTC-200) and the IC-910H radio (via CAT). SatPC32’s ability to split RX/TX control and apply doppler compensation magic to the radio VFOs is what makes linear-transponder contacts quite easy. The IC-910H’s CAT integration lets SatPC32 set RX and TX frequencies in real time for each pass, so the radio follows the satellite precisely. It’s also great that I can change the frequency via the radio’s VFO knob while SatPC32 takes care of doppler shift correction for both, the receive band and the transmit band.

For logging I run [Wavelog](https://www.wavelog.org/) together with [Cloudlog Aurora](https://aurora.cloudlog.org/). Aurora reads SatPC32’s current frequency, satellite name, band, and mode, then pre-populates some QSO fields in Wavelog. This bridge eliminates frantic typing during the quite short satellite passes and reduces entry errors. I still manually confirm the locator but time, SAT name, band and frequency fields are filled automatically.

Not only can I now use almost all of the satellite passes from FM satellites (previously, nothing worked below 30 degrees), but I can also work linear transponder satellites RS-44 is particularly fun at the moment, and I’m trying every day to finally make my first QSO via Oscar 7 (in mode B). I am very happy with the outcome but I am still eye-balling the IC-9700…
