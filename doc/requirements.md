
# API Requirements

## 1. Acknowledgements

The 7-th requirement of our project needs an asynchronous system, which means: Our program needs to wait for user input & load mails **simultaneously**. That's called multi-threading. And I am in charge of making the Graphical User Interface, consequently the said asynchronous system.

In order to build such system, I need the mail receiver functions to work as I demand. This document addresses what I want those functions do. And please, **DO NOT** modify the input/output of those functions.

## 2. Mail downloading fuction

Prototype:

```py
"""
Using `(host, port)` as the POP3 socket,
save all mails that belong to `user_address` into `save_path`.

The returned list `ls` contains the path of all downloaded mail. It should looks like this:
    ls = [
        './saved_mail/someone@example.com/Inbox/1.msg',
        './saved_mail/someone@example.com/Spam/2.msg',
        ...
    ]
"""
def download(host: str, port: int, user_address: str, save_path: str):
    # Do whatever you need here to download the emails from the given parameters.
    # You may construct your socket object via `host` and `port`, then do anything necessary.
    # Just make sure the job is done.
    # And, most importantly, DO NOT touches stdin/stdout. That would mess up the whole GUI.
    # In other words, DO NOT use print()/input().
    return ls
```

## 3. Mail reading function

Prototype:

```py
"""
Take a path of a mail, read that mail.
There are no limit of what this function can or cannot do.
"""
def view_mail(path: str):
    print to console the mail's content

    for each attachments:
        ask if user want to save this
        ask save directory
        save the attachment to file
```
