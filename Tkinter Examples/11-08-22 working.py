from tkinter import *

root = Tk()
root.geometry("1000x1000")


xcc=0



canvas= Canvas(root)
canvas.config(width=1000,height=1000)
leftside=canvas.create_rectangle(0,0,500,1000,fill="red")
rightside=canvas.create_rectangle(500,0,1000,1000,fill="orange")



triangle = canvas.create_polygon(120,100,180,0,250,100,fill="green")
triangle1 = canvas.create_polygon(120,100,180,0,250,100,fill="green")
canvas.grid(column=0,row=0)
old=canvas.create_rectangle(0,0,100,100,fill="blue")

class MouseMover():
  def __init__(self):
    self.triangle = canvas.create_polygon(120,100,180,0,250,100,fill="green")
    self.triangle1 = canvas.create_polygon(120,100,180,0,250,100,fill="green")
    self.item = 0; self.previous = (0, 0)
    self.rect=canvas.create_rectangle(0,0,100,100,fill="blue")
    self.rect1=canvas.create_rectangle(0,0,100,100,fill="blue")
    print(self.item)
  def select(self, event):
    global xcc
    
    widget = event.widget                       # Get handle to canvas 
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    print(self.item)
   
    
   
    
  def drag(self, event):
  
  
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    if self.item !=1 and self.item != 2:
          canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
          self.previous = (xc, yc)
    
    
  def release(self,event):
     global old
     
     widget = event.widget
     xc = widget.canvasx(event.x)
     if  self.item==5 and xc<500:
          canvas.delete(self.rect)
          self.rect1=canvas.create_rectangle(0,0,100,100,fill="blue")
          canvas.delete(self.triangl1)
          self.triangle1 = canvas.create_polygon(120,100,180,0,250,100,fill="green")
     elif xc<500:
          canvas.delete(self.rect1)
          self.rect1=canvas.create_rectangle(0,0,100,100,fill="blue")
          canvas.delete(self.triangle1)
          self.triangle1 = canvas.create_polygon(120,100,180,0,250,100,fill="green")
     else:
          self.rect1=canvas.create_rectangle(0,0,100,100,fill="blue")
          self.triangle1 = canvas.create_polygon(120,100,180,0,250,100,fill="green")
          #for trinagle
    
     
    
# Get an instance of the MouseMover object
mm = MouseMover()

# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)
canvas.bind("<ButtonRelease-1>",mm.release)





root.mainloop()