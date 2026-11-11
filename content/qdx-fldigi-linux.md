---
title: QDX and Fldigi on Debian Linux
date: 2024-08-09
---

The following instructions describe how to configure Fldigi for operation with the [QRP Labs QDX transceiver](/qubedx/) on Debian Linux 12 / Raspberry Pi OS (64bit).

In the configuration menu, click on *Soundcard -> Devices* and select *PulseAudio*:

![](/img/qdx-fldigi-linux-01.png)

Afterwards, click on *Rig Control -> Hamlib* and configure it as follows:

![](/img/qdx-fldigi-linux-02.png)

With these few settings it almost worked for me - but only almost. The QDX switched to transmit mode, but no signal was emitted and the red LED flashed twice continuously. This indicated that the audio signal was too low.

To fix this, open the *PulseAudio Volume Control* tool and set the volume under *Output Devices* to 11dB:

![](/img/qdx-fldigi-linux-03.png)

If *PulseAudio Volume Control* is not installed on the system, this can be done using the following command:

```
# sudo apt install pavucontrol
```
