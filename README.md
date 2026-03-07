# Linux & Networking Labs Portfolio

This README summarizes all my Linux, Networking, and Teraco labs.

==================================================

## LAB1

### netstat_results.txt
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

### ping_results.txt
PING google.com (142.251.216.14) 56(84) bytes of data.
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=1 ttl=117 time=7.67 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=2 ttl=117 time=8.16 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=3 ttl=117 time=7.42 ms
64 bytes from lcjnbi-af-in-f14.1e100.net (142.251.216.14): icmp_seq=4 ttl=117 time=7.29 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3285ms
rtt min/avg/max/mdev = 7.288/7.633/8.160/0.332 ms

### ss_results.txt
Netid State  Recv-Q Send-Q  Local Address:Port Peer Address:PortProcess                                   
udp   UNCONN 0      0           127.0.0.1:323       0.0.0.0:*                                             
udp   UNCONN 0      0          127.0.0.54:53        0.0.0.0:*    users:(("systemd-resolve",pid=104,fd=16))
udp   UNCONN 0      0       127.0.0.53%lo:53        0.0.0.0:*    users:(("systemd-resolve",pid=104,fd=14))
udp   UNCONN 0      0      10.255.255.254:53        0.0.0.0:*                                             
udp   UNCONN 0      0               [::1]:323          [::]:*                                             
tcp   LISTEN 0      4096       127.0.0.54:53        0.0.0.0:*    users:(("systemd-resolve",pid=104,fd=17))
tcp   LISTEN 0      1000   10.255.255.254:53        0.0.0.0:*                                             
tcp   LISTEN 0      4096    127.0.0.53%lo:53        0.0.0.0:*    users:(("systemd-resolve",pid=104,fd=15))

### traceroute_results.txt
traceroute to google.com (142.251.47.174), 30 hops max, 60 byte packets
 1  LuNgoma.mshome.net (172.18.160.1)  0.444 ms  1.019 ms  0.572 ms
 2  localhost (10.0.0.2)  424.339 ms  424.291 ms  424.282 ms
 3  wwg-ip-bng-2.south.dsl.telkomsa.net (105.228.20.1)  424.404 ms  427.844 ms  427.822 ms
 4  105-187-235-230.telkomsa.net (105.187.235.230)  427.470 ms  427.369 ms  427.357 ms
 5  105-187-235-94.telkomsa.net (105.187.235.94)  424.190 ms  424.177 ms  424.156 ms
 6  142.251.53.107 (142.251.53.107)  423.718 ms  419.055 ms  419.039 ms
 7  192.178.73.129 (192.178.73.129)  419.212 ms 192.178.73.127 (192.178.73.127)  88.040 ms  87.994 ms
 8  jnb03s10-in-f14.1e100.net (142.251.47.174)  88.011 ms  87.991 ms  246.714 ms

---

## LAB2

### dig_results.txt

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


### netstat_results.txt
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

### ping_results.txt
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=34.3 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=8.07 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=118 time=8.81 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=118 time=8.12 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3198ms
rtt min/avg/max/mdev = 8.071/14.826/34.303/11.248 ms

### ps_results.txt
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

### top_results.txt
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

### traceroute_results.txt
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  LuNgoma.mshome.net (172.18.160.1)  0.682 ms  9.461 ms  9.424 ms
 2  localhost (10.0.0.2)  15.804 ms  15.795 ms  15.773 ms
 3  wwg-ip-bng-2.south.dsl.telkomsa.net (105.228.20.1)  17.495 ms  17.482 ms  17.436 ms
 4  105-187-235-230.telkomsa.net (105.187.235.230)  18.378 ms  21.364 ms  18.354 ms
 5  105-187-235-94.telkomsa.net (105.187.235.94)  18.343 ms  21.242 ms  21.118 ms
 6  142.251.53.107 (142.251.53.107)  21.114 ms 209.85.247.39 (209.85.247.39)  12.103 ms  11.362 ms
 7  192.178.73.129 (192.178.73.129)  11.294 ms 192.178.73.217 (192.178.73.217)  10.890 ms 192.178.74.201 (192.178.74.201)  13.088 ms
 8  dns.google (8.8.8.8)  10.858 ms  10.042 ms  8.218 ms

### whois_results.txt
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

---

## LAB3

### find_results.txt
./testfile.txt
./find_results.txt
./ls_results.txt
./newfile.txt

### ls_results.txt
total 4
-rw-r--r-- 1 tumelo tumelo 50 Mar  5 17:57 find_results.txt
-rw-r--r-- 1 tumelo tumelo  0 Mar  5 18:00 ls_results.txt
-rw-r--r-- 1 tumelo tumelo  0 Mar  5 17:57 newfile.txt
total 8
-rw-r--r-- 1 tumelo tumelo  50 Mar  5 17:57 find_results.txt
-rw-r--r-- 1 tumelo tumelo 181 Mar  5 18:00 ls_results.txt
-rw-r--r-- 1 tumelo tumelo   0 Mar  5 17:57 newfile.txt
-rw-r--r-- 1 tumelo tumelo   0 Mar  5 18:00 testfile.txt
total 8
-rw-r--r-- 1 tumelo tumelo  50 Mar  5 17:57 find_results.txt
-rw-r--r-- 1 tumelo tumelo 422 Mar  5 18:00 ls_results.txt
-rw-r--r-- 1 tumelo tumelo   0 Mar  5 18:00 newfile.txt
-rw-r--r-- 1 tumelo tumelo   0 Mar  5 18:00 testfile.txt

### newfile.txt

### testfile.txt

---

## LAB4

### disk_usage.txt
Filesystem      Size  Used Avail Use% Mounted on
none            1.9G     0  1.9G   0% /usr/lib/modules/6.6.87.2-microsoft-standard-WSL2
none            1.9G  4.0K  1.9G   1% /mnt/wsl
drivers         476G  162G  314G  35% /usr/lib/wsl/drivers
/dev/sdd       1007G  2.2G  954G   1% /
none            1.9G  112K  1.9G   1% /mnt/wslg
none            1.9G     0  1.9G   0% /usr/lib/wsl/lib
rootfs          1.9G  2.7M  1.9G   1% /init
none            1.9G  528K  1.9G   1% /run
none            1.9G     0  1.9G   0% /run/lock
none            1.9G     0  1.9G   0% /run/shm
C:\             476G  162G  314G  35% /mnt/c
none            1.9G   76K  1.9G   1% /mnt/wslg/versions.txt
none            1.9G   76K  1.9G   1% /mnt/wslg/doc
tmpfs           374M   20K  374M   1% /run/user/1000

### memory_usage.txt
               total        used        free      shared  buff/cache   available
Mem:           3.6Gi       409Mi       3.1Gi       3.5Mi       219Mi       3.2Gi
Swap:          1.0Gi          0B       1.0Gi

### ps_results.txt
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.3  21832 12488 ?        Ss   13:29   0:04 /sbin/init
root           2  0.0  0.0   3120  2048 ?        Sl   13:29   0:00 /init
root           6  0.0  0.0   3136  1892 ?        Sl   13:29   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
root          42  0.0  0.4  50428 16128 ?        S<s  13:29   0:05 /usr/lib/systemd/systemd-journald
root          88  0.0  0.1  25144  6272 ?        Ss   13:29   0:07 /usr/lib/systemd/systemd-udevd
systemd+     104  0.0  0.3  21460 13056 ?        Ss   13:29   0:01 /usr/lib/systemd/systemd-resolved
systemd+     105  0.0  0.2  91028  7808 ?        Ssl  13:29   0:02 /usr/lib/systemd/systemd-timesyncd
root         154  0.0  0.0   4236  2560 ?        Ss   13:29   0:00 /usr/sbin/cron -f -P
message+     155  0.0  0.1   9804  5120 ?        Ss   13:29   0:01 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         162  0.0  0.2  17964  8448 ?        Ss   13:29   0:01 /usr/lib/systemd/systemd-logind
root         170  0.0  0.0   3160  2048 hvc0     Ss+  13:29   0:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 115200,38400,9600 vt220
root         190  0.0  0.0   3116  1920 tty1     Ss+  13:29   0:00 /sbin/agetty -o -p -- \u --noclear - linux
root         191  0.0  0.5 107012 22272 ?        Ssl  13:29   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         268  0.0  0.0   3124   768 ?        Ss   13:29   0:00 /init
root         282  0.0  0.0   3140  1152 ?        S    13:29   0:00 /init
tumelo       283  0.0  0.1   6184  5256 pts/0    Ss   13:29   0:02 -bash
root         451  0.0  0.1   6692  4736 pts/1    Ss   13:41   0:00 /bin/login -f
tumelo       497  0.0  0.2  20312 11264 ?        Ss   13:41   0:00 /usr/lib/systemd/systemd --user
tumelo       498  0.0  0.0  21152  3516 ?        S    13:41   0:00 (sd-pam)
tumelo       527  0.0  0.1   6056  5120 pts/1    S+   13:41   0:00 -bash
polkitd      879  0.0  0.2 308164  7680 ?        Ssl  13:44   0:00 /usr/lib/polkit-1/polkitd --no-debug
syslog      1337  0.0  0.1 222508  5376 ?        Ssl  13:44   0:00 /usr/sbin/rsyslogd -n -iNONE
tumelo      3072  0.0  0.1   9424  4992 ?        Ss   14:23   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
tumelo      6060  200  0.1   8280  4224 pts/0    R+   19:03   0:00 ps aux

