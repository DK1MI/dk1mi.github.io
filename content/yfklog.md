---
title: YFKlog
date: 2025-03-13
---

I think I’ve tried pretty much every amateur radio logbook software (including one for the Commodore C64) and I’m probably still not at the end of my search. Most of the time I used [Wavelog](https://www.wavelog.org/). This web application, which I have running on a [Proxmox server](/proxmox-server/) at home, actually fulfils a lot of my requirements: web-based and therefore usable on my Linux desktop, open source software, many integrations and is actively being developed further. However, the fact that I have to operate a radio, a keyboard and a mouse when playing radio has been annoying. That may sound a bit petty, but I see potential for improvement. I myself have always had a soft spot for text-based command line applications and have also used the [YFKlog](https://fkurz.net/ham/yfklog.html) logbook software written in [Perl](https://www.perl.org/) in the past. At that time, integrations with eQSL, QRZ.com etc. were still very important to me, which is why I eventually switched to Cloudlog and then to Wavelog. In the meantime, [QSL is no longer important to me](/on-qsling/) and I don’t really hunt DX anymore. That’s why I ended up back at YFKlog:

![](/img/yfklog-01.jpg)

What I like about this software is that I know what’s going on under the bonnet because I’ve worked with the code in the past. But the most important thing is that I can use it without a mouse. There is a QSO input screen, a search function and the possibility to export or import QSOs as ADIF, everything else is not really important for me. The only feature I would like to see is an automatic upload to the QRZ.com logbook. I use this as my offsite backup. No matter what happens locally, I can reliably generate and download an ADIF export from there. This is also exactly how I migrate from one logbook to the next.

I’m still thinking about how to solve this problem. Either I do a manual export once a month and then upload the ADIF, or I try to integrate the functionality into YFKlog. In any case, I am very happy with the usability and simplicity of the software and hope that I have finally reached my goal.
