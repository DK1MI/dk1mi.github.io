---
title: Notes on the QRP Labs QDX
date: 2024-08-08
---

On this page I am continuously recording all the findings that I have been able to collect in connection with the QDX Transceiver Rev 6 from QRP Labs. What I am writing here might seem negative since it’s mostly about issues and how to fix them but I am actually a big fan of this device and have already ordered a second kit.

A post on my QDX build can be found [here](/qubedx).

## Low output power on 15m {#low-output-power-on-15m}

After I’ve finished building my QDX (high bands version), I measured the output power of all bands and got these results:

- 20m: 4.6W
- 17m: 4.9W
- 15m: **2.4W**
- 12m: 3.5W
- 10m: 3.5W

After reading <https://qrp-labs.com/qdx/qdxtrouble.html> I was confused why there is significantly less power on 15m than on 17m as they share an LPF. [VA3RR gave me the excellent hint to check if the power output on 15m decreases when I compress the windings on L3](https://groups.io/g/QRPLabs/topic/107788674) - which actually was the case. I followed his advice and **reduced the windings of L3 from 12 to 11** and furthermore prettified the spacing between the windings of L2, L3 and L4 which resulted in the following:

- 20m: 4.7W
- 17m: 4.6W
- 15m: **3.4W**
- 12m: 3.9W
- 10m: 3.9W

## No High SWR Protection {#no-high-swr-protection}

As the QDX does not have an SWR measuring bridge, it does not have a protective circuit to protect the device from high SWR. I was warned against using the QDX together with an automatic tuner, as even the short spikes during the tuning process can lead to the destruction of the four BS170 transistors.

As an alternative to not using an ATU, I was given the following options:

### Reducing the Output Power {#reducing-the-output-power}

One recommendation is to temporarily or permanently reduce the supply voltage to reduce the output power. This should help to protect the PA transistors, especially during the tuning process. I have carried out experiments on this, to determine which voltage is needed for a specific level of output power.

The following table shows the output power in Watt per band in dependency of the supply voltage. This refers to a 9V build of the QDX Rev 6.

<table>
<thead>
<tr>
<th></th>
<th>9.0V</th>
<th>8.5V</th>
<th>8.0V</th>
<th>7.5V</th>
<th>7.0V</th>
<th>6.5V</th>
</tr>
</thead>
<tbody>
<tr>
<td>20m</td>
<td>4.7</td>
<td>4.3</td>
<td>3.9</td>
<td>3.4</td>
<td>3.0</td>
<td>2.5</td>
</tr>
<tr>
<td>17m</td>
<td>4.6</td>
<td>4.2</td>
<td>3.9</td>
<td>3.4</td>
<td>2.9</td>
<td>2.4</td>
</tr>
<tr>
<td>15m</td>
<td>3.4</td>
<td>3.0</td>
<td>2.8</td>
<td>2.5</td>
<td>2.2</td>
<td>1.8</td>
</tr>
<tr>
<td>12m</td>
<td>3.9</td>
<td>3.5</td>
<td>3.3</td>
<td>2.9</td>
<td>2.7</td>
<td>2.1</td>
</tr>
<tr>
<td>10m</td>
<td>3.9</td>
<td>3.5</td>
<td>3.1</td>
<td>2.8</td>
<td>2.5</td>
<td>2.0</td>
</tr>
</tbody>
</table>

At 6.0V the QDX would only boot into its flash drive mode.

I’ve decided to settle with a supply voltage of 7.5V.

### Replacing the Transistors {#replacing-the-transistors}

On [groups.io/g/QRPLabs](https://groups.io/g/QRPLabs/) I have so far been able to find the following attempts to replace the BS170 transistors, which are installed as standard and are considered to be quite sensitive:

**Replacement with TN0110 transistors**. These are supposed to be more robust, but have the disadvantage that their polarity is reversed. As a result, the round and not the flat side of the transistors rest on the circuit board. As I operate the QDX without a housing, this would even be an advantage if I use a heat sink instead of the washer.

![](/img/notes-on-the-qrp-labs-qdx-01.jpg)
*(Note: This picture shows the heat sink with the four BS170)*

**Exchange for two FDT86256 mosfets**. This procedure developed by WB2CBA is described in more detail here: <https://github.com/WB2CBA/QDX-PA-MODIFICATION>. The whole thing is now even available as a kit: <https://www.tindie.com/products/jasonkits_qrp/qdx-mosfet-pa-mod-kit/>. However, it is recommended to drive it with 6V instead of the original 5V. More information here: <https://groups.io/g/QRPLabs/topic/qdx_pa_upgrade/103093403>

## Attenuated RX on 20m {#attenuated-rx-on-20m}

### Problem {#problem}

The RF filter sweep for the 20m band resulted in the following graph:

![](/img/notes-on-the-qrp-labs-qdx-02.png)

This is the result of the image rejection sweep for the 20m band:

![](/img/notes-on-the-qrp-labs-qdx-03.png)

### (Partial) Solution {#partial-solution}

I fixed this issue by rearranging the windings on L12 and resoldering all solder joints of L12. Turned out I didn’t burn all of the wire’s coating the first time:

![](/img/notes-on-the-qrp-labs-qdx-04.png)

This looks much better but not really fixed - until you read [this thread on groups.io](https://groups.io/g/QRPLabs/topic/qdx_rf_filter_sweep/102685749?page=1&dir=asc).

Looks like 20m is a compromise band of the high band version as the 80m band is on the low band version. The issue is that I primarily work on 20m but there seems no better solution that to build a low band or even a mid band QDX.

## Socketed Transistors {#socketed-transistors}

I followed the advice of G7VKQ and built my second QDX with socketed transistors. This is how I’ve bent the transistors:

![](/img/notes-on-the-qrp-labs-qdx-05.jpg)

All BS170 installed:

![](/img/notes-on-the-qrp-labs-qdx-06.jpg)

The result:

![](/img/notes-on-the-qrp-labs-qdx-07.jpg)
