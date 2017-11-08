```
from distutils.log import warn
if hasattr(__builtins__, 'print'):
    printf = print
else:
    printf = warn
```

The problem with the above code is that the `if` condition is `True` even for
Python2. To fix it, we must `import sys` and change that line to:
`if sys.version_info[0] == 3:`

Further, we can add an `elif` statement to see whether this is part of the main
script to be executed, or if it is imported to some other script, just like
we did in `ushuffle_dbU.py`.