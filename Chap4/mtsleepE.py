#!/usr/bin/env python3
"""
This script demonstrates basic use of threading.Thread class by subclassing it.
"""

from mtsleepD import loop
import threading
from time import sleep, ctime

loops = (4, 2)

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def main():
    print("starting at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:  # Starts threads
        threads[i].start()

    # Waits for all threads to finish.
    for i in nloops:
        threads[i].join()

    print("all DONE at:", ctime())

if __name__ == "__main__":
    main()
