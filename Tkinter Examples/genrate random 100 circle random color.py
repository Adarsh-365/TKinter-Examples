from tkinter import *
import random
from random import randint
root=Tk()

canvas= Canvas(root)
canvas.configure(width=1000,height=1000)
canvas.pack()
for i in range(100):
    ch1=("1","2","3","4","5","6", "7", "8", "9", "0", "A", "B", "C", "D", "E",  "F" )      
  
    selt1=random.choice(ch1) 
    selt2=random.choice(ch1) 
    selt3=random.choice(ch1)
    selt4=random.choice(ch1) 
    selt5=random.choice(ch1) 
    selt6=random.choice(ch1)
    
    string = "#"+str(selt1)+str(selt2) +str(selt3)+str(selt4)+str(selt5) +str(selt6)
    
    x=randint(0, 1000)
    y=randint(0, 1000)
    x1=x+100
    y1=y+100
    canvas.create_oval(x,y,x1,y1, fill=string)

class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
  def select(self, event):
    widget = event.widget                       # Get handle to canvas 
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    print((xc, yc, self.item))
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)


# Get an instance of the MouseMover object
mm = MouseMover()

# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)
root.mainloop()
