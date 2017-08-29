#!/usr/bin/env python3
import os, tkinter

def display(fn):
    global current_file
    if state == 0:
        display_popup(fn=[current_file, fn], change=True)  # To ask for saving pending changes.
    else:
        show(fn)
    current_file = fn


def show(fn):

    text_field.bind("<KeyPress>", lambda event: change_state())
    
    if not (os.path.exists(fn) and not os.path.isdir(fn)):
        top.title(main_title+" - "+fn+": New file")
    else:
        with open(fn) as f:
            text_field.delete("1.0", tkinter.END)  # Removes any previous text.
            text_field.insert(tkinter.INSERT, f.read())
        top.title(main_title+" - "+fn)
    change_dimensions()


def save(filen, q=None, popup=None):
    global state
    with open(filen, "w") as f:
        f.write((text_field.get("1.0", tkinter.END).strip()))  # Save the entire content, from start to end.
        top.title(main_title+" - "+filen)
    state = 1
    if q: top.quit()  # If the window's close button is pressed.
    if popup:
        popup.destroy()
    change_dimensions()
    if not q:
        show(filename.get())


def display_popup(fn, q=None, change=False):
    def no_func():
        popup.destroy()
        show(fn[1])

    popup = tkinter.Toplevel()
    popup.geometry("200x60")
    popup.title("Save changes?")
    if change:  # When new file is loaded without saving the current file.
        p = popup  # p is to be passed into save for closing the popup.
    else:
        p = None
    yes = tkinter.Button(popup, text="Yes", command=lambda: save(fn[0], q, popup=p))
    yes.pack()

    if q:  # When the window's close button in pressed.
        c = top.quit
    else:
        c = no_func
    no = tkinter.Button(popup, text="No", command=c)
    no.pack()
    #top.wait_window(popup)


def on_closing():
    if state == 0:
        display_popup(fn=[current_file, current_file], q=True)
    else:
        top.quit()


def change_state():
    def do_nothing():
        pass
    
    global state
    state =  0
    top.title(main_title+" - "+filename.get()+"*")
    change_dimensions()
    text_field.bind("<KeyPress>", lambda event: do_nothing())

def change_dimensions():
    global switch
    switch = not switch
    if switch:
        width = 481
    else:
        width = 480
    top.geometry("640x%i" % width)


top = tkinter.Tk()
top.geometry("640x480")
main_title = "File Reader"
top.title(main_title)
switch = False  # For dimension changes.
state = 1  # 1 for saved, 0 for unsaved.
filename = tkinter.StringVar()
text_field = tkinter.Text(top)
text_field.pack(fill='both')

entry_field = tkinter.Entry(top, width=50, textvariable=filename)
entry_field.bind("<Return>", lambda event: display(filename.get()))
entry_field.pack()

save_button = tkinter.Button(top, text="Save", command=lambda: save(filename.get()))
save_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

tkinter.mainloop()