
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sun Dec  3 11:07:05 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

import os, time, threading
from config import Config
from filemanager import FileManager
from app.printer import Printer

class CInbox(Printer):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.allow_upd = False  # allow self.drawing_thread() to works
        self.upd_itval = Config.load()['refresh_interval']
        FileManager.initdir(user)
        self.iterate()

    def iterate(self):
        choice = self.askdir()
        if choice == 0:
            return
        self.viewdir(choice)
        self.iterate()

    """
    @ comms
    """
    def askdir(self):
        userdir = FileManager.get_user_dir(self.user)
        ls = [os.path.join(userdir, x) for x in os.listdir(userdir)]

        self.greet()
        self.syslog("Available mail directories:")
        for i, d in enumerate(ls):
            if os.path.isdir(d):
                self.syslog(f'    {i+1} - {os.path.basename(d)}')
        self.syslog("You may type '0' to cancel this operation")

        self.askinp("Index of your desired directory: ")
        choice = int(input())
        if choice == 0:
            return 0
        return ls[choice - 1]

    def viewdir(self, targ: str):
        self.greet()

        self.allow_upd = True
        t = threading.Thread(target=self.drawing_thread, args=(targ, ))
        t.start()

        self.syslog("Type in the index of the mail you want to read")
        self.askinp("Your choice: ")
        choice = int(input())
        self.allow_upd = False  # stop updating the mail list

    """
    @ utils
    """
    def greet(self):
        self.scrclr()
        self.gdelog(self.sepbar)
        self.skipln()
        self.gdelog("This is the mail receiving scene.")
        self.gdelog("Be precise at your inputs. Exceptions are not handled.")
        self.skipln()
        self.gdelog(self.sepbar)
        self.skipln()

    """
    @ threading
    """
    def drawing_thread(self, targ: str):
        while True:
            ls = os.listdir(targ)
            if self.allow_upd:
                self.draw(ls)
            else:
                return
            time.sleep(self.upd_itval)

    def draw(self, ls):
        print(ls)

