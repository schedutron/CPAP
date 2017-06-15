#!/usr/bin/env python3
from ftplib import FTP, error_perm
import re

f = FTP('prep.ai.mit.edu')
f.login()
dirname = f.pwd()
f.dir()
while dirname:
    dirname = input('\nProvide directory name to cd into, or just press enter to continue with this directory: ')
    if dirname:
        try:
            f.cwd(dirname)
        except error_perm:
            print("Can't cd to %s. Try again." % dirname)
        else:
            f.dir()

data = []
f.dir(data.append)

pattern = input("Provide filename pattern: ")
extract = r'\d[ ]([^: ]+)'
names = [re.findall(extract, item)[-1] for item in data]
wanted = [item for item in names if re.search(pattern, item)]
print("\nFiles you want:")
for item in wanted:
    print(item)
print("\n(Total %s)\n" % len(wanted))
for item in wanted:
    print("Downloading %s..." % item)
    with open(item, 'wb') as content:
        f.retrbinary("RETR %s" % item, content.write)
    print("Download complete!\n")
print("\nAll content downloaded to pwd!")
f.quit()
