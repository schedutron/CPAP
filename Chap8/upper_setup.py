#!/usr/bin/env python2

from distutils.core import setup, Extension

MOD = "upper"
setup(name=MOD, ext_modules=[
    Extension(MOD, sources=['upper.c'])
    ]
)