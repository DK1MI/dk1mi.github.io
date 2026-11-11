#!/usr/bin/env python3
"""
js8notifier.py 

Version: 1.1
Author: Michael Clemens, DK1MI

Connects as a Telnet client (using telnetlib) to a running JS8Call instance,
reads , filteryncoming line, filters lines to ones that are directed to our
call sign (MY_CALL) and sends a Pushover notification containing the message.

On Debian Trixie, install 'telnetlib' via the following command:

# sudo apt install python3-zombie-telnetlib

DISCLAIMER: Use at your own risk. Read and understand the code, then use it.

"""

import os
import json
import time
import telnetlib
import requests
import re

# Adapt this if the script runs on a different host than
# JS8CAll or if you have configured another port in JS8Call
REMOTE_HOST = "127.0.0.1"
REMOTE_PORT = "2442"
RECONNECT_DELAY_SEC = 5.0

# Configure this in any case! Set MY_CALL to your call sign
# as configured in JS8Call. 
PUSHOVER_USER = ""
PUSHOVER_TOKEN = ""
MY_CALL = "DK1MI"

PUSHOVER_API = "https://api.pushover.net/1/messages.json"

# Regex to detect heartbeat messages
HEARTBEAT_SNR_PATTERN = re.compile(r'^\s*' + re.escape(MY_CALL) + r'\b.*\bHEARTBEAT\b.*\bSNR\b', re.IGNORECASE)


# Generic function that sends messages via Pushover
# Doesn't contain any JS8 specific code
def send_pushover(title: str, message: str) -> bool:
    if not PUSHOVER_USER or not PUSHOVER_TOKEN:
        print("Pushover credentials not configured.")
        return False
    payload = {
        "token": PUSHOVER_TOKEN,
        "user": PUSHOVER_USER,
        "title": title,
        "message": message,
    }
    try:
        r = requests.post(PUSHOVER_API, data=payload, timeout=10)
        r.raise_for_status()
        return True
    except Exception as e:
        print("Pushover send failed:", e)
        return False

# Checks if the text dontains specific words in order to get
# ignored (e.g. we don't want notifications for HB replies).
def should_ignore_text(text: str) -> bool:
    if not isinstance(text, str):
        return True
    if not text.startswith(MY_CALL):
        return False
    # Check pattern: HEARTBEAT and SNR appear after the call sign in the text.
    if HEARTBEAT_SNR_PATTERN.search(text):
        return True
    return False


# Executed for every line received from JS8Call via its TCP interface
def process_line(line: str):
    line = line.strip()
    if not line:
        return
    try:
        obj = json.loads(line)
    except json.JSONDecodeError:
        return
    params = obj.get("params", {})
    text = params.get("TEXT")
    from_call = params.get("FROM") or params.get("CALL") or params.get("FROMCALL")
    # Only continue if a line is of type "TEXT" and if the text starts with our call
    if isinstance(text, str) and text.startswith(MY_CALL):
        if should_ignore_text(text):
            return
        from_display = str(from_call) if from_call else "<unknown>"
        text_clean = text.strip()
        push_message = f"{from_display}: {text_clean}"
        push_title = f"Message from {from_display}"
        print("Matched:", push_message)
        # Send the "from call" and extracted messages via Pushover
        sent = send_pushover(push_title, push_message)
        print("Pushover sent:", sent)

# Endless loop listening to the JS8Call TXP interface / API
# Executes process_line for every received line
def connect_and_listen(host: str, port: int):
    while True:
        tn = None
        try:
            print(f"Connecting to JS8Call ({host}:{port})...")
            tn = telnetlib.Telnet(host, port, timeout=20)
            # Optionally disable local echo handling and set socket timeout
            tn.sock.settimeout(None)
            print("Connected.")
            while True:
                # Read a single line (blocks until newline or connection close)
                raw = tn.read_until(b"\n")
                if not raw:
                    print("Connection closed by JS8Call.")
                    break
                try:
                    line = raw.decode("utf-8", errors="replace")
                except Exception:
                    line = raw.decode("utf-8", errors="replace")
                process_line(line)
        except (KeyboardInterrupt, SystemExit):
            print("Interrupted, exiting.")
            if tn:
                try:
                    tn.close()
                except Exception:
                    pass
            break
        except Exception as e:
            print("Connection error:", e)
        finally:
            try:
                if tn:
                    tn.close()
            except Exception:
                pass
        print(f"Reconnecting to JS8Call in {RECONNECT_DELAY_SEC} seconds...")
        time.sleep(RECONNECT_DELAY_SEC)

if __name__ == "__main__":
    connect_and_listen(REMOTE_HOST, REMOTE_PORT)
