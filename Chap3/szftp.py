#!/usr/bin/env python3
#this, in a way, is a solution to Exercise 3-11 as well!
import subprocess, sys, os, shutil

for i in range(len(sys.argv)):
    if '-z' == sys.argv[i]:
        msg = sys.argv[1:i]
        name = sys.argv[i+1] #name of the zip file
        os.mkdir(name)
        os.chdir(name)
        subprocess.call(['../srpmftp.py'] + msg) #to do the download
        os.chdir('..')
        shutil.make_archive(name, 'zip', '.', name)
        shutil.rmtree(name)
        break
else:
    msg = sys.argv[1:]
    subprocess.call(['./srpmftp.py']+msg)
