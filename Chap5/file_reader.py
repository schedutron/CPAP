#!/usr/bin/env python3
import os, tkinter

def display(filename):
    if not (os.path.exists(filename) and not os.path.isdir(filename)):
        content.set(filename+": No such file")
        top.title(main_title+" - "+filename+": No such file")
        return
    with open(filename) as f:
        content.set(f.read())
        top.title(main_title+" - "+filename)

top = tkinter.Tk()
main_title = "File Reader"
top.title(main_title)
content = tkinter.StringVar()
filename = tkinter.StringVar()
text_label = tkinter.Label(top, textvariable=content, justify=tkinter.LEFT)
text_label.pack(fill='both')

entry_field = tkinter.Entry(top, width=50, textvariable=filename)
entry_field.bind("<Return>", lambda event: display(filename.get()))
entry_field.pack()

tkinter.mainloop()