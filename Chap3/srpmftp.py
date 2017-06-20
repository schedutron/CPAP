#!/usr/bin/env python3

#this is just a download client, upload functionality absent
from ftplib import FTP, error_perm
import re, sys, os

def download(wanted):
    f.cwd(wanted)
    os.mkdir(wanted)
    os.chdir(wanted)
    data = []
    f.dir(data.append)
    names = [re.findall(extract, item)[-1] for item in data if item[0] != 'd']
    sizes = []
    for identifier in names:
        sizes.append([int(re.search(r"\s+(\d+) [A-Za-z]{3} ", line).groups()[0]) for line in data if re.findall(extract, line)[-1]==identifier][0]) #complex!
    for i in range(len(names)):
        name = names[i]
        size = sizes[i]
        with open(name, 'wb') as canvas:
            print("Downloading %s..." % name)
            callback = Callback(canvas, size)
            f.retrbinary('RETR %s' % name, callback.write)
            print("\nDownload complete!\n")

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

class Callback(): #for the progress bar
    def __init__(self, f, size):
        self.file = f
        self.size = size
        self.total = 0

    def write(self, stuff):
        self.total += len(stuff)
        fraction = self.total/self.size #python3 takes care of floats
        stars = int(fraction*33)

        #bufsiz = 1024
        #chunks = [stuff[i:i+bufsiz] for i in range(0, len(stuff), bufsiz)]
        #for i in tqdm.tqdm(chunks):
        self.file.write(stuff)
        print('\r'+'-#'*stars+' '*2*(33-stars)+'|%i' % (fraction*100)+'%', end="") #progress bar
        sys.stdout.flush() #it works without this, but just for safety...
        #time.sleep(5)

def display(list):
    if not list:
        print("Empty!")
    for item in list:
        print(item)

f = FTP(sys.argv[1]) #connects to host
f.login()

try:
    f.cwd(sys.argv[2]) #changes to user-specified directory
except error_perm:
    print(sys.argv[2], "- no such directory")
    f.quit()
    quit()

data = []
f.dir(data.append)

pattern = sys.argv[3]
if pattern == '-r':
    pattern = sys.argv[4]

extract = r'\d[ ]([^: ]+)'
names = [re.findall(extract, item)[-1] for item in data]
wanted = [item for item in names if re.search(pattern, item)]
sizes = []
for item in wanted:
    sizes.append([int(re.search(r"\s+(\d+) [A-Za-z]{3} ", line).groups()[0]) for line in data if re.findall(extract, line)[-1]==item][0]) #complex!
if not wanted:
    print("No such files found. Try again.")
    f.quit()
    quit()
print("\nFiles you want:")
for item in wanted:
    print(item)
print("\n(Total %s)\n" % len(wanted))
dirname = f.pwd()
if not dirname.endswith('/'):
    dirname += '/'
for i in range(len(wanted)):
    item = wanted[i]
    size = sizes[i]
    print("Downloading %s..." % item) #informative!
    if data[names.index(item)][0] != 'd': #its a file, not a subdirectory
        with open(item, 'wb') as content:
            callback = Callback(content, size)
            f.retrbinary("RETR %s" % item, callback.write, 1024)
            print("\nDownload complete!\n")
    elif sys.argv[3] != '-r':
        download(item)
    else:
        downloadRecursive(item)

print("\nAll content downloaded to pwd!")
f.quit()
