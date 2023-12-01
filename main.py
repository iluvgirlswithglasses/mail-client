
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sat Nov 11 15:23:27 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

import os, sys
from client import Client
from smtp.smtp_client import SmtpClient

def main():
    rcpt = {
        'To': ['mika@example.com'],
        'Cc': ['iluv@example.com'],
        'Bcc': ['tmp@here.com', 'there@there.com']
    }
    mssg = ['', 'This mail has four attachments']
    attc = ['config.json', 'LICENSE', 'README.md', '.gitignore']

    c = SmtpClient('localhost', 4000)
    c.send_mail('iluv@admin', rcpt, 'Four attachments mail', mssg, attc)


if __name__ == "__main__":
    main()

