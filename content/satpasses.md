---
title: satpasses - a satellite pass prediction HTML file generator
date: 2025-09-18
---

[satpasses](https://github.com/DK1MI/satpasses) is a simple Python script that pulls satellite information on your favorite SATs from [N2YO.com](https://n2yo.com) via their API to build an even simpler static HTML page listing all satellite passes over a user definable location for the next n days. Each row of the generated table has a different shade of green depending on the max elevation of the corresponding pass. A higher maximum elevation results in a brighter green.

This is how it looks like:

![](/img/satpasses-02.jpg)

You can find a live demo [on my server](https://sat.rz01.org). Please note that the data there is only accurate for my location.

Minimum elevation, location and more are user configurable. The script can be found on [my GitHub](https://github.com/DK1MI/satpasses).
