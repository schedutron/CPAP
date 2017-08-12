#!/usr/bin/env python3

import random, time
from threading import Condition, Thread

# This will be used to represent the availability of a produced item.
condition = Condition()

box = []

def producer(box, nitems):
    for i in range(nitems):
        time.sleep(random.randrange(2, 5))  # Sleeps for some time.
        condition.acquire()
        num = random.randint(1, 10)
        box.append(num)  # Puts an item into box for consumption.
        condition.notify()  # Notifies the consumer about the availability.
        print("Produced:", num)
        condition.release()

def consumer(box, nitems):
    for i in range(nitems):
        condition.acquire()
        condition.wait()  # Blocks until an item is available for consumption.
        print("%s: Acquired: %s" % (time.ctime(), box.pop()))
        condition.release()

threads = []
nloops = random.randrange(3, 6)  # Number of times an item will be produced and consumed.
for func in [producer, consumer]:
    threads.append(Thread(target=func, args=(box, nloops)))
    threads[-1].start()  # Starts the thread.

for thread in threads:
    '''Waits for the threads to complete before moving on
       with the main script.
    '''
    thread.join()
print("All done.")
