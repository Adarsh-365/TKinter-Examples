import tkinter as tk
from tkinter import *

root=tk.Tk()

l=tk.Label(root,text="Right click display Menu",width=50,height=50)
l.pack()
m=Menu(root,tearoff=0)

m.add_command(label="View")
m.add_command(label="Sort by")
m.add_command(label="Refresh")
m.add_separator()
m.add_command(label="Paste")
m.add_command(label="Paste Shortcut")
m.add_separator()
m.add_cascade(label="New")

def dopopof(event):
    try:
        m.tk_popup(event.x_root,event.y_root)
        
    finally:
        m.grab_release()
l.bind('<Button-3>',dopopof)

root.mainloop()