### top_results.txt
top - 19:04:26 up  7:58,  1 user,  load average: 0.06, 0.01, 0.00
Tasks:  24 total,   1 running,  23 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.8 sy,  0.0 ni, 99.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
MiB Mem :   3737.2 total,   3199.4 free,    409.9 used,    219.6 buff/cache     
MiB Swap:   1024.0 total,   1024.0 free,      0.0 used.   3327.3 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
      1 root      20   0   21832  12488   9416 S   0.0   0.3   0:04.86 systemd
      2 root      20   0    3120   2048   1920 S   0.0   0.1   0:00.07 init-sy+
      6 root      20   0    3136   1892   1792 S   0.0   0.0   0:00.00 init
     42 root      19  -1   50428  16128  15232 S   0.0   0.4   0:05.39 systemd+
     88 root      20   0   25144   6272   4992 S   0.0   0.2   0:07.55 systemd+
    104 systemd+  20   0   21460  13056  10880 S   0.0   0.3   0:01.18 systemd+
    105 systemd+  20   0   91028   7808   6912 S   0.0   0.2   0:02.46 systemd+
    154 root      20   0    4236   2560   2432 S   0.0   0.1   0:00.17 cron
    155 message+  20   0    9804   5120   4352 S   0.0   0.1   0:01.33 dbus-da+
    162 root      20   0   17964   8448   7552 S   0.0   0.2   0:01.15 systemd+
    170 root      20   0    3160   2048   1920 S   0.0   0.1   0:00.02 agetty
    190 root      20   0    3116   1920   1792 S   0.0   0.1   0:00.01 agetty
    191 root      20   0  107012  22272  13184 S   0.0   0.6   0:00.27 unatten+
    268 root      20   0    3124    768    768 S   0.0   0.0   0:00.00 Session+
    282 root      20   0    3140   1152   1024 S   0.0   0.0   0:00.79 Relay(2+
    283 tumelo    20   0    6184   5256   3584 S   0.0   0.1   0:02.41 bash
    451 root      20   0    6692   4736   3968 S   0.0   0.1   0:00.02 login
    497 tumelo    20   0   20312  11264   9216 S   0.0   0.3   0:00.58 systemd
    498 tumelo    20   0   21152   3516   1792 S   0.0   0.1   0:00.00 (sd-pam)
    527 tumelo    20   0    6056   5120   3584 S   0.0   0.1   0:00.03 bash
    879 polkitd   20   0  308164   7680   6912 S   0.0   0.2   0:00.87 polkitd
   1337 syslog    20   0  222508   5376   4608 S   0.0   0.1   0:00.60 rsyslogd
   3072 tumelo    20   0    9424   4992   4608 S   0.0   0.1   0:00.06 dbus-da+
   6062 tumelo    20   0    9284   5248   3200 R   0.0   0.1   0:00.01 top

### uptime_results.txt
 19:05:42 up  7:59,  1 user,  load average: 0.02, 0.01, 0.00

---

## LAB6_SYSTEM_MONITORING

### cpu_memory.txt
top - 11:39:00 up 20:58,  1 user,  load average: 0.00, 0.00, 0.00
Tasks:  25 total,   1 running,  24 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  4.6 sy,  0.0 ni, 95.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
MiB Mem :   3737.2 total,   3190.1 free,    414.0 used,    224.9 buff/cache     
MiB Swap:   1024.0 total,   1024.0 free,      0.0 used.   3323.2 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
     88 root      20   0   25144   6272   4992 S  13.8   0.2   0:22.61 systemd+
   7691 tumelo    20   0    9284   5248   3200 R   3.4   0.1   0:00.34 top
      1 root      20   0   21832  12616   9416 S   0.0   0.3   0:31.32 systemd
      2 root      20   0    3120   2048   1920 S   0.0   0.1   0:00.29 init-sy+
      6 root      20   0    3136   1892   1792 S   0.0   0.0   0:00.00 init
     42 root      19  -1   50428  16896  16000 S   0.0   0.4   0:27.58 systemd+
    104 systemd+  20   0   21460  13056  10880 S   0.0   0.3   0:06.17 systemd+
    105 systemd+  20   0   91028   7808   6912 S   0.0   0.2   0:15.14 systemd+
    154 root      20   0    4236   2560   2432 S   0.0   0.1   0:02.54 cron
    155 message+  20   0    9804   5120   4352 S   0.0   0.1   0:07.85 dbus-da+
    162 root      20   0   17964   8448   7552 S   0.0   0.2   0:05.35 systemd+
    170 root      20   0    3160   2048   1920 S   0.0   0.1   0:00.02 agetty
    190 root      20   0    3116   1920   1792 S   0.0   0.1   0:00.01 agetty
    191 root      20   0  107012  22272  13184 S   0.0   0.6   0:00.27 unatten+
    268 root      20   0    3124    768    768 S   0.0   0.0   0:00.00 Session+
    282 root      20   0    3140   1152   1024 S   0.0   0.0   0:00.89 Relay(2+
    283 tumelo    20   0    6184   5256   3584 S   0.0   0.1   0:03.33 bash
    451 root      20   0    6692   4736   3968 S   0.0   0.1   0:00.02 login
    497 tumelo    20   0   20312  11264   9216 S   0.0   0.3   0:03.53 systemd
    498 tumelo    20   0   21152   3516   1792 S   0.0   0.1   0:00.00 (sd-pam)
    527 tumelo    20   0    6056   5120   3584 S   0.0   0.1   0:00.03 bash
    879 polkitd   20   0  308164   7680   6912 S   0.0   0.2   0:04.81 polkitd
   1337 syslog    20   0  222508   5376   4608 S   0.0   0.1   0:04.39 rsyslogd
   3072 tumelo    20   0    9424   4992   4608 S   0.0   0.1   0:00.06 dbus-da+
   7692 root      20   0   25148   3588   2176 S   0.0   0.1   0:00.00 (udev-w+

### disk_usage.txt
Filesystem      Size  Used Avail Use% Mounted on
none            1.9G     0  1.9G   0% /usr/lib/modules/6.6.87.2-microsoft-standard-WSL2
none            1.9G  4.0K  1.9G   1% /mnt/wsl
drivers         476G  159G  318G  34% /usr/lib/wsl/drivers
/dev/sdd       1007G  2.2G  954G   1% /
none            1.9G  156K  1.9G   1% /mnt/wslg
none            1.9G     0  1.9G   0% /usr/lib/wsl/lib
rootfs          1.9G  2.7M  1.9G   1% /init
none            1.9G  528K  1.9G   1% /run
none            1.9G     0  1.9G   0% /run/lock
none            1.9G     0  1.9G   0% /run/shm
C:\             476G  159G  318G  34% /mnt/c
none            1.9G   76K  1.9G   1% /mnt/wslg/versions.txt
none            1.9G   76K  1.9G   1% /mnt/wslg/doc
tmpfs           374M   20K  374M   1% /run/user/1000

### memory_usage.txt
               total        used        free      shared  buff/cache   available
Mem:           3.6Gi       410Mi       3.1Gi       3.5Mi       225Mi       3.2Gi
Swap:          1.0Gi          0B       1.0Gi

### running_processes.txt
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.3  21832 12616 ?        Ss   Mar05   0:31 /sbin/init
root           2  0.0  0.0   3120  2048 ?        Sl   Mar05   0:00 /init
root           6  0.0  0.0   3136  1892 ?        Sl   Mar05   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
root          42  0.0  0.4  50428 16896 ?        S<s  Mar05   0:27 /usr/lib/systemd/systemd-journald
root          88  0.0  0.1  25144  6272 ?        Ss   Mar05   0:22 /usr/lib/systemd/systemd-udevd
systemd+     104  0.0  0.3  21460 13056 ?        Ss   Mar05   0:06 /usr/lib/systemd/systemd-resolved
systemd+     105  0.0  0.2  91028  7808 ?        Ssl  Mar05   0:15 /usr/lib/systemd/systemd-timesyncd
root         154  0.0  0.0   4236  2560 ?        Ss   Mar05   0:02 /usr/sbin/cron -f -P
message+     155  0.0  0.1   9804  5120 ?        Ss   Mar05   0:07 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         162  0.0  0.2  17964  8448 ?        Ss   Mar05   0:05 /usr/lib/systemd/systemd-logind
root         170  0.0  0.0   3160  2048 hvc0     Ss+  Mar05   0:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 115200,38400,9600 vt220
root         190  0.0  0.0   3116  1920 tty1     Ss+  Mar05   0:00 /sbin/agetty -o -p -- \u --noclear - linux
root         191  0.0  0.5 107012 22272 ?        Ssl  Mar05   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         268  0.0  0.0   3124   768 ?        Ss   Mar05   0:00 /init
root         282  0.0  0.0   3140  1152 ?        S    Mar05   0:00 /init
tumelo       283  0.0  0.1   6184  5256 pts/0    Ss   Mar05   0:03 -bash
root         451  0.0  0.1   6692  4736 pts/1    Ss   Mar05   0:00 /bin/login -f
tumelo       497  0.0  0.2  20312 11264 ?        Ss   Mar05   0:03 /usr/lib/systemd/systemd --user
tumelo       498  0.0  0.0  21152  3516 ?        S    Mar05   0:00 (sd-pam)
tumelo       527  0.0  0.1   6056  5120 pts/1    S+   Mar05   0:00 -bash
polkitd      879  0.0  0.2 308164  7680 ?        Ssl  Mar05   0:04 /usr/lib/polkit-1/polkitd --no-debug
syslog      1337  0.0  0.1 222508  5376 ?        Ssl  Mar05   0:04 /usr/sbin/rsyslogd -n -iNONE
tumelo      3072  0.0  0.1   9424  4992 ?        Ss   Mar05   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
tumelo      7704  266  0.1   8280  4224 pts/0    R+   11:41   0:00 ps aux

---

## LAB7_NMAP

### fast_scan.txt
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-03-06 12:40 SAST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00021s latency).
All 100 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 100 closed tcp ports (conn-refused)

Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds

### nmap_local_scan.txt
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-03-06 12:40 SAST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000049s latency).
All 1000 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Nmap done: 1 IP address (1 host up) scanned in 0.20 seconds

### service_scan.txt
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-03-06 12:41 SAST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00026s latency).
All 1000 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.40 seconds

