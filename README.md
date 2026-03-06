# Linux, Networking & Cybersecurity Labs

This repository contains hands-on labs demonstrating my learning journey in:

• Linux Administration  
• Networking Fundamentals  
• Cybersecurity Concepts  
• Python Automation  
• Cloud Infrastructure Foundations  

These labs are part of my transition into **Cloud Engineering and Cybersecurity**.

---

# Lab Portfolio

## Lab 1 – Network Connectivity

Commands used:

ping google.com  
traceroute google.com  
netstat -tulnp  
ss -tulnp  

Purpose:

Understand network connectivity and packet routing.

---

## Lab 2 – DNS Investigation

Commands used:

dig google.com  
nslookup google.com  

Purpose:

Understand how domain names resolve to IP addresses.

---

## Lab 3 – Linux File System

Commands used:

ls  
pwd  
find  

Purpose:

Understanding file navigation and discovery.

---

## Lab 4 – File Permissions

Commands used:

chmod  
chown  

Purpose:

Learning Linux security permissions and ownership.

---

## Lab 5 – Process Monitoring

Commands used:

ps  
top  
kill  

Purpose:

Understanding system processes and resource management.

---

## Lab 6 – System Monitoring

Commands used:

top  
df -h  
free -h  
ps aux  

Purpose:

Monitoring CPU, memory and disk usage in Linux environments.

---

## Lab 7 – Network Port Scanning

Tool used:

nmap

Purpose:

Identify open network ports and understand network reconnaissance.

---

## Lab 8 – Python Log Analyzer

Python script used to analyze Linux system logs.

Purpose:

Combine Python automation with Linux administration tasks.

---

## Previous Data Center Lab

Teraco Data Centre related learning and exercises.

---

# Technologies Used

Linux  
Python  
Networking Tools  
Git & GitHub  
Cybersecurity Fundamentals  

---

# Author

Tumelo Ngoma

Technical Project Manager | Logical Analyst  
Cybersecurity & Cloud Engineering Journey

GitHub:# Linux, Networking & Cybersecurity Labs

This repository contains hands-on labs demonstrating my learning journey in:

• Linux Administration  
• Networking Fundamentals  
• Cybersecurity Concepts  
• Python Automation  
• Cloud Infrastructure Foundations  

These labs are part of my transition into **Cloud Engineering and Cybersecurity**.

---

# Lab Portfolio

## Lab 1 – Network Connectivity

Commands used:

ping google.com  
traceroute google.com  
netstat -tulnp  
ss -tulnp  

Purpose:

Understand network connectivity and packet routing.

---

## Lab 2 – DNS Investigation

Commands used:

dig google.com  
nslookup google.com  

Purpose:

Understand how domain names resolve to IP addresses.

---

## Lab 3 – Linux File System

Commands used:

ls  
pwd  
find  

Purpose:

Understanding file navigation and discovery.

---

## Lab 4 – File Permissions

Commands used:

chmod  
chown  

Purpose:

Learning Linux security permissions and ownership.

---

## Lab 5 – Process Monitoring

Commands used:

ps  
top  
kill  

Purpose:

Understanding system processes and resource management.

---

## Lab 6 – System Monitoring

Commands used:

top  
df -h  
free -h  
ps aux  

Purpose:

Monitoring CPU, memory and disk usage in Linux environments.

---

## Lab 7 – Network Port Scanning

Tool used:

nmap

Purpose:

Identify open network ports and understand network reconnaissance.

---

## Lab 8 – Python Log Analyzer

Python script used to analyze Linux system logs.

Purpose:

Combine Python automation with Linux administration tasks.

---

## Previous Data Center Lab

Teraco Data Centre related learning and exercises.

---

# Technologies Used

Linux  
Python  
Networking Tools  
Git & GitHub  
Cybersecurity Fundamentals  

---

# Author

Tumelo Ngoma

Technical Project Manager | Logical Analyst  
Cybersecurity & Cloud Engineering Journey

GitHub:
https://github.com/Tumelo-max
https://github.com/Tumelo-max# Linux & Networking Labs Portfolio

Linux & Networking Lab Summary
========================================

Contents of ../lab1:

--- ping_results.txt ---
PING google.com (142.251.216.14) 56(84) bytes of data.
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=1 ttl=117 time=7.67 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=2 ttl=117 time=8.16 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=3 ttl=117 time=7.42 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=4 ttl=117 time=7.29 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3285ms
rtt min/avg/max/mdev = 7.288/7.633/8.160/0.332 ms

