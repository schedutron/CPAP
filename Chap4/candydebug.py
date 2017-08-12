#!/usr/bin/env python3

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)


def refill():
    lock.acquire()
    print("Refilling candy...", end=" ")
    try:
        candytray.release()
    except ValueError:
        print("full, skipping")
    else:
        print("inventory:", candytray._value)
    lock.release()


def buy():
    lock.acquire()
    print("Buying candy...", end=" ")
    if candytray.acquire(False):
        print("inventory:", candytray._value)
    else:
        print("empty, skipping")
    lock.release()


def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def _main():
    print("starting at:", ctime())
    nloops = randrange(2, 6)
    print("THE CANDY MACHINE (full with %d bars)!" % MAX)
    Thread(
    target=consumer, args=(randrange(nloops, nloops+MAX+2),)
    ).start()  # buyer
    Thread(target=producer, args=(nloops,)).start()  # vndr


@register
def _atexit():
    print("all done at:", ctime())


if __name__ == "__main__":
    _main()
