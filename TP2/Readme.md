# TP2 : Environnement virtuel #

# I. Topologie réseau #

# Compte-rendu

* Carte Résaux :
```
[florentinfallon@node2~]$ ip a

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
        valid_lft forever preferred_lft forever
2: enp0s1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 100
0
    link/ether 56:9a:12:3b:92:cf brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global nopref ixroute enp0s1
        valid_lft forever prefereed_lft forever
    inet6 fe80: :549a:12ff:fe3b:92cf/64 scope link
        valid_lft forever preferred_lft forever
```

* Table de routage :
```
[florentinfallon@node2~]$ ip route show
default via 10.1.1.254 dev enp0s1 proto static metric 100
10.1.1.0/24 dev enp0s1 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0 via 10.1.1.254 dev enp0s1 proto static metric 100
```

# II. Interlude accès internet #

# III. Services réseau #

# 1. DHCP #

# 2. Web web web #