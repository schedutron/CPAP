#!/usr/bin/env python3
import email
import mailbox
import re
import requests
import socket
# Display X-Mailer or X-Mailfrom for each email
# Display senders for emails with invalid Message-ID's
# Display X-Authentication-Warning header if present.

# At last, basic masquerading check has been added to kinda detect phishing.
# But statement of Exercise 3-28-e is still vague!


def check_spam(msg_word_list):
    for spam_word in spam_word_list:
        count = 0
        for word in msg_word_list:
            if word == spam_word:
                count += 1
                if count == 3:
                    return True
    return False

mbox = mailbox.mbox('my_mbox.txt')

# This loops prints the X-Mailer or X-Mailfrom header for each email.
messages = []
for mail in mbox:
    mail_str = str(mail)
    msg = email.message_from_string(mail_str[mail_str.find('X-Received'):]) # [1:] removes the leading \n
    if msg['X-Mailer']:
        print(msg['X-Mailer'], " - ", end="")
    elif msg['X-Mailfrom']:
        print(msg['X-Mailfrom'], " - ", end="")
    else:
        print('No email client information for: ', end="")
    print(msg['From'])
    messages.append(msg)

valid_mid = re.compile(r'.*@[\.\S]+(\.[\.\S]+)+')
print('\n')
for msg in messages:
    if not valid_mid.match(msg['Message-ID']):
        print("Bad Message-ID:", end=" ")
        print(msg['Message-ID'])
        print("For sender %s\n" % msg['From'])
print('\n')
for msg in messages:
    if msg['X-Authentication-Warning']:
        print('X-Authentication-Warning: %s' % msg['X-Authentication-Warning'])
        print("For sender %s" % msg['From'])
        print('Subject: %s' % msg['Subject'])
        print()

name_with_ip = re.compile(r'\((.*)\)')
domain_return_path = re.compile(r'<.*@(.*)>')
further_filter = re.compile(r'(.*\.)*(.+\..+)')
print('\n')
for msg in messages:
    name_and_ip = name_with_ip.search(msg['Received']).groups()[0]
    chunks = name_and_ip.split()
    name_raw = chunks[0][:-1] # [:-1] strips off the trailing '.'
    return_path_domain = domain_return_path.search(msg['Return-Path']) # CHANGE THE RE NAME!
    if return_path_domain:
        return_path_domain = further_filter.search(return_path_domain.groups()[0]).groups()[1]
        name = further_filter.search(name_raw).groups()[1]
        if return_path_domain != name:
            print("Domain name conflict between Received and Return-Path headers:")
            print("Received: %s" % name)
            print("Return-Path: %s" % return_path_domain)
            print()

        ip = chunks[1][1:-1] # Slicing strips off '[' and ']'.
        real_ip = socket.getaddrinfo(name_raw, 80)[1][4][0] #80 is http
        if real_ip != ip:
            print("Domain name and IP conflict:")
            print("Domain name: %s" % name_raw)
            print("IP: %s" % ip)
            print("Real IP: %s" % real_ip)

    else:
        print("No return path for sender: %s" % msg['From'])
        print()

print('\n')
# Displays domain information.
for msg in messages:
    domain_name = domain_return_path.search(msg['From']).groups()[0]
    domain_name = further_filter.search(domain_name).groups()[1]
    ip = socket.getaddrinfo(domain_name, 80)[1][4][0] #80 is http
    info = requests.get('http://ipinfo.io/%s' % ip).json()
    print("From: %s" % msg['From'])
    print('-*-'*22, end="\n")
    print()
    for key in info:
        print("%s: %s" % (key, info[key]))
    print()

spam_word_list = ['lol', 'joke', 'lottery', 'credit', 'approval', 'bonanza']
for i in range(len(mbox)):
    if check_spam(str(mbox[i]).split()):
        print("Detected spam mail:")
        print("From: %s" % messages[i]['From'])
        print("Subject: %s\n" % messages[i]['Subject'])

for msg in messages:
    if msg['X-Google-Original-From']:
        # Sorry but for simplicity I assume that mails are downloaded from gmail.
        if msg['From'] != msg['X-Google-Original-From']:
            print("Possible Masquerading:")
            print("From: %s" % msg['From'])
            print("X-Google-Original-From: %s\n" % msg['X-Google-Original-From'])
