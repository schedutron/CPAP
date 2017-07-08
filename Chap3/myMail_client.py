#!/usr/bin/env python3
# Requires a secret.pyc file containing email credentials for running
from imaplib import IMAP4_SSL
from smtplib import SMTP_SSL, SMTPAuthenticationError
from poplib import POP3_SSL, error_proto
import pydoc
from secret import * # Gets credentials for gmail account.
from socket import gaierror
import subprocess
from time import sleep

SMTPSVR = 'smtp.gmail.com'
IMAPSVR = 'imap.gmail.com'
who = MAILBOX + '@gmail.com'
def send_msg():
    with open('email', 'w') as msg:
        msg.write('From: YOUR_NAME_HERE <%s>\n' % who)
        msg.write('To: RECIPIENTS_HERE\n')
        msg.write('Subject: YOUR_SUBJECT_HERE\n\n')
    subprocess.call(['nano', 'email'])

    with open('email', 'rb') as msg:
        body = msg.read().decode('unicode_escape') # INCLUDES HEADERS

    body_list = body.split('\n')
    breaker = body_list.index('')
    origHeaders = body_list[:breaker] # List
    recipients = origHeaders[1].split(', ')
    origBody = '\n'.join(body_list[breaker+1:])
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
    errs = sendSvr.sendmail(who, recipients, body)
    sendSvr.quit()
    assert len(errs) == 0, errs
    print("Email sent!")

wanna_mail = input("Welcome to your email client. Would you like to compose an email? (Y/N) ")
if wanna_mail == 'Y':
    send_msg()
else:
    print("Alright. Now your inbox will be displayed.")
    # IMAP stuff below.
    try:
        recvSvr = IMAP4_SSL(IMAPSVR, 993)
    except gaierror:
        print("Can't connect to %s." % IMAPSVR)
        exit()
    try:
        recvSvr.login(who, PASSWD)
    except Exception:
        print("Can't login. Check your credentials and try again.")
        exit()
    rsp, msgs = recvSvr.select('INBOX', True)
    length = input("How many latest email would you like to be displayed? ")
    low = int(msgs[0]) - int(length)
    if low <= 0:
        low = 1
    #try:
    rsp, data = recvSvr.fetch("%s:%s" % (low, int(msgs[0])), '(BODY[HEADER])')
    #except Exception:
    #    print("Can't fetch email.")
    #    exit()
    titles = []
    for item in data:
        if isinstance(item, tuple):
            mid = item[0].decode('unicode_escape').split()[0]
            for line in item[1].decode('unicode_escape').split('\r\n'):
                if line.startswith('Subject:'):
                    sub = line
                    break
            titles.append(mid + ' - ' + sub)

    string = '\n'.join(titles[::-1])
    string = 'Use message id to access a specific email.\n\n' + string
    print(string)
    while 1:
        mid = input("Enter the mid of the message you want to read, or skip to quit: ")
        if not mid:
            break

        rsp, data = recvSvr.fetch(mid, '(RFC822)')
        stuff = data[0][1].decode('unicode_escape').split('\r\n')
        for i in range(len(stuff)):
            if stuff[i].startswith('From:'):
                break
        headers = stuff[i:i+3]
        breaker = stuff.index('')
        body = stuff[breaker:] #includes the empty string
        msg_to_be_displayed = '\n'.join(headers + body)
        pydoc.pager(msg_to_be_displayed)

print("Thanks for using the client. Exit done.")
