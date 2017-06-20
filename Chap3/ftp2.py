#!/usr/bin/env python3
from ftplib import FTP

class FTP2(FTP):
    def __init__(self, *args): #maybe there are other arguments, but I'm not implementing them here
        FTP.__init__(self, *args)

    def retrlines2(self, fname, callback=None):
        FTP.retrlines(self, 'RETR %s' % fname, callback)

    def retrbinary2(self, fname, callback=None):
        FTP.retrbinary(self, 'RETR %s' % fname, callback)

    def storlines2(self, f): #f is the file to be uploaded
        FTP.storlines('STOR %s' % f.name, f)

    def storbinary2(self, f):
        FTP.storbinary('STOR %s' % f.name, f)
