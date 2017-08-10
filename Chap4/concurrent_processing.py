#!/usr/bin/env python3
from os import listdir, stat
from sys import argv
from threading import Thread


def counter(filename, byte):
    size = stat(filename).st_size
    with open(filename, 'rb') as f:
        count = 0
        for i in range(size):
            if f.read(1) == byte:
                count += 1
        print("%s: %s" % (filename, count))


dir_path = argv[1]  # Assumes trailing '/'.
byte = bytes(argv[2], "utf-8")  # Assumes Unicode encoding as default.
try:
    filenames = listdir(dir_path)
except FileNotFoundError:
    print("No such directory found.")
    quit()

threads = []
for filename in filenames:
    #counter(dir_path+filename, byte)
    threads.append(Thread(target=counter, args=(dir_path+filename, byte)))
    threads[-1].start()
for thread in threads:
    thread.join()
