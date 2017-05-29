#!/usr/bin/env python

from socket import *
from select import select

HOST = ''
PORT = 7000
BUFSIZ = 1024
ADDR = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(10)

inputs = [server]
outputs = []
exceptional = []

services = {}

print "Waiting for connection..."
while True:
    readable, writable, exceptional = select(inputs, outputs, inputs)

    for s in readable:
        if s is server:
            user, user_address = s.accept()
            inputs.append(user)
            msg = "If you want to add a service, type {<name> <address>} and your service will be name-registered in this name server.\n"
            msg += "Thus, clients would be able to find your service with ease.\n\n"
            msg += "If you're a client, you can simply type a service name to get it's address, or look at all existing services by typing {show}.\n\n"
            user.send(msg)
            print "%s:%s connected." % user_address
        else:
            msg = s.recv(1024)
            if not msg:
                s.close()
                inputs.remove(s)
            elif msg == "{show}":
                if services == {}:
                    s.send("No services available :(")
                else:
                    resp = '\n'
                    for service in services:
                        resp += "%s - %s\n" % (service, services[service])
                    s.send(resp)

            elif msg[0] == '{':
                comp = msg.split()
                address = comp[1][:-1] #ideally
                name = comp[0][1:]
                if name in services:
                    s.send("Service %s already exists." % name)
                else:
                    services[name] = address
                    s.send("Service %s added!" % name)
            else:
                if msg in services:
                    s.send(msg+" - %s" % services[msg])
                else:
                    s.send("No such service exists.")

        for s in writable:
            pass

        for s in exceptional:
            s.close()
            inputs.remove(s)
            print "%s disconnected." % s.getpeername()
server.close() #not really used
