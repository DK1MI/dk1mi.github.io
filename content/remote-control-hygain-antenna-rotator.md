---
title: Remote Control for the Hy-Gain AR-500X Antenna Rotator
date: 2024-02-03
---

The project described here attempts to solve the following problem: an antenna is to be rotated remotely using a Hy-Gain AR-500X antenna rotor. The rotor comes with a control unit for this purpose. However, the aim is to develop a remote control for the control unit and to make the control unit network-compatible so that it can be controlled by a computer via the network.

![](/img/remote-control-hygain-antenna-rotator-3.jpg)

## Preconditions {#preconditions}

- The original antenna rotor control unit should remain unmodified
- A bidirectional antenna is installed, so the rotator only needs to be able to rotate 180 degrees, not the full 360 degrees.

## The Idea {#the-idea}

The control unit has an infrared receiver that was originally intended for the infrared remote control supplied. This was replaced in this project by an ESP8285 microcontroller board, the *Hailege ESP8285 ESP-01M Digital Infrared Transceiver*, which also has an infrared transmitter and receiver module integrated on the circuit board.

As I only need a rotation of 180 degrees and the controller has 12 memory locations from A to L, I have distributed the headings to the available memory locations as follows:

<table>
<thead>
<tr>
<th>Memory</th>
<th>Heading 1</th>
<th>Heading 2</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>0</td>
<td>180</td>
</tr>
<tr>
<td>B</td>
<td>15</td>
<td>195</td>
</tr>
<tr>
<td>C</td>
<td>30</td>
<td>210</td>
</tr>
<tr>
<td>D</td>
<td>45</td>
<td>225</td>
</tr>
<tr>
<td>E</td>
<td>60</td>
<td>240</td>
</tr>
<tr>
<td>F</td>
<td>75</td>
<td>255</td>
</tr>
<tr>
<td>G</td>
<td>90</td>
<td>270</td>
</tr>
<tr>
<td>H</td>
<td>105</td>
<td>285</td>
</tr>
<tr>
<td>I</td>
<td>120</td>
<td>300</td>
</tr>
<tr>
<td>J</td>
<td>135</td>
<td>315</td>
</tr>
<tr>
<td>U</td>
<td>150</td>
<td>330</td>
</tr>
<tr>
<td>L</td>
<td>165</td>
<td>345</td>
</tr>
</tbody>
</table>

## The Code {#the-code}

You can find the Arduino sketch here: [hygain-ir-controller.tar.gz](/files/hygain-ir-controller.tar.gz)

The resulting web application is not really beautiful but functional:

![Screenshot of the web application](/img/remote-control-hygain-antenna-rotator-1.jpg)

Every button has a letter from A to L assigned. A click on a button of the web application sends the corresponding infrared code to the HyGain control unit, selects this specific memory channel and turns the antenna to the pre-programmed direction.

Follow the resulting GET request to select the memory location G:

```
http://<IP_ADDRESS>/get?memory=G

```

The webserver can also be given a numerical value for the desired heading. The closest memory location is then selected. The request looks like this for a heading of 210 degrees:

```
http://<IP_ADDRESS>/get?heading=210

```

## Hardware Implementation {#hardware-implementation}

No soldering was necessary as the *Hailege ESP8285 ESP-01M Digital Infrared Transceiver* already has everything on board that is needed. I’ve mounted the board with a zip tie to a board right above the sensor of the base unit and connected it to a 5V power source.

![The base control unit](/img/remote-control-hygain-antenna-rotator-2.jpg)
