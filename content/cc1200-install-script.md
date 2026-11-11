---
title: Installation Script for the M17 CC1200 Hotspot
date: 2025-07-18
---

**UPDATE: The script was now updated to include [Jim N1ADJ’s m17-gateway](https://github.com/jancona/m17)**

One of the ways to get QRV in the [M17 digital voice mode](http://m17project.org) is to use a hotspot. Many are already familiar with Pi-Star based MMDVM hotspots from other digital modes, but there is a relatively new M17 dedicated variant, the [CC1200 M17 hotspot hat](/cc1200/). Unfortunately, until now there was no easy way to install the software components required to run the hotspot on the Raspberry Pi needed for it.

I have therefore written a bash installation script that performs all the necessary steps automatically. These are in detail:

- Verifies root and OS requirements
- Ensures it’s run on a **fresh install** of Raspberry Pi OS Lite (Bookworm, 64-bit)
- Configures UART for GPIO access
- Prompts for required reboots after system update and boot option changes
- Installs all necessary packages via APT
- Creates a dedicated *m17* user for running services
- Clones and compiles the following M17 Project repositories:
  - [libm17](https://github.com/M17-Project/libm17)
  - [rpi-interface](https://github.com/M17-Project/rpi-interface/)
  - [CC1200_HAT-fw](https://github.com/M17-Project/CC1200_HAT-fw) (firmware flashing optional)
  - [rpi-dashboard](https://github.com/M17-Project/rpi-dashboard) (web interface)
- Configures NGINX and PHP-FPM to serve the dashboard
- Adds a systemd service for rpi-interface
- Optionally flashes/updates the CC1200 firmware via stm32flash

After the installation is finished, the result is a ready-to-use M17 hotspot including a basic web dashboard that will be improved in the near future.

If you have ideas how to improve the script or have found a bug, please contact me and/or send a pull request.

More information and the script can be found in the project’s [GitHub repository](https://github.com/DK1MI/cc1200-hotspot-installer).
