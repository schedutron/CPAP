import re

with open('redata.txt', 'r') as f:
    for eachLine in f:
        email = re.search(r'[A-Za-z]+@[A-Za-z]+\.[A-Za-z]{3}', eachLine)
        if email: print email.group()
