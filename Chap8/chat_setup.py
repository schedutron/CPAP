#!/usr/bin/env python2

from distutils.core import setup, Extension

MOD = "chat"
setup(name=MOD, ext_modules=[
    Extension(MOD, sources=["chat.c"])
    ]
)