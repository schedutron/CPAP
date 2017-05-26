#!/usr/bin/env python

from socket import *

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print "Waiting for connection..."
    tcpCliSock, addr = tcpSerSock.accept()
    print "... connection from:", addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(data)
    tcpCliSock.close()
tcpSerSock.close()