---

## LAB7_PORT_SCANNING

### localhost_scan.txt
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-03-06 12:01 SAST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000047s latency).
All 1000 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Nmap done: 1 IP address (1 host up) scanned in 0.32 seconds

---

## LAB8_LOG_ANALYZER

### log_results.txt
Total log lines: 512
Error entries found: 9

### system_logs.txt
[    0.000000] Linux version 6.6.87.2-microsoft-standard-WSL2 (root@439a258ad544) (gcc (GCC) 11.2.0, GNU ld (GNU Binutils) 2.37) #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025
[    0.000000] Command line: initrd=\initrd.img WSL_ROOT_INIT=1 panic=-1 nr_cpus=12 hv_utils.timesync_implicit=1 console=hvc0 debug pty.legacy_count=0 WSL_ENABLE_CRASH_DUMP=1
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009ffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000e0fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000001fffff] ACPI data
[    0.000000] BIOS-e820: [mem 0x0000000000200000-0x00000000f4bfffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] APIC: Static calls initialized
[    0.000000] DMI not present or invalid.
[    0.000000] Hypervisor detected: Microsoft Hyper-V
[    0.000000] Hyper-V: privilege flags low 0xae7f, high 0x3b8030, hints 0x9a4e24, misc 0xe0bed7b2
[    0.000000] Hyper-V: Nested features: 0x3e0101
[    0.000000] Hyper-V: LAPIC Timer Frequency: 0xc3500
[    0.000000] Hyper-V: Using hypercall for remote TLB flush
[    0.000000] clocksource: hyperv_clocksource_tsc_page: mask: 0xffffffffffffffff max_cycles: 0x24e6a1710, max_idle_ns: 440795202120 ns
[    0.000000] clocksource: hyperv_clocksource_msr: mask: 0xffffffffffffffff max_cycles: 0x24e6a1710, max_idle_ns: 440795202120 ns
[    0.000000] tsc: Detected 2495.999 MHz processor
[    0.000049] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000051] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000054] last_pfn = 0xf4c00 max_arch_pfn = 0x400000000
[    0.000069] MTRR map: 5 entries (4 fixed + 1 variable; max 20), built from 8 variable MTRRs
[    0.000071] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000110] Using GB pages for direct mapping
[    0.000161] RAMDISK: [mem 0x04be4000-0x04e8bfff]
[    0.000164] ACPI: Early table checksum verification disabled
[    0.000167] ACPI: RSDP 0x00000000000E0000 000024 (v02 VRTUAL)
[    0.000171] ACPI: XSDT 0x0000000000100000 000044 (v01 VRTUAL MICROSFT 00000001 MSFT 00000001)
[    0.000176] ACPI: FACP 0x0000000000101000 000114 (v06 VRTUAL MICROSFT 00000001 MSFT 00000001)
[    0.000180] ACPI: DSDT 0x00000000001011B8 01E11C (v02 MSFTVM DSDT01   00000001 INTL 20230628)
[    0.000183] ACPI: FACS 0x0000000000101114 000040
[    0.000185] ACPI: OEM0 0x0000000000101154 000064 (v01 VRTUAL MICROSFT 00000001 MSFT 00000001)
[    0.000187] ACPI: SRAT 0x000000000011F2D4 000370 (v02 VRTUAL MICROSFT 00000001 MSFT 00000001)
[    0.000190] ACPI: APIC 0x000000000011F644 0000A8 (v04 VRTUAL MICROSFT 00000001 MSFT 00000001)
[    0.000191] ACPI: Reserving FACP table memory at [mem 0x101000-0x101113]
[    0.000193] ACPI: Reserving DSDT table memory at [mem 0x1011b8-0x11f2d3]
[    0.000193] ACPI: Reserving FACS table memory at [mem 0x101114-0x101153]
[    0.000193] ACPI: Reserving OEM0 table memory at [mem 0x101154-0x1011b7]
[    0.000194] ACPI: Reserving SRAT table memory at [mem 0x11f2d4-0x11f643]
[    0.000194] ACPI: Reserving APIC table memory at [mem 0x11f644-0x11f6eb]
[    0.000219] SRAT: PXM 0 -> APIC 0x00 -> Node 0
[    0.000220] SRAT: PXM 0 -> APIC 0x01 -> Node 0
[    0.000221] SRAT: PXM 0 -> APIC 0x02 -> Node 0
[    0.000221] SRAT: PXM 0 -> APIC 0x03 -> Node 0
[    0.000221] SRAT: PXM 0 -> APIC 0x04 -> Node 0
[    0.000222] SRAT: PXM 0 -> APIC 0x05 -> Node 0
[    0.000222] SRAT: PXM 0 -> APIC 0x06 -> Node 0
[    0.000223] SRAT: PXM 0 -> APIC 0x07 -> Node 0
[    0.000223] SRAT: PXM 0 -> APIC 0x08 -> Node 0
[    0.000223] SRAT: PXM 0 -> APIC 0x09 -> Node 0
[    0.000224] SRAT: PXM 0 -> APIC 0x0a -> Node 0
[    0.000224] SRAT: PXM 0 -> APIC 0x0b -> Node 0
[    0.000226] ACPI: SRAT: Node 0 PXM 0 [mem 0x00000000-0xf4bfffff] hotplug
[    0.000227] ACPI: SRAT: Node 0 PXM 0 [mem 0xf4c00000-0xf7ffffff] hotplug
[    0.000228] ACPI: SRAT: Node 0 PXM 0 [mem 0x100000000-0x9ffdfffff] hotplug
[    0.000229] ACPI: SRAT: Node 0 PXM 0 [mem 0x1000000000-0xffffffffff] hotplug
[    0.000229] ACPI: SRAT: Node 0 PXM 0 [mem 0x10000000000-0x1ffffffffff] hotplug
[    0.000230] ACPI: SRAT: Node 0 PXM 0 [mem 0x20000000000-0x3ffffffffff] hotplug
[    0.000230] ACPI: SRAT: Node 0 PXM 0 [mem 0x40000000000-0x7ffffffffff] hotplug
[    0.000231] ACPI: SRAT: Node 0 PXM 0 [mem 0x80000000000-0xfffffffffff] hotplug
[    0.000232] ACPI: SRAT: Node 0 PXM 0 [mem 0x100000000000-0x1fffffffffff] hotplug
[    0.000232] ACPI: SRAT: Node 0 PXM 0 [mem 0x200000000000-0x3fffffffffff] hotplug
[    0.000233] ACPI: SRAT: Node 0 PXM 0 [mem 0x400000000000-0x7fffffffffff] hotplug
[    0.000233] ACPI: SRAT: Node 0 PXM 0 [mem 0x800000000000-0xffffffffffff] hotplug
[    0.000234] ACPI: SRAT: Node 0 PXM 0 [mem 0x1000000000000-0x1ffffffffffff] hotplug
[    0.000234] ACPI: SRAT: Node 0 PXM 0 [mem 0x2000000000000-0x3ffffffffffff] hotplug
[    0.000235] ACPI: SRAT: Node 0 PXM 0 [mem 0x4000000000000-0x7ffffffffffff] hotplug
[    0.000236] ACPI: SRAT: Node 0 PXM 0 [mem 0x8000000000000-0xfffffffffffff] hotplug
[    0.000240] NODE_DATA(0) allocated [mem 0xf4bde000-0xf4bfffff]
[    0.000367] Zone ranges:
[    0.000367]   DMA32    [mem 0x0000000000001000-0x00000000f4bfffff]
[    0.000369]   Normal   empty
[    0.000370]   Device   empty
[    0.000370] Movable zone start for each node
[    0.000371] Early memory node ranges
[    0.000372]   node   0: [mem 0x0000000000001000-0x000000000009ffff]
[    0.000373]   node   0: [mem 0x0000000000200000-0x00000000f4bfffff]
[    0.000374] Initmem setup node 0 [mem 0x0000000000001000-0x00000000f4bfffff]
[    0.000398] On node 0, zone DMA32: 1 pages in unavailable ranges
[    0.003013] On node 0, zone DMA32: 352 pages in unavailable ranges
[    0.003752] On node 0, zone DMA32: 13312 pages in unavailable ranges
[    0.003793] ACPI: PM-Timer IO Port: 0x408
[    0.003809] ACPI: LAPIC_NMI (acpi_id[0x01] dfl dfl lint[0x1])
[    0.004770] IOAPIC[0]: apic_id 12, version 17, address 0xfec00000, GSI 0-23
[    0.004778] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.004784] ACPI: Using ACPI (MADT) for SMP configuration information
[    0.004786] TSC deadline timer available
[    0.004787] smpboot: Allowing 12 CPUs, 0 hotplug CPUs
[    0.004798] PM: hibernation: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.004799] PM: hibernation: Registered nosave memory: [mem 0x000a0000-0x000dffff]
[    0.004800] PM: hibernation: Registered nosave memory: [mem 0x000e0000-0x000e0fff]
[    0.004800] PM: hibernation: Registered nosave memory: [mem 0x000e1000-0x000fffff]
[    0.004800] PM: hibernation: Registered nosave memory: [mem 0x00100000-0x001fffff]
[    0.004802] [mem 0xf4c00000-0xffffffff] available for PCI devices
[    0.004803] Booting paravirtualized kernel on Hyper-V
[    0.004805] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.004849] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:12 nr_cpu_ids:12 nr_node_ids:1
[    0.007105] percpu: Embedded 63 pages/cpu s221184 r8192 d28672 u262144
[    0.007115] pcpu-alloc: s221184 r8192 d28672 u262144 alloc=1*2097152
[    0.007117] pcpu-alloc: [0] 00 01 02 03 04 05 06 07 [0] 08 09 10 11 -- -- -- -- 
[    0.007136] Hyper-V: PV spinlocks enabled
[    0.007138] PV qspinlock hash table entries: 256 (order: 0, 4096 bytes, linear)
[    0.007139] Kernel command line: initrd=\initrd.img WSL_ROOT_INIT=1 panic=-1 nr_cpus=12 hv_utils.timesync_implicit=1 console=hvc0 debug pty.legacy_count=0 WSL_ENABLE_CRASH_DUMP=1
[    0.007212] Unknown kernel command line parameters "WSL_ROOT_INIT=1 WSL_ENABLE_CRASH_DUMP=1", will be passed to user space.
[    0.007229] random: crng init done
[    0.009880] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.010720] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.010938] Fallback order for Node 0: 0 
[    0.010944] Built 1 zonelists, mobility grouping on.  Total pages: 986320
[    0.010945] Policy zone: DMA32
[    0.010956] mem auto-init: stack:off, heap alloc:on, heap free:off
[    0.010963] software IO TLB: area num 16.
[    0.064188] Memory: 257116K/4008572K available (20480K kernel code, 3457K rwdata, 13496K rodata, 4492K init, 6208K bss, 191804K reserved, 0K cma-reserved)
[    0.064392] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=12, Nodes=1
[    0.064441] ftrace: allocating 55808 entries in 218 pages
[    0.072765] ftrace: allocated 218 pages with 5 groups
[    0.073738] Dynamic Preempt: none
[    0.073901] rcu: Preemptible hierarchical RCU implementation.
[    0.073902] rcu: 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=12.
[    0.073904] 	Trampoline variant of Tasks RCU enabled.
[    0.073904] 	Rude variant of Tasks RCU enabled.
[    0.073904] 	Tracing variant of Tasks RCU enabled.
[    0.073905] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.073905] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=12
[    0.077467] Using NULL legacy PIC
[    0.077469] NR_IRQS: 524544, nr_irqs: 520, preallocated irqs: 0
[    0.077503] rcu: srcu_init: Setting srcu_struct sizes based on contention.
[    0.077883] Console: colour dummy device 80x25
[    0.077899] ACPI: Core revision 20230628
[    0.077987] Failed to register legacy timer interrupt
[    0.077988] APIC: Switch to symmetric I/O mode setup
[    0.081398] x2apic enabled
[    0.085226] APIC: Switched APIC routing to: physical x2apic
[    0.085234] Hyper-V: Host Build 10.0.26100.7920-7-0
[    0.085237] Hyper-V: enabling crash_kexec_post_notifiers
[    0.085328] Hyper-V: Disabling IBT because of Hyper-V bug
[    0.085330] Hyper-V: Using IPI hypercalls
[    0.085333] APIC: send_IPI() replaced with hv_send_ipi()
[    0.085339] APIC: send_IPI_mask() replaced with hv_send_ipi_mask()
[    0.085341] APIC: send_IPI_mask_allbutself() replaced with hv_send_ipi_mask_allbutself()
[    0.085342] APIC: send_IPI_allbutself() replaced with hv_send_ipi_allbutself()
[    0.085344] APIC: send_IPI_all() replaced with hv_send_ipi_all()
[    0.085345] APIC: send_IPI_self() replaced with hv_send_ipi_self()
[    0.085450] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x23fa763a3d1, max_idle_ns: 440795313647 ns
[    0.085461] Calibrating delay loop (skipped), value calculated using timer frequency.. 4991.99 BogoMIPS (lpj=9983996)
[    0.085556] x86/cpu: User Mode Instruction Prevention (UMIP) activated
[    0.085580] Last level iTLB entries: 4KB 0, 2MB 0, 4MB 0
[    0.085582] Last level dTLB entries: 4KB 0, 2MB 0, 4MB 0, 1GB 0
[    0.085587] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
[    0.085589] Spectre V2 : Mitigation: Enhanced / Automatic IBRS
[    0.085590] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    0.085591] Spectre V2 : Spectre v2 / PBRSB-eIBRS: Retire a single CALL on VMEXIT
[    0.085591] RETBleed: Mitigation: Enhanced IBRS
[    0.085593] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
[    0.085595] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl
[    0.085596] Register File Data Sampling: Mitigation: Clear Register File
[    0.085614] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.085616] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.085617] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.085618] x86/fpu: Supporting XSAVE feature 0x800: 'Control-flow User registers'
[    0.085619] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.085620] x86/fpu: xstate_offset[11]:  832, xstate_sizes[11]:   16
[    0.085622] x86/fpu: Enabled xstate features 0x807, context size is 848 bytes, using 'compacted' format.
[    0.089456] Freeing SMP alternatives memory: 44K
[    0.089456] pid_max: default: 32768 minimum: 301
[    0.089456] LSM: initializing lsm=capability,landlock,yama,safesetid,selinux,integrity
[    0.089456] landlock: Up and running.
[    0.089456] Yama: becoming mindful.
[    0.089456] SELinux:  Initializing.
[    0.089456] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.089456] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.089456] smpboot: CPU0: 13th Gen Intel(R) Core(TM) i5-1334U (family: 0x6, model: 0xba, stepping: 0x3)
[    0.089456] RCU Tasks: Setting shift to 4 and lim to 1 rcu_task_cb_adjust=1 rcu_task_cpu_ids=12.
[    0.089456] RCU Tasks Rude: Setting shift to 4 and lim to 1 rcu_task_cb_adjust=1 rcu_task_cpu_ids=12.
[    0.089456] RCU Tasks Trace: Setting shift to 4 and lim to 1 rcu_task_cb_adjust=1 rcu_task_cpu_ids=12.
[    0.089456] Performance Events: unsupported p6 CPU model 186 no PMU driver, software events only.
[    0.089456] signal: max sigframe size: 1776
[    0.089456] rcu: Hierarchical SRCU implementation.
[    0.089456] rcu: 	Max phase no-delay instances is 1000.
[    0.089456] NMI watchdog: Perf NMI watchdog permanently disabled
[    0.089456] smp: Bringing up secondary CPUs ...
[    0.089456] smpboot: x86: Booting SMP configuration:
[    0.089456] .... node  #0, CPUs:        #2  #4  #6  #8 #10  #1  #3  #5  #7  #9 #11
[    0.105919] smp: Brought up 1 node, 12 CPUs
[    0.105924] smpboot: Max logical packages: 1
[    0.105925] smpboot: Total of 12 processors activated (59903.97 BogoMIPS)
[    0.129520] node 0 deferred pages initialised in 20ms
[    0.130452] devtmpfs: initialized
[    0.133463] x86/mm: Memory block size: 128MB
[    0.133883] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.133883] futex hash table entries: 4096 (order: 6, 262144 bytes, linear)
[    0.133883] pinctrl core: initialized pinctrl subsystem
[    0.135770] NET: Registered PF_NETLINK/PF_ROUTE protocol family
[    0.135904] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
[    0.135968] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.135985] audit: initializing netlink subsys (disabled)
[    0.136010] thermal_sys: Registered thermal governor 'step_wise'
[    0.136010] thermal_sys: Registered thermal governor 'user_space'
[    0.136010] cpuidle: using governor ladder
[    0.136010] cpuidle: using governor menu
[    0.136010] audit: type=2000 audit(1772698455.048:1): state=initialized audit_enabled=0 res=1
[    0.136010] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.136010] dca service started, version 1.12.1
[    0.136010] PCI: Fatal: No config space access function found
[    0.137596] kprobes: kprobe jump-optimization is enabled. All kprobes are optimized if possible.
[    0.137617] HugeTLB: registered 1.00 GiB page size, pre-allocated 0 pages
[    0.137617] HugeTLB: 16380 KiB vmemmap can be freed for a 1.00 GiB page
[    0.137617] HugeTLB: registered 2.00 MiB page size, pre-allocated 0 pages
[    0.137617] HugeTLB: 28 KiB vmemmap can be freed for a 2.00 MiB page
[    0.138550] cryptd: max_cpu_qlen set to 1000
[    0.138550] ACPI: Added _OSI(Module Device)
[    0.138550] ACPI: Added _OSI(Processor Device)
[    0.138550] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.138550] ACPI: Added _OSI(Processor Aggregator Device)
[    0.144735] ACPI: 1 ACPI AML tables successfully acquired and loaded
[    0.145702] ACPI: _OSC evaluation for CPUs failed, trying _PDC
[    0.145808] ACPI: Interpreter enabled
[    0.145814] ACPI: PM: (supports S0 S5)
[    0.145815] ACPI: Using IOAPIC for interrupt routing
[    0.145829] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.145830] PCI: Using E820 reservations for host bridge windows
[    0.146019] ACPI: Enabled 2 GPEs in block 00 to 0F
[    0.148012] iommu: Default domain type: Translated
[    0.148012] iommu: DMA domain TLB invalidation policy: lazy mode
[    0.148012] SCSI subsystem initialized
[    0.148012] libata version 3.00 loaded.
[    0.148012] pps_core: LinuxPPS API ver. 1 registered
[    0.148012] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.148012] PTP clock support registered
[    0.148012] EDAC MC: Ver: 3.0.0
[    0.169465] hv_vmbus: Vmbus version:5.3
[    0.169715] hv_vmbus: Unknown GUID: 6e382d18-3336-4f4b-acc4-2b7703d4df4a
[    0.169741] hv_vmbus: Unknown GUID: dde9cbc0-5060-4436-9448-ea1254a5d177
[    0.170270] NetLabel: Initializing
[    0.170272] NetLabel:  domain hash size = 128
[    0.170273] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.170282] NetLabel:  unlabeled traffic allowed by default
[    0.170283] PCI: Using ACPI for IRQ routing
[    0.170284] PCI: System does not support PCI
[    0.170312] vgaarb: loaded
[    0.173643] clocksource: Switched to clocksource tsc-early
[    0.175463] VFS: Disk quotas dquot_6.6.0
[    0.175486] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.175551] FS-Cache: Loaded
[    0.175732] pnp: PnP ACPI init
[    0.176245] pnp: PnP ACPI: found 1 devices
[    0.191859] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.191928] NET: Registered PF_INET protocol family
[    0.192036] IP idents hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    0.192559] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    0.192606] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
[    0.192659] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.192902] TCP bind hash table entries: 32768 (order: 8, 1048576 bytes, linear)
[    0.192997] TCP: Hash tables configured (established 32768 bind 32768)
[    0.193087] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    0.193105] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    0.193154] NET: Registered PF_UNIX/PF_LOCAL protocol family
[    0.193163] NET: Registered PF_XDP protocol family
[    0.193169] PCI: CLS 0 bytes, default 64
[    0.193246] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.193247] software IO TLB: mapped [mem 0x00000000ec200000-0x00000000f0200000] (64MB)
[    0.193936] Trying to unpack rootfs image as initramfs...
[    0.194717] RAPL PMU: API unit is 2^-32 Joules, 0 fixed counters, 10737418240 ms ovfl timer
[    0.194739] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x23fa763a3d1, max_idle_ns: 440795313647 ns
[    0.195796] clocksource: Switched to clocksource tsc
[    0.199055] Initialise system trusted keyrings
[    0.199081] Key type blacklist registered
[    0.199289] Freeing initrd memory: 2720K
[    0.199765] workingset: timestamp_bits=36 max_order=20 bucket_order=0
[    0.200442] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.200457] fuse: init (API version 7.39)
[    0.200912] SGI XFS with ACLs, security attributes, realtime, verbose warnings, quota, no debug enabled
[    0.202149] 9p: Installing v9fs 9p2000 file system support
[    0.209152] Key type asymmetric registered
[    0.209155] Asymmetric key parser 'x509' registered
[    0.209189] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 245)
[    0.209295] io scheduler mq-deadline registered
[    0.209296] io scheduler kyber registered
[    0.212321] hv_vmbus: registering driver hv_pci
[    0.213077] hv_pci c4b741f5-5582-4c98-8f8b-2e082933c396: PCI VMBus probing: Using version 0x10004
[    0.213627] hv_pci c4b741f5-5582-4c98-8f8b-2e082933c396: PCI host bridge to bus 5582:00
[    0.213628] pci_bus 5582:00: root bus resource [mem 0x9ffe00000-0x9ffe02fff window]
[    0.213630] pci_bus 5582:00: No busn resource found for root bus, will use [bus 00-ff]
[    0.213978] pci 5582:00:00.0: [1af4:1043] type 00 class 0x010000
[    0.214310] pci 5582:00:00.0: reg 0x10: [mem 0x9ffe00000-0x9ffe00fff 64bit]
[    0.214497] pci 5582:00:00.0: reg 0x18: [mem 0x9ffe01000-0x9ffe01fff 64bit]
[    0.214680] pci 5582:00:00.0: reg 0x20: [mem 0x9ffe02000-0x9ffe02fff 64bit]
[    0.216618] pci_bus 5582:00: busn_res: [bus 00-ff] end is updated to 00
[    0.216626] pci 5582:00:00.0: BAR 0: assigned [mem 0x9ffe00000-0x9ffe00fff 64bit]
[    0.217018] pci 5582:00:00.0: BAR 2: assigned [mem 0x9ffe01000-0x9ffe01fff 64bit]
[    0.217327] pci 5582:00:00.0: BAR 4: assigned [mem 0x9ffe02000-0x9ffe02fff 64bit]
[    0.218205] hv_pci cafd55ca-733f-420e-94a3-a3776f02eeaf: PCI VMBus probing: Using version 0x10004
[    0.218905] hv_pci cafd55ca-733f-420e-94a3-a3776f02eeaf: PCI host bridge to bus 733f:00
[    0.218906] pci_bus 733f:00: No busn resource found for root bus, will use [bus 00-ff]
[    0.219062] pci 733f:00:00.0: [1414:008e] type 00 class 0x030200
[    0.221064] pci_bus 733f:00: busn_res: [bus 00-ff] end is updated to 00
[    0.221644] ioatdma: Intel(R) QuickData Technology Driver 5.00
[    0.221888] virtio-pci 5582:00:00.0: enabling device (0000 -> 0002)
[    0.225475] Serial: 8250/16550 driver, 8 ports, IRQ sharing enabled
[    0.249726] Linux agpgart interface v0.103
[    0.249745] AMD-Vi: AMD IOMMUv2 functionality not available on this system - This is not a bug.
[    0.249754] ACPI: bus type drm_connector registered
[    0.252893] printk: console [hvc0] enabled
[    0.254248] brd: module loaded
[    0.256480] loop: module loaded
[    0.258269] Loading iSCSI transport class v2.0-870.
[    0.258864] rdac: device handler registered
[    0.259532] Microchip SmartPQI Driver (v2.1.24-046)
[    0.260506] VMware PVSCSI driver - version 1.0.7.0-k
[    0.260981] hv_vmbus: registering driver hv_storvsc
[    0.262399] PPP generic driver version 2.4.2
[    0.262715] scsi host0: storvsc_host_t
[    0.263118] VMware vmxnet3 virtual NIC driver - version 1.7.0.0-k-NAPI
[    0.264015] hv_vmbus: registering driver hv_netvsc
[    0.264997] Fusion MPT base driver 3.04.20
[    0.265404] Copyright (c) 1999-2008 LSI Corporation
[    0.265890] Fusion MPT SPI Host driver 3.04.20
[    0.267723] Fusion MPT SAS Host driver 3.04.20
[    0.268048] Fusion MPT misc device (ioctl) driver 3.04.20
[    0.268488] mptctl: Registered with Fusion MPT base driver
[    0.269071] mptctl: /dev/mptctl @ (major,minor=10,220)
[    0.270051] i8042: PNP: No PS/2 controller found.
[    0.270755] hv_vmbus: registering driver hyperv_keyboard
[    0.271151] rtc_cmos 00:00: RTC can wake from S4
[    0.272707] rtc_cmos 00:00: registered as rtc0
[    0.273460] rtc_cmos 00:00: setting system clock to 2026-03-05T08:14:15 UTC (1772698455)
[    0.274672] rtc_cmos 00:00: alarms up to one month, 114 bytes nvram
[    0.275107] device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
[    0.275684] device-mapper: uevent: version 1.0.3
[    0.276053] device-mapper: ioctl: 4.48.0-ioctl (2023-03-01) initialised: dm-devel@redhat.com
[    0.276779] intel_pstate: CPU model not supported
[    0.277157] hv_utils: Registering HyperV Utility Driver
[    0.277578] hv_vmbus: registering driver hv_utils
[    0.277956] hv_vmbus: registering driver hv_balloon
[    0.278577] hv_vmbus: registering driver dxgkrnl
[    0.278626] hv_utils: TimeSync IC version 4.0
[    0.281857] hv_balloon: Using Dynamic Memory protocol version 2.0
[    0.283715] Free page reporting enabled
[    0.284010] drop_monitor: Initializing network drop monitor service
[    0.284165] hv_balloon: Cold memory discard hint enabled with order 9
[    0.297163] NET: Registered PF_INET6 protocol family
[    0.298584] Segment Routing with IPv6
[    0.298913] In-situ OAM (IOAM) with IPv6
[    0.299591] NET: Registered PF_PACKET protocol family
[    0.301282] 9pnet: Installing 9P2000 support
[    0.302241] NET: Registered PF_VSOCK protocol family
[    0.302891] hv_vmbus: registering driver hv_sock
[    0.304138] IPI shorthand broadcast: enabled
[    0.304506] AVX2 version of gcm_enc/dec engaged.
[    0.305967] AES CTR mode by8 optimization enabled
[    0.307464] sched_clock: Marking stable (296476099, 7618709)->(325388833, -21294025)
[    0.308341] registered taskstats version 1
[    0.308757] Loading compiled-in X.509 certificates
[    0.310604] ima: No TPM chip found, activating TPM-bypass!
[    0.311264] ima: Allocated hash algorithm: sha256
[    0.311675] ima: No architecture policies found
[    0.363426] RAS: Correctable Errors collector initialized.
[    0.364797] clk: Disabling unused clocks
[    0.370700] Freeing unused decrypted memory: 2028K
[    0.373514] Freeing unused kernel image (initmem) memory: 4492K
[    0.374960] Write protecting the kernel read-only data: 34816k
[    0.376192] Freeing unused kernel image (rodata/data gap) memory: 840K
[    0.376600] Run /init as init process
[    0.376741]   with arguments:
[    0.376927]     /init
[    0.377051]   with environment:
[    0.377181]     HOME=/
[    0.377302]     TERM=linux
[    0.377390]     WSL_ROOT_INIT=1
[    0.377637]     WSL_ENABLE_CRASH_DUMP=1
[    0.465376] scsi 0:0:0:0: Direct-Access     Msft     Virtual Disk     1.0  PQ: 0 ANSI: 5
[    0.475931] scsi 0:0:0:1: Direct-Access     Msft     Virtual Disk     1.0  PQ: 0 ANSI: 5
[    0.501100] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    0.501835] sd 0:0:0:0: [sda] 795880 512-byte logical blocks: (407 MB/389 MiB)
[    0.503078] sd 0:0:0:1: Attached scsi generic sg1 type 0
[    0.503559] sd 0:0:0:1: [sdb] 381016 512-byte logical blocks: (195 MB/186 MiB)
[    0.503799] sd 0:0:0:1: [sdb] Write Protect is on
[    0.503972] sd 0:0:0:0: [sda] Write Protect is on
[    0.503976] sd 0:0:0:0: [sda] Mode Sense: 0f 00 80 00
[    0.504468] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    0.509865] sd 0:0:0:0: [sda] Attached SCSI disk
[    0.510816] sd 0:0:0:1: [sdb] Mode Sense: 0f 00 80 00
[    0.512889] sd 0:0:0:1: [sdb] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    0.522241] sd 0:0:0:1: [sdb] Attached SCSI disk
[    0.528236] scsi 0:0:0:2: Direct-Access     Msft     Virtual Disk     1.0  PQ: 0 ANSI: 5
[    0.548033] sd 0:0:0:2: Attached scsi generic sg2 type 0
[    0.550833] sd 0:0:0:2: [sdc] 2097160 512-byte logical blocks: (1.07 GB/1.00 GiB)
[    0.552451] sd 0:0:0:2: [sdc] 4096-byte physical blocks
[    0.553936] sd 0:0:0:2: [sdc] Write Protect is off
[    0.555055] sd 0:0:0:2: [sdc] Mode Sense: 0f 00 00 00
[    0.556367] sd 0:0:0:2: [sdc] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    0.561064] sd 0:0:0:2: [sdc] Attached SCSI disk
[    0.722893] EXT4-fs (sda): mounted filesystem 00000000-0000-0000-0000-000000000000 ro without journal. Quota mode: none.
[    0.729532] EXT4-fs (sdb): mounted filesystem 00000000-0000-0000-0000-000000000000 ro without journal. Quota mode: none.
[    0.774152] tun: Universal TUN/TAP device driver, 1.6
[    0.819816] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[    0.832188] Adding 1048576k swap on /dev/sdc.  Priority:-2 extents:1 across:1048576k 
[    0.836617] Bridge firewalling registered
[    4.285749] hv_pci 6d259806-1fc4-4466-8e9d-622bd28d0a16: PCI VMBus probing: Using version 0x10004
[    4.288674] hv_pci 6d259806-1fc4-4466-8e9d-622bd28d0a16: PCI host bridge to bus 1fc4:00
[    4.289522] pci_bus 1fc4:00: root bus resource [mem 0xc00000000-0xe00001fff window]
[    4.290492] pci_bus 1fc4:00: No busn resource found for root bus, will use [bus 00-ff]
[    4.292247] pci 1fc4:00:00.0: [1af4:105a] type 00 class 0x088000
[    4.293560] pci 1fc4:00:00.0: reg 0x10: [mem 0xe00000000-0xe00000fff 64bit]
[    4.294908] pci 1fc4:00:00.0: reg 0x18: [mem 0xe00001000-0xe00001fff 64bit]
[    4.296236] pci 1fc4:00:00.0: reg 0x20: [mem 0xc00000000-0xdffffffff 64bit]
[    4.299451] pci_bus 1fc4:00: busn_res: [bus 00-ff] end is updated to 00
[    4.300208] pci 1fc4:00:00.0: BAR 4: assigned [mem 0xc00000000-0xdffffffff 64bit]
[    4.301309] pci 1fc4:00:00.0: BAR 0: assigned [mem 0xe00000000-0xe00000fff 64bit]
[    4.302650] pci 1fc4:00:00.0: BAR 2: assigned [mem 0xe00001000-0xe00001fff 64bit]
[    4.304033] virtio-pci 1fc4:00:00.0: enabling device (0000 -> 0002)
[    4.320045] virtiofs virtio1: Cache len: 0x200000000 @ 0xc00000000
[    4.839586] scsi 0:0:0:3: Direct-Access     Msft     Virtual Disk     1.0  PQ: 0 ANSI: 5
[    4.882377] sd 0:0:0:3: Attached scsi generic sg3 type 0
[    4.889961] sd 0:0:0:3: [sdd] 2147483648 512-byte logical blocks: (1.10 TB/1.00 TiB)
[    4.894660] sd 0:0:0:3: [sdd] 4096-byte physical blocks
[    4.897746] sd 0:0:0:3: [sdd] Write Protect is off
[    4.901040] sd 0:0:0:3: [sdd] Mode Sense: 0f 00 00 00
[    4.906750] sd 0:0:0:3: [sdd] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    4.918838] sd 0:0:0:3: [sdd] Attached SCSI disk
[    5.220935] hv_storvsc fd1d2cbd-ce7c-535c-966b-eb5f811c95f0: tag#663 cmd 0x2a status: scsi 0x0 srb 0x4 hv 0xc00000a1
[    5.394622] EXT4-fs (sdd): mounted filesystem dbbea291-09b6-4ae2-b648-b3c99cd3b750 r/w with ordered data mode. Quota mode: none.
[    9.618890] WSL (240) ERROR: CheckConnection: getaddrinfo() failed: -5
[   29.001419] EXT4-fs (sdd): unmounting filesystem dbbea291-09b6-4ae2-b648-b3c99cd3b750.
[   29.123357] EXT4-fs (sdd): mounted filesystem dbbea291-09b6-4ae2-b648-b3c99cd3b750 r/w with ordered data mode. Quota mode: none.
[   30.463819] misc dxg: dxgk: dxgkio_is_feature_enabled: Ioctl failed: -22
[   30.470077] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[   30.472006] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[   30.473615] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[   30.475417] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[   31.002955] Failed to connect to bus: No such file or directory
[   31.274830] Failed to connect to bus: No such file or directory
[   31.535200] Failed to connect to bus: No such file or directory
[   31.776336] systemd-journald[58]: Collecting audit messages is disabled.
[   32.168021] systemd-journald[58]: Received client request to flush runtime journal.
[   32.542771] weston[276]: memfd_create() called without MFD_EXEC or MFD_NOEXEC_SEAL set
[   33.079878] ACPI: AC: AC Adapter [AC1] (on-line)
[   33.103373] ACPI: battery: Slot [BAT1] (battery present)
[   34.035765] kvm_intel: Using Hyper-V Enlightened VMCS
[   34.428424] intel_rapl_msr: PL4 support detected.
[   35.340478] TCP: eth0: Driver has suspect GRO implementation, TCP performance may be compromised.
[   48.391813] hv_balloon: Max. dynamic memory size: 3916 MB
[  624.251527] mini_init (224): drop_caches: 1
[ 2693.992482] WSL (240) ERROR: CheckConnection: getaddrinfo() failed: -5
[ 8933.954357] Exception: 
[ 8933.962087] Operation canceled @p9io.cpp:258 (AcceptAsync)

