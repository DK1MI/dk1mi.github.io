---
title: Finding current ham radio satellite information
date: 2025-12-30
---

Working amateur radio LEO satellites reliably depends on good sources for which satellites are active and how to work them. You furthermore want to know about upcoming passes that are suitable for your station setup. You also might want to know about new satellite launches, active modes of satellites and if their transponders are active right now. Below are some useful resources I use every day:

## AMSAT Live OSCAR Satellite Status Page {#amsat-live-oscar-satellite-status-page}

This is one of most valuable resources provided by AMSAT and fed with data from satellite operators. You can find this page here: [AMSAT Live OSCAR Satellite Status Page](https://www.amsat.org/status/). This site

- Lists AMSAT-tracked amateur satellites and their current operational state.
- Shows which satellites have been heard recently, by which station and when.
- Provides links to each satellite’s information page with uplink/downlink frequencies, mode and operational notes.

I monitor this page for new satellites, changes in operation modes or to see when to expect traffic on specific sats. The following screenshot shows the status from the time of this post’s writing:

![](/img/ham-sat-info-01.png)

Your information for this page can be manually entered at the bottom of the page or via an [API](https://en.wikipedia.org/wiki/API). I have configured my [wavelog](https://www.wavelog.org/) instance to automatically send sat QSO info to this site which is very convenient and fool proof.

## Hams.at {#hamsat}

[Hams.at](https://hams.at/) states in its [about page](https://hams.at/about) that “*This site is not intended to be a replacement for satellite pass prediction software. For now, it’s just a tool to promote operating activity*”. Well … I use it for satellite pass predictions and it is doing an excellent job at this. It’s one of my most important pinned tabs in my browser which I use to plan my (ham radio) day. After you have entered your locator, it provides you with a filtered list of upcoming [satellite passes](https://en.wikipedia.org/wiki/Orbital_pass) including all necessary information like AOS (aquisition of signal / start of the pass), length of pass, maximum elevation, direction of pass and if another operator announced that he/she will be QRV during a particular pass on a satellite.

![](/img/ham-sat-info-02.png)

## N2YO.com {#n2yocom}

[N2YO.com](https://www.n2yo.com/) is the [OG](https://www.merriam-webster.com/dictionary/OG) when it comes to satellite resources on the net. I haven’t explored it fully yet but here’s what I know about it:

- Provides per-satellite details, real-time position/visibility maps, and pass predictions for a given location.
- Offers an API for programmatic access
- Many other resources on the net use the data from N2YO.com to present it in a different way or to use it in other ways

I use it to access information on specific satellites by entering the satellite’s name into the search box on the top right. From there you not only get lots of details on the sat but also a live view map and a link to a 10 day prediction for your location. This of course requires you to create an account beforehand. If I am interested in a specific future pass, I can click on the corresponding line of the 10 days prediction table to add it to my notifications list. This will then lead to a notification via mail before the pass starts so I don’t forget about it and can prepare my station in time.

![](/img/ham-sat-info-03.png)

## AMSAT Mailing Lists {#amsat-mailing-lists}

Another valuable source of information are the [AMSAT mailing lists](https://www.amsat.org/amsat-email-lists/). To get started, please read their [FAQ](https://www.amsat.org/mailing-list-faq/). I especially find the [ANS list](https://mailman.amsat.org/hyperkitty/list/ans@amsat.org/) useful as it delivers a great overview on what is new in the world of ham radio satellites right into your inbox.

## Telegram {#telegram}

Not a service per se but a great resource (despite the QRM that such groups bring with them) is the [International AMSAT Ops Telegram Group](https://t.me/amsatops). This group has more than 500 members that discuss everything related to working amateur radio satellites. Here you will hear about new sats, dying sats, skeds, technical issues and their solutions and much more. In my opnion the fastest way to get informed about anything new in this part of our hobby.

## Apps {#apps}

There are several apps that can be used to predict satellite passes and are especially useful for portable operations as some of these can also be used to align one’s antenna. Two good Android apps are [Look4Sat](https://play.google.com/store/apps/details?id=com.rtbishop.look4sat&hl=en) and [ISS Detector](https://play.google.com/store/apps/details?id=com.runar.issdetector&hl=en).

## The AMSAT Journal {#the-amsat-journal}

If you enjoy satellite communications, it would be a good thing to join your local AMSAT club or become an [AMSAT.org member](https://www.amsat.org/join-amsat/). I am a member of AMSAT and therefore receive the AMSAT Journal, which is “*a bi-monthly digital magazine for amateur radio in space enthusiasts, published by the Radio Amateur Satellite Corporation (AMSAT).*” [source](https://launch.amsat.org/The_AMSAT_Journal). While the journal keeps you informed, you also support important AMSAT projects with your membership fees.

## Closing Thoughts {#closing-thoughts}

I think that the information above will get you a long way, although there are of course many other sources of information out there. There are certainly various social media groups/accounts that you can follow, but that’s not my thing. I consider silos like Facebook to be harmful and unethical, and they should not be something that our hobby depends on. Telegram is bad enough, but I am willing to make this compromise in order to be able to contact other operators and get the latest news.
