#!/usr/bin/env python

from socket import *

HOST = raw_input("Enter host: ")
if not HOST:
    HOST = "localhost"
PORT = raw_input("Enter port: ")
if not PORT:
    PORT = 9000
else:
    PORT = int(PORT)
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('-|-> ')
    if not data:
        break
    tcpCliSock.send("%s\r\n" % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()
