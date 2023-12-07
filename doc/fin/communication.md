
# Communication

Contrary to the impression that implementing a SMTP/POP3 protocol is complicated, it is actually easy & straight-forward. It is, in fact, so exceedingly easy given that we work with [this test mail server](https://github.com/eugenehr/test-mail-server). To implement our own mail client, all we need is to observe how [Thunder Bird](https://www.thunderbird.net) sends mail to (or receives mail from) the mail server, then we replicate exactly that.

Upon observation, we discovered that all SMTP/POP3 operations are accomplished using only plain text, and all of that happen exclusively within the server's standard input/output device (stdin/out). And what can establish input/output streams from a host & a port? That's a **socket**!

To facilitate socket manipulation, we've created a `Client` class that simplifies the socket implementation. A `Client` object establishes an immediate connection to the server upon initialization, then it offers two main functionalities:

1. Sends contents to the server's stdin
2. Receives contents from the server's stdout

Simple as it is, this is all that's needed to implement the SMTP/POP3 protocols, including the protocol for sending binary files. It's worth noting that all communication between this project and the mail server is confined exclusively to the `Client` class.

