import re, os

f = os.popen('who', 'r')
for eachLine in f:
    print re.split(r'\s+(?!\d+)|\t', eachLine.rstrip())
f.close()
