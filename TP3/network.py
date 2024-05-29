from socket import gethostbyname
from os import system
from psutil import net_if_addrs
from sys import argv 

mode = argv[1]
arg = argv[2] if len(argv) > 2 else ""

def lookup(domaine):
    return gethostbyname(domaine)

def ping(q):
    return "UP" if system("ping " + q + " > /dev/null") == 0 else "DOWN"

def ip():
    return net_if_addrs()["en0"][2].address

radiou = ""

match argv[1]:
    case "lookup":
       radiou = lookup(arg)
    case "ping":
        radiou = ping(arg)
    case "ip":
        radiou = ip()
    case _:
        radiou = f"{argv[1]} is not an available command. Déso."

print(radiou)