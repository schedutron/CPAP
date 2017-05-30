#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    while True:
        print "Waiting for connection..."
        tcpCliSock, addr = tcpSerSock.accept()
        print "... connection from:", addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (ctime(), data))
        tcpCliSock.close()
    tcpSerSock.close()
except KeyboardInterrupt:
    pass
finally:
    print "\nShutting down server..."
    tcpSerSock.close()
