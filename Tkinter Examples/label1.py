from tkinter import *

root = Tk()
var = StringVar()
label = Message( root, textvariable=var, relief=RAISED,bg="blue",fg="red" ,width=2000)

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()