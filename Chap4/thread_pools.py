#!/usr/bin/env python3

from myThread import MyThread
from queue import Queue
from random import randint
from sys import argv
from time import sleep


def writeQ(queue):
    print("producing object for Q...", end=" ")
    queue.put("xxx", 1)
    print("size now:", queue.qsize())


def readQ(queue):
    if queue.get(1):
        print("consumed object from Q... size now", queue.qsize())
    else:
        print("Q currently empty...")


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(5, 7))


def main():
    nloops = int(argv[1])
    q = Queue(32)
    nconsumers = int(argv[2])

    if nloops < nconsumers:
        print("Too many threads for %s loops. Use less threads." % nloops)
        return

    threads = [MyThread(writer, (q, nloops), writer.__name__)]
    for i in range(nconsumers):
        t = MyThread(reader, (q, nloops//nconsumers), 'consumer %s' % i)
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("all DONE")


if __name__ == "__main__":
    main()
