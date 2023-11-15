
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
        self.ehlo('localhost')

        # sender/recipients informations
        self.send(f'MAIL FROM:{strt}')
        for mode, recipients in dest.items():
            for rcpt in recipients:
                self.send(f'RCPT TO:{rcpt}')

        # headers
        self.putcmd('DATA')
        self.send(f'Message-ID: {self.gen_mssg_id(strt)}')
        self.send(f'Date: {self.gen_cdate()}')
        self.send(f'MIME-Version: {self.__get_mime_version()}')
        self.send(f'User-Agent: {self.__get_user_agent()}')
        self.send(f'Content-Language: {self.__get_content_language()}')

        # to/cc/bcc/from
        for mode, recipients in dest.items():
            if mode not in ['To', 'Cc']:
                continue
            self.send(f'{mode}: {", ".join(recipients)}')
        self.send(f'From: {strt}')

        # subject/content declarations
        self.send(f'Subject: {subj}')
        self.send(f'Content-Type: {self.__get_content_type()}')
        self.send(f'Content-Transfer-Encoding: {self.__get_content_transfer_encoding()}')

        # contents
        for line in mssg:
            self.send(line)

        # attachments

    """
    @ protocol components
    """
    def ehlo(self, host):
        """Perform EHLO verification"""
        self.putcmd('EHLO', f'[{host}]')

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
    @ constants

    these should be clarified in config.xml
    """
    def __get_mime_version(self):
        return '1.0'

    def __get_user_agent(self):
        return 'Schwimmende Mohre Mail Client'

    def __get_content_language(self):
        return 'en-US'

    def __get_content_type(self):
        return 'text/plain; charset=UTF-8; format=flowed'

    def __get_content_transfer_encoding(self):
        return '7bit'

    """
    @ tools
    """
    def putcmd(self, cmd, args=''):
        """Send a command to the server."""
        if args == '':
            s = cmd
        else:
            s = f'{cmd} {args}'
        if '\r' in s or '\n' in s:
            s = s.replace('\n', '\\n').replace('\r', '\\r')
            raise ValueError('Command contains prohibited characters')
        self.send(s)