[ 8934.735791] systemd-journald[58]: Received SIGTERM from PID 1 (systemd-shutdow).
[ 8936.086642] systemd-journald[42]: Collecting audit messages is disabled.
[ 8936.309386] systemd-journald[42]: Received client request to flush runtime journal.
[ 8936.309937] systemd-journald[42]: File /var/log/journal/5211b72c926945c083f457f07723a489/system.journal corrupted or uncleanly shut down, renaming and replacing.
[ 8936.323790] misc dxg: dxgk: dxgkio_is_feature_enabled: Ioctl failed: -22
[ 8936.340627] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[ 8936.341646] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[ 8936.342515] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[ 8936.343757] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[ 8982.016432] mini_init (224): drop_caches: 1
[ 9491.079484] WSL (240) ERROR: CheckConnection: getaddrinfo() failed: -5
[ 9922.969540] mini_init (224): drop_caches: 1
[10110.691284] mini_init (224): drop_caches: 1
[10486.359139] mini_init (224): drop_caches: 1
[10960.109831] mini_init (224): drop_caches: 1
[11086.269851] mini_init (224): drop_caches: 1
[11149.311284] mini_init (224): drop_caches: 1
[12132.932894] mini_init (224): drop_caches: 1
[15162.419774] weston[1579]: segfault at 28 ip 00007c7675d93cbe sp 00007ffc48c6a630 error 4 in libwayland-server.so.0.21.0[7c7675d8f000+9000] likely on CPU 1 (core 0, socket 0)
[15162.427860] Code: 48 8b 47 08 48 8d 77 10 48 8b 78 08 e9 7b bf ff ff 66 66 2e 0f 1f 84 00 00 00 00 00 f3 0f 1e fa 41 54 55 48 89 fd 48 83 ec 08 <8b> 57 28 4c 8b 67 08 85 d2 79 37 48 8d 05 50 b6 00 00 48 39 07 0f
[15162.428023] weston: weston: potentially unexpected fatal signal 11.
[15162.430268] CPU: 1 PID: 1579 Comm: weston Not tainted 6.6.87.2-microsoft-standard-WSL2 #1
[15162.430703] RIP: 0033:0x7c7675d93cbe
[15162.433116] Code: 48 8b 47 08 48 8d 77 10 48 8b 78 08 e9 7b bf ff ff 66 66 2e 0f 1f 84 00 00 00 00 00 f3 0f 1e fa 41 54 55 48 89 fd 48 83 ec 08 <8b> 57 28 4c 8b 67 08 85 d2 79 37 48 8d 05 50 b6 00 00 48 39 07 0f
[15162.433119] RSP: 002b:00007ffc48c6a630 EFLAGS: 00010206
[15162.433990] RAX: 0000000000000000 RBX: 0000000000000000 RCX: 00007c7675ef808b
[15162.434016] RDX: 0000000000000000 RSI: 0000000000000000 RDI: 0000000000000000
[15162.434017] RBP: 0000000000000000 R08: 0000000000000000 R09: 00007c767294d73c
[15162.434019] R10: 00007c7654000ac0 R11: 0000000000000293 R12: 0000000000000000
[15162.434020] R13: 00005e10d65b93b0 R14: 00005e10d65df8f0 R15: 0000000000000059
[15162.434022] FS:  00007c7672e5d980 GS:  0000000000000000
[15162.455930] WSL (5038 - CaptureCrash): Capturing crash for pid: 20, executable: !usr!bin!weston, signal: 11, port: 50005
[20939.395630] mini_init (224): drop_caches: 1
[27259.787429] mini_init (224): drop_caches: 1
[34464.698736] WSL (240) ERROR: CheckConnection: getaddrinfo() failed: -5
[38319.844476] WSL (240) ERROR: CheckConnection: getaddrinfo() failed: -5
[38608.198989] mini_init (224): drop_caches: 1
[40567.788350] mini_init (224): drop_caches: 1
[48567.525002] mini_init (224): drop_caches: 1
[50594.789859] mini_init (224): drop_caches: 1
[52597.872972] mini_init (224): drop_caches: 1
[68676.120590] mini_init (224): drop_caches: 1
[69980.978937] mini_init (224): drop_caches: 1
[72739.458753] mini_init (224): drop_caches: 1
[74778.305668] mini_init (224): drop_caches: 1
[76797.690636] mini_init (224): drop_caches: 1
[80654.091356] weston[5043]: segfault at 28 ip 00007f6f36f89cbe sp 00007ffc7a160450 error 4 in libwayland-server.so.0.21.0[7f6f36f85000+9000] likely on CPU 3 (core 1, socket 0)
[80654.094666] Code: 48 8b 47 08 48 8d 77 10 48 8b 78 08 e9 7b bf ff ff 66 66 2e 0f 1f 84 00 00 00 00 00 f3 0f 1e fa 41 54 55 48 89 fd 48 83 ec 08 <8b> 57 28 4c 8b 67 08 85 d2 79 37 48 8d 05 50 b6 00 00 48 39 07 0f
[80654.094915] weston: weston: potentially unexpected fatal signal 11.
[80654.095833] CPU: 3 PID: 5043 Comm: weston Not tainted 6.6.87.2-microsoft-standard-WSL2 #1
[80654.096082] RIP: 0033:0x7f6f36f89cbe
[80654.097864] Code: 48 8b 47 08 48 8d 77 10 48 8b 78 08 e9 7b bf ff ff 66 66 2e 0f 1f 84 00 00 00 00 00 f3 0f 1e fa 41 54 55 48 89 fd 48 83 ec 08 <8b> 57 28 4c 8b 67 08 85 d2 79 37 48 8d 05 50 b6 00 00 48 39 07 0f
[80654.097866] RSP: 002b:00007ffc7a160450 EFLAGS: 00010206
[80654.097992] RAX: 0000000000000000 RBX: 0000000000000000 RCX: 00007f6f370ee08b
[80654.098016] RDX: 0000000000000000 RSI: 0000000000000000 RDI: 0000000000000000
[80654.098017] RBP: 0000000000000000 R08: 0000000000000000 R09: 00007f6f33b4373c
[80654.098018] R10: 00007f6f14000ce0 R11: 0000000000000293 R12: 0000000000000000
[80654.098018] R13: 00005c4e2692f3b0 R14: 00005c4e269551c0 R15: 0000000000000061
[80654.098039] FS:  00007f6f34053980 GS:  0000000000000000
[80654.126721] WSL (9634 - CaptureCrash): Capturing crash for pid: 3454, executable: !usr!bin!weston, signal: 11, port: 50005
[81126.174158] WSL (240) ERROR: CheckConnection: getaddrinfo() failed: -5
[81536.362693] mini_init (224): drop_caches: 1
[84685.740362] mini_init (224): drop_caches: 1
[84796.516325] Bluetooth: Core ver 2.22
[84796.518624] NET: Registered PF_BLUETOOTH protocol family
[84796.519851] Bluetooth: HCI device and connection manager initialized
[84796.520390] Bluetooth: HCI socket layer initialized
[84796.520398] Bluetooth: L2CAP socket layer initialized
[84796.520483] Bluetooth: SCO socket layer initialized
[84796.645729] hv_netvsc 1007e2cb-1e99-41a9-bb92-2213e61b5e32 eth0: entered promiscuous mode
[84879.623336] hv_netvsc 1007e2cb-1e99-41a9-bb92-2213e61b5e32 eth0: left promiscuous mode

