import re
from time import ctime

with open('redata.txt', 'r') as f:
    for eachLine in f:
        dtstr = re.match('(.+?)::', eachLine).group(1)
        dtstr_exp = ctime(int(re.search('::(\d+)-', eachLine).group(1)))
        if dtstr != dtstr_exp:
            print False
            break
    else:
        print True
