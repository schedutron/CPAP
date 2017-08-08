#!/usr/bin/env python3
import linecache, re, sys
from threading import Lock, Thread


def render_HTML(start, end):
    with open("links_v2.html", "a") as page:
        for i in range(start, end):
            line = linecache.getline(filename, i)
            match = EMAIL_PATT.match(line)
            if match:
                sender = match.groups()[0]
                addr = match.groups()[1]
                site = 'http://www.' + addr.split('@')[1]
                lock.acquire()
                page.write("<p><a href='{0}'>{1}</a></p>\n".format(site, sender))  # [1:] removes leading '>'.
                lock.release()


filename = sys.argv[1]
nthreads = int(sys.argv[2])
messages = []
EMAIL_PATT = re.compile(r"From: (.+) <(\S+)>")
lock = Lock()

with open(filename) as f:
    nlines = int(f.readline().strip())  # Assumes 1st line to be # of lines in the file.
if nlines < nthreads:
    print("Too many threads for processing file. Use less threads.")
    quit()

chunksize = nlines // nthreads
threads = []
i = 0
with open("links_v2.html", "w") as f:
    f.write("<html>\n")

while i < nlines:
    thread = Thread(target=render_HTML, args=(i, i+chunksize))
    thread.start()
    threads.append(thread)
    i += chunksize
    if i > nlines:
        i = nlines

for thread in threads:
    thread.join()

with open("links_v2.html", "a") as f:
    f.write("</html>")
print("HTML file written. Open links_v2.html to view the contents.")