---

## LAB8_TCPDUMP

### tcpdump_capture.txt
12:54:15.789933 IP 172.18.160.107.34541 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
12:54:16.049978 IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.34541: NTPv4, Server, length 48
12:54:22.222849 ARP, Request who-has 172.18.160.107 (00:15:5d:df:48:25 (oui Unknown)) tell LuNgoma.mshome.net, length 28
12:54:22.224854 ARP, Reply 172.18.160.107 is-at 00:15:5d:df:48:25 (oui Unknown), length 28
12:54:50.012472 IP 172.18.160.107.45772 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
12:54:50.258678 IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.45772: NTPv4, Server, length 48
12:54:55.427888 ARP, Request who-has 172.18.160.107 (00:15:5d:df:48:25 (oui Unknown)) tell LuNgoma.mshome.net, length 28
12:54:55.427938 ARP, Reply 172.18.160.107 is-at 00:15:5d:df:48:25 (oui Unknown), length 28
12:54:56.109692 ARP, Request who-has LuNgoma.mshome.net tell 172.18.160.107, length 28
12:54:56.110048 ARP, Reply LuNgoma.mshome.net is-at 00:15:5d:55:90:01 (oui Unknown), length 28
12:55:04.061562 IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 SRV (QM)? SWTV-22AE-4K-9a5278b0e93ea1a4128c5d83e83bc9a8._googlecast._tcp.local. (86)
12:55:04.063419 IP6 fe80::ff53:70e2:d3ac:d16.mdns > ff02::fb.mdns: 0 SRV (QM)? SWTV-22AE-4K-9a5278b0e93ea1a4128c5d83e83bc9a8._googlecast._tcp.local. (86)
12:55:04.066727 IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 SRV (QM)? SWTV-7d84401c111afe94432d4630805b21ce._googlecast._tcp.local. (78)
12:55:04.067830 IP6 fe80::ff53:70e2:d3ac:d16.mdns > ff02::fb.mdns: 0 SRV (QM)? SWTV-7d84401c111afe94432d4630805b21ce._googlecast._tcp.local. (78)
12:55:04.072842 IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 SRV (QM)? SWTV-24AE-FHD-c1981b8088638a7f42a0762f165ec7c9._googlecast._tcp.local. (87)
12:55:04.074194 IP6 fe80::ff53:70e2:d3ac:d16.mdns > ff02::fb.mdns: 0 SRV (QM)? SWTV-24AE-FHD-c1981b8088638a7f42a0762f165ec7c9._googlecast._tcp.local. (87)
12:55:23.259396 IP 172.18.160.107.53045 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
12:55:23.484200 IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.53045: NTPv4, Server, length 48
12:55:29.762795 ARP, Request who-has 172.18.160.107 (00:15:5d:df:48:25 (oui Unknown)) tell LuNgoma.mshome.net, length 28
12:55:29.762855 ARP, Reply 172.18.160.107 is-at 00:15:5d:df:48:25 (oui Unknown), length 28

