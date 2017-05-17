import re

with open('redata.txt', 'r') as f:
    for eachLine in f:
        phrase = re.match(r'\w{3} (\w{3}) [ ]?(\d\d?).+?(\d{4})', eachLine)
        print '%s, %s, %s' % (phrase.group(1), phrase.group(2), phrase.group(3))
