
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
from app.mail_viewer import MailViewer
from pop3.pop3_client import Pop3Client

class CInbox(Printer):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.allow_upd = False  # allow self.drawing_thread() to works
        self.upd_itval = Config.load()['refresh_interval']
        FileManager.initdir(user)
        self.download_mails()
        self.iterate()

    def iterate(self):
        choice = self.askdir()
        if choice == 0:
            return
        self.viewdir(choice)
        self.iterate()

    def download_mails(self):
        conf = Config.load()
        c = Pop3Client(conf['server_host'], conf['server_pop3_port'])
        c.inbox(self.user, '')

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
        self.syslog("\n\n\nAll mail in this directory:")
        choice = int(input())
        self.allow_upd = False  # stop updating the mail list
        self.viewmail(targ, choice)

    def viewmail(self, targ: str, indx: int):
        self.scrclr()
        if indx == 0:
            return

        # read mssg
        mailname = os.listdir(targ)[indx - 1]
        mssg = ""
        with open(os.path.join(targ, mailname), 'r') as f:
            mssg = f.read()

        # show mssg
        viewer = MailViewer()
        viewer.view_mail(mssg)

        # wait for exit
        self.skipln()
        self.askinp("Press <Return> to continue: ")
        input()

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
        CInbox.move_cursor(14, 1)   # mail list position
        for i, f in enumerate(ls):
            print(f'    {i + 1}\t{f}')
        CInbox.move_cursor(10, 13)  # input prompt position
        print('', end='\r\n--> ')

    @staticmethod
    def move_cursor(y, x):
        print("\033[%d;%dH" % (y, x), end="")

