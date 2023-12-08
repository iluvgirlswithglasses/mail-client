
# Inbox Refresh

The seventh requirement of this project is to automatically refresh the inbox at a fixed interval—which is specified in `config.json`. This functionality is achieved via two modules:

## Console Manipulator

This is a console application. And if the application needs to update the inbox while waiting for user input, it needs to render text onto the console without interrupting the user's cursor. A manipulator is, therefore, provided to accomplish this.

## Threading Manager

A thread is spawned to automatically download new mails from the mail server. After each download, it utilizes the Console Manipulator to render the mails onto the screen.

## Note

While these two mentioned modules should be implemented in two separated files; they were, in fact, all written within the inbox viewer module. This is malpratice, and it happened due to improper planning. However, it currently functions flawlessly. So unless extensions are needed, I am not fixing it.

