#!/usr/bin/env python

from socket import *

HOST = raw_input('Enter host: ')
if not HOST:
    HOST = 'localhost'
PORT = int(raw_input('Enter port: '))
if not PORT:
    PORT = 7000

BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
print tcpCliSock.recv(1024)

while True:
    data = raw_input('-|-> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpCliSock.close()
