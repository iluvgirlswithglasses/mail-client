
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Wed Nov 15 14:01:03 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

import json

class Config:
    @staticmethod
    def load():
        f = open('config.json', 'r')
        return json.loads(f.read())

