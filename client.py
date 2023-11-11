
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
    def __init__(self):
        self.sock = None

    def connect(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def is_connected(self):
        return self.sock is not None

    def close(self):
        if self.is_connected():
            self.sock.close()

    def send(self, mssg):
        if self.sock is None:
            return
        self.sock.sendall(bytes(mssg + '\r\n', 'utf8'))

