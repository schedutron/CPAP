#!usr/bin/env python

from socket import *

HOST = 'time.nist.gov' #got this from stackoverflow
PORT = getservbyname('daytime', 'tcp') #udp not working as of this writing :(
BUFSIZ = 1024
ADDR = (HOST, PORT)

dtCliSock = socket(AF_INET, SOCK_STREAM) 
dtCliSock.connect(ADDR)
data = dtCliSock.recv(BUFSIZ)
print data
dtCliSock.close()
