---
title: Adding a UPS to the QMX+ Remote Digital Mode Station
date: 2026-06-04
---

Here's a quick update on my QMX+ based [Remote Digital Mode Station](/qmx) which I now use to provide a [24/7 running JS8 station](/js8).

I’ve been looking for an uninterruptible power supply (UPS) for my garden shed server rack for quite some time. I was about to buy a used rack-mountable 230V UPS when it occurred to me that I only run low-voltage devices in the rack: The switch requires 5V, the Raspberry Pi 5 does as well, and I had modified my QMX+ to run on 13.8V using a buck converter. After a quick online search, I discovered that such low-voltage UPS units do indeed exist. They are essentially power banks that can be plugged into a 230V outlet, have a large battery on board, and then provide various low-voltage outputs. I ultimately chose a 20000 mAh (74 Wh) UPS with 12V, 9V, and 5V outputs:

![](/img/qmx-ups-01.jpg)

In the process, I converted my QMX+ back to its original configuration and replaced the Power Pole connector with a hollow socket for a 12V supply voltage. The updated station looks like this when mounted on the rack shelf:

![](/img/qmx-ups-02.jpg)

This modification furthermore allowed me to get rid of the 13.8V power supply (a modified DELL server PSU), which also simplifies the entire setup. I haven't been able to test yet how long the station would run during a power outage, but I expect it to last for several hours.
