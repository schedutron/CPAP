#!/usr/bin/env python3
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen

REGEX = compile(r"#([\d,]+) in Books ")
AMZN = "http://amazon.com/dp/"
ISBNs = {
    '0132269937': "Core Python Programming",
    '0132356139': "Python Web Development with Django",
    '0137143419': "Python Fundamentals"
}

def get_ranking(isbn):
    page = urlopen("%s%s" % (AMZN, isbn))  # Or str.format()
    data = page.read().decode()
    page.close()
    return REGEX.findall(data)[0]

def _show_ranking(isbn):
    print("- %r ranked %s" % (ISBNs[isbn], get_ranking(isbn)))

def _main():
    print("At", ctime(), "on Amazon...")
    for isbn in ISBNs:
        Thread(target=_show_ranking, args=(isbn,)).start()

@register
def _atexit():
    print("all DONE at:", ctime())

if __name__ == "__main__":
    _main()
