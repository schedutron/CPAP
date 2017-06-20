#!/usr/bin/env python3

#we could implement progress bar here as well

import sys, re, os
from ftplib import FTP, error_perm

def download(wanted):
    f.cwd(wanted)
    os.mkdir(wanted)
    os.chdir(wanted)
    data = []
    f.dir(data.append)
    names = [re.findall(extract, item)[-1] for item in data if item[0] != 'd']
    for name in names:
        with open(name, 'wb') as canvas:
            f.retrbinary('RETR %s' % name, canvas.write)

def downloadRecursive(wanted):
    download(wanted)
    data = []
    f.dir(data.append)
    for item in data:
        if item[0] == 'd':
            folname = re.findall(extract, item)[-1]
            downloadRecursive(folname)

    #traceback
    f.cwd('..')
    os.chdir('..')

f = FTP(sys.argv[1])
f.login() #for now, only anonymous login supported by this script

data = []
f.dir(data.append)

extract = r'\d[ ]([^: ]+)'
names = [re.findall(extract, item)[-1] for item in data]

wanted = sys.argv[2]
if wanted == '-r':
    wanted = sys.argv[3]
#typ = data[names.index(wanted)][0] #d or something else
try:
    with open(wanted, 'wb') as canvas:
        f.retrbinary('RETR %s' % wanted, canvas.write)
    f.quit()
    quit()
except error_perm:
    os.unlink(wanted)
    pass
try:
    f.cwd(wanted)
except error_perm:
    print("No such file / directory.")
    quit()
f.cwd('/') #back to root

if sys.argv[2] == '-r':
    downloadRecursive(wanted)
else:
    download(wanted)
f.quit()
