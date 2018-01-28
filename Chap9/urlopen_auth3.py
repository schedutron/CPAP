#!/usr/bin/env python2

import urllib.request, urllib.error, urllib.parse

LOGIN = 'schedutron'
PASSWD = 'somerandomstuff'
URL = 'http://localhost'
REALM = 'Secure Archive'

def handler_version(url):
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urllib.parse.urlparse(url)[1], LOGIN, PASSWD)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return url


def request_version(url):
    from base64 import encodestring
    req = urllib.request.Request(url)
    b64str = encodestring(bytes('%s:%s' % (LOGIN, PASSWD), 'utf-8'))[:-1]
    req.add_header("Authorization", "Basic %s" % b64str)
    return req


for func_type in ('handler', 'request'):
    print("*** Using %s:" % func_type.upper())
    url = eval("%s_version" % func_type)(URL)
    f = urllib.request.urlopen(url)
    print(str(f.readline(), 'utf-8'))
    f.close()
