We need to check whether `__builtins__` is a dict versus a module so as to
assign the appropriate input function to `scanf`. In an imported module,
`__builtins__` is a dict, whereas in the main application which is executed,
it is a module. The conditionals basically say that if we were imported, check
if `raw_input` was in the dictionary, otherwise check if it is defined in the
main module, via `hasattr`, or else assign `input` to `scanf`, which is to say
the script is using Python3. All of this is done to have a well-defined,
universal `scanf` for taking user inputs, which runs in both Python2 and
Python3.