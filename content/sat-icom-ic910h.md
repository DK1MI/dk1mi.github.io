---
title: CSN Technologies S.A.T. and the Icom IC-910H
date: 2025-10-01
---

I have recently purchased a [CSN Technologies S.A.T.](http://www.csntechnologies.net/sat) which is “a self contained antenna rotator and radio controller” which “natively controls Icom radios, Yaesu rotators and can interface with PSTRotator.” My main motivation for buying this device was to get rid of Windows on the Shack PC. I installed it for SatPC32, which works great, but runs on the “wrong” operating system. However, that wasn’t the only reason. I also liked the fact that it is a standalone device that doesn’t need a PC. Everything is controlled via a web interface, which I can also open and operate on my cell phone, tablet, or another PC. I could also use it for portable operations. The web interface offers many other great features, such as planning satellite passes, logging QSOs, alerting passes, and much more. There were also almost exclusively positive reports on eHam.net, but always in connection with the Icom IC-9700. And that’s where the problem lies: I only own an Icom IC-910H.

What I initially didn’t understand was that the IC-910H doesn’t support all functions. Gradually, the following became clear:

## Automatic configuration of the Radio {#automatic-configuration-of-the-radio}

The S.A.T. is not able to make some convenient settings via CAT on the IC-910H. This includes, for example, deactivating the radio’s satellite mode. SatPC32 can do this without any problems. What works is setting/changing the frequencies and modes. More on this further below.

**Workaround/Solution**: None. You have to take care of the settings by yourself when switching to a different kind of satellite.

## Working with the VFOs {#working-with-the-vfos}

On the IC-910H you can only transmit on the MAIN VFO, not the SUB VFO. This means that if you want to search for signals on a linear transponder, you need the SUB VFO (and therefore the downlink frequency) to be activated when you turn the VFO knob. Problem is that the S.A.T. wants to adapt the uplink frequency incl. doppler shift continously. To achieve this, the active VFO is switched between MAIN and SUB back and forth all the time. You need to turn the VFO knob whenever the SUB VFO is active. While you are turning the knob, the SUB VFO will stay activated.

**Workaround/Solution**: Be quick and precise. If you accidentally turn the VFO knob while the radio is on the MAIN VFO, then you need to wait a bit and try again.

## RIT {#rit}

At the point in the web interface where you can select and view the frequencies for a satellite’s transponder, the RIT can also be preset on the radio for each satellite. This is not possible with the IC-910H. I have never held an IC-9700 in my hands, but I assume that it has a rotary encoder for the RIT functionality, while the IC-910H has a potentiometer.

**Workaround/Solution**: None.

The real problem is the following: As stated above, this radio can only transmit on the MAIN VFO so you always have to configure this VFO for the uplink. This is also true for RIT: You can only use RIT on the MAIN VFO. You obviously need to have RIT active where the downlink frequency is but this is not possible.

**Workaround/Solution**: Only a not so great one by changing the downlink frequency in the transponder frequency settings in the S.A.T. interface permanently. That works if every OP has their frequencies in sync but you can’t adapt your downlink frequency during a QSO if the other station is off sync.

In the following screenshot you can see that I have added 500Hz to the downlink frequency for the SSB transponder of the RS-44:

![](/img/sat-icom-ic910h-01.jpg)

## CTCSS Tones {#ctcss-tones}

The IC-910H also does not support the automatic setting of CTCSS tones while SatPC32 has no problem doing it. This is a problem with FM satellites.

**Workaround/Solution**: You need to manually enable CTCSS tones in the radio. To do this you have to disable CAT control for the radio in the web interface, change your active VFO to MAIN, enable the CTCSS tone and re-activate CAT control. Sometimes weird things happen automatically and your radio would have CTCSS automatically set on the SUB VFO when selecting an FM satellite. Then you first need to deactivate it there before you move on. You also might need to change the tone frequency by pushing the SET button, then FM and then change the displayed value.

![](/img/sat-icom-ic910h-02.jpg)

![](/img/sat-icom-ic910h-03.jpg)

# The (somewhat) working Configuration {#the-somewhat-working-configuration}

In the following, I describe how I configured the S.A.T. and the IC-910H so that it still works, with the above limitations:

![](/img/sat-icom-ic910h-04.jpg)

The following settings must be made in the “RADIO” window of the S.A.T. web interface:

- **TYPE:** Icom 820H/821H/910H
- **BAUD:** 19200 (must match the settings in the IC-910H)
- **ADDRES:** 60h (must match the settings in the IC-910H)
- **VFO TYPE:** Main-up, Sub-down

The following must be configured on the IC-910H:

- Satellite Mode: Off
- Always make sure that the uplink frequency is in the upper / MAIN VFO
- Always make sure that CTCSS is not enabled on the SUB VFO (downlink frequency)
- Configure the CTCSS tone frequency in the FM settings menu
- Manually enable/disable CTCSS for the MAIN VFO (uplink frequency)
- Statically pre-set your downlink frequency for all transponders to match the uplink frequency

# Conclusion {#conclusion}

I really like the S.A.T. and I would love it if I had an IC-9700. The web interface is great, the logging feature, too. It feels consistent and mature. User support is fast and polite. Would I recommend it for a IC-910H user? No, I wouldn’t. Will I buy an IC-9700 in the future? Maybe I will.
