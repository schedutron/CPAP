#!/usr/bin/env python

from socket import *

site = raw_input('Enter the site: ')
PORT = 80
HOST = 'www.'+site
ADDR = (site, PORT)

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)
client.send('GET / HTTP/1.1\nHost: %s\n\n' % HOST)
with open('contents.html', 'w') as contents:
    data = client.recv(1024)
    contents.write(data)