---

## LAB9_PACKET_SNIFFING

### lab9_capture.pcap
*Cannot display binary file, saved at lab9_capture.pcap*

### lab9_results.txt
14:05:38.743127 eth0  Out IP 172.18.160.107.36123 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
14:05:39.004574 eth0  In  IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.36123: NTPv4, Server, length 48
14:06:14.137510 eth0  Out IP 172.18.160.107.51391 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
14:06:14.366032 eth0  In  IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.51391: NTPv4, Server, length 48
14:06:21.824782 eth0  In  ARP, Request who-has 172.18.160.107 (00:15:5d:c6:5c:b1 (oui Unknown)) tell LuNgoma.mshome.net, length 28
14:06:21.824806 eth0  Out ARP, Reply 172.18.160.107 is-at 00:15:5d:c6:5c:b1 (oui Unknown), length 28
14:06:22.277692 eth0  Out ARP, Request who-has LuNgoma.mshome.net tell 172.18.160.107, length 28
14:06:22.277865 eth0  In  ARP, Reply LuNgoma.mshome.net is-at 00:15:5d:4c:83:21 (oui Unknown), length 28
14:06:49.349806 eth0  Out IP 172.18.160.107.60438 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
14:06:49.512470 eth0  In  IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.60438: NTPv4, Server, length 48
14:06:57.495766 eth0  Out ARP, Request who-has LuNgoma.mshome.net tell 172.18.160.107, length 28
14:06:57.496419 eth0  In  ARP, Reply LuNgoma.mshome.net is-at 00:15:5d:4c:83:21 (oui Unknown), length 28
14:07:24.561731 eth0  Out IP 172.18.160.107.47346 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
14:07:24.770208 eth0  In  IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.47346: NTPv4, Server, length 48
14:07:31.868390 eth0  In  ARP, Request who-has 172.18.160.107 (00:15:5d:c6:5c:b1 (oui Unknown)) tell LuNgoma.mshome.net, length 28
14:07:31.868411 eth0  Out ARP, Reply 172.18.160.107 is-at 00:15:5d:c6:5c:b1 (oui Unknown), length 28
14:07:32.661735 eth0  Out ARP, Request who-has LuNgoma.mshome.net tell 172.18.160.107, length 28
14:07:32.662262 eth0  In  ARP, Reply LuNgoma.mshome.net is-at 00:15:5d:4c:83:21 (oui Unknown), length 28
14:07:59.720757 eth0  Out IP 172.18.160.107.32998 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
14:07:59.930113 eth0  In  IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.32998: NTPv4, Server, length 48
14:08:07.849586 eth0  Out ARP, Request who-has LuNgoma.mshome.net tell 172.18.160.107, length 28
14:08:07.849793 eth0  In  ARP, Reply LuNgoma.mshome.net is-at 00:15:5d:4c:83:21 (oui Unknown), length 28
14:08:18.554982 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 A (QM)? wpad.local. (28)
14:08:18.556747 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 A (QM)? wpad.local. (28)
14:08:18.939306 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 A (QM)? wpad.local. (28)
14:08:18.940042 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 A (QM)? wpad.local. (28)
14:08:19.321745 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 A (QM)? wpad.local. (28)
14:08:19.322922 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 A (QM)? wpad.local. (28)
14:08:21.032328 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 A (QM)? wpad.local. (28)
14:08:21.033823 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 A (QM)? wpad.local. (28)
14:08:21.035521 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 AAAA (QU)? wpad.local. (28)
14:08:21.036992 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 AAAA (QU)? wpad.local. (28)
14:08:21.411249 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 A (QM)? wpad.local. (28)
14:08:21.413731 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 A (QM)? wpad.local. (28)
14:08:21.425361 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 AAAA (QM)? wpad.local. (28)
14:08:21.427932 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 AAAA (QM)? wpad.local. (28)
14:08:21.793377 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 A (QM)? wpad.local. (28)
14:08:21.794401 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 A (QM)? wpad.local. (28)
14:08:21.808755 eth0  M   IP LuNgoma.mshome.net.mdns > mdns.mcast.net.mdns: 0 AAAA (QU)? wpad.local. (28)
14:08:21.811328 eth0  M   IP6 fe80::46c1:23c9:4ebc:e1d7.mdns > ff02::fb.mdns: 0 AAAA (QU)? wpad.local. (28)
14:08:34.911714 eth0  Out IP 172.18.160.107.35078 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
14:08:35.188160 eth0  In  IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.35078: NTPv4, Server, length 48
14:08:42.389760 eth0  In  ARP, Request who-has 172.18.160.107 (00:15:5d:c6:5c:b1 (oui Unknown)) tell LuNgoma.mshome.net, length 28
14:08:42.389846 eth0  Out ARP, Reply 172.18.160.107 is-at 00:15:5d:c6:5c:b1 (oui Unknown), length 28
14:08:43.067215 eth0  Out ARP, Request who-has LuNgoma.mshome.net tell 172.18.160.107, length 28
14:08:43.067401 eth0  In  ARP, Reply LuNgoma.mshome.net is-at 00:15:5d:4c:83:21 (oui Unknown), length 28
14:09:10.365238 eth0  Out IP 172.18.160.107.53193 > prod-ntp-4.ntp1.ps5.canonical.com.ntp: NTPv4, Client, length 48
14:09:10.619469 eth0  In  IP prod-ntp-4.ntp1.ps5.canonical.com.ntp > 172.18.160.107.53193: NTPv4, Server, length 48
14:09:18.495764 eth0  Out ARP, Request who-has LuNgoma.mshome.net tell 172.18.160.107, length 28
14:09:18.495966 eth0  In  ARP, Reply LuNgoma.mshome.net is-at 00:15:5d:4c:83:21 (oui Unknown), length 28

