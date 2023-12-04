
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Mon Dec  4 22:28:51 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

import os

class History:
    @staticmethod
    def load():
        if not os.path.isfile('history'):
            return []
        ls = []
        with open('history', 'r') as f:
            for line in f:
                if len(line) == 0:
                    continue
                ls.append(line)
        return ls

    @staticmethod
    def write(line):
        with open('history', 'a') as f:
            f.write(line + '\n')