--- ss_results.txt ---
Netid State  Recv-Q Send-Q  Local Address:Port Peer Address:PortProcess                                   
udp   UNCONN 0      0           127.0.0.1:323       0.0.0.0:*                                             
udp   UNCONN 0      0          127.0.0.54:53        0.0.0.0:*    users:(("systemd-resolve",pid=104,fd=16))
udp   UNCONN 0      0       127.0.0.53%lo:53        0.0.0.0:*    users:(("systemd-resolve",pid=104,fd=14))
udp   UNCONN 0      0      10.255.255.254:53        0.0.0.0:*                                             
udp   UNCONN 0      0               [::1]:323          [::]:*                                             
tcp   LISTEN 0      4096       127.0.0.54:53        0.0.0.0:*    users:(("systemd-resolve",pid=104,fd=17))
tcp   LISTEN 0      1000   10.255.255.254:53        0.0.0.0:*                                             
tcp   LISTEN 0      4096    127.0.0.53%lo:53        0.0.0.0:*    users:(("systemd-resolve",pid=104,fd=15))

--- traceroute_results.txt ---
traceroute to google.com (142.251.47.174), 30 hops max, 60 byte packets
 1  LuNgoma.mshome.net (172.18.160.1)  0.444 ms  1.019 ms  0.572 ms
 2  localhost (10.0.0.2)  424.339 ms  424.291 ms  424.282 ms
 3  wwg-ip-bng-2.south.dsl.telkomsa.net (105.228.20.1)  424.404 ms  427.844 ms  427.822 ms
 4  105-187-235-230.telkomsa.net (105.187.235.230)  427.470 ms  427.369 ms  427.357 ms
 5  105-187-235-94.telkomsa.net (105.187.235.94)  424.190 ms  424.177 ms  424.156 ms
 6  142.251.53.107 (142.251.53.107)  423.718 ms  419.055 ms  419.039 ms
 7  192.178.73.129 (192.178.73.129)  419.212 ms 192.178.73.127 (192.178.73.127)  88.040 ms  87.994 ms
 8  jnb03s10-in-f14.1e100.net (142.251.47.174)  88.011 ms  87.991 ms  246.714 ms

--- netstat_results.txt ---
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN      104/systemd-resolve 
tcp        0      0 10.255.255.254:53       0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      104/systemd-resolve 
udp        0      0 127.0.0.1:323           0.0.0.0:*                           -                   
udp        0      0 127.0.0.54:53           0.0.0.0:*                           104/systemd-resolve 
udp        0      0 127.0.0.53:53           0.0.0.0:*                           104/systemd-resolve 
udp        0      0 10.255.255.254:53       0.0.0.0:*                           -                   
udp6       0      0 ::1:323                 :::*                                -                   

----------------------------------------

Contents of ../lab2:

--- ping_results.txt ---
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=34.3 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=8.07 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=118 time=8.81 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=118 time=8.12 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3198ms
rtt min/avg/max/mdev = 8.071/14.826/34.303/11.248 ms

--- traceroute_results.txt ---
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  LuNgoma.mshome.net (172.18.160.1)  0.682 ms  9.461 ms  9.424 ms
 2  localhost (10.0.0.2)  15.804 ms  15.795 ms  15.773 ms
 3  wwg-ip-bng-2.south.dsl.telkomsa.net (105.228.20.1)  17.495 ms  17.482 ms  17.436 ms
 4  105-187-235-230.telkomsa.net (105.187.235.230)  18.378 ms  21.364 ms  18.354 ms
 5  105-187-235-94.telkomsa.net (105.187.235.94)  18.343 ms  21.242 ms  21.118 ms
 6  142.251.53.107 (142.251.53.107)  21.114 ms 209.85.247.39 (209.85.247.39)  12.103 ms  11.362 ms
 7  192.178.73.129 (192.178.73.129)  11.294 ms 192.178.73.217 (192.178.73.217)  10.890 ms 192.178.74.201 (192.178.74.201)  13.088 ms
 8  dns.google (8.8.8.8)  10.858 ms  10.042 ms  8.218 ms

--- dig_results.txt ---

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 34911
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		155	IN	A	142.251.47.174

;; Query time: 15 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Thu Mar 05 16:30:49 SAST 2026
;; MSG SIZE  rcvd: 55


