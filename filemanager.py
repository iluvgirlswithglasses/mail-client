
"""
author:     iluvgirlswithglasses
github:     https://github.com/iluvgirlswithglasses
created:    Mon Dec  4 16:13:38 2023
tab-width:  4 spaces

 /\_/\
( o.o )
 > ^ <

I firmly believe in the supremacy of the Euphonium
FYI I use Debian
"""

import os, sys

class FileManager:
    DirectoryList = ['Inbox', 'Important', 'Project', 'Work', 'Spam']
    SaveDirectory = 'saved_mail'

    @staticmethod
    def initdir(user):
        for i in FileManager.DirectoryList:
            targ = f'{FileManager.SaveDirectory}/{user}/{i}'
            if not os.path.exists(targ):
                os.makedirs(targ)

    @staticmethod
    def get_user_dir(user):
        return f'{FileManager.SaveDirectory}/{user}'

