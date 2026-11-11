---
title: Chrome extension to sync WebSDRs with a radio
date: 2026-11-08 13:00
summary: I have long suffered from extreme interference at my home QTH, to the point where shortwave radio operation has become nearly impossible. Many attempts to solve the problem have failed, so I’ve been on the verge of giving up completely several times. Lately, I’ve accepted the situation and adopted the following strategy: transmitting with my own transceiver and listening with one of the many available WebSDRs. WebSDRs are radio receivers connected to the internet that can be operated simultaneously by multiple users via a web interface...
---

### Updates

**2026-11-09:** I've added a list with POTA, SOTA, WWFF etc. spots with band, mode and programme filters. You can click on a spot and the SDR and radio jump to it.
Furthermore, you can log the contact in Cloudlog/Wavelog with another click on the "Log" button.

### Original Article

I have long suffered from extreme interference at my home QTH, to the point where shortwave radio operation has become nearly impossible.
Many attempts to solve the problem have failed, so I’ve been on the verge of giving up completely several times.
Lately, I’ve accepted the situation and adopted the following strategy:
transmitting with my own transceiver and listening with one of the many available WebSDRs.
WebSDRs are radio receivers connected to the internet that can be operated simultaneously by multiple users via a web interface.
They are freely available and often provide interference-free reception.

While my problem can be circumvented using a WebSDR, practical operation is somewhat complicated and prone to errors.
Sometimes you change the frequency in the WebSDR, discover an interesting station,
and start transmitting - only to realize that your own transceiver is still tuned to a different frequency.

I needed to find a solution to reliably synchronize any WebSDR with my own transceiver.
After some thought, I came up with the idea of developing a Chrome browser extension that does the following:

The browser extension connects via CAT (USB/serial) to a local, physical transceiver so it can control it directly.
It also detects the frequency, mode, and band from any WebSDR, OpenWebRX, or KiwSDR instance and can modify them.
With these two capabilities, it is now able to connect and synchronize both worlds.
You can either change the frequency in WebSDR and the transceiver will synchronize, or you can turn the transceiver’s VFO knob and WebSDR will remain synchronized.

Another feature allows you to send the synchronized data to a Cloudlog/Wavelog instance via its API, so you can log the QSO there easily and conveniently.

![](/img/websdr-radio-sync-01.png)

I'm currently still waiting for this Chrome extension to be approved and published in the Chrome Web Store.
If you'd like to try out the tool right now, you can download it and install it in Chrome.
All the details about this and more can be found on the project page on GitHub: <https://github.com/DK1MI/websdr-radio-sync>
