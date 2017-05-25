#!/usr/bin/env python
import sys, requests, socket

url = 'http://ipinfo.io'
if len(sys.argv) != 1:
    ip = socket.getaddrinfo(sys.argv[1], 80)[1][4][0] #80 is http
    url += '/%s' % ip
info = requests.get(url).json()
for key in info:
    print "%-10s: %s" % (key, info[key])
