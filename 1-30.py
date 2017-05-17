import re

patt = r'(\S+\.\S+\.\S{3})((?: \S+)*)'

with open('1-30data.txt', 'r') as data, open('list.html', 'w') as page:
    page.write('''
    <html>
    <head>
    <title>Cool Websites</title>
    </head>
    <body>
    <h1>Check out these cool websites!</h1>
    <h3>(Exercise 1-30)</h3>
    ''')
    for eachLine in data:
        match = re.match(patt, eachLine)
        page.write('<p>')
        if match.groups()[1] != '': #description provided
            page.write("<a href='%s' target='_blank'>%s</a>" % (match.group(1), match.group(2)))
        else:
            page.write("<a href='%s' target='_blank'>%s</a>" % (match.group(1), match.group(1)))
        page.write('</p>\n')
    page.write('''
    </body>
    </html>
    ''')
