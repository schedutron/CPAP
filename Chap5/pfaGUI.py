#!/usr/bin/env python3
from functools import partial as pto
from tkinter import Button, Tk, X
from tkinter.messagebox import showinfo, showwarning, showerror

CRIT = "crit"
WARN = "warn"
REGU = "regu"

SIGNS = {
    "do not enter": CRIT,
    "railroad crossing": WARN,
    "55\nspeed limit": REGU,
    "merging traffic": WARN,
    "wrong way": CRIT,
    "one way": REGU,
}

critCB = lambda: showerror("Error", "Error Button Pressed!")
warnCB = lambda: showwarning("Warning", "Warning Button Pressed!")
reguCB = lambda: showinfo("Info", "Info Button Pressed")

top = Tk()
top.title("Road Signs")
Button(top, text="QUIT", command=top.quit, bg="red", fg="white").pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg="white", fg="red")
WarnButton = pto(MyButton, command=warnCB, bg="goldenrod1")
ReguButton = pto(MyButton, command=reguCB, bg="white")

for each_sign in SIGNS:
    sign_type = SIGNS[each_sign]
    cmd = "%sButton(text=%r%s).pack(fill=X, expand=True)" % (sign_type.title(),
        each_sign, '.upper()' if sign_type == CRIT else '.title()')
    eval(cmd)
top.mainloop()
