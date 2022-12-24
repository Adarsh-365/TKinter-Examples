from tkinter import *
from tkinter import ttk



root =Tk()

root.title("Python Gui")

root.geometry("900x900")
canvas=Canvas(root)

canvas.config(width=1820,height=920)


coord = 400, 50, 540, 210
arc = canvas.create_arc(coord, start=0, extent=180, fill="blue")
rect=canvas.create_rectangle(60,220,380,360,fill="red")
squr=canvas.create_rectangle(120,420,320,620,fill="black")

oval=canvas.create_oval(120,20,280,180,fill="green")
poly=canvas.create_polygon(200,650,100,850,300,850,fill="orange")


class MouseMover():
  def __init__(self):
    self.store=StringVar()
    self.store=""
    self.item = 0; self.previous = (0, 0)
  def select(self, event):
    widget = event.widget                       # Get handle to canvas 
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
   
   
   
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    #canvas.configure(3,fill="orange")
    self.previous = (xc, yc)
   
  def dbcl(self,event):
      widget = event.widget
      canvas.lift(self.item)  
  def right(self,event):
      widget=event.widget
      xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
      self.store=str(xc)+","+str(yc)+","+str(self.item)
      
      print(self.store)
 
      

# Get an instance of the MouseMover object
mm = MouseMover()



# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<ButtonRelease-1>", mm.right)
canvas.bind("<B1-Motion>", mm.drag)
canvas.bind("<Double-1>",mm.dbcl)

canvas.pack()

root.mainloop()