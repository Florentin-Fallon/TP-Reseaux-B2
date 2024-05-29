# TP3 DEV : Python et réseau #

# I. Ping #

# 🌞 ping_simple.py #

Voici le résultat du ping sur l'ip 8.8.8.8 :

```shell
florentinfallon@MacBook-Pro-de-Florentin TP-DEV % /usr/local/bin/python3 /Users/florentinfallon/Documents/B2/Réseaux/TP-DEV/TP-Dev/TP3/ping_simple.py
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=114 time=27.659 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=114 time=24.890 ms
```

Voici le fichier avec le code .py :

[ping_simple.py](ping_simple.py)

# 🌞 ping_arg.py #

Voici le résultat du ping sur l'ip 8.8.8.8 :

```shell
florentinfallon@MacBook-Pro-de-Florentin TP3 % python3 ping_arg.py 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=114 time=21.215 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=114 time=27.429 ms
```

Voici le fichier avec le code .py :

[ping_arg.py](ping_arg.py)

# 🌞 is_up.py #

Voici le résultat pour effectuer le UP ou le DOWN :

```
florentinfallon@MacBook-Pro-de-Florentin TP3 % python3 is_up.py 8.8.8.8
UP
```

Voici le fichier avec le code .py :

[is_up.py](is_up.py)

# II. DNS

# 🌞 lookup.py

Voici le résultat :

```shell
florentinfallon@MacBook-Pro-de-Florentin TP3 % python3 lookup.py ynov.com
104.26.11.233
```

Voici le code pour trouver l'ip du nom de domaine donner en argument :

[lookup.py](lookup.py)

# III. Get your IP

Installation de psutil : 

```shell
florentinfallon@MacBook-Pro-de-Florentin TP3 % pip3 install psutil
Collecting psutil
Installing collected packages: psutil
Successfully installed psutil-5.9.6
```

# 🌞 get_ip.py

voici mon adresse Mac :

```shell
florentinfallon@MacBook-Pro-de-Florentin TP3 % python3 get_ip.py
9c:3e:53:8c:90:1b
```

Voici le code pour trouver cette fameuse adresse Mac :

[get_ip.py](get_ip.py)

# IV. Mix

# 🌞 network.py

Voici les résultats avec un seul print() :

```shell
florentinfallon@MacBook-Pro-de-Florentin TP3 % python3 network.py ip
fe80::c6e:383:3539:ad21%en0

florentinfallon@MacBook-Pro-de-Florentin TP3 % python3 network.py lookup shein.com
52.39.206.44

florentinfallon@MacBook-Pro-de-Florentin TP3 % python3 network.py ping 8.8.8.8
^CUP

florentinfallon@MacBook-Pro-de-Florentin TP3 % python3 network.py ka          
 is not an available command. Déso.
```

# V. Deploy