### packet_results.txt
Ether / IP / ICMP 172.18.160.107 > 192.178.54.174 echo-request 0 / Raw
Ether / IP / ICMP 192.178.54.174 > 172.18.160.107 echo-reply 0 / Raw
Ether / IP / ICMP 172.18.160.107 > 192.178.54.174 echo-request 0 / Raw
Ether / IP / ICMP 192.178.54.174 > 172.18.160.107 echo-reply 0 / Raw
Ether / IP / ICMP 172.18.160.107 > 192.178.54.174 echo-request 0 / Raw
Ether / IP / ICMP 192.178.54.174 > 172.18.160.107 echo-reply 0 / Raw
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https S
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 SA
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https A
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https PA / Raw
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 A
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 A / Raw
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 PA / Raw
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https A
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https A
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https PA / Raw
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https PA / Raw
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https PA / Raw
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 A
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 PA / Raw
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 PA / Raw
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 PA / Raw
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 PA / Raw
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https A
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https A
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https A
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https A
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https PA / Raw
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https PA / Raw
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https FA
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https FA
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 A
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 A
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 FA
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 A
Ether / IP / TCP 104.18.26.120:https > 172.18.160.107:54282 A
Ether / IP / TCP 172.18.160.107:54282 > 104.18.26.120:https A
Ether / IP / UDP / NTP v4, client
Ether / IP / UDP / NTP v4, server

### tcpdump_results.txt


---

## TERACO_LAB

### teraco_notes.txt
Teraco Data Center Lab

This lab is based on my previous learning about data center infrastructure.

Topics covered:
- Data center networking
- Fiber connectivity
- Structured cabling
- Network redundancy
- Data center security

Key Concepts:

1. Fiber optic cables are used for long distance high-speed connections.
2. Copper cables are used inside buildings.
3. Data centers use redundant power and cooling systems.
4. Network switches connect servers within the rack.

This lab demonstrates understanding of data center networking environments.

---

