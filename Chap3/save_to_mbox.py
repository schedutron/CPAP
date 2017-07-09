#!/usr/bin/env python3

import email.utils
from imaplib import IMAP4_SSL
import mailbox
from secret import * # Gets credentials for gmail account.
from socket import gaierror

IMAPSVR = 'imap.gmail.com'
who = MAILBOX + '@gmail.com'

try:
    recvSvr = IMAP4_SSL(IMAPSVR, 993)
except gaierror:
    print("Can't connect to %s." % IMAPSVR)
    exit()
print("Connected to %s." % IMAPSVR)
try:
    recvSvr.login(who, PASSWD)
except Exception:
    print("Can't login. Check your credentials and try again.")
    exit()
print("Login successful.")

rsp, msgs = recvSvr.select('INBOX', True)
high = int(msgs[0])
rsp, headers = recvSvr.fetch('%s:%s' % (high-30, high), '(BODY[HEADER])')
print("Headers fetched.")
rsp, bodies = recvSvr.fetch('%s:%s' % (high-30, high), '(BODY[TEXT])')
print("Bodies fetched.")
mbox = mailbox.mbox('my_mbox.txt')
mbox.lock()
mails = []
for index in range(len(headers)):
    item = headers[index]
    if isinstance(item, tuple):
        msg = mailbox.mboxMessage()
        mail = item[1].decode().split('\r\n')
        for i in range(len(mail)):
            if mail[i].startswith('From:'):
                #msg.set_unixfrom('author')
                colon_ind = mail[i].find(':')
                msg['From'] = mail[i][colon_ind+2:]
                break

        for j in range(len(mail[i+1:])):
            if mail[j].startswith('To:'):
                msg['To'] = mail[j][4:]
                break

        for k in range(len(mail[j+1:])):
            if mail[k].startswith('Subject:'):
                msg['Subject'] = mail[k][9:]
                break
        msg.set_payload(bodies[index][1].decode())
        mails.append('\n'.join(mail[i:]))
        mbox.add(msg)
mbox.flush()
mbox.unlock()
