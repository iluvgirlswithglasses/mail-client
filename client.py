
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sat Nov 11 10:10:25 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

import socket

class Client:
    def __init__(self, host, port, bfsz=2**20, verbose=False):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.bfsz = bfsz
        if verbose:
            print(self.recv())
        else:
            self.recv()

    def close(self):
        self.sock.close()

    def send(self, mssg, flsh=False):
        self.sock.sendall(bytes(mssg + '\r\n', 'utf8'))
        if flsh:
            self.sock.recv(self.bfsz)

    def recv(self):
        data = self.sock.recv(self.bfsz)
        mssg = data.decode('utf8')
        return mssg

