---
title: I've vibe coded an application to see what it's like
date: 2026-08-09 20:00
summary: I’ve always wanted to write a simple, custom CLI application that would let me log amateur radio contacts quickly and easily. The focus was on logging satellite contacts and the desire to avoid using a database. Instead, the log entries should be edited, deleted, or added directly in the ADIF file. So far, I’ve only used AI for translation in my personal life. At work, I use AI to automate security analyses in a SOC as part of a SOAR. I have virtually no experience with AI-supported software development and am very skeptical of the topic. But I decided to give it a try, partly because one should engage with topics that are relevant both personally and professionally - even if it feels like a chore. Furthermore, while I’d like to have this application, I don’t have the motivation invest a lot of effort into it...
---

I’ve always wanted to write a simple, custom CLI application that would let me log amateur radio contacts quickly and easily. The focus was on logging satellite contacts and the desire to avoid using a database. Instead, the log entries should be edited, deleted, or added directly in the ADIF file. So far, I’ve only used AI for translation in my personal life. At work, I use AI to automate security analyses in a SOC as part of a SOAR. I have virtually no experience with AI-supported software
development and am very skeptical of the topic. But I decided to give it a try, partly because one should engage with topics that are relevant both personally and professionally - even if it feels like a chore. Furthermore, while I’d like to have this application, I don’t have the motivation invest a lot of effort into it.

My initial prompt looked like this:

> Create me a Python TUI application for logging amateur radio QSOs. It should not rely on databases but require the user to provide an ADIF file. adif-logger should then read out the ADIF file and dynamically build its user interface based on the fields found in this ADIF file. A user should be able to log new QSOs, edit existing QSOs, delete existing QSOs and search for exisiting QSOs. When entering a new QSO, adif-logger should query qrz.com via user provided credentials via the
> qrz.com api to get information on the call sign entered (name, QTH, locator). Furthermore, the last 5 QSOs with this call sign should be shown in a separate list in the same window. New qsos should be appended to the user supplied ADIF, editing QSOs should update the affected entry in this ADIF etc. The application should include a translation table for ADIF fields so that a human readable label can be used instead of the technical ADIF field name.

This already resulted in a working application with which I was able to log, edit and delete QSOs. Pretty impressive! Over the next hours I tested the application and got many more ideas that I then prompted to Claude. The application got better and feature-richer every time it generated me a new version. The result is impressive: The code works, the application does what I want and the README is super detailed and updated every time the code changes.

Here's what I learned or understood today:

- AI-generated software projects can actually work. What Claude is able to generate from a simple prompt is amazing.
- I can code in Python myself. Not particularly well, but I can get done what I want or need to get done. What happened today, I can’t really call “vibe coding”. **I didn’t code**. I didn’t even look at the code. My role was that of a client or project manager who contracted someone/thing else to code for money. Furthermore, I was also the QA guy testing the application and giving feedback to Claude.
- For the reason above, the resulting code isn’t mine. I’m not even the code maintainer. To be able to do anything with it at all, I’d first have to read and understand the code - but then I might as well have written it myself.
- That somehow makes the generated application a throwaway product.
- I now have the application in a public Git repo, but can I share it in good conscience? I have my reservations about it.
- As a professional developer, I would find it very frustrating to have to debug someone else's code and also be held responsible for that code.
- As a hobbyist developer, it would bother me that I'm no longer a developer.
- It's impossible for me to be proud of the code that was generated.
