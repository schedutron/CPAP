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
.
.
.
def add_to_the_last(some_list, val):
    lock.acquire()
    some_list.append(val)
    lock.release()
    return some_list
```
