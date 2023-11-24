
# smtp/smtp_client.py

To understand how [smtp_client.py](../smtp/smtp_client.py) was implemented, let first see what happen when [Thunder Bird](https://www.thunderbird.net) sends a mail to [our server](https://github.com/eugenehr/test-mail-server).

After the email was sent, the server's log looks like this:

```
[09:14:47.350] [worker-0] [INFO ] r.e.t.SMTPHandler:57 - Client connected: /127.0.0.1:51268
[09:14:47.351] [worker-0] [DEBUG] r.e.t.SMTPHandler:64 - >>: 220 Test Mail Server
[09:14:47.368] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: EHLO [127.0.0.1]
[09:14:47.369] [worker-0] [DEBUG] r.e.t.SMTPHandler:186 - >>: 250 OK
[09:14:47.395] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: MAIL FROM:<iluv@example.com>
[09:14:47.395] [worker-0] [DEBUG] r.e.t.SMTPHandler:186 - >>: 250 sender <iluv@example.com> OK
[09:14:47.396] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: RCPT TO:<kumiko@some.where>
[09:14:47.396] [worker-0] [DEBUG] r.e.t.SMTPHandler:186 - >>: 250 recipient <kumiko@some.where> OK
[09:14:47.396] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: DATA
[09:14:47.397] [worker-0] [DEBUG] r.e.t.SMTPHandler:186 - >>: 354 enter mail, end with line containing only "."
[09:14:47.397] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Message-ID: <b73864a6-6e6b-4bd4-8bec-89aab3bc6a27@example.com>
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Date: Sat, 11 Nov 2023 09:14:47 +0700
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: MIME-Version: 1.0
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: User-Agent: Mozilla Thunderbird
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Content-Language: en-US
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: To: kumiko@some.where
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: From: iluvgirlswithglasses <iluv@example.com>
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Subject: Eupho
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Content-Type: text/plain; charset=UTF-8; format=flowed
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Content-Transfer-Encoding: 7bit
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: 
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Euphonium!
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: 
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: .
[09:14:47.423] [worker-0] [INFO ] r.e.t.SMTPHandler:138 - Message saved to [/home/mika/r/repos/mail-client/3rd-party/.test-mail-server/kumiko@some.where/20231111091447416.msg]
[09:14:47.423] [worker-0] [DEBUG] r.e.t.SMTPHandler:186 - >>: 250 371 bytes accepted
```

By looking at what the server's stdin received, we know exactly what our mail client needs so as to send a mail like [Thunder Bird](https://www.thunderbird.net):

```
[09:14:47.368] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: EHLO [127.0.0.1]
[09:14:47.395] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: MAIL FROM:<iluv@example.com>
[09:14:47.396] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: RCPT TO:<kumiko@some.where>
[09:14:47.396] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: DATA
[09:14:47.397] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Message-ID: <b73864a6-6e6b-4bd4-8bec-89aab3bc6a27@example.com>
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Date: Sat, 11 Nov 2023 09:14:47 +0700
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: MIME-Version: 1.0
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: User-Agent: Mozilla Thunderbird
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Content-Language: en-US
[09:14:47.414] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: To: kumiko@some.where
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: From: iluvgirlswithglasses <iluv@example.com>
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Subject: Eupho
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Content-Type: text/plain; charset=UTF-8; format=flowed
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Content-Transfer-Encoding: 7bit
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: 
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: Euphonium!
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: 
[09:14:47.415] [worker-0] [DEBUG] r.e.t.SMTPHandler:120 - <<: .
```

And that is precisely, line-to-line, what `smtp_client.py` does. When you envoke `SmtpClient.send_mail(*args)`, it sends a mail by writing these lines to the server's stdin:

1. `EHLO [127.0.0.1]`: Verifies the host address
2. `MAIL FROM: someone@somewhere`: Indicates who the sender is
3. For every address in receivers list, it writes:
    - `RCPT TO: receiver@somewhere.else`: Indicates the recipient
4. `DATA`: Indicates that the mail's content begins at the next line
5. Writes every line of the mail's content (see [smtp_client.py](../smtp/smtp_client.py) line 45-66)

