from sys import argv
from os import system

print("UP" if system("ping " + argv[1] + " > /dev/null") == 0 else "DOWN")