#!/usr/bin/env python3
import psycopg2
from password import PASSWORD

conn = psycopg2.connect("dbname='py_test' user='binaryBoy' host='localhost' password='%s'" % PASSWORD)
cur = conn.cursor()

cur.execute("SELECT * FROM nums")
rows = cur.fetchall()
with open("output.html", "w") as f:
    f.write("<html?\n<head>\n<title>Output</title>\n</head>\n<body>\n")
    for row in rows:
        f.write("<p>%s</p>" % row[0])
    f.write("</body>\n</html>")