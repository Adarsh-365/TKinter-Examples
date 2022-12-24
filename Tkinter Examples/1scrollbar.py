from tkinter import *
from tkinter import ttk
root = Tk()
color="red"
h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set,
xscrollcommand=h.set)
canvas.create_rectangle(0,0,500,500, fill="red")
h['command'] = canvas.xview
v['command'] = canvas.yview
#ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))
canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


root.mainloop()