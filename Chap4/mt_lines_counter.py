#!/usr/bin/env python3
from os import listdir
from sys import argv
from threading import Thread


def counter(filename):
    with open(filename) as f:
        count = 0
        for line in f:
            count += 1
        print("%s: %s" % (filename, count))

dir_path = argv[1]  # Assumes trailing '/'.
try:
    filenames = listdir(dir_path)
except FileNotFoundError:
    print("No such directory found.")
    quit()

for filename in filenames:
    #counter(dir_path+filename)
    Thread(target=counter, args=(dir_path+filename,)).start()
