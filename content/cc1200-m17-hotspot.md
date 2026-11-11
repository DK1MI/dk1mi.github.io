---
title: A lightweight M17 Hotspot
date: 2025-07-29
---

Until now, [CC1200 Hat](/cc1200) users had to operate their [M17](https://m17project.org) digital data/voice hotspot using the [rpi-interface](https://github.com/M17-Project/rpi-interface) software on the command line, for example. To change this, Jim N1ADJ and I have spent the last few days developing a lightweight M17 hotspot based on the CC1200 and a Raspberry Pi. The heart of the hotspot is Jim’s [m17-gateway](https://github.com/jancona/m17), which he has now brought to a stable release. In the meantime, I have completely rebuilt the dashboard [rpi-dashboard](https://github.com/M17-Project/rpi-dashboard) started by Wojciech SP5WWP and adapted it to Jim’s m17-gateway.

![](/img/cc1200-m17-hotspot-01.png)

The following things can now be done via this dashboard:

- Monitor incoming and outgoing calls
- Read text messages
- Edit the configuration of the dashboard
- Edit the configuration of the m17-gateway and thus
  - Changing the reflector
  - Changing the module
  - Changing the hotspot frequency
  - and much more
- Updating the M17 hosts file
- Starting/stopping the m17-gateway

It offers all the essential functions you need for daily use while more features are already planned. Jim is also developing his m17-gateway further, whereby we both involve each other, as gateway and dashboard go hand in hand.

It is not a ready-to-use, downloadable Raspberry Pi image, but we provide an installation script, which I have [already presented here](/cc1200-install-script). In the meantime, this has been adapted so that it no longer installs the rpi-interface but the m17-gateway.

If there are any problems with the installation or if you have any other questions, you can find us on the [M17 Discord Server](https://discord.gg/4brEP8wwVp)
