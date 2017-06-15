#!/usr/bin/env python3
from ftplib import FTP

f = FTP('prep.ai.mit.edu')
f.login()
f.cwd('video') #prone to errors because the directory structure may change
with open('geeky_video.webm', 'wb') as vid:
    name = "A_Digital_Media_Primer_For_Geeks-360p.webm"
    print("Downloading %s..." % name)
    f.retrbinary('RETR %s' % name, vid.write)
print("*** Video downloaded to pwd!")
f.quit()
