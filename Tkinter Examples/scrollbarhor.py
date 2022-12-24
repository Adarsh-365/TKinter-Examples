from tkinter import *

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var ,repeatdelay=3000,sliderlength=50,tickinterval=0.25
             , from_=-330,to_=755,label="from 5 to 55",length=700,orient=HORIZONTAL )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()