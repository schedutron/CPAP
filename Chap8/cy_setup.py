#!/usr/bin/env python2
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("helloworld.pyx")
)
