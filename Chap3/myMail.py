#!/usr/bin/env python3

from smtplib import SMTP_SSL
from poplib import POP3_SSL
from secret import *
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
print(origBody)
sendSvr = SMTP_SSL(SMTPSVR, 465)
sendSvr.ehlo()
#sendSvr.starttls()
sendSvr.login(who, PASSWD)
errs = sendSvr.sendmail(who, [who], body)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10) #wait for mail to be delivered

recvSvr = POP3_SSL(POPSVR, 995)
recvSvr.user(who)
recvSvr.pass_(PASSWD)
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
#strip headers and compare to orig msg
#print(msg)
#print("Full message: ")

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
recvSvr.quit() #important! commits pending changes!
print('recvHeaders:\n%s\n' % recvHeaders)
print('origHeaders:\n%s\n' % origHeaders)
#assert recvHeaders == origHeaders
assert recvBody == origBody #assert identical
