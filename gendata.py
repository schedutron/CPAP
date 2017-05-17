#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')
with open('redata.txt', 'w') as f:
    for i in xrange(randrange(5, 11)):
        dtint = randrange(2**32) #pick date
        dtstr = ctime(dtint)      #date string
        llen = randrange(4, 8)    #login is shorter
        login = ''.join(choice(lc) for j in xrange(llen))
        dlen = randrange(llen, 13)#domain is longer
        dom = ''.join(choice(lc) for j in xrange(dlen))
        print >>f, '%s::%s@%s.%s::%s-%s-%s' % (dtstr, login, dom, choice(tlds),
                                      dtint, llen, dlen)
