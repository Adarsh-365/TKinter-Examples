from tkinter import *
from time import time
from PIL import ImageTk, Image


root=Tk()
root.configure(background='black')
st=time()
root.wm_attributes('-fullscreen',True)

img = ImageTk.PhotoImage(Image.open("add.jpg"))


label = Label(root, image = img)
label.place(x=200,y=250)


def count():
   ct=time()
   t=ct-st
  
   if t>5:
      
       label.destroy()
       root.destroy()
       
   root.after(1000,count)







count()
root.mainloop()