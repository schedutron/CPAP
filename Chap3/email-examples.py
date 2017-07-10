#!/usr/bin/env python3
'email-examples.py - demo creation of email messages'
'Textbook had this in Python2, I ported it to Python3.'

from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from secret import * # Gets credentials for login.
from smtplib import SMTP
import re
import requests

img_patt = re.compile(r'(jp|pn)g|(g|t)if')
url_patt = re.compile(r'https?://')

#multipart alternative: text and html
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    '''if 'alternative' is not passed, each of the two parts will be a separate
    attachment, so some email systems will show both'''
    text = MIMEText('Hello, World!\r\n', 'plain')
    email.attach(text)

    html = MIMEText('<html><body><h4>Hello, World!</h4></body></html>', 'html')
    email.attach(html)
    return email

#multipart: images
def attach_images(*fns):
    email = MIMEMultipart()
    for fn in fns:
        if not img_patt.search(fn.split('.')[-1]):
            # Following is kinda like throwing an exception, but better.
            print("%s doesn't seem to be an image file. Skipping." % fn)
            continue
        if url_patt.match(fn):
            data = requests.get(fn).content
        else:
            with open(fn, 'rb') as f:
                data = f.read()
        img = MIMEImage(data, name=f)
        img.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
        email.attach(img)
    return email


def attach_sheets(*fns):
    '''Adds multipart spreadsheets.'''
    email = MIMEMultipart()
    for fn in fns:
        with open(fn, 'rb') as f:
            data = f.read()
        sheet = MIMEBase('application', 'vnd.ms-excel')
        sheet.set_payload(data)
        sheet.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
        email.attach(sheet)
    return email


def attach_docs(*fns):
    """Adds multipart docs."""
    email = MIMEMultipart()
    for fn in fns:
        with open(fn, 'rb') as f:
            data = f.read()
        doc = MIMEBase('application', 'vnd.ms-word')
        doc.set_payload(data)
        encoders.encode_base64(doc)
        doc.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
        email.attach(doc)
    return email


def attach_files(*fns):
    """Adds multipart files."""
    email = MIMEMultipart()
    for fn in fns:
        with open(fn, 'rb') as f:
            data = f.read()
        stuff = MIMEBase('application', 'octet-stream')
        stuff.set_payload(data)
        encoders.encode_base64(stuff)
        stuff.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
        email.attach(stuff)
    return email


def sendMsg(fr, to, msg):
    s = SMTP('smtp.gmail.com')
    s.starttls()
    s.login(MAILBOX + '@gmail.com', PASSWD)
    errs = s.sendmail(fr, to ,msg)
    assert len(errs) == 0, errs #not in book
    s.quit()

if __name__ == "__main__":
    print("Sending multipart alternative msg...")
    msg = make_mpa_msg()
    un = MAILBOX + '@gmail.com'
    msg['From'] = un
    rcps = [un, '16ucc086@lnmiit.ac.in']
    msg['To'] = ', '.join(rcps)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(un, rcps, msg.as_string())

    '''print('Sending image msg...')
    # Any number of image files can be passed.
    msg = attach_images('https://docs.python.org/3/_static/py.png')
    msg['From'] = un
    msg['To'] = ', '.join(rcps)
    msg['Subject'] = 'image file test'
    sendMsg(un, rcps, msg.as_string())

    print('Sending spreadsheet msg...')
    # Any number of image files can be passed.
    msg = attach_sheets('check.csv', 'check2.csv')
    msg['From'] = un
    msg['To'] = ', '.join(rcps)
    msg['Subject'] = 'spreadsheet file test'
    sendMsg(un, rcps, msg.as_string())

    print('Sending doc msg...')
    # Any number of image files can be passed.
    msg = attach_docs('check.docx')
    msg['From'] = un
    msg['To'] = ', '.join(rcps)
    msg['Subject'] = 'doc file test'
    sendMsg(un, rcps, msg.as_string())'''

    print('Sending files msg...')
    # Any number of image files can be passed.
    msg = attach_files('check.csv', 'favicon.ico', 'calculator.kv', 'email-examples.py')
    msg['From'] = un
    msg['To'] = ', '.join(rcps)
    msg['Subject'] = 'files test'
    sendMsg(un, rcps, msg.as_string())
