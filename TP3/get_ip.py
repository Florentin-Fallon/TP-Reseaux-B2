from psutil import net_if_addrs
from sys import argv 

print(net_if_addrs()["en0"][1][1])