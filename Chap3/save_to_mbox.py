#!/usr/bin/env python3

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
rsp, headers = recvSvr.fetch('%s:%s' % (high-30, high), '(RFC822)')
print("Mails fetched.")
#rsp, bodies = recvSvr.fetch('%s:%s' % (high-30, high), '(BODY[TEXT])')
#print("Bodies fetched.")

mbox = mailbox.mbox('my_mbox.txt')
mbox.lock()
for index in range(len(headers)):
    item = headers[index]
    if isinstance(item, tuple):
        msg = mailbox.mboxMessage()
        msg.set_payload(item[1].decode())
        mbox.add(msg)
mbox.flush()
mbox.unlock()
print("30 Emails successfully written to my_mbox.txt!")
