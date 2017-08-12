#!/usr/bin/env python3
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num = 4
b = Barrier(num) # 4 threads will need to pass this barrier to get released.
names = ["Harsh", "Lokesh", "George", "Iqbal"]

def player():
    name = names.pop()
    sleep(randrange(2, 5))
    print("%s reached the barrier at: %s" % (name, ctime()))
    b.wait()

threads = []
print("Race starts now...")
for i in range(num):
    threads.append(Thread(target=player))
    threads[-1].start()

for thread in threads:  # Waits for the threads to complete before moving on with the main script.
    thread.join()
print("\nRace over!")
