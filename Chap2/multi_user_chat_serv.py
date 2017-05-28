#!/usr/bin/env python

#make Terminal bounce for notifications

from socket import *
import select

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

inputs = [server]
outputs = []

clients = {}
addresses = {}

msg = ''
errMsg = ''
print "Waiting for connection..."
while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
        if s is server:
            client, client_address = s.accept()
            print "%s:%s has connected." % client_address
            client.send("Welcome to the cave! Now type your name and press enter!")
            addresses[client] = client_address
            inputs.append(client)
        else:
            msg = s.recv(BUFSIZ)
            if msg == '{quit}':
                if s in clients:
                    name = clients[s]
                    del clients[s]
                    if s in outputs:
                        outputs.remove(s)
                    msg = "%s has left the chat." % name
                writable.remove(s)
                inputs.remove(s)
                s.close()
                print "%s:%s has disconnected." % addresses[s]
                del addresses[s]
            elif s not in clients:
                name = msg
                welcome = 'Welcome %s! Type {who} to see users already logged in or {quit} to exit. Anything else is treated as your message :)' % name
                s.send(welcome) #assume for now it's writable
                msg = "%s has joined the chat!" % name
                clients[s] = name
                outputs.append(s)
            else:
                if msg == '{who}':
                    if clients != {}:
                        resp = '\n'.join(clients.values())
                    else:
                        resp = "It's lonely here :("
                    s.send(resp) #assume for now it's writable
                    msg = ''
                else:
                    msg = clients[s] +": "+ msg

    if msg or errMsg:
        if errMsg:
            for s in writable:
                s.send(errMsg)
            errMsg = ''
        if msg:
            for s in writable:
                s.send(msg)
            msg = '' # to avoid duplication

    for s in exceptional:
        name = clients[s]
        s.close()
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        del client[s]
        errMsg += "%s has unexpectedly left the chat." % name
server.close() #not really used
