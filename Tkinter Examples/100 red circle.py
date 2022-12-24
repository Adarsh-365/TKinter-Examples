from tkinter import *
import random

root=Tk()
root.geometry("1000x1000")
canvas=Canvas(root)
canvas.configure(width=1000,height=1000)
canvas.pack()
for i in range(10):
  x=i*100
  y=i
  x1=x+100
  y1=y+100
  for i in range(10):
    canvas.create_oval(x,y,x1,y1,fill="red")
    x=x
    y=y+100
    x1=x+100
    y1=y+100
    
   
   

root.mainloop()