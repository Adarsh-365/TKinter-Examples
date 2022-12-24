from tkinter import *

root=Tk()
root.geometry("300x300")
root.configure(bg="Silver")

lb= Listbox(root,bg="Magenta",bd=5,fg="Cyan",selectbackground="Maroon",selectmode=EXTENDED    )

lb.insert(1, "Python")
lb.insert(2, "Python")
lb.insert(3, "Python")
lb.insert(4, "Python")
lb.insert(5, "Python")
lb.insert(6, "Python")
lb.insert(7, "Python")
lb.insert(8, "Python")

lb.grid(column=0,row=0)

root.mainloop()