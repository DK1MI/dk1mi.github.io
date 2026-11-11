---
title: Migrating to the EU
date: 2026-03-22
---

[Deutsch / German](#deutsch)

## Introduction {#introduction}

For various reasons, I have decided to move as many services and subscriptions as possible from non-EU countries to the EU or to switch to European service providers. The reasons for this are the current global political situation and improved data protection. I don’t want to go into the first point any further for various reasons, but the second point should be immediately obvious, since the EU currently has the most user-friendly laws when it comes to data protection. Below, I will list both the old and new service providers; this is not an advertisement, but simply the result of my research, which was aimed at achieving the same or better quality at affordable prices.

I would call this post an interim report, and I will expand on it if I end up migrating more services.

## Mail

In my opinion, [Fastmail](https://www.fastmail.com/) is one of the best email providers. In all the years I’ve had my email accounts there, I’ve never had any problems. I paid 10 euros a month for two accounts, could use an unlimited number of my own domains, and could not only set up catch-all addresses but also send emails from any email address I wanted. This is important for [my email setup](/how-i-do-email). The calendar is also solid and was used within the family. All of this was also available in a well-designed Android app.
Finding a European alternative that offers all of this proved difficult. First, I tried [mailbox.org](https://mailbox.org), which I can generally recommend without reservation. Unfortunately, you can’t send emails from any address on your own domain without a workaround, so the search continued. Eventually, I landed on [Uberspace](https://uberspace.de). This “pay what you want” provider offers a shell account, web hosting, email hosting, and more at fair prices. In addition, you can use as many of your own domains as you like for
both web and email, and send emails from any sender address. There isn’t a dedicated app, which is why I now use Thunderbird for Android and am very satisfied with it.

## Calendar

[Uberspace](https://uberspace.de) doesn't offer a built-in calendar solution. So I tried installing various CalDAV servers, but none of them really convinced me. In the end, I simply installed NextCloud on my [Uberspace](https://uberspace.de) Asteroid, which has CalDAV and CardDAV built in. On my desktop, I use Thunderbird as a client; on Android, I use DAVx5 and Fossil Calendar. It works great, even if NextCloud does come with some overhead. In return, I can now easily share files with others and, in theory, also use NextCloud’s
online office functionality.

## Web

Now that I’m already using [Uberspace](https://uberspace.de) for my email and calendar, I was able to host this website there as well. I previously had a VPS with Hetzner for this purpose, which I no longer need. The only minor hurdle was that I use SSI on this site to manage the header centrally. I had previously used Nginx, but [Uberspace](https://uberspace.de) hosts on Apache, where the SSI implementation is handled slightly differently. However, adapting my HTML code
was quite simple, so I was able to quickly migrate the site to [Uberspace](https://uberspace.de).

## Domains and DNS

For a long time, I was a satisfied [Namecheap](https://www.namecheap.com/) customer. They offer good prices, a wide selection of available domains, their DNS management has everything you need, and their support team has helped me quickly on several occasions. But now it was time to look for a comparable provider in the EU. In the end, I settled on [hosting.de](https://hosting.de). Some of the reasons were the prices, reviews, the location in Germany, and the availability of .is domains. So far, everything has been running smoothly; support helped me quickly and competently with one issue; and while prices for non-German domains are slightly higher, they’re still within an acceptable range.

## Git

At some point, pretty much everyone had their code on [GitHub](https://github.com) (or still does). I was no exception, though I had also hosted my own Gitea instance. Eventually, I got tired of that too and migrated all my Git repositories to codeberg.org. [Codeberg](https://codeberg.org) is a German-based nonprofit organization, and it’s hard to imagine going wrong with this choice.

## VPN

No changes here. I’ve always been a happy [Mullvad](https://mullvad.net) customer. For 5 euros a month, I pay a Swedish company that has proven it doesn’t log any data and doesn’t even require me to create an account. No subscription traps, no weird Black Friday deals, no discounts: just 5 euros a month for a reliable, trustworthy service.

## Android, Chromebook and Google

For many years, I used my work smartphone for personal use as well. I was more than satisfied with the Pixel 6, but understandably, I wasn’t allowed to install a custom ROM or use alternative app stores like F-Droid. That’s why I decided to buy a separate personal smartphone. I chose the Pixel 9a, which is supported by [Graphene OS](https://grapheneos.org/). I still installed the Google Play Store so I could install a significant number of apps that are only available there. However, I can now use alternative
app stores, which allows me to install and use apps like NewPipe. This way, I can enjoy YouTube ad-free and without an account.

For casual use on the couch, a Chromebook has been unbeatable for me so far. It’s affordable, the battery lasts forever, and it wakes up from sleep mode extremely quickly. To break away from Google here as well, I recently bought a cheap used 11-inch MacBook Air (A1465) to install [MX Linux with Fluxbox](https://mxlinux.org/) on it and use it for browsing and watching videos. I haven’t had a chance to test it out yet, but I’m hoping it will be able to replace the Chromebook.

<br/><br/>

---

<br/><br/><span class="anchor" id="deutsch"></span>

## Einleitung

Aus verschiedenen Gründen habe ich beschlossen, so viele Dienste und Abonnements wie möglich aus Nicht-EU-Ländern in die EU zu verlagern oder zu europäischen Dienstanbietern zu wechseln. Gründe hierfür sind die aktuelle weltpolitische Lage und der verbesserte Datenschutz. Auf den ersten Punkt möchte ich aus verschiedenen Gründen nicht näher eingehen, aber der zweite Punkt sollte sofort einleuchten, da die EU derzeit über die nutzerfreundlichsten Gesetze in Sachen Datenschutz verfügt. Im Folgenden werde ich sowohl die alten als auch die neuen Dienstleister auflisten; dies ist keine Werbung, sondern lediglich das Ergebnis meiner Recherchen, die darauf abzielten, die gleiche oder eine bessere Qualität zu erschwinglichen Preisen zu erreichen.

Ich würde diesen Beitrag als Zwischenbericht bezeichnen und werde ihn ergänzen, falls ich noch weitere Dienste umstelle.

## E-Mail

Meiner Meinung nach ist [Fastmail](https://www.fastmail.com/) einer der besten E-Mail-Anbieter. In all den Jahren, in denen ich dort meine E-Mail-Konten hatte, gab es nie Probleme. Ich zahlte 10 Euro im Monat für zwei Konten, konnte eine unbegrenzte Anzahl eigener Domains nutzen und nicht nur Catch-All-Adressen einrichten, sondern auch E-Mails von jeder beliebigen E-Mail-Adresse versenden. Das ist wichtig für [meine E-Mail-Konfiguration](/how-i-do-email). Auch der Kalender ist solide und wurde innerhalb der Familie genutzt. All dies war zudem in einer gut gestalteten Android-App verfügbar.
Eine europäische Alternative zu finden, die all das bietet, erwies sich als schwierig. Zunächst probierte ich [mailbox.org](https://mailbox.org) aus, das ich grundsätzlich uneingeschränkt empfehlen kann. Leider kann man ohne einen Workaround keine E-Mails von einer beliebigen Adresse auf der eigenen Domain versenden, sodass die Suche weiterging. Schließlich bin ich bei [Uberspace](https://uberspace.de) gelandet. Dieser „Pay-what-you-want“-Anbieter bietet ein Shell-Konto, Webhosting, E-Mail-Hosting und mehr zu fairen Preisen. Außerdem kann man beliebig viele eigene Domains sowohl für
das Web als auch für E-Mails nutzen und E-Mails von jeder beliebigen Absenderadresse versenden. Es gibt keine eigene App, weshalb ich nun Thunderbird für Android nutze und damit sehr zufrieden bin.

## Kalender

[Uberspace](https://uberspace.de) bietet keine integrierte Kalenderlösung an. Also habe ich versucht, verschiedene CalDAV-Server zu installieren, aber keiner davon hat mich wirklich überzeugt. Letztendlich habe ich einfach NextCloud auf meinem [Uberspace](https://uberspace.de) Asteroid installiert, das über integrierte CalDAV- und CardDAV-Funktionen verfügt. Auf meinem Desktop nutze ich Thunderbird als Client; auf Android verwende ich DAVx5 und Fossil Calendar. Es funktioniert hervorragend, auch wenn NextCloud einen gewissen Mehraufwand mit sich bringt. Dafür kann ich nun problemlos Dateien mit anderen teilen und theoretisch auch die
Online-Office-Funktionen von NextCloud nutzen.

## Web

Da ich [Uberspace](https://uberspace.de) bereits für meine E-Mails und meinen Kalender nutze, konnte ich diese Website ebenfalls dort hosten. Zuvor hatte ich zu diesem Zweck einen VPS bei Hetzner, den ich nun nicht mehr benötige. Die einzige kleine Hürde bestand darin, dass ich auf dieser Seite SSI verwende, um den Header zentral zu verwalten. Zuvor hatte ich Nginx verwendet, aber [Uberspace](https://uberspace.de) hostet auf Apache, wo die SSI-Implementierung etwas anders gehandhabt wird. Die Anpassung meines HTML-Codes
war jedoch recht einfach, sodass ich die Seite schnell zu [Uberspace](https://uberspace.de) migrieren konnte.

## Domains und DNS

Lange Zeit war ich ein zufriedener Kunde von [Namecheap](https://www.namecheap.com/). Sie bieten gute Preise, eine große Auswahl an verfügbaren Domains, ihre DNS-Verwaltung bietet alles, was man braucht, und ihr Support-Team hat mir mehrfach schnell geholfen. Doch nun war es an der Zeit, nach einem vergleichbaren Anbieter in der EU zu suchen. Letztendlich habe ich mich für [hosting.de](https://hosting.de) entschieden. Einige der Gründe waren die Preise, die Bewertungen, der Standort in Deutschland und die Verfügbarkeit von .is-Domains. Bislang läuft alles reibungslos; der Support hat mir bei einem Problem schnell und kompetent geholfen; und obwohl die Preise für nicht-deutsche Domains etwas höher sind, liegen sie immer noch in einem akzeptablen Rahmen.

## Git

Irgendwann hatte so gut wie jeder seinen Code auf [GitHub](https://github.com) (oder hat ihn immer noch dort). Ich war da keine Ausnahme, obwohl ich auch meine eigene Gitea-Instanz gehostet hatte. Schließlich hatte ich auch davon genug und habe alle meine Git-Repositorys zu codeberg.org migriert. [Codeberg](https://codeberg.org) ist eine in Deutschland ansässige gemeinnützige Organisation, und es ist schwer vorstellbar, mit dieser Wahl etwas falsch zu machen.

## VPN

Hier gibt es keine Änderungen. Ich war schon immer ein zufriedener [Mullvad](https://mullvad.net)-Kunde. Für 5 Euro im Monat bezahle ich ein schwedisches Unternehmen, das bewiesen hat, dass es keine Daten protokolliert und von mir nicht einmal verlangt, ein Konto anzulegen. Keine Abonnementfallen, keine seltsamen Black-Friday-Angebote, keine Rabatte: einfach 5 Euro im Monat für einen zuverlässigen, vertrauenswürdigen Dienst.

## Android, Chromebook und Google

Viele Jahre lang habe ich mein Arbeits-Smartphone auch privat genutzt. Mit dem Pixel 6 war ich mehr als zufrieden, aber verständlicherweise durfte ich kein Custom-ROM installieren oder alternative App-Stores wie F-Droid nutzen. Deshalb habe ich mich entschlossen, ein separates Smartphone für den privaten Gebrauch zu kaufen. Ich habe mich für das Pixel 9a entschieden, das von [Graphene OS](https://grapheneos.org/) unterstützt wird. Ich habe trotzdem den Google Play Store installiert, damit ich eine ganze Reihe von Apps installieren kann, die nur dort erhältlich sind. Allerdings kann ich nun auch alternative
App-Stores nutzen, wodurch ich Apps wie NewPipe installieren und verwenden kann. So kann ich YouTube werbefrei und ohne Konto genießen.

Für den gelegentlichen Gebrauch auf der Couch ist ein Chromebook für mich bisher unschlagbar. Es ist erschwinglich, der Akku hält ewig und es erwacht extrem schnell aus dem Ruhemodus. Um mich auch hier von Google zu lösen, habe ich mir kürzlich ein günstiges gebrauchtes 11-Zoll-MacBook Air (A1465) gekauft, um darauf [MX Linux mit Fluxbox](https://mxlinux.org/) zu installieren und es zum Surfen und zum Anschauen von Videos zu nutzen. Ich hatte noch keine Gelegenheit, es auszuprobieren, aber ich hoffe, dass es das Chromebook ersetzen kann.
