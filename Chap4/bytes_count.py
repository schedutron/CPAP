#!/usr/bin/env python3
"""Script to count number of occurences of a byte in a given file. Default
encoding of file and passed letter is assumed to be utf-8."""
import sys

filename = sys.argv[1]
byte = bytes(sys.argv[2], 'utf-8')

with open(filename, 'rb') as f:
    count = 0
    while True:
        c = f.read(1)
        if not c:
            break
        if c == byte:
            count += 1
print(count)
