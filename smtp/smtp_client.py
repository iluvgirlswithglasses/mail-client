
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sat Nov 11 15:39:41 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

from typing import Dict, List
from datetime import datetime
from client import Client
from config import Config
import base64
import os

class SmtpClient(Client):
    """
    @ complete operations

    parameters:
        strt:   address of the sender (start)
        dest:   address of the receiver(s) (destinations)
            format: { 'to/cc/bcc', {receivers} }
        mssg:   message
        attc:   attachments' path
    """
    def send_mail(self, strt: str, dest: Dict[str, List[str]], subj: str, mssg: List[str], attc: List[str]):
        """Send a whole mail"""
        # verification
        self.send('EHLO [localhost]', flsh=True)

        # sender/recipients informations
        self.send(f'MAIL FROM: <{strt}>', flsh=True)
        for mode, recipients in dest.items():
            for rcpt in recipients:
                self.send(f'RCPT TO: <{rcpt}>', flsh=True)

        # headers
        cnfg = Config.load()
        self.send('DATA', flsh=True)

        boundary = f'------------{int(datetime.timestamp(datetime.now()))}'
        self.send(f'Content-Type: multipart/mixed; boundary="{boundary}"')
        self.send(f'Message-ID: {self.gen_mssg_id(strt)}')
        self.send(f'Date: {self.gen_cdate()}')
        self.send(f'MIME-Version: {cnfg["mime_version"]}')
        self.send(f'User-Agent: {cnfg["user_agent"]}')
        self.send(f'Content-Language: {cnfg["content_language"]}')

        # to/cc/bcc/from
        for mode, recipients in dest.items():
            if mode not in ['To', 'Cc']:
                continue
            self.send(f'{mode}: {", ".join(recipients)}')
        self.send(f'From: {strt}')

        # subject/content declarations
        self.send(f'Subject: {subj}')
        self.send('')
        self.send(f'This is a multi-part message in MIME format.')

        # text content
        self.send(f'--{boundary}')
        self.send(f'Content-Type: {cnfg["content_type"]}')
        self.send(f'Content-Transfer-Encoding: {cnfg["content_transfer_encoding"]}')
        for line in mssg:
            self.send(line)

        # attachments
        for item in attc:
            self.send_attachment(boundary, item)

        self.send(f'--{boundary}--')
        self.send('.')

    """
    @ generators
    """
    def gen_mssg_id(self, strt: str):
        """Give the message an ID"""
        return '{}-{}'.format(datetime.now().timestamp(), strt)

    def gen_cdate(self):
        """Return current date in C format"""
        return datetime.now().strftime("%a %b %d %H:%M:%S %Y")

    """
    @ attachment
    """
    def send_attachment(self, boundary: str, attc: str):
        file_name = os.path.basename(attc)
        if os.path.getsize(attc) > 3 * 1024 * 1024:
            print(f"Skipping attachment '{file_name}' as it is larger than 3MB.")
            return

        # header
        self.send(f'--{boundary}')
        self.send(f'Content-Type: application/octet-stream; name="{file_name}"')
        self.send(f'Content-Disposition: attachment; filename="{file_name}"')
        self.send(f'Content-Transfer-Encoding: base64')
        self.send('')

        # content
        with open(attc, 'rb') as f:
            f = base64.b64encode(f.read()).decode('utf-8')
            for i in range(0, len(f), 72):
                chunk = f[i: i+72]
                self.send(chunk)
        self.send('')

