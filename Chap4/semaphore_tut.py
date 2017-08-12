#!/usr/bin/env python3
import random, time
from threading import BoundedSemaphore, Thread

max_items = 5
container = BoundedSemaphore(max_items)  # consider this as a container with a capacity of 5 items.
                                         # Defaults to 1 if nothing is passed.

def producer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        try:
            container.release()
            print("Produced an item.")
        except ValueError:
            print("Full, skipping.")

def consumer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        if container.acquire(False):  # Here we disable the default blocking behaviour by passing False for the blocking flag.
            print("Consumed an item.")
        else:
            print("Empty, skipping.")

threads = []
nloops = random.randrange(3, 6)
print("Starting with %s items." % max_items)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops+max_items+2),)))

for thread in threads:  # Starts all the threads.
    thread.start()
for thread in threads:  # Waits for threads to complete before moving on with the main script.
    thread.join()
print("All done.")
