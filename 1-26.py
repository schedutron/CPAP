import re

lines = []
with open('redata.txt', 'r') as f:
    for eachLine in f:
        eachLine = re.sub(r'[A-Za-z]+@[A-Za-z]+\.[A-za-z]{3}', 'saurabh.chaturvedi63@gmail.com', eachLine)
        lines.append(eachLine)

with open('redata.txt', 'w') as f:
    for line in lines:
        f.write(line)
