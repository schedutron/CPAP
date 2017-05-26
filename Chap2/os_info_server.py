#!/usr/bin/env python

from socket import *
from time import ctime
import os

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

infoServSock = socket(AF_INET, SOCK_STREAM)
infoServSock.bind(ADDR)
infoServSock.listen(5)

while 1:
    print 'Waiting for connection...'
    infoCliSock, addr = infoServSock.accept()
    start = "Now you're connected. Type 'date', 'os', 'ls' or 'ls <dir>' to receive info.\n"
    infoCliSock.send(start)
    print "Connected to:", addr
    
    while True:
        data = infoCliSock.recv(BUFSIZ)
        if not data: #client closed the connection
            print #for gap
            break
        print "Requested:", data
        if data == 'date':
            data = ctime()
        elif data == 'os':
            data = os.name
        elif data.startswith('ls'):
            req = data.split()
            if len(req) == 1:
                content = os.listdir(os.curdir)
            else:
                try:
                    content = os.listdir(req[1])
                except:
                    infoCliSock.send('No such directory.')
                    continue
            data = '\n'.join(content)
        else:
            data = "Unrecognized command!"
        infoCliSock.send(str(data))
        
infoServSock.close()
