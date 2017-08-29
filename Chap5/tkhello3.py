#!/usr/bin/env python3
import tkinter


class TextButton(tkinter.Button):  # For Exercise 5-4.
    def __init__(self, *args, **kwargs):
        self.modify_button = kwargs["modify_button"]
        del kwargs["modify_button"]  # So that it isn't passed to tkinter.Button, as that will give an 'unknown option' error.
        kwargs["command"] = lambda: change_text(self.modify_button, self.cget("text"))  # Overrinding command.
        tkinter.Button.__init__(self, *args, **kwargs)


def change_text(button, text):
    button.config(text=text)


top = tkinter.Tk()
top.title("Text Changer")

hello = tkinter.Label(top, text="Hello World!")
hello.pack()

#change_frame = tkinter.Frame(top)  # To contain the label-text-changing buttons. 

v = tkinter.StringVar(top)
v.set(hello["text"])
for text in ["Click here", "Click on Me", "I'm the One"]:
    text_button = tkinter.Radiobutton(top, text=text, variable=v, value=text)
    text_button.pack(anchor=W)

update = tkinter.Button(top, text="Update", command=lambda: hello.config(text=v.get()))  # To update the label's text.
update.pack()


quit = tkinter.Button(top, text="QUIT", command=top.quit, bg="red", fg="white")
quit.pack(fill=tkinter.X, expand=1, side=tkinter.BOTTOM)
tkinter.mainloop()
