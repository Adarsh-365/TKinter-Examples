from tkinter import *

root = Tk()

root.geometry("300x300")

root.configure(background="green")

var=DoubleVar()

scale=Scale(root, variable = var,activebackground="blue",bg="red",bd=10)
scale.pack(anchor=CENTER)

root.mainloop()
