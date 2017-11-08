It can be easily shown that `distutils.log.warn()` is not completely
compatible with `print`. Consider the following code snippet:

```
from distutils.log import warn
print("hello", "world")
warn("hello", "world")
```

When this snippet is run, the `print` function executes successfully,
displaying the passed strings to the console. But `warn()` spits out a
`TypeError`; perhaps because it doesn't expect an arbitrary number of strings
passed to it.