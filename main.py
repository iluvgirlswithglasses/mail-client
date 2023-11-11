
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sat Nov 11 15:23:27 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

import os, sys
from client import Client

if __name__ == "__main__":
    c = Client()

    c.connect('localhost', 4000)
    print(c.recv())

    c.send('EHLO [localhost]')
    print(c.recv())

