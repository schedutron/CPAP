#!/usr/bin/env python3
"""
Script to count occurences of a particular byte in a file.

There was no noticeable difference in single threaded and multithreaded runs.
However, the multithreaded run indeed executed faster (on the order of
milliseconds). Also, more threads didn't necessarily mean more performance, e.g,
a run with 20 threads executed slightly faster than a run with 100 threads.
"""

import os, sys
from threading import Thread, Lock

def count(filename, byte, start, end):
    global global_count
    number = 0
    with open(filename, 'rb') as f:
        f.seek(start)
        for i in range(start, end):
            c = f.read(1)
            if c == byte:
                number += 1
    lock.acquire()
    global_count += number
    lock.release()

lock = Lock()
filename = sys.argv[1]
byte = bytes(sys.argv[2], 'utf-8')
global_count = 0
filesize = os.stat(filename).st_size
nthreads = int(sys.argv[3])

if nthreads > filesize:
    print("Too many threads for reading this file! Use less threads.")
    quit()

readsize = filesize // nthreads
ranges = []
threads = []
i = 0
while i < filesize:
    ranges.append([i, i+readsize])
    i += readsize
if ranges[-1][1] > filesize:
    ranges[-1][1] = filesize

for pair in ranges:
    thread = Thread(target=count, args=(filename, byte, pair[0], pair[1]))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(global_count)
