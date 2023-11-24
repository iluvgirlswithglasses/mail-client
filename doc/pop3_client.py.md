
After [Thunder Bird](https://www.thunderbird.net) loaded a mail to `iluv@example.com`'s inbox, the server's log looks like this:

```
[19:05:15.029] [worker-1] [INFO ] r.e.t.POP3Handler:59 - Client connected: /127.0.0.1:37476
[19:05:15.030] [worker-1] [DEBUG] r.e.t.POP3Handler:66 - >>: +OK Test Mail Server
[19:05:15.036] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: CAPA
[19:05:15.037] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
UIDL
.
[19:05:15.037] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: USER iluv@example.com
[19:05:15.040] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
[19:05:17.370] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: PASS 
[19:05:17.371] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
[19:05:17.385] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: STAT
[19:05:17.387] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK 4 1436
[19:05:17.389] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: LIST
[19:05:17.389] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
1 357
2 357
3 357
4 365
.
[19:05:17.390] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: UIDL
[19:05:17.390] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
1 20231115132058121.msg
2 20231115140959481.msg
3 20231124190243550.msg
4 20231124190501328.msg
.
[19:05:17.390] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: DELE 1
[19:05:17.391] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
[19:05:17.391] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: DELE 2
[19:05:17.391] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
[19:05:17.392] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: DELE 3
[19:05:17.392] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
[19:05:17.393] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: RETR 4
[19:05:17.396] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK 365
Message-ID: 1700827501.283877-iluv@here
Date: Fri Nov 24 19:05:01 2023
MIME-Version: 1.0
User-Agent: Schwimmende Mohre Mail Client
Content-Language: en-US
To: mika@example.com
Cc: iluv@example.com
From: iluv@here
Subject: Sample Subject
Content-Type: text/plain; charset=UTF-8; format=flowed
Content-Transfer-Encoding: 7bit

Another sample paragraph

.
[19:05:17.410] [worker-1] [DEBUG] r.e.t.POP3Handler:111 - <<: QUIT
[19:05:17.412] [worker-1] [DEBUG] r.e.t.POP3Handler:317 - >>: +OK
[19:05:17.413] [worker-1] [INFO ] r.e.t.POP3Handler:76 - Client disconnected: /127.0.0.1:37476
```

Look carefully at those five commands [Thunder Bird](https://www.thunderbird.net) sent:

- `UIDL`
- `DELE 1`
- `DELE 2`
- `DELE 3`
- `RETR 4`

With the first command, [Thunder Bird](https://www.thunderbird.net) asks the server to list all the mails which `iluv@example.com` has in their inbox.

With 3 `DELE` commands, the server is asked to delete those 3 mails:

- `1 20231115132058121.msg`
- `2 20231115140959481.msg`
- `3 20231124190243550.msg`

Finally, the `RETR` command is to load the fourth indexed mail. In response, the mail server replied with this:

```
Message-ID: 1700827501.283877-iluv@here
Date: Fri Nov 24 19:05:01 2023
MIME-Version: 1.0
User-Agent: Schwimmende Mohre Mail Client
Content-Language: en-US
To: mika@example.com
Cc: iluv@example.com
From: iluv@here
Subject: Sample Subject
Content-Type: text/plain; charset=UTF-8; format=flowed
Content-Transfer-Encoding: 7bit

Another sample paragraph

.
```

Your job is to replicate exactly what [Thunder Bird](https://www.thunderbird.net) did there.

