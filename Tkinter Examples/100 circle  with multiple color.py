from tkinter import *
from tkinter import ttk
import random



root =Tk()

root.title("Python Gui")

root.geometry("900x900")
canvas=Canvas(root)

canvas.config(width=1820,height=920)

for i in range(100):
  
    ch1=("1","2","3","4","5","6", "7", "8", "9", "0", "A", "B", "C", "D", "E",  "F", )      
  
    selt1=random.choice(ch1) 
    selt2=random.choice(ch1) 
    selt3=random.choice(ch1)
    selt4=random.choice(ch1) 
    selt5=random.choice(ch1) 
    selt6=random.choice(ch1)
    
    string = "#"+str(selt1)+str(selt2) +str(selt3)+str(selt4)+str(selt5) +str(selt6)
    string1 = "#"+str(selt6)+str(selt5) +str(selt4)+str(selt3)+str(selt2) +str(selt1)
 
    oval=canvas.create_oval(120,20,280,180,fill=string,outline=("black"))
    rect= canvas.create_rectangle(120,200,280,480,fill=string1,outline=("black"))

class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
   
  def select(self, event):
    widget = event.widget        
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]       
    self.previous = (xc, yc)
    print((xc, yc, self.item))
    
   
   
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)
 
    
      


mm = MouseMover()




canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)


canvas.pack()

root.mainloop()