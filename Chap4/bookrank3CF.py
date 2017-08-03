#!/usr/bin/env python3
from atexit import register
from concurrent.futures import ThreadPoolExecutor
from re import compile
import requests
from threading import Thread
from time import ctime
#from urllib.request import urlopen - Doesn't work.

REGEX = compile(b"#([\d,]+) in Books ")
AMZN = "http://amazon.com/dp/"
ISBNs = {
    '0132269937': "Core Python Programming",
    '0132356139': "Python Web Development with Django",
    '0137143419': "Python Fundamentals"
}


def get_ranking(isbn):
    with requests.get("{0}{1}".format(AMZN, isbn)) as page:
        return str(REGEX.findall(page.content)[0], "utf-8")


def _show_ranking(isbn):
    print("- %r ranked %s" % (ISBNs[isbn], get_ranking(isbn)))


def _main():
    print("At", ctime(), "on Amazon...")
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(
        ISBNs,
        executor.map(get_ranking, ISBNs)
        ):
            print("- %r ranked %s" % (ISBNs[isbn], ranking))


@register
def _atexit():
    print("all DONE at:", ctime())

if __name__ == "__main__":
    _main()
