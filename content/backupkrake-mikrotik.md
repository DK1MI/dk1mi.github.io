---
title: Backing up Mikrotik devices with Backupkrake
date: 2026-11-26 16:00
---

[Backupkrake](https://backupkrake.rz01.org/) is my pull-based backup server: it connects via SSH to every
machine on the network and pulls its data into hard-linked snapshots, with encrypted offsite copies
via restic. Until now, only Linux and Unix hosts were supported.

The one box nobody thinks of until it dies is the router. Its configuration is the result of
years of small changes: firewall rules, VLANs, WireGuard peers, DHCP leases, scripts. Version 0.7
of Backupkrake adds a third kind of host next to "whole system" and "home folder": **MikroTik router**.

## What gets backed up

Every backup of a RouterOS 7 device saves three files into a normal Backupkrake snapshot:

| File | Content |
|---|---|
| `export.rsc` | the full configuration, from `/export terse`, optionally with secrets (`show-sensitive`) |
| `system.txt` | RouterOS version, model, serial number and firmware, so you know what to restore onto |
| `backupkrake.backup` | optional: a binary backup the router creates itself |

The export is plain text: readable, diffable, and importable on any model. The binary backup also
contains users, passwords and certificate keys, but restores only to the same model. Keeping both covers
"the router died, here's a new one" as well as "I broke something last Tuesday".

## How it works

RouterOS has neither rsync nor forced commands in `authorized_keys`, so routers are handled
differently from Linux hosts:

- **A read-only user.** Backupkrake logs in as its own RouterOS user. That user's group has the policies
  `ssh,read,sensitive,ftp` but **no `write`**, so it can read the whole configuration and download
  files, but can't mess up your router. `address=` restricts logins to the backup server.

    ```
    /user group add name=backupkrake policy=ssh,read,sensitive,ftp
    /user add name=backupkrake group=backupkrake address=<backupkrake-IP>/32 password=<long random password>
    /user ssh-keys import user=backupkrake public-key-file=backupkrake.pub
    ```

- **The router makes its own binary backup.** Creating a `.backup` file would need `write`, so the
  router does it with its own scheduler, shortly before Backupkrake's schedule. Backupkrake downloads it
  over SFTP and warns if it's missing or older than two days, which usually means the router's
  scheduler stopped.

    ```
    /system scheduler add name=backupkrake-backup interval=1d start-time=01:30:00 \
        on-event="/system backup save name=backupkrake password=<backup password>"
    ```

- **No changes, no space.** RouterOS puts a timestamp in the first line of every export. Backupkrake
  drops that line, so an unchanged configuration produces an identical file. That file is hard-linked to
  the previous snapshot, and the run simply says *no changes*. A daily router backup costs next to
  nothing.
- **Secrets stay out of the logs.** With secrets enabled, the export contains WireGuard keys and Wi-Fi
  and PPPoE passwords. It's captured directly into the snapshot and never written to the run log. The
  connection test reads the export *without* secrets.
- **Its own sanity check.** RouterOS exits with code 0 even when a command fails, so Backupkrake looks
  for RouterOS error messages in the output. It also marks a run as a warning if the export suddenly has
  far fewer lines than the last one.

Everything else works as for any other host: schedules, backup windows, retention with pinned
snapshots, notifications, overdue alerts, browsing and downloading as well as offsite copies with restic.

## Setting it up

1. Download the server's key (`backupkrake.pub`) from the host form and upload it to the router.
2. Run the three user commands above in the RouterOS terminal (the form shows them with your values).
3. Optionally, add the scheduler for the binary backup.
4. **Add host** → **MikroTik router**, enter the address, and click **Test connection**.

Restoring is deliberately manual: download `export.rsc` and `/import` it on a reset router, or load the
`.backup` file on the same model. The manual covers the details in
[Adding a MikroTik router](https://backupkrake.rz01.org/hosts/#adding-a-mikrotik-router) and
[Restoring a MikroTik router](https://backupkrake.rz01.org/restoring/#restoring-a-mikrotik-router).

To update, change the image tag in your `docker-compose.yml` to `0.7.0` or later and run
`docker compose pull && docker compose up -d`.
