#!/usr/bin/env python3
import email
import mailbox
import re
# Display X-Mailer or X-Mailfrom for each email
# Display senders for emails with invalid Message-ID's
# Display X-Authentication-Warning header if present.

def match(from_dom, return_path_dom):
    pass


mbox = mailbox.mbox('my_mbox.txt')

# This loops prints the X-Mailer or X-Mailfrom header for each email.
messages = []
for mail in mbox:
    msg = email.message_from_string(str(mail)[1:]) # [1:] removes the leading \n
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

domain_from = re.compile(r'<.*@(.*)>')
domain_return_path = re.compile(r'<.*@(.*\.)*(.+\..+)>')
print('\n')
for msg in messages:
    from_domain = domain_from.search(msg['From']).groups()[0]
    return_path_domain = domain_return_path.search(msg['Return-Path'])
    if return_path_domain:
        return_path_domain = return_path_domain.groups()[1]
        if return_path_domain not in from_domain:
            print("Domain name conflict between From and Return-Path headers:")
            print("From: %s" % msg['From'])
            print("Return-Path: %s" % msg['Return-Path'])
            print()
    else:
        print("No return path for sender: %s" % msg['From'])
        print()
