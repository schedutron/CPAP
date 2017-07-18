#!/usr/bin/env python3
"""This script demonstrates basic use of threading module."""

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print("starting loop", nloop, "at:", ctime())
    sleep(nsec)
    print("loop ", nloop, "done at:", ctime())

def main():
    print("starting at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:  # Starts threads
        threads[i].start()

    # Waits for all threads to finish.
    for i in nloops:
        threads[i].join()

    print("all DONE at:", ctime())

if __name__ == "__main__":
    main()
