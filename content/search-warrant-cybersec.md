---
title: How a Search Warrant sparked my Interest in Cybersecurity
date: 2026-02-13
---

As I [described in a previous post](/three-events-career), I started my IT career first as a software developer and then as a system administrator. In 2004, I had already been using computers privately for 15 years, but I was still relatively inexperienced professionally. I would not have progressed in my job as a system and database administrator if I had not also been involved with it privately. At that time, it was already relatively affordable to rent virtual private servers, which I did in order to host a small private website. Back then, it was still significantly more expensive, especially the traffic. While nowadays you get several TB of inclusive traffic, back then 1 GB of traffic cost 99 cents. As I said, the server only ran Apache and a MySQL database, but otherwise nothing out of the ordinary.

## The EMail {#the-email}

In February 2005, I received an email from my VPS provider, who had kindly shut down my server after it suddenly generated 90GB of traffic. He informed me that my Apache had loaded a vulnerable module, which was being used to carry out DoS attacks and also as a proxy. In fact, my server's IP address was listed on public proxy lists. This meant that bascially anyone could carry out illegal activities using my IP address. You can well imagine how uncomfortable I felt about this. On the one hand, I had to pay a rather hefty bill for the traffic I had caused, and on the other, I had to live with the fear that I might get into legal trouble. Fortunately, my provider was accommodating and "only" charged me 49 Cent per GB for this incident.

## The Move {#the-move}

By autumn 2005, the incident had already been forgotten. A lot had happened in my life and my wife (then still my girlfriend) and I had found a flat together. This flat was only a few streets away from my previous flat. Then the day of the move and the handover of the flat arrived. On that day, I drove to my old flat once more, where I removed my name tag from the letterbox and sealed it with tape.

## The Phone Call {#the-phone-call}

Just a few days later, I was abruptly woken up in our new appartment when my mobile phone rang at around 05:30. As a database administrator, I was used to being woken up by phone calls, but this time something was different: the number was withheld. I had a bad feeling, but luckily I answered it anyway. What happened next overwhelmed my still half-asleep brain: Apparently, the criminal investigation department was standing in front of the building where my old flat was and had a search warrant. They were very unhappy that the alleged criminal had apparently fled. I told them that I had moved and wanted to know what they wanted from me. In return, they wanted to know where I now lived. Neither side wanted to reveal their cards, and a somewhat unpleasant back-and-forth ensued which made them quite angry.

Fortunately, it then occurred to me that a search warrant applies to an address rather than a person. The detectives obviously did not know my address, and even if they did, they would first have to wake up a judge to obtain a new warrant. Since this was only a matter of time, I only had the upper hand for a short while and had to make use of it. So I offered to meet them on neutral ground. But only if they would tell me what it was about. The only answer I got was that it was "an IT matter". Unfortunately, that didn't really help me, but it was something to work with. Grinding their teeth, the officers then agreed to meet me at a local police station. They asked me to bring my PC with me.

Now, it's not that I really had a guilty conscience, but I had often read that when the police have a search warrant, they like to take everything related to IT: computers, laptops, CDs, hard drives - everything. All these things are then neatly numbered, archived somewhere and can be locked away for a few years until you get them back. I didn't have the money for new hardware. Fortunately, I still had an unused, second-hand Thinkpad R30 and a Debian installation CD lying around.

## The Meeting {#the-meeting}

While getting dressed and brushing my teeth, I was able to boot the CD, format the hard drive and start the Linux installation. On the way to the police station, I had the laptop on the passenger seat and was just able to finish the installation and shut down the laptop.

Armed with fear, adrenaline and the laptop, I entered the police station and encountered three very suspicious and not particularly happy detectives. They made me sit on a chair in a corner while they stood in front of me. I gave them my laptop and my ID, and they began to explain what it was all about: eBay fraud. They must have noticed my relief immediately, because the mood changed instantly.

Since I am obviously not an eBay fraudster, I knew that although I was being accused, I was not the guilty party. Relieved but curious, I listened to the rest of the story: A fraudster had created an account with a German email provider and used my hacked web server as a proxy. He then registered with eBay using this email address and provided the postal address of a member of the German Bundestag. He then used this eBay account to carry out his fraudulent activities until one of his victims
reported him to the police. During the investigation, the police obtained the address of the member of parliament from eBay and took action against him. However, he was very unhappy about this, which in turn made the police unhappy. Further investigations then led to the police first obtaining the email address of the fraudster and then the IP address used to create the email address. The IP address led them to my VPS provider, who then gave the officials my private address. Without checking
this further, they obtained a search warrant and then tried to pay me a visit.

## The Aftermath {#the-aftermath}

I was able to explain plausibly that I was not the fraudster they were looking for, and why. After my personal details had been taken, we agreed on the following: they would believe me, but charges would still be pressed. I was to fax them the email correspondence with my provider as proof and appear at the criminal investigation department the next day so that I could sign a nice long statement.

With my laptop under my arm and feeling quite emotional, I drove to work. There, I printed out the entire email correspondence with my provider and faxed it to the criminal investigation department.

The next day, I went to a meeting with them, signed some papers and was able to talk to the officers on a completely different level. They assured me that they believed me and that the charges would be dropped. A few weeks later, I actually received a letter from the public prosecutor's office apologising for the inconvenience and informing me that the charges had been dropped.

## The Impact {#the-impact}

Since this incident, the way I think and act as a system administrator has changed significantly. I no longer just think about how to get things to work, but also whether this could be exploited by an attacker. The fact that systems or applications can be successfully attacked and vulnerabilities exploited was no longer a grey theory for me, but a tangible reality. I became increasingly interested in cybersecurity, but couldn't do anything with it in my job at the time. As you can see from the post linked above, a happy accident occurred, which suddenly turned me into a cybersecurity consultant and allowed me to continue my career there.
