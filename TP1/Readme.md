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

* Adresse IP du serveur DHCP : ``

* Adresse IP du serveur DNS : ``


# ☀️ Table de routage # 

* Route par défaut : ``

# II. Go further #

