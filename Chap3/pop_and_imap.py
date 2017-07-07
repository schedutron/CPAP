#!/usr/bin/env python3

from imaplib import IMAP4_SSL
from poplib import POP3_SSL
# This fetches credentials.
from secret import *

def getSubject(msg, default='(no subject line)'):
    '''
        getSubject(msg) - iterate over 'msg' looking for Subject line; return
        if found otherwise 'default'
    '''
    for line in msg:
        if str(line).startswith('Subject:'):
            return line.strip()
        '''if not line:
            return default''' #in book. I think its incorrect...
    return default


# ---POP stuff
print('*** Doing POP3_SSL recv')
s = POP3_SSL('pop.gmail.com', 995)
s.user(MAILBOX)
s.pass_(PASSWD)
rv, msg, sz = s.retr(s.stat()[0])
s.quit()
sub = getSubject(msg)
print("Received msg via POP3_SSL: %s" % sub)

# ---IMAP STUFF
print('*** Doing IMAP4_SSL recv')
s = IMAP4_SSL('imap.gmail.com', 993)
s.login(MAILBOX, PASSWD)
rsp, msgs = s.select('INBOX', True)
rsp, data = s.fetch(msgs[0], '(RFC822)')
s.close()
s.logout()
sub = getSubject(data[0][1].decode('unicode_escape').split('\r\n'))
print("Received msg via IMAP4_SSL: %s" % sub)
