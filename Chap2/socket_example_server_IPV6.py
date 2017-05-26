#!/usr/bin/env python
import socket, sys

HOST = None #symbolic name meaning all available interfaces
PORT = 21567
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print "Could not open socket"
    sys.exit(1)
conn, addr = s.accept()

print "Connected by", addr
while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()
