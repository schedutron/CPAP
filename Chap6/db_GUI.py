#!/usr/bin/env python3
import time, tkinter
from ushuffle_dbU import *  #DBNAME, NAMELEN, randName, FIELDS, tformat, cformat,\
#setup

top = tkinter.Tk()
top.title("User Shuffle")

choice = tkinter.StringVar()
choice.set("sqlite, mysql or gadfly")

choice_input = tkinter.Entry(top, textvariable=choice)
choice_input.pack()
choose = tkinter.Button(top, text="Go!", command = lambda: main(choice.get()))
choose.pack()

status = tkinter.StringVar()
status.set("Waiting for input...")
status_disp = tkinter.Label(top, textvariable=status)
status_disp.pack()


def db_dump(cur, data_frame):
    title_frame = tkinter.Frame(data_frame)
    columns = []
    for attribute in FIELDS:
        col = tkinter.Frame(title_frame)
        header = tkinter.Label(col, text=attribute.upper())
        header.pack()
        col.pack(side=tkinter.RIGHT)
        columns.append(col)

    title_frame.pack()

    cur.execute('SELECT * FROM users')
    for data in cur.fetchall():
        for i in range(len(data)):
            attrib = data[i]
            col = tkinter.Label(columns[i], text=attrib)
            col.pack()


def random_move():
    status.set("Randomly moving folks")
    fr, to, num = update(cur)
    top.after(1000, lambda: status.set("(%d users moved) from (%d) to (%d)" % (num, fr, to)))
    data_frame = tkinter.Frame(top)
    data_frame.pack()
    db_dump(cur, data_frame)

    top.after(3000, data_frame.pack_forget)


def random_remove():
    status.set("Randomly choosing group")
    rm, num = delete(cur)
    top.after(1000, lambda: status.set('(group #%d; %d users removed)' % (rm, num)))
    data_frame = tkinter.Frame(top)
    data_frame.pack()
    db_dump(cur, data_frame)

    top.after(3000, data_frame.pack_forget)


def final():
    status.set("Dropping users table")
    drop(cur)
    top.after(1000, status.set("Close cxns"))
    cur.close()
    cxn.commit()
    cxn.close()


def main(db):
    global cur
    global cxn
    status.set("Connect to %r database" % db)
    cxn = connect(db, DBNAME)

    if not cxn:
        status.set("ERROR: %r not supported or unreachable, exit" % db)
        return
    cur = cxn.cursor()
    status.set('Creating users table')
    if create(cur) == 3:
        return None

    status.set("Inserting names into table")
    insert(cur, db)

    #time.sleep(1)
    data_frame = tkinter.Frame(top)
    #scrollbar = tkinter.Scrollbar(data_frame)
    #scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    #container = tkinter.Canvas(data_frame, yscrollcommand=scrollbar.set)
    #scrollbar.configure(command=container.yview)
    #container.pack(side=tkinter.LEFT)
    db_dump(cur, data_frame)
    data_frame.pack()
    top.after(3000, data_frame.pack_forget)

    top.after(3000, random_move)
    top.after(6000, random_remove)
    top.after(9000, final)


if __name__ == '__main__':
    tkinter.mainloop()
