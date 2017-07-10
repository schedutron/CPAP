#!/usr/bin/env python3
"This is a HTTP Client Application implemented via webbrowser module."
import webbrowser

url = input("Enter a url to visit: ")
webbrowser.open(url)
print("Thanks for using this client!")
