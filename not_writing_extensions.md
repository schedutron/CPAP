I used Cython to redo the program in Exercise 8-5 and I didn't have to write a single
line of C! First I created a Python file containing the functionality to be
ported to C (and thus be an extension to Python), and then created a small
[setup.py](./cy_setup.py) file for building. Then a single command line
statement built the compiled extension which was ready to be imported and used
in Python! This felt like orders of magnitude easier than writing manual
extensions in C (with the overhead of the 'glue' functions involved (those
which retured `PyObject`s)), even for the small program of E8-5! For larger
codebases, the difference will be surely more vibrant.