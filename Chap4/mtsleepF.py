#!/usr/bin/env python3
from atexit import register
from random import randrange
from threading import currentThread, Lock, Thread
from time import ctime, sleep

class CleanOutputSet(set):
    def __str__(self):
        return ", ".join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print("[%s] Started %s" % (ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print("[%s] Completed %s (%d secs)" % (ctime(), myname, nsec))
    print("    (remaining: %s)" % (remaining or "NONE"))
    lock.release()


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print("all DONE at:", ctime())


if __name__ == "__main__":
    _main()
