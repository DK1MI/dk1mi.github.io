---
title: Getting paged from OscarWatch
date: 2026-10-11 13:00
summary: I use OscarWatch not only to track satellites but also to plan the passes I want to work on. To do this, you can simply select and mark any passes you want within the pass planner integrated into OscarWatch, and then receive a notification via a pop-up window 5 minutes before the start of the pass. Unfortunately, I miss flyovers from time to time because I can’t keep an eye on OscarWatch all the time...
---

I use [OscarWatch](/oscarwatch) not only to track satellites but also to plan the passes I want to work.
To do this, you can simply select and mark any passes you want within the pass planner integrated into OscarWatch, and
then receive a notification via a pop-up window 5 minutes before the start of the pass.
Unfortunately, I miss passes from time to time because I can’t keep an eye on OscarWatch all the time.

Fortunately, the application offers a WebSocket through which a wide variety of information can be received over the network.
This data also includes alerts about an upcoming pass, so that a helper tool can be used to relay this information
through various other channels. I’ve written a small Python tool for this purpose that receives these messages and
then notifies me, for example, via Pushover or a DAPNET pager.

![](/img/oscarwatch-notifier-01.jpg)

You can find the code and more information on installation and usage here: <https://github.com/DK1MI/oscarwatch-notifier>
