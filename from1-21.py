import re

def extract(what, eachLine):
    if what == 'months':
        return re.search(r'[A-Za-z]{3} ([A-Za-z]{3}) [ ]?\d\d?', eachLine)
    if what == 'years':
        return re.search(r'\d (\d{4})::', eachLine)
    if what == 'time':
        return re.search(r'(\d{2}:\d{2}:\d{2})', eachLine)
    if what == 'login domain':
        return re.search(r'([A-Za-z]+)@([A-Za-z]+\.[A-Za-z]{3})', eachLine)

with open('redata.txt', 'r') as f:
    what = raw_input('What do you want to extract? ')
    for eachLine in f:
        text = extract(what, eachLine)
        if text:
            for g in text.groups():
                print g,
            print
