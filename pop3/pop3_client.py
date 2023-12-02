
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

class Pop3Client(Client):

    def inbox(self, user, pwds):
        # open connection
        self.send(f'USER {user}', flsh=True)
        self.send(f'PASS {pwds}', flsh=True)
        self.send('STAT', flsh=True)

        # get list of messages
        self.send('LIST')
        mlst = self.recv()
        mcnt = int(mlst.split()[1])

        # get mails
        self.send('UIDL', flsh=True)
        for i in range(mcnt):
            self.send(f'RETR {i+1}')
            print(self.recv())

        self.send('QUIT')