--- netstat_results.txt ---
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN      104/systemd-resolve 
tcp        0      0 10.255.255.254:53       0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      104/systemd-resolve 
udp        0      0 127.0.0.1:323           0.0.0.0:*                           -                   
udp        0      0 127.0.0.54:53           0.0.0.0:*                           104/systemd-resolve 
udp        0      0 127.0.0.53:53           0.0.0.0:*                           104/systemd-resolve 
udp        0      0 10.255.255.254:53       0.0.0.0:*                           -                   
udp6       0      0 ::1:323                 :::*                                -                   

--- whois_results.txt ---
   Domain Name: GOOGLE.COM
   Registry Domain ID: 2138514_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.markmonitor.com
   Registrar URL: http://www.markmonitor.com
   Updated Date: 2019-09-09T15:39:04Z
   Creation Date: 1997-09-15T04:00:00Z
   Registry Expiry Date: 2028-09-14T04:00:00Z
   Registrar: MarkMonitor Inc.
   Registrar IANA ID: 292
   Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
   Registrar Abuse Contact Phone: +1.2086851750
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Domain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited
   Domain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited
   Domain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited
   Name Server: NS1.GOOGLE.COM
   Name Server: NS2.GOOGLE.COM
   Name Server: NS3.GOOGLE.COM
   Name Server: NS4.GOOGLE.COM
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2026-03-05T14:32:10Z <<<

For more information on Whois status codes, please visit https://icann.org/epp

NOTICE: The expiration date displayed in this record is the date the
registrar's sponsorship of the domain name registration in the registry is
currently set to expire. This date does not necessarily reflect the expiration
date of the domain name registrant's agreement with the sponsoring
registrar.  Users may consult the sponsoring registrar's Whois database to
view the registrar's reported date of expiration for this registration.

TERMS OF USE: You are not authorized to access or query our Whois
database through the use of electronic processes that are high-volume and
automated except as reasonably necessary to register domain names or
modify existing registrations; the Data in VeriSign Global Registry
Services' ("VeriSign") Whois database is provided by VeriSign for
information purposes only, and to assist persons in obtaining information
about or related to a domain name registration record. VeriSign does not
guarantee its accuracy. By submitting a Whois query, you agree to abide
by the following terms of use: You agree that you may use this Data only
for lawful purposes and that under no circumstances will you use this Data
to: (1) allow, enable, or otherwise support the transmission of mass
unsolicited, commercial advertising or solicitations via e-mail, telephone,
or facsimile; or (2) enable high volume, automated, electronic processes
that apply to VeriSign (or its computer systems). The compilation,
repackaging, dissemination or other use of this Data is expressly
prohibited without the prior written consent of VeriSign. You agree not to
use electronic processes that are automated and high-volume to access or
query the Whois database except as reasonably necessary to register
domain names or modify existing registrations. VeriSign reserves the right
to restrict your access to the Whois database in its sole discretion to ensure
operational stability.  VeriSign may restrict or terminate your access to the
Whois database for failure to abide by these terms of use. VeriSign
reserves the right to modify these terms at any time.

The Registry database contains ONLY .COM, .NET, .EDU domains and
Registrars.
Domain Name: google.com
Registry Domain ID: 2138514_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.markmonitor.com
Registrar URL: http://www.markmonitor.com
Updated Date: 2024-08-02T02:17:33+0000
Creation Date: 1997-09-15T07:00:00+0000
Registrar Registration Expiration Date: 2028-09-13T07:00:00+0000
Registrar: MarkMonitor, Inc.
Registrar IANA ID: 292
Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
Registrar Abuse Contact Phone: +1.2086851750
Domain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)
Domain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)
Domain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)
Domain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)
Domain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)
Domain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)
Registrant Organization: Google LLC
Registrant Country: US
Registrant Email: Select Request Email Form at https://domains.markmonitor.com/whois/google.com
Tech Email: Select Request Email Form at https://domains.markmonitor.com/whois/google.com
Name Server: ns1.google.com
Name Server: ns4.google.com
Name Server: ns3.google.com
Name Server: ns2.google.com
DNSSEC: unsigned
URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/
>>> Last update of WHOIS database: 2026-03-05T14:30:31+0000 <<<

For more information on WHOIS status codes, please visit:
  https://www.icann.org/resources/pages/epp-status-codes

