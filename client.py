
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
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def close(self):
        self.sock.close()

    def send(self, mssg, flsh=False):
        self.sock.sendall(bytes(mssg + '\r\n', 'utf8'))
        if flsh:
            self.sock.recv(1024)

    def recv(self):
        data = self.sock.recv(1024)
        code, mssg = data.decode('utf8').split(' ', 1)
        return code, mssg.strip()

