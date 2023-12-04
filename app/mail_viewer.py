
from pop3.separator import Separator
from app.printer import Printer

class MailViewer(Printer):

    def view_mail(self, response):
        content, attac = Separator.separate_content(response)

        self.syslog('-------------------')
        print(content)
        self.syslog('-------------------')

        for i, (filename, content) in enumerate(attac, start=1):
            self.syslog(f"Attachment {i}:")
            self.syslog(f"Filename: {filename}")

            self.askinp("Do you want to download it (y/n)?: ")
            ans = input()

            if ans.lower() == 'y' or ans.lower() == 'yes':
                self.askinp("Enter path: ")
                save_path = input()
                Separator.decode_attachment(content, save_path)
                self.syslog("File saved successfully")
                self.syslog("------------------------------")
            elif ans.lower() == 'n' or ans.lower() == 'no':
                continue

