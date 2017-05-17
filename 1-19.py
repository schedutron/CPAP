import re

with open('redata.txt', 'r') as f:
    for eachLine in f:
        time = re.search(r'\w{3} \w{3} [ ]?\d\d? \d{2}:\d{2}:\d{2} \d{4}', eachLine)
        if time: print time.group()
