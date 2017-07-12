#!/usr/bin/env python3
"""This script demonstrates locks for threads."""

import _thread #thread in Python2.x
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print("starting loop", nloop, "at:", ctime())
    sleep(nsec)
    print("loop ", nloop, "done at:", ctime())
    lock.release()


def main():
    print("starting at:", ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire() # 'locks' the lock
        locks.append(lock)

    """
    Why not start threads in the above loop itself?
    There are 2 reasons:
    1st: threads are synchronized in a separate loop - all horses start out the
    gate around the same time.
    2nd: locks take some time to acquire, so we don't want to start threads with
    unprepared locks.
    """
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    """
    Notice an interesting thing in the following loop: we're at mercy of slower
    iterations if they're near the beginning. When the zeroth lock is released,
    the other lock has already been unlocked!
    """
    for i in nloops:
        while locks[i].locked(): pass

    print("all DONE at:", ctime())

if __name__ == "__main__":
    main()
