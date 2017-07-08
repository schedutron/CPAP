#!/usr/bin/env python3

from smtplib import SMTP_SSL, SMTPAuthenticationError
from poplib import POP3_SSL, error_proto
from secret import *
from socket import gaierror
from time import sleep
SMTPSVR = 'smtp.gmail.com'
POPSVR = 'pop.gmail.com'

who = MAILBOX + '@gmail.com'
body = """From: %(who)s
To: %(who)s
Subject: test msg

Hello, World!""" % {'who': who}

body_list = body.split('\n')
breaker = body_list.index('')
origHeaders = body_list[:breaker] # List
origBody = ''.join(body_list[breaker+1:])
try:
    sendSvr = SMTP_SSL(SMTPSVR, 465)
except gaierror:
    print("Can't connect to %s." % SMTPSVR)
    exit()
sendSvr.ehlo()
#sendSvr.starttls()
try:
    sendSvr.login(who, PASSWD)
except SMTPAuthenticationError:
    print("Invalid SMTP credentials.")
    exit()
errs = sendSvr.sendmail(who, [who], body)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10) #wait for mail to be delivered

try:
    recvSvr = POP3_SSL(POPSVR, 995)
except gaierror:
    print("Can't connect to %s." %POPSVR)
    exit()
# No need of the following try-except block.
# This error would be already catched in SMTP part.
# It's present to signify that invalid credential error has been taken care of.
try:
    recvSvr.user(who)
    recvSvr.pass_(PASSWD)
except error_proto as e:
    print("For POP:", end=" ")
    print(str(e)[2:-1]) # This may be a stupid thing to do.
    exit()
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
#strip headers and compare to orig msg
#print(msg)
#print("Full message: ")
recvSvr.quit() #important! commits pending changes!
recvBody = [text.decode('unicode_escape') for text in msg] #to convert the recieved binary strings in msg
breaker = recvBody.index('')
for text in recvBody:
    print(text)
#for item in recvBody:
#    print(item)
recvHeaders = recvBody[:breaker]
# Loop used to ignore new headers.
for i in range(len(recvHeaders)):
    if recvHeaders[i].startswith('From:'):
        break
recvHeaders = recvHeaders[i:i+3]
recvBody = '\n'.join(recvBody[breaker+1:])
#print('recvBody:\n%s\n' % recvBody)
#print('origBody:\n%s\n' % origBody)
print('recvHeaders:\n%s\n' % recvHeaders)
print('origHeaders:\n%s\n' % origHeaders)
#assert recvHeaders == origHeaders
assert recvBody == origBody #assert identical
