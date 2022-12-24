from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="This is a LabelFrame",bg="red",padx=100,pady=100)
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

root.mainloop()