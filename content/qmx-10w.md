---
title: Building a 10W QMX Transceiver
date: 2026-11-22
---

Since I’m more than satisfied with my [QMX+ build](/qmx/) and recently discovered that the latest firmware allows SSB operation without any restrictions, 
I sold my Xiegu G90 and ordered a [QMX kit](https://qrp-labs.com/qmx.html) for portable operations instead. The [PA0RDT 10W modification](https://qrp-labs.com/qmxp/qmxpmod/pa0rdt.html) had already worked great with the QMX+, so I wanted to implement it on the QMX as well. With the QMX, however, this isn't quite so simple, since there's very little space available.

The kit was delivered quickly as usual (I've already ordered and built a QCX, QMX+ as well as two QDX) and consisted of the following parts:

![](/img/qmx-10w-01.jpg)

## The 10W modification

I started by soldering in the four included BS170 transistors. Then I've cut a piece of 0.5mm thin copper sheet and drilled a 3mm hole into the middle of it. 
After I placed it on the four transistors, another set of four BS170 have been placed on top of the copper sheet and soldered to the underlying transistors.
The whole package was then secured by a washer and an M3 screw. To make it fit between the main PCB and the display PCB, I had to make a few adaptions.

At first I filed down the screw's head to an absolute minimum:

![](/img/qmx-10w-02.jpg)

Then I've used a rotary mini tool to grind down one of the six tabs that hold the LCD to the display PCB. I've also grinded down the surrounding solder joints:

![](/img/qmx-10w-03.jpg)

With these small modifications, the eight transistors fit right inbetween the two PCBs:

![](/img/qmx-10w-04.jpg)

## Building the kit

Building the QMX is a bit more demanding than the QMX+, but the instructions are excellent as usual. I once again chose to build the transceiver for 12V and ended up making a 3:3 WTST instead of the RWTST intended for 12V.

This is what the QMX looked like before mounting it into the enclosure:

![](/img/qmx-10w-05.jpg)

I've later on rearranged the windings on the toroids (see "Issues").

Here's the finished QMX in all its glory:

![](/img/qmx-10w-06.jpg)

## Issues

I only had some minor issues during the assembly. First, I destroyed a 0603 resistor without realizing it but discovered it during a visual review with the microscope. Replacing it was easier than I thought. 
Second, I only had an output of 3.5W on 15m while all other bands performed much better. After I have resoldered L510 and L513 and rearranged the windings on the toroids, I measured a satisfying 6.8 W.

## Test Results

In the end, all tests went through without any issues. The serial console access to the QMX is brilliant and allows you to test the transceiver thoroughfully. The following table shows the power output and efficiency per band with a receive current of 92mA:

| Band | Output power | Total current | PA current | PA DC input | Overall efficiency | PA efficiency |
|------|-------------:|--------------:|-----------:|------------:|-------------------:|--------------:|
| 60m  | 10.3 W | 1252 mA | 1160 mA | 13.92 W | 68.6 % | 74.0 % |
| 40m  | 9.7 W  | 1216 mA | 1124 mA | 13.49 W | 66.5 % | 71.9 % |
| 30m  | 8.9 W  | 1116 mA | 1024 mA | 12.29 W | 66.5 % | 72.4 % |
| 20m  | 11.9 W | 1650 mA | 1558 mA | 18.70 W | 60.1 % | 63.6 % |
| 17m  | 9.7 W  | 1495 mA | 1403 mA | 16.84 W | 54.1 % | 57.6 % |
| 15m  | 6.8 W  | 1161 mA | 1069 mA | 12.83 W | 48.8 % | 53.0 % |
