One obvious advantage of using extensions is the performance improvement.
Considering the examples we went through, the time taken to calculate
factorials (which fit in `int` data type) was about 100 times faster than
a traditional Python method delivering the same functionality (since the
code gets already compiled). Another advantage is that extensions can act like
a glue for programs written in C and Python. For example, if we have some code
written in C and want to re-use its functionality in Python, we can simply
write Python extensions for that code instead of porting it to Python by
re-writing the functionality in the latter language.