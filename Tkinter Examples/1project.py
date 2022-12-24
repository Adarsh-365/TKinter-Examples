from tkinter import *




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
line=canvas.create_line(10,0,10,200,fill="#ff0066",width=10)

class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
  def select(self, event):
    widget = event.widget 
 # widget = event.widget
    canvas.lift(self.item)                        # Get handle to canvas 
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasy(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    ww="black"
    tt=squr
    if self.item==1:
        ww="blue"
    elif self.item==2:
        ww="red"
    elif self.item==3:
        ww="black"
    elif self.item==4:
        ww="green"
    elif self.item==5:
        ww="orange"
    else:
        ww="#ff0066"
  
    canvas.itemconfigure(tt,fill=ww)
    print("Coordinates of the object are:", canvas.coords(oval))
   
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasy(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)
   
  def dbcl(self,event):
      widget = event.widget
      canvas.lift(self.item)    
 
  
      

# Get an instance of the MouseMover object
mm = MouseMover()



# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
#canvas.bind("<Button-1>", mm.changecolor)
canvas.bind("<B1-Motion>", mm.drag)
canvas.bind("<Double-1>",mm.dbcl)

canvas.pack()

root.mainloop()