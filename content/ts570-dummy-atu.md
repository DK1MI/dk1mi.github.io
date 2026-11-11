---
title: Low power carrier plug for the Kenwood TS-570
date: 2026-09-26 13:00
summary: Although the Kenwood TS-570 shortwave transceiver has a built-in tuner, it tunes virtually no bands with my antenna configuration. That’s why I use an ATU-100 based on N7DDC’s design, which I operate remotely near the antenna. This works, but it’s annoying to have to first reduce the output power from 100W to 10W and switch the mode to CW every time I want to tune, in order to transmit a steady, low-power signal for the tuning process...
---

Although the Kenwood TS-570 shortwave transceiver has a built-in tuner, it tunes virtually no bands with my antenna configuration.
That’s why I use an [ATU-100 based on N7DDC’s design](https://github.com/Dfinitski/N7DDC-ATU-100-mini-and-extended-boards),
which I operate remotely near the antenna. This works, but it’s annoying to have to first reduce the output power from 100W to 10W and
switch the mode to CW every time I want to tune, in order to transmit a steady, low-power signal for the tuning process. Fortunately,
the Kenwood has a connector for an external tuner and an “AT Tune” button to start the tuning process when a tuner is connected to a
dedicated port on the back of the unit. After doing some research, I came across the following thread on groups.io:
[ Low power carrier plug for external/remote tuners](https://groups.io/g/Kenwood-TS-570/topic/low_power_carrier_plug_for/95297739).
It describes how to use a 1,500-ohm resistor to trick the radio into thinking a tuner is connected to it.
This allows you to simply press the “AT Tune” button to automatically transmit a 10W carrier signal, which prompts the remote ATU-100 to automatically tune the antenna.

To build such an ATU dummy dongle, you need the following:

- 1x ELP-06V plug housing
- 2x JST SLF-01T-P1.3E contacts (female)
- 1x 1,500 Ohm resistor

The following diagram shows what which pin of the ELP-06V connector does:

![](/img/ts570-dummy-atu-01.png)

All the necessary materials:

![](/img/ts570-dummy-atu-02.jpg)

The build of this dummy ATU plug is very easy. All you need to do is to solder the resistor to the two metal contacts:

![](/img/ts570-dummy-atu-03.jpg)

Now all is left is to insert the two contacts into the middle pins of the housing:

![](/img/ts570-dummy-atu-04.jpg)

For a particularly professional finish, you can apply a little hot glue to the back. When inserted, the plug looks like this:

![](/img/ts570-dummy-atu-05.jpg)
