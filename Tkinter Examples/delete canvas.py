from tkinter import *

root = Tk()
root.geometry("1000x1000")





flag1=FALSE

canvas= Canvas(root)
canvas.config(width=550,height=920)
canvas.config(background="#FFF9CA")
rect=canvas.create_rectangle(0,0,100,100,fill="blue")
triangle = canvas.create_polygon(120,100,180,0,250,100,fill="green")
canvas.grid(column=0,row=0)

canvas1= Canvas(root)
canvas1.config(width=550,height=920)
canvas1.config(background="white")
canvas1.grid(column=1,row=0)

class MouseMover():
  def __init__(self):
     
    self.item = 0; self.previous = (0, 0)
  def select(self, event):
    global flag1
    
    widget = event.widget                       # Get handle to canvas 
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    print((xc, yc, self.item))
    
  def drag(self, event):\
  
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)
    tty=canvas.create_rectangle(0,0,100,100,fill="blue")
    triangle = canvas.create_polygon(120,100,180,0,250,100,fill="green")
    
  def release(self,event):
     widget = event.widget
     print("working")
     canvas.delete(rect)
     
     canvas.delete(triangle)
# Get an instance of the MouseMover object
mm = MouseMover()

# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)
canvas.bind("<ButtonRelease-1>",mm.release)





root.mainloop()