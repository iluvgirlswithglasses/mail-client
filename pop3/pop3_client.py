
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sat Dec  2 18:28:11 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

from client import Client
from filemanager import FileManager
from pop3.classifier import Classifier
from pop3.separator import Separator

class Pop3Client(Client):

    def inbox(self, user, pwds):
        # open connection
        self.send(f'USER {user}', flsh=True)
        self.send(f'PASS {pwds}', flsh=True)
        self.send('STAT', flsh=True)

        # get list of messages
        self.send('LIST')
        mlst = self.recv().split('\r\n')[1:-2]  # cut of the first & last item

        # get mails
        self.send('UIDL', flsh=True)
        for i in mlst:
            index, id = i.split()
            self.send(f'RETR {index}')
            mssg = self.recv()
            cate = Classifier.classify_email(mssg)
            name = f'{Separator.get_subject(mssg)} ({id}).msg'
            self.write_down(mssg, f'{FileManager.get_user_dir(user)}/{cate}/{name}')

        self.send('QUIT')

    def write_down(self, mssg: str, path: str):
        f = open(path, "w")
        f.write(mssg)
        f.close()

