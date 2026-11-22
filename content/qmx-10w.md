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

In the end, all tests went through without any issues. The serial console access to the QMX is brilliant and allows you to test the transceiver thoroughfully. What might be of interest for you is the power output per band that can be taken from the following table:


<table>
<thead>
<tr>
<th>Band</th>
<th>Power</th>
</tr>
</thead>
<tbody>
<tr>
<td>60m</td>
<td>10.3 W</td>
</tr>
<tr>
<td>40m</td>
<td>9.7 W</td>
</tr>
<tr>
<td>30m</td>
<td>8.9 W</td>
</tr>
<tr>
<td>20m</td>
<td>11.9 W</td>
</tr>
<tr>
<td>17m</td>
<td>9.7 W</td>
</tr>
<tr>
<td>15m</td>
<td>6.8 W</td>
</tr>
</table>




