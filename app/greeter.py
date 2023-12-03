
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sat Dec  2 23:05:23 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

from app.printer import Printer
from app.sender import CSender
from app.inbox import CInbox

class CGreeter(Printer):
    def __init__(self):
        super().__init__()
        self.greet()
        self.syslog("This is Schwimmende Mohre Mail Client")
        self.askinp("Your mail address: ")
        self.user = input()
        self.iterate()

    def iterate(self):
        self.scrclr()
        self.gdelog("You logged in as " + self.user)
        self.skipln()
        self.syslog("Options:")
        self.syslog("  0 - Quit")
        self.syslog("  1 - Send mail via SMTP")
        self.syslog("  2 - Read inbox")
        self.askinp("Your choice: ")
        choice = int(input())

        # since I have not tested the efficiency of python switch-case yet
        # so if-else it goes
        if choice == 0:
            self.scrclr()
            return
        elif choice == 1:
            CSender(self.user)
        elif choice == 2:
            CInbox(self.user)
        self.iterate()

    def greet(self):
        self.scrclr()
        self.gdelog(self.sepbar)
        self.skipln()
        self.gdelog("This project was made to show our understanding of SMTP/POP3 protocol,")
        self.gdelog("not to show our application making skill. Thus, the interface of this")
        self.gdelog("program is keep as simple as possible, and thus it's not idiot-proof.")
        self.skipln()
        self.gdelog("Be precise at your inputs. Exceptions are not handled.")
        self.skipln()
        self.gdelog(self.sepbar)
        self.skipln()

