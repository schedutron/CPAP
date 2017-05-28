#!/usr/bin/env python

from socket import *
import select

def broadcast(people, msg):
    for person in people:
        person.send(msg)

HOST = ''
PORT = 33000
ADDR = (HOST, PORT)
BUFSIZ = 1024

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(10)

inputs = [server]
outputs = []
rooms = {'Main':[]} #name:people(i.e, sockets)
user_room = {} #user:room_name
clients = {}
addresses = {}

print "Waiting for connection..."
while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server:
            client, client_address = s.accept()
            client.send("Connection establised. Now we can chat! Type your name and press enter to continue :)")
            print "%s:%s connected." % client_address
            addresses[client] = client_address
            inputs.append(client)
        else:
            msg = s.recv(BUFSIZ)
            if msg == '{quit}':
                inputs.remove(s)
                if s in outputs:
                    outputs.remove(s)
                if s in clients:
                    name = clients[s]
                    del clients[s]
                    room_name = user_room[name]
                    rooms[room_name].remove(s)
                    del user_room[name]
                    msg = "\n-----%s has left the cave.\n" % name
                    broadcast(rooms[room_name], msg)
                print "%s:%s disconnected." % addresses[s]

            elif msg == '{exit}':
                if clients[s] in user_room:
                    if s in outputs:
                        outputs.remove(s)
                    name = clients[s]
                    room_name = user_room[name]
                    del user_room[name]
                    rooms[room_name].remove(s)
                    msg = "%s has left the room." % name
                    broadcast(rooms[room_name], msg)
                else:
                    s.send('First join a room!')

            elif msg.startswith('{create'):
                room_name = msg[8:-1] #ideally
                rooms[room_name] = []
                s.send('Room "%s" created!' % room_name)
            elif msg.startswith('{join '):
                room_name = msg[6:-1] #ideally
                if room_name in rooms:
                    if clients[s] in user_room:
                        s.send('First exit room "%s".' % user_room[clients[s]])
                    else:
                        msg = "%s has joined the room!" % clients[s]
                        broadcast(rooms[room_name], msg)
                        rooms[room_name].append(s)
                        user_room[clients[s]] = room_name
                        s.send("Welcome to %s!" % room_name)
                else:
                    s.send("There is no such room!")

            elif msg == "{see}":
                if clients[s] in user_room:
                    msg = ''
                    room_name = user_room[clients[s]]
                    for p in rooms[room_name]:
                        msg += "\n"+clients[p]
                    s.send(msg)
                else:
                    s.send("First enter a room!")

            elif msg == "{who}":
                msg = ''
                for client in clients:
                    msg += "\n"+clients[client]
                s.send(msg)

            elif msg == "{rooms}":
                msg = '\n'
                for room in rooms:
                    msg += "%s (%i)\n" % (room, len(rooms[room]))
                s.send(msg)

            elif s not in clients:
                name = msg
                clients[s] = name
                welcome = "Welcome %s!" % name
                welcome += " We're adding you to our main chat room. But there are multiple rooms in the cave. Feel free to roam!\n"
                welcome += "To leave a room, type {exit}. To leave the cave, type {quit}.\n"
                welcome += "To see which people are in the room, type {see}. To see which people are in the cave, type {who}.\n"
                welcome += "To join a room, type {join room_name}. To see available rooms, type {rooms}.\n"
                welcome += "Finally, anything else you type is treated as your message :)\n"

                msg = "%s has joined the room!" % name #redundancy :(
                broadcast(rooms["Main"], msg)
                user_room[name] = "Main"
                rooms["Main"].append(s)
                s.send(welcome)

            else:
                name = clients[s]
                msg = name +": "+msg
                try:
                    room_name = user_room[name]
                    broadcast(rooms[room_name], msg)
                except KeyError:
                    s.send("First enter a room to chat!")

        for s in writable:
            pass #for now

        for s in exceptional:
            if s in clients:
                name = clients[s]
                room_name = user_room[name]
                rooms[room_name].remove(s)
                del user_room[name]
                del clients[s]
                errMsg = "%s has unexpectedly left the cave." % name
                broadcast(rooms[room_name], errMsg)
            s.close()
            print "%s:%s disconnected." % addresses[s]
            del addresses[s]

server.close() #not really used
