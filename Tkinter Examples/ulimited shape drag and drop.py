import math
import tkinter.messagebox
from tkinter import *

root = Tk()

root.configure(background="lightgray")
root.resizable(width=True,height=True)
root.geometry("900x900")




canvas= Canvas(root)
canvas.config(width=1820,height=920)
canvas.config(background="#FFF9CA")
rect=canvas.create_rectangle(0,0,100,100,fill="red")
triangle = canvas.create_polygon(120,100,180,0,250,100,fill="green")
canvas.pack()
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
    rect=canvas.create_rectangle(0,0,100,100,fill="red")
    triangle = canvas.create_polygon(120,100,180,0,250,100,fill="green")

# Get an instance of the MouseMover object
mm = MouseMover()

# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)

root.mainloop()
    