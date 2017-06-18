#!/usr/bin/env python3
from ftplib import FTP, error_perm
import re, pickle, sys #maybe sqlite3 is a better option here instead of pickle
from time import ctime

class Callback():
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
        print('\r'+'-*'*stars+' '*2*(33-stars)+'|%i' % (fraction*100)+'%', end="") #progress bar
        sys.stdout.flush() #it works without this, but just for safety...
        #time.sleep(5)

def display(list):
    if not list:
        print("Empty!")
    for item in list:
        print(item)

with open('history.pkl', 'rb') as h:
    history = pickle.load(h)

while 1:
    with open('history.pkl', 'wb') as h: #this block writes additions to the file
        pickle.dump(history, h)

    command = input("\nEnter your command: ")
    if command.lower() == "quit":
        break

    chunks = command.split()
    if len(chunks) == 1:
        try:
            display(history[chunks[0].lower()])
        except KeyError:
            print("Please enter a valid command")
        continue

    if chunks[0].lower() == "connect":
        try:
            f = FTP(chunks[1])
        except:
            print("Can't connect to %s. Try again." % chunks[1])
            continue
    else:
        print("Please enter a valid command.")
        continue

    history['history'].append('%s - %s' % (chunks[1], ctime())) #won't look too pretty
    f.login()
    dirname = f.pwd()
    f.dir()
    while dirname:
        dirname = input('\nProvide directory name to cd into, or just press enter to continue with this directory: ')
        if dirname:
            try:
                f.cwd(dirname)
                f.dir()
            except error_perm:
                print("Can't cd to %s. Try again." % dirname)

    data = []
    f.dir(data.append)
    location = "%s" % chunks[1]+f.pwd()
    if location not in history['bookmarks']:
        choice = input("Do you want to bookmark this location? (y/n) ")
        if choice == 'y':
            history["bookmarks"].append(location)

    pattern = input("\nProvide filename pattern: ")
    extract = r'\d[ ]([^: ]+)'
    names = [re.findall(extract, item)[-1] for item in data]
    wanted = [item for item in names if re.search(pattern, item)]
    sizes = []
    for item in wanted:
        sizes.append([int(re.search(r"\s+(\d+) [A-Za-z]{3} ", line).groups()[0]) for line in data if re.findall(extract, line)[-1]==item][0]) #complex!
    if not wanted:
        print("No such files found. Try again.")
        f.quit()
        continue
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
        print("Downloading %s..." % item)
        with open(item, 'wb') as content:
            callback = Callback(content, size)
            f.retrbinary("RETR %s" % item, callback.write, 1024)
            history["downloads"].append("%s%s%s - %s" % (chunks[1], dirname, item, ctime()))

        print("\nDownload complete!\n")
    print("\nAll content downloaded to pwd!")
    f.quit()
