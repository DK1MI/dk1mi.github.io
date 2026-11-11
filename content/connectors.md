---
title: Check your connectors
date: 2026-09-08 13:00
summary: Seriously. You really should check your connectors every time before you connect them, and especially if you're having problems with high SWR. This can save you a lot of time and money. I never really took this seriously, but I've learned my lesson now...
---

Seriously. You really should check your connectors every time before you connect them, and especially if you're having problems with high SWR.
This can save you a lot of time and money. I never really took this seriously, but I've learned my lesson now:

Recently, [I moved the cross-Yagis from my LEO setup from a lower location up to the roof of the house](/leo-upgrade/).
In the process, I also had to reroute the two 10mm coaxial cables that connect the antennas to the radio.
Before putting everything into operation, I measured the standing wave ratio first and discovered that something was wrong with the cable connected to the 70 cm Yagi.
After an incorrect analysis on my part, I assumed that the approximately 20m long coaxial cable was defective and ordered new cables and connectors at great expense.
Even before they arrived, I determined through further experiments that the actual problem seemed to be the diplexer, which [I had used as a J-mode filter between the 70-cm Yagi and the preamp](/desense/).
After swapping it out for another diplexer I had on hand, the SWR was optimal. Now, two weeks later, I took a closer look at the supposedly defective diplexer.
Unlike the new diplexer, this one didn’t have an N-type connector on the 70 cm side but had a PL-type connector instead.
So that I could still connect a cable with an N-type plug, I built an adapter cable back then. And this is what the N-connector on this cable looked like now:

![](/img/connectors-01.jpg)

On the left, you can see a healthy female N-connector; on the right, the one from the short adapter cable. As you can clearly see, something unpleasant has happened to this connector.
I don’t know exactly what happened. Maybe I screwed a PL plug onto it, or an N-plug with a bent pin. In any case, it’s now clear that the diplexer isn’t the problem either.

If I had visually inspected the connectors before screwing them together, I could have saved a lot of time, hassle, and money.
