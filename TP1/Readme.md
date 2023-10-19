# TP1 : Maîtrise réseau du poste #

# I. Basics #

# ☀️ Carte réseau WiFi #

* L'adresse MAC de la carte wifi :

```
florentinfallon@MacBook-Pro-de-Florentin ~ % ifconfig
[...]
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 9c:3e:53:8c:90:1b
	inet6 fe80::87:89c1:dd27:e892%en0 prefixlen 64 secured scopeid 0xc 
	inet 10.33.76.1 netmask 0xfffff000 broadcast 10.33.79.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
[...]
```

* Adresse MAC : `9c:3e:53:8c:90:1b`
* Adresse IP : `10.33.76.1`
* Masque sous-réseau CIDR : `/20`
* Masque de sous-réseau décimal : `255.255.240.0`

# ☀️ Déso pas déso #

* Adresse réseau LAN : `10.33.76.0`

* Adresse Broadcast : `10.33.79.255`

* Nombre d'IP dans le réseau : `4094`

# ☀️ Hostname #

* Hostname : `florentinfallon@MacBook-Pro-de-Florentin ~ % hostname MacBook-Pro-de-Florentin.local`

# ☀️ Passerelle du réseau #

```
florentinfallon@MacBook-Pro-de-Florentin ~ % route get default
   route to: default
destination: default
       mask: default
    gateway: 10.33.79.254
  interface: en0
      flags: <UP,GATEWAY,DONE,STATIC,PRCLONING,GLOBAL>
 recvpipe  sendpipe  ssthresh  rtt,msec    rttvar  hopcount      mtu     expire
       0         0         0         0         0         0      1500         0 

```

* Adresse IP de la passerelle : `gateway: 10.33.79.254`

* Adresse MAC de la passerelle : 

```
florentinfallon@MacBook-Pro-de-Florentin ~ % arp -a || 10.33.79.255

? (10.33.79.254) at 7c:5a:1c:d3:d8:76 on en0 ifscope [ethernet]
````

# ☀️ Serveur DHCP et DNS #

* Adresse IP du serveur DHCP : 
```
florentinfallon@MacBook-Pro-de-Florentin ~ % ipconfig getpacket en0
dhcp_message_type (uint8): ACK 0x5
server_identifier (ip): 10.33.79.254
```

* Adresse IP du serveur DNS : 
```
florentinfallon@MacBook-Pro-de-Florentin Desktop % scutil --dns                           
DNS configuration

resolver #1
  nameserver[0] : 8.8.8.8
  nameserver[1] : 1.1.1.1
```


# ☀️ Table de routage # 

* Route par défaut : 
```
florentinfallon@MacBook-Pro-de-Florentin ~ % netstat -nr
florentinfallon@MacBook-Pro-de-Florentin Desktop % netstat -nr
Routing tables

Internet:
Destination        Gateway            Flags               Netif Expire
default            10.33.79.254       UGScg                 en0       
10.33.64/20        link#12            UCS                   en0      !
```

# II. Go further #

# ☀️ Hosts ? #
* Le nom :
```
florentinfallon@MacBook-Pro-de-Florentin Desktop % sudo hostname b2.hello.vous 

florentinfallon@MacBook-Pro-de-Florentin Desktop % hostname
b2.hello.vous
```

* IP :
```
florentinfallon@MacBook-Pro-de-Florentin Desktop % sudo nano /etc/hosts
Password:
```

* Test :
```
florentinfallon@MacBook-Pro-de-Florentin Desktop % ping b2.hello.vous
PING b2.hello.vous (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: icmp_seq=0 ttl=56 time=23.201 ms
```

# ☀️ Go mater une vidéo youtube et déterminer, pendant qu'elle tourne... #
```
florentinfallon@MacBook-Pro-de-Florentin Desktop % netstat -an       
tcp4       0      0  10.33.76.1.62241       91.68.245.76.443       ESTABLISHED
```

Pour l'IP, le port connéctés et le port local, [Voici la capture Wireshark](Youtube.pcapng)

# ☀️ Requêtes DNS #

* IP ynov.com

```
florentinfallon@MacBook-Pro-de-Florentin Desktop % nslookup
> ynov.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	ynov.com
Address: 104.26.11.233
```

* 174.43.238.89

```
florentinfallon@MacBook-Pro-de-Florentin Desktop % nslookup
> 174.43.238.89
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
89.238.43.174.in-addr.arpa	name = 89.sub-174-43-238.myvzw.com.
```

# ☀️ Hop hop hop #

```
florentinfallon@MacBook-Pro-de-Florentin Desktop % traceroute www.ynov.com
traceroute: Warning: www.ynov.com has multiple addresses; using 104.26.10.233
traceroute to www.ynov.com (104.26.10.233), 64 hops max, 52 byte packets
 1  10.33.79.254 (10.33.79.254)  11.405 ms  4.334 ms  3.847 ms
 2  145.117.7.195.rev.sfr.net (195.7.117.145)  4.406 ms  6.609 ms  3.732 ms
 3  * * *
 4  196.224.65.86.rev.sfr.net (86.65.224.196)  5.920 ms  7.211 ms  5.750 ms
 5  68.150.6.194.rev.sfr.net (194.6.150.68)  13.148 ms  15.015 ms
    12.148.6.194.rev.sfr.net (194.6.148.12)  14.291 ms
 6  12.148.6.194.rev.sfr.net (194.6.148.12)  13.318 ms  16.465 ms  12.538 ms
 7  141.101.67.48 (141.101.67.48)  13.679 ms  13.613 ms  14.125 ms
 8  172.71.124.4 (172.71.124.4)  12.875 ms
    172.71.120.4 (172.71.120.4)  18.876 ms
    172.71.132.4 (172.71.132.4)  16.024 ms
 9  104.26.10.233 (104.26.10.233)  13.080 ms  12.739 ms  13.741 ms
```

# ☀️ IP publique #

* Adresse IP de la passerelle : `gateway: 10.33.79.254`

# ☀️ Scan réseau #

* Voici le scan réseaux dans le LAN :

```

```

# III. Le requin #

# ☀️ Capture ARP #

* Voici un échange ARP : [ARP Wireshark](arp.pcapng)

# ☀️ Capture DNS #

* Voici la requête DNS : [Via Wireshark](dns.pcapng), J'ai effectuez un filtre `dns` dans Wireshark pour mieux rechercher la requête DNS

Via le terminal :

```
florentinfallon@MacBook-Pro-de-Florentin Desktop % nslookup www.thenorthface.fr
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
www.thenorthface.fr	canonical name = www.thenorthface.eu.edgekey.net.
www.thenorthface.eu.edgekey.net	canonical name = e11781.b.akamaiedge.net.
Name:	e11781.b.akamaiedge.net
Address: 104.85.36.234
```

# ☀️ Capture TCP #

* Voici le résultat TCP : [TCP Wireshark]()

Avec tous les éléments demandés un 3-way handshake, un peu de trafic et la fin de la connexion.