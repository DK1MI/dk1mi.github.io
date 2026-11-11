---
title: Statistics and Likes
date: 2025-02-26
---

With social media there is undoubtedly the potential for addiction to likes. If you post something on X, Mastodon, Bluesky, Facebook or whatever, your post gets a certain number of likes. If you enjoy getting likes, you inevitably change your writing behaviour and post more and more content that others like instead of expressing yourself. To escape this perverse behaviour, I’m hardly active on social media anymore and when I am, 99% of the time I just read. Because of all this, I have, to a certain extent, retreated to my own website.

On your own website, you can express yourself more precisely, determine the rules yourself (within the legal framework) and receive practically no feedback that can influence you. That’s what I thought at first and I found myself checking the web traffic statistics that I had automatically generated using web server logs on a daily basis. Here I could see how many unique visitors I had per day, which pages linked to my website and which posts were read the most. It’s not really the same as getting likes, but it’s very similar. Above all because your own writing behaviour is also influenced here.

I have therefore decided to completely dispense with web server logs and statistics of any kind. This static website, which is generated using [Hugo](https://gohugo.io/) and whose Markdown code is hosted on Github, is regenerated fully automatically with every Git push using a Github integration and automatically published on Cloudflare Pages. I have thus completely decoupled myself from the hosting side of things, write my content with *vim* on the command line and then publish the new version with a simple *git commit -a* and a final *git push*. The result is then finally a website that

- doesn’t have a newsletter, login form, comment function, admin backend, database, maps integration or similar shenanigans
- is pure static HTML generated with Hugo
- is free of cookies
- doesn’t include any JavaScript
- does not track its readers
- does not collect any data
- is not generating any statistics at all
- is 100% non-commercial, ad-free and free of referral links
- provides information that has been compiled by a human being with the aim of passing it on to other human beings
- is not there to satisfy any greed
- is intended to be accessible (e.g. screen reader compatible)
