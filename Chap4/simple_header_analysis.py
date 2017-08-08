#!/usr/bin/env python3
import email, mailbox, re

mbox = mailbox.mbox("../Chap3/my_mbox.txt")
messages = []
with open("links.html", "w") as page:
    page.write("<html>\n")
    for mail in mbox:
        mail_str = str(mail)
        msg = email.message_from_string(mail_str[mail_str.find('X-Received'):]) # [1:] removes the leading '\n'.
        addr = msg['From']
        site = 'http://www.' + addr.split('@')[1]
        name = msg["From"].split('<')[0][:-1]
        page.write("<p><a href={0}>{1}</a></p>\n".format(site, name))  # [1:] removes leading '>'.
    page.write("</html>")
print("HTML file written. Open links.html to view the contents.")
