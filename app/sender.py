
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Sun Dec  3 11:06:26 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

from app.printer import Printer
from smtp.smtp_client import SmtpClient
from config import Config

class CSender(Printer):
    def __init__(self, user):
        super().__init__()
        self.greet()
        rcpt = self.ask_rcpt()
        subj = self.ask_subj()
        mssg = self.ask_mssg()
        attc = self.ask_attc()

        conf = Config.load()
        smtp = SmtpClient(conf['server_host'], conf['server_smtp_port'])
        smtp.send_mail(user, rcpt, subj, mssg, attc)

        self.skipln()
        self.gdelog("Mail sent successfully!")
        self.gdelog("Press <Return> to exit.")
        input()

    def ask_rcpt(self):
        self.syslog("Recipients list (seperate via empty spaces, or skip via empty line):")

        self.askinp("To: ")
        rpto = input().split()
        self.askinp("CC: ")
        rpcc = input().split()
        self.askinp("BCC: ")
        rpbc = input().split()

        return {
            'To': rpto,
            'Cc': rpcc,
            'Bcc': rpbc
        }

    def ask_subj(self):
        self.syslog("Your mail's subject:")
        self.askinp("Subject: ")
        return input()

    def ask_mssg(self):
        self.syslog("Enter your mail, end with line containing only '.':")
        return [''] + self.multiline_ask() + ['']   # there's padding

    def ask_attc(self):
        self.syslog("Attachments list (end with line containing only '.':)")
        return self.multiline_ask()

    def multiline_ask(self):
        mssg = []
        while True:
            line = input()
            if line == '.':
                return mssg # does not contain the final dot, this is deliberate
            mssg.append(line)

    def greet(self):
        self.scrclr()
        self.gdelog(self.sepbar)
        self.skipln()
        self.gdelog("This is the mail composing scene.")
        self.gdelog("Be precise at your inputs. Exceptions are not handled.")
        self.skipln()
        self.gdelog(self.sepbar)
        self.skipln()

