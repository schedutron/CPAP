#!/usr/bin/env python3
import psycopg2
from password import PASSWORD

conn = psycopg2.connect("dbname='py_test' user='binaryBoy' host='localhost' password='%s'" % PASSWORD)
cur = conn.cursor()

cur.execute("SELECT * FROM nums")
rows = cur.fetchall()
total = 0
for row in rows:
    total += int(row[0])
    print(row[0])
print("Sum of the numbers is: %d" % total)