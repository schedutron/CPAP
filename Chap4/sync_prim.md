# Synchronization Primitives
## My answer to Exercise 4-11

### Locks
Locks are perhaps the simplest synchronization primitives in Python. A Lock has
only two states - locked and unlocked (surprise). It is created in the unlocked
state and has two principal methods - `acquire()` and `release()`. The `acquire()`
method locks the Lock and blocks execution until the `require()` method in some
other coroutine sets it to unlocked. Then it locks the Lock again
and returns `True`. The `release()` method should only be called in the locked
state, it sets the state to unlocked and returns immediately. If `release()` is
called in the unlocked state, a `RunTimeError` is raised.

Snippet:
```
lock = Lock()
g = 0

def add_one():
    lock.acquire()
    g += 1
    lock.release()

def add_two():
    lock.acquire()
    g += 2
    lock.release()

threads = []
for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

print(g)
```

### RLocks
The standard Lock doesn’t know which thread is currently holding the
lock. If the lock is held, any thread that attempts to acquire it will
block, even if the same thread itself is already holding the lock. (Source: [effbot.org]
[effbot]).
In such cases, RLock (re-entrant lock) is used.

Snippet:
```
import threading

num = 0

lock = Threading.Lock()
lock.acquire()
num += 1
lock.acquire()  # This will block.
num += 2
lock.release()

# With RLock, that problem doesn't happen.
lock = Threading.RLock()
lock.acquire()
num += 3
lock.acquire()  # This won't block.
num += 4
lock.release()
lock.release() # You need to call release once for each call to acquire.
```

One good use case for RLocks is recursion, when a parent call  of a function would otherwise
block its nested call. Thus, the main use for RLocks is nested access to shared
resources.

[effbot]: http://effbot.org/zone/thread-synchronization.htm
