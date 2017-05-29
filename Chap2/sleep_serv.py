#!/usr/bin/env python

from socket import *

HOST = ''
PORT = 6002
ADDR = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
#this is not a concurrent (is that the appropriate word?) server yet...

while True:
    print "\nWaiting for connection..."
    client, client_address = server.accept()
    print "Connected to %s:%s." % client_address

    while True:
        msg = client.recv(1024)
        if not msg:
            break
        else:
            sec = msg
            msg = "sleep(%s)" % sec
            tup = client_address+(sec,)
            print "%s:%s requested sleep for %s seconds." % tup
            client.send(msg)
    client.close()
    print "%s:%s disconnected." % client_address
server.close() #not really used
