---
title: Dynamic DNS for NSD
date: 2018-05-03
---

## Introduction {#introduction}

nsd-dyndns is a simple script that adds dynamic DNS dunctionality to NSD (authoritative DNS name server).

## Requirements {#requirements}

The following is required or suggested:

- OpenBSD (or another BSD or some Linux distro) with HTTPD and NSD installed (pkg_add nsd), configured and running
- (sub-)domain for your webserver. Needed for updating the NS record of your actual DynDNS domain.
  - In this example:&nbsp;*update.example.com*
- (sub-)domain that is updated dynamically.
  - In this example:&nbsp;*dyn.example.com*
- A router capable of sending custom GET-requests to your DynDNS server.
  - In this example: A FritzBox

## Installation {#installation}

### Configure your HTTPD {#configure-your-httpd}

Add the following new virtual host to your&nbsp;*/etc/httpd.conf*:

```
 server "update.example.com" {
    listen on $ext_addr port 80
    root "/htdocs/dyndns"
    log access dyndns.log
 }

```

Create an empty&nbsp;*update.html*:

```
# mkdir /var/www/htdocs/dyndns/
# touch /var/www/htdocs/dyndns/update.html

```

After reloading HTTPD, try to access&nbsp;\[http://update.example.com/update.html\]&nbsp;The request should show up in&nbsp;*/var/www/logs/dyndns.log*

### **Create a zone file for dyn.example.com** {#create-a-zone-file-for-dynexamplecom}

Create a new zone file (e.g. at&nbsp;*/var/nsd/zones/dyn.example.com.zone*) with the following content

```
$ORIGIN example.com.
$TTL 300
@ IN SOA ns1.example.com. admin.example.com. (
1524952218
300 ; refresh
900 ; retry
1209600 ; expire
1800 ; ttl
)

; Name servers
IN NS ns1.example.com.
IN NS ns1.example.com.

; A records
@ IN A 123.123.123.123
update IN A 123.123.123.123
dyn IN A 123.123.123.123

```

Don’t forget to set your own domain names, name servers and ip addresses Furthermore, add this zone file to your&nbsp;*/var/nsd/etc/nsd.conf*

### Configure and Install nsd-dyndns {#configure-and-install-nsd-dyndns}

- Download the scripts here: [nsd-dyndns.tar.gz](/files/nsd-dyndns.tar.gz)
- Copy&nbsp;dyndns.conf-dist&nbsp;to&nbsp;/etc/dyndns.conf
  - *# cp dyndns.conf-dist /etc/dyndns.conf*
- Edit&nbsp;/etc/dyndns.conf&nbsp;to your needs
- Copy&nbsp;dyndns.sh&nbsp;to&nbsp;/usr/local/bin/dyndns.sh
  - *# cp dyndns.sh /usr/local/bin/dyndns.sh*
- Make the script executable:
  - *# chmod u+x /usr/local/bin/dyndns.sh*
- Add&nbsp;/usr/local/bin/dyndns.sh&nbsp;to your crontab

### Configure your router {#configure-your-router}

Configure your router to query the following URL:

```
http://update.example.com/update.html?qwertzuiop1234567890

```

Don’t forget to set your own domain name and to replace the string after “?” with the password you configured in the config file.

## What it does {#what-it-does}

When your router gets a new IP and therefore sends an HTTP request to your server, a similar entry should appear in your&nbsp;/var/www/logs/dyndns.log:

```
update.example.com 123.123.123.123 - - [29/Apr/2018:20:48:19 +0200] "GET /update.html?qwertzuiop1234567890 HTTP/1.1" 200 6

```

When the script is executed e.g. via cron, the following happens:

- It greps the last line of&nbsp;/var/www/logs/dyndns.log&nbsp;where the correct password was found and extracts the requesting IP address
- It checks if this IP is the same than the last time
- If it’s a new IP, then it replaces the forth line in your zone file (the line with the version number) with a new version (current unix time stamp)
- As a second step, it updates the A record of you DynDNS domain (dyn.example.com in our example)
- It then stores the new IP in the file&nbsp;/tmp/last_dyndns_ip.txt
- Finally it reloads NSD