If you wish to contact this domain’s Registrant or Technical
contact, and such email address is not visible above, you may do so via our web
form, pursuant to ICANN’s Temporary Specification. To verify that you are not a
robot, please enter your email address to receive a link to a page that
facilitates email communication with the relevant contact(s).

Web-based WHOIS:
  https://domains.markmonitor.com/whois/contact/google.com

If you have a legitimate interest in viewing the non-public WHOIS details, send
your request and the reasons for your request to whoisrequest@markmonitor.com
and specify the domain name in the subject line. We will review that request and
may ask for supporting documentation and explanation.

The data in MarkMonitor’s WHOIS database is provided for information purposes,
and to assist persons in obtaining information about or related to a domain
name’s registration record. While MarkMonitor believes the data to be accurate,
the data is provided "as is" with no guarantee or warranties regarding its
accuracy.

By submitting a WHOIS query, you agree that you will use this data only for
lawful purposes and that, under no circumstances will you use this data to:
  (1) allow, enable, or otherwise support the transmission by email, telephone,
or facsimile of mass, unsolicited, commercial advertising, or spam; or
  (2) enable high volume, automated, or electronic processes that send queries,
data, or email to MarkMonitor (or its systems) or the domain name contacts (or
its systems).

MarkMonitor reserves the right to modify these terms at any time.

By submitting this query, you agree to abide by this policy.

MarkMonitor Domain Management(TM)
Protecting companies and consumers in a digital world.

Visit MarkMonitor at https://www.markmonitor.com
Contact us at +1.8007459229
In Europe, at +44.02032062220
--

