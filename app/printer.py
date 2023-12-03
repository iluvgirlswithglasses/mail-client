
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sat Dec  2 20:35:21 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

import os
from colorama import Fore, Back, Style

class Printer:

    def __init__(self):
        self.sepbar = '-' * 70

    def scrclr(self):
        # always reserve the first line
        os.system('clear')
        print()

    def skipln(self):
        print(Style.RESET_ALL)

    def syslog(self, msg: str):
        # usage: show system text
        print(Fore.GREEN + msg + Style.RESET_ALL)

    def gdelog(self, msg: str):
        # usage: show guidance (note) text
        print(Fore.YELLOW + msg + Style.RESET_ALL)

    def askinp(self, msg: str):
        # usage: ask for user's input
        print(Fore.CYAN + msg + Style.RESET_ALL, end='')

