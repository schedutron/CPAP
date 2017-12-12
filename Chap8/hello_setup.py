#!/usr/bin/env python2
from distutils.core import setup, Extension

MOD = "helloWorld"
setup(name=MOD, ext_modules=[
    Extension(MOD, sources=["helloWorld.c"])
    ]
)