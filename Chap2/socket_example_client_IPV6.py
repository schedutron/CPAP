#!/usr/bin/env python

import socket, sys

HOST = 'localhost'
PORT = 21567
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, cannonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print "Could not open socket."
    sys.exit(1)
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
