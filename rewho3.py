import re, os

with os.popen('who', 'r') as f:
    for eachLine in f:
        print(re.split(r'\s+(?!\d+)|\t', eachLine.rstrip()))
