---
title: js8notifier.py - notifies of JS8 Messages via Pushover
date: 2026-06-15 13:00
summary: Since my JS8Call station runs 24/7, but I can't always keep an eye on it, I wrote a small Python script that notifies me of incoming messages (directed text and messages) via Pushover.
---

Since my JS8Call station runs 24/7, but I can't always keep an eye on it, I wrote a small Python script that notifies me of incoming messages (directed text and messages) via [Pushover](https://pushover.net).

If anyone else wants to use this script for their station, here’s what to do:

[Download the script](/files/js8notifier.py) and make it executable:

```
# wget https://rz01.org/files/js8notifier.py
# chmod u+x ./js8notifier.py
```

Then install all necessary dependencies. In my case (on Debian Trixie), that was just “telnetlib”:

```
# sudo apt install python3-zombie-telnetlib
```

Next, you must configure the following variables:

```
REMOTE_HOST = “127.0.0.1”
REMOTE_PORT = “2442”

PUSHOVER_USER = “”
PUSHOVER_TOKEN = “”
MY_CALL = “NOCALL”
```

If the script is running on the same system as JS8Call, REMOTE_HOST and REMOTE_PORT should already be set correctly. You can find the PUSHOVER_USER and PUSHOVER_TOKEN on the Pushover website after logging in. As the name suggests, you should enter your own call sign under MY_CALL.

This is how such a notification looks like on an Android phone:

![](/img/js8notifier-01.jpg)