--- top_results.txt ---
top - 16:33:45 up  5:38,  1 user,  load average: 0.00, 0.00, 0.00
Tasks:  26 total,   1 running,  25 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  1.3 sy,  0.0 ni, 98.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
MiB Mem :   3737.2 total,   3090.8 free,    412.5 used,    325.6 buff/cache     
MiB Swap:   1024.0 total,   1024.0 free,      0.0 used.   3324.7 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
      1 root      20   0   21832  12488   9416 S   0.0   0.3   0:02.86 systemd
      2 root      20   0    3120   2048   1920 S   0.0   0.1   0:00.04 init-sy+
      6 root      20   0    3136   1892   1792 S   0.0   0.0   0:00.00 init
     42 root      19  -1   50428  16000  15104 S   0.0   0.4   0:02.65 systemd+
     88 root      20   0   25144   6272   4992 S   0.0   0.2   0:03.60 systemd+
    104 systemd+  20   0   21460  13056  10880 S   0.0   0.3   0:00.52 systemd+
    105 systemd+  20   0   91028   7808   6912 S   0.0   0.2   0:00.79 systemd+
    154 root      20   0    4236   2560   2432 S   0.0   0.1   0:00.09 cron
    155 message+  20   0    9804   5120   4352 S   0.0   0.1   0:00.73 dbus-da+
    162 root      20   0   17964   8448   7552 S   0.0   0.2   0:00.54 systemd+
    170 root      20   0    3160   2048   1920 S   0.0   0.1   0:00.02 agetty
    190 root      20   0    3116   1920   1792 S   0.0   0.1   0:00.01 agetty
    191 root      20   0  107012  22272  13184 S   0.0   0.6   0:00.27 unatten+
    268 root      20   0    3124    768    768 S   0.0   0.0   0:00.00 Session+
    282 root      20   0    3140   1152   1024 S   0.0   0.0   0:00.48 Relay(2+
    283 tumelo    20   0    6184   5256   3584 S   0.0   0.1   0:00.86 bash
    451 root      20   0    6692   4736   3968 S   0.0   0.1   0:00.02 login
    497 tumelo    20   0   20312  11264   9216 S   0.0   0.3   0:00.29 systemd
    498 tumelo    20   0   21152   3516   1792 S   0.0   0.1   0:00.00 (sd-pam)
    527 tumelo    20   0    6056   5120   3584 S   0.0   0.1   0:00.03 bash
    879 polkitd   20   0  308164   7680   6912 S   0.0   0.2   0:00.48 polkitd
   1337 syslog    20   0  222508   5376   4608 S   0.0   0.1   0:00.30 rsyslogd
   3072 tumelo    20   0    9424   4992   4608 S   0.0   0.1   0:00.06 dbus-da+
   3986 root      20   0 1830608  13056  11008 S   0.0   0.3   0:00.21 wsl-pro+
   4534 root      20   0  370096  20096  17280 S   0.0   0.5   0:00.07 package+
   4552 tumelo    20   0    9284   5248   3200 R   0.0   0.1   0:00.02 top

--- ps_results.txt ---
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.3  21832 12488 ?        Ss   13:18   0:02 /sbin/init
root           2  0.0  0.0   3120  2048 ?        Sl   13:18   0:00 /init
root           6  0.0  0.0   3136  1892 ?        Sl   13:18   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
root          42  0.0  0.4  50428 16000 ?        S<s  13:18   0:02 /usr/lib/systemd/systemd-journald
root          88  0.0  0.1  25144  6272 ?        Ss   13:18   0:03 /usr/lib/systemd/systemd-udevd
systemd+     104  0.0  0.3  21460 13056 ?        Ss   13:18   0:00 /usr/lib/systemd/systemd-resolved
systemd+     105  0.0  0.2  91028  7808 ?        Ssl  13:18   0:00 /usr/lib/systemd/systemd-timesyncd
root         154  0.0  0.0   4236  2560 ?        Ss   13:18   0:00 /usr/sbin/cron -f -P
message+     155  0.0  0.1   9804  5120 ?        Ss   13:18   0:00 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         162  0.0  0.2  17964  8448 ?        Ss   13:18   0:00 /usr/lib/systemd/systemd-logind
root         170  0.0  0.0   3160  2048 hvc0     Ss+  13:18   0:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 115200,38400,9600 vt220
root         190  0.0  0.0   3116  1920 tty1     Ss+  13:18   0:00 /sbin/agetty -o -p -- \u --noclear - linux
root         191  0.0  0.5 107012 22272 ?        Ssl  13:18   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         268  0.0  0.0   3124   768 ?        Ss   13:18   0:00 /init
root         282  0.0  0.0   3140  1152 ?        S    13:18   0:00 /init
tumelo       283  0.0  0.1   6184  5256 pts/0    Ss   13:18   0:00 -bash
root         451  0.0  0.1   6692  4736 pts/1    Ss   13:30   0:00 /bin/login -f
tumelo       497  0.0  0.2  20312 11264 ?        Ss   13:30   0:00 /usr/lib/systemd/systemd --user
tumelo       498  0.0  0.0  21152  3516 ?        S    13:30   0:00 (sd-pam)
tumelo       527  0.0  0.1   6056  5120 pts/1    S+   13:30   0:00 -bash
polkitd      879  0.0  0.2 308164  7680 ?        Ssl  13:33   0:00 /usr/lib/polkit-1/polkitd --no-debug
syslog      1337  0.0  0.1 222508  5376 ?        Ssl  13:34   0:00 /usr/sbin/rsyslogd -n -iNONE
tumelo      3072  0.0  0.1   9424  4992 ?        Ss   14:12   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root        3986  0.0  0.3 1830608 13056 ?       Ssl  16:25   0:00 /usr/libexec/wsl-pro-service
root        4534  0.0  0.5 370096 20096 ?        Ssl  16:32   0:00 /usr/libexec/packagekitd
tumelo      4553  0.0  0.1   8280  4224 pts/0    R+   16:34   0:00 ps aux

----------------------------------------


## Lab 2 Outputs
==============================

--- ss_results.txt ---
Netid State  Recv-Q Send-Q  Local Address:Port Peer Address:PortProcess
udp   UNCONN 0      0           127.0.0.1:323       0.0.0.0:*          
udp   UNCONN 0      0          127.0.0.54:53        0.0.0.0:*          
udp   UNCONN 0      0       127.0.0.53%lo:53        0.0.0.0:*          
udp   UNCONN 0      0      10.255.255.254:53        0.0.0.0:*          
udp   UNCONN 0      0               [::1]:323          [::]:*          
tcp   LISTEN 0      4096       127.0.0.54:53        0.0.0.0:*          
tcp   LISTEN 0      1000   10.255.255.254:53        0.0.0.0:*          
tcp   LISTEN 0      4096    127.0.0.53%lo:53        0.0.0.0:*          

--- netstat_results.txt ---
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 10.255.255.254:53       0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
udp        0      0 127.0.0.1:323           0.0.0.0:*                           -                   
udp        0      0 127.0.0.54:53           0.0.0.0:*                           -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.255.255.254:53       0.0.0.0:*                           -                   
udp6       0      0 ::1:323                 :::*                                -                   

--- traceroute_google_results.txt ---
traceroute to google.com (142.251.216.14), 30 hops max, 60 byte packets
 1  LuNgoma.mshome.net (172.18.160.1)  0.485 ms  0.446 ms  0.292 ms
 2  localhost (10.0.0.2)  2.811 ms  2.740 ms  2.682 ms
 3  wwg-ip-bng-2.south.dsl.telkomsa.net (105.228.20.1)  6.472 ms  6.444 ms  6.101 ms
 4  105-187-235-230.telkomsa.net (105.187.235.230)  10.335 ms  10.328 ms  10.040 ms
 5  105-187-235-94.telkomsa.net (105.187.235.94)  9.897 ms  9.807 ms  7.828 ms
 6  142.251.53.107 (142.251.53.107)  9.012 ms  8.748 ms 192.178.97.57 (192.178.97.57)  8.100 ms
 7  192.178.73.133 (192.178.73.133)  9.622 ms 192.178.73.131 (192.178.73.131)  9.619 ms  9.535 ms
 8  lcjnbi-af-in-f14.1e100.net (142.251.216.14)  7.997 ms  7.904 ms  8.424 ms

--- ping_google_results.txt ---
PING google.com (142.251.216.14) 56(84) bytes of data.
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=1 ttl=117 time=89.6 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=2 ttl=117 time=17.9 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=3 ttl=117 time=8.88 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=4 ttl=117 time=8.12 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3166ms
rtt min/avg/max/mdev = 8.121/31.133/89.647/34.000 ms

## Lab 2 Outputs
==============================

--- ss_results.txt ---
Netid State  Recv-Q Send-Q  Local Address:Port Peer Address:PortProcess
udp   UNCONN 0      0           127.0.0.1:323       0.0.0.0:*          
udp   UNCONN 0      0          127.0.0.54:53        0.0.0.0:*          
udp   UNCONN 0      0       127.0.0.53%lo:53        0.0.0.0:*          
udp   UNCONN 0      0      10.255.255.254:53        0.0.0.0:*          
udp   UNCONN 0      0               [::1]:323          [::]:*          
tcp   LISTEN 0      4096       127.0.0.54:53        0.0.0.0:*          
tcp   LISTEN 0      1000   10.255.255.254:53        0.0.0.0:*          
tcp   LISTEN 0      4096    127.0.0.53%lo:53        0.0.0.0:*          

--- netstat_results.txt ---
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 10.255.255.254:53       0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
udp        0      0 127.0.0.1:323           0.0.0.0:*                           -                   
udp        0      0 127.0.0.54:53           0.0.0.0:*                           -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.255.255.254:53       0.0.0.0:*                           -                   
udp6       0      0 ::1:323                 :::*                                -                   

--- traceroute_google_results.txt ---
traceroute to google.com (142.251.216.14), 30 hops max, 60 byte packets
 1  LuNgoma.mshome.net (172.18.160.1)  0.485 ms  0.446 ms  0.292 ms
 2  localhost (10.0.0.2)  2.811 ms  2.740 ms  2.682 ms
 3  wwg-ip-bng-2.south.dsl.telkomsa.net (105.228.20.1)  6.472 ms  6.444 ms  6.101 ms
 4  105-187-235-230.telkomsa.net (105.187.235.230)  10.335 ms  10.328 ms  10.040 ms
 5  105-187-235-94.telkomsa.net (105.187.235.94)  9.897 ms  9.807 ms  7.828 ms
 6  142.251.53.107 (142.251.53.107)  9.012 ms  8.748 ms 192.178.97.57 (192.178.97.57)  8.100 ms
 7  192.178.73.133 (192.178.73.133)  9.622 ms 192.178.73.131 (192.178.73.131)  9.619 ms  9.535 ms
 8  lcjnbi-af-in-f14.1e100.net (142.251.216.14)  7.997 ms  7.904 ms  8.424 ms

--- ping_google_results.txt ---
PING google.com (142.251.216.14) 56(84) bytes of data.
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=1 ttl=117 time=89.6 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=2 ttl=117 time=17.9 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=3 ttl=117 time=8.88 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=4 ttl=117 time=8.12 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3166ms
rtt min/avg/max/mdev = 8.121/31.133/89.647/34.000 ms
