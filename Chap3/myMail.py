#!/usr/bin/env python3

from smtplib import SMTP
from poplib import POP3_SSL
from time import sleep

SMTPSVR = 'smtp.gmail.com'
POPSVR = 'pop.gmail.com'

who = 'ImNotGonnaReveal@myEmail.com'
body = '''
From: %(who)s
To: %(who)s
Subject: test msg

Hello, World!''' % {'who': who}

origBody = body[body.index('')+1:].split('\n')
sendSvr = SMTP(SMTPSVR)
sendSvr.starttls()
sendSvr.login(who, 'ImNotGonnaRevealMyPassword')
errs = sendSvr.sendmail(who, [who], body)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(5) #wait for mail to be delivered

recvSvr = POP3_SSL(POPSVR)
recvSvr.user(who)
recvSvr.pass_('ImNotGonnaRevealMyPassword')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
#strip headers and compare to orig msg
#print(msg)
recvBody = [text.decode('unicode_escape') for text in msg] #to convert the recieved binary strings in msg
recvBody = recvBody[recvBody.index('')+1:]
#print('recvBody:\n%s\n' % recvBody)
#print('origBody:\n%s\n' % origBody)
assert recvBody == origBody #assert identical
