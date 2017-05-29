#!/usr/bin/env python

from socket import *
from time import sleep

HOST = raw_input("Enter host: ")
if not HOST:
    HOST = 'localhost'
PORT = raw_input("Enter port: ")
if not PORT:
    PORT = 6000
else:
    PORT = int(PORT)

ADDR = (HOST, PORT)

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)
print "Connection established. Type the number of seconds to sleep as your message. It can be fractional."
while True:
    msg = raw_input("Seconds to sleep: ")
    if not msg:
        break
    client.send(msg)
    command = client.recv(1024) #1024 characters?
    if not command:
        break
    print "Sleeping for %s second(s)..." % msg
    exec(command)
client.close()
