---
title: Building a LEO SAT ground station - this time for real
date: 2025-08-19
---

I have already [experimented with 70cm/2m eggbeater antennas before](/70cm-eggbeater-antenna) with the goal to build a LEO SAT ground station. Basically, the eggbeater antennas worked, but I couldn’t find a good place to install them on my property. (Un)fortunately, the QRM situation on HF at my QTH has deteriorated so much that I can only operate on the 40m band while the other bands have become mostly unusable. So I decided to take the [10m/6m Moxon](/2850mox) off the mast and install eggbeater antennas for VHF and UHF instead. As I said, my homemade ones worked, but unfortunately I am unable to find out how well they work. That’s why I decided to purchase two commercial eggbeater antennas. These were not cheap, but they are very high quality, fully tuned, and recommended by other OMs.

## Station {#station}

For the future, I plan to expand the station to be more universal, but for now (mainly for cost reasons) I have decided to work only with FM LEO SATs in V/U mode. Therefore, the setup will initially look like this:

![](/img/leo-sat-ground-station-v2-01.jpg)

- Yaesu FTM-2980 VHF mobile rig
- 2m eggbeater antenna directly connected to the VHF radio via Ecoflex 10
- Orange Pi Zero 2 running OpenWebRX+ with an Airspy Mini SDR dongle mounted at the top of the mast
- 70cm eggbeater connected to the Airspy Mini

![](/img/leo-sat-ground-station-v2-02.jpg)

## Operation {#operation}

On my shack PC, I listen to and watch the overflying satellite via OpenWebRX in a browser and can gradually adjust the RX frequency to compensate for the Doppler effect. I also use OpenWebRX’s recording function to create an MP3 recording of each pass. This allows me to analyze the pass again if something goes wrong during logging and correct any errors in the log if necessary.

![](/img/leo-sat-ground-station-v2-03.jpg)

I transmit via the Yaesu FM VHF mobile transceiver, in which I have stored the uplink frequencies of all FM LEO satellites that my station theoretically could work.

With this setup, I have a full-duplex system that is limited to VHF uplink and UHF downlink, but works very well for me. The OpenWebRX waterfall and recording function are a great help to me.

The satellites I can work with (or am familiar with so far) are the following:

- [ISS (ARISS)](https://www.ariss.org/current-status-of-iss-stations.html) - 145.990 MHz up (PL 67 Hz) / 437.800 MHz down
- [SO-50](https://www.amsat.org/two-way-satellites/so-50-satellite-information/) - 145.850 MHz up (PL 67 Hz) / 436.795 MHz down
- [ASRTU-1 (AO-123)](https://iaru.amsat-uk.org/formal_detail.php?serialnum=830) - 145.850 MHz up / 435.400 MHz down
- [HADES-R (SO-124)](https://www.amsat.org/two-way-satellites/so-124-hades-r/) - 145.925 MHz up / 436.885 MHz down
- [TEVEL2](https://www.amsat.org/two-way-satellites/tevel2-constellation/) - 145.970 MHz up / 436.400 MHz down (still inactive?)

So far I have only successfully worked the ISS and SO-50.

## Closing notes {#closing-notes}

I find the operation via LEO satellites exciting and challenging. It is ideal for hams who have limited space in their garden, problems with QRM on shortwave, and prefer short QSOs. I will probably expand the station further so that I can also work SSB satellites and/or satellites whose uplink is UHF and downlink is VHF. The only disadvantage I see so far is that you can’t play radio when you want to or have the time to, but are tied to the satellite’s overflight times.
