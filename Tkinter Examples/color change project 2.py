from tkinter import *
from tkinter import ttk



root =Tk()

root.title("Python Gui")

root.geometry("900x900")
canvas=Canvas(root)

canvas.config(width=1820,height=920)


coord = 400, 50, 540, 210
arc = canvas.create_arc(coord, start=0, extent=180, fill="blue")
arc1 = canvas.create_arc(coord, start=0, extent=180, fill="blue")
arc2 = canvas.create_arc(coord, start=0, extent=180, fill="blue")
arc3 = canvas.create_arc(coord, start=0, extent=180, fill="blue")
arc4 = canvas.create_arc(coord, start=0, extent=180, fill="blue")


rect=canvas.create_rectangle(60,220,380,360,fill="red")
rect1=canvas.create_rectangle(60,220,380,360,fill="red")
rect2=canvas.create_rectangle(60,220,380,360,fill="red")
rect3=canvas.create_rectangle(60,220,380,360,fill="red")
rect4=canvas.create_rectangle(60,220,380,360,fill="red")


squr=canvas.create_rectangle(120,420,320,620,fill="#ff0066")
squr1=canvas.create_rectangle(120,420,320,620,fill="#ff0066")
squr2=canvas.create_rectangle(120,420,320,620,fill="#ff0066")
squr3=canvas.create_rectangle(120,420,320,620,fill="#ff0066")
squr4=canvas.create_rectangle(120,420,320,620,fill="#ff0066")



oval=canvas.create_oval(120,20,280,180,fill="green")
oval1=canvas.create_oval(120,20,280,180,fill="green")
oval2=canvas.create_oval(120,20,280,180,fill="green")
oval3=canvas.create_oval(120,20,280,180,fill="green")
oval4=canvas.create_oval(120,20,280,180,fill="green")





poly=canvas.create_polygon(200,650,100,850,300,850,fill="orange")
poly1=canvas.create_polygon(200,650,100,850,300,850,fill="orange")
poly2=canvas.create_polygon(200,650,100,850,300,850,fill="orange")
poly3=canvas.create_polygon(200,650,100,850,300,850,fill="orange")
poly4=canvas.create_polygon(200,650,100,850,300,850,fill="orange")






class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
    self.tt=rect
    self.tt1=rect1
    self.tt2=rect2
    self.tt3=rect3
    self.tt4=rect4
  def select(self, event):
    widget = event.widget                       # Get handle to canvas 
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    print((xc, yc, self.item))
    
    ww="#ff0066"
    
   
    if self.item==1 or self.item== 2 or self.item ==3 or self.item ==4 or self.item==5 :
        ww="blue"
    elif self.item==6 or self.item== 7 or self.item ==8 or self.item ==9 or self.item==10 :
        ww="red"
    elif  self.item==11 or self.item==12 or self.item ==13 or self.item ==14 or self.item==15 :
        ww="#ff0066"
    elif  self.item==16 or self.item== 17 or self.item ==18 or self.item ==19 or self.item==20 :
        ww="green"
 
    else:
        ww="orange"
    print(ww)
    canvas.itemconfigure(self.tt,fill=ww)
    canvas.itemconfigure(self.tt1,fill=ww)
    canvas.itemconfigure(self.tt2,fill=ww)
    canvas.itemconfigure(self.tt3,fill=ww)
    canvas.itemconfigure(self.tt4,fill=ww)
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)
  def dbcl(self,event):
      widget = event.widget
      self.tt=squr
      if self.item==1 or self.item== 2 or self.item ==3 or self.item ==4 or self.item==5 :
          self.tt=arc
          self.tt1=arc1
          self.tt2=arc2
          self.tt3=arc3
          self.tt4=arc4
          
      elif self.item==6 or self.item== 7 or self.item ==8 or self.item ==9 or self.item==10 :
          self.tt=rect
          self.tt1=rect1
          self.tt2=rect2
          self.tt3=rect3
          self.tt4=rect4
      elif  self.item==11 or self.item==12 or self.item ==13 or self.item ==14 or self.item==15 :
          self.tt=squr
          self.tt1=squr1
          self.tt2=squr2
          self.tt3=squr3
          self.tt4=squr4
      elif  self.item==16 or self.item== 17 or self.item ==18 or self.item ==19 or self.item==20 :
          self.tt=oval
          self.tt1=oval1
          self.tt2=oval2
          self.tt3=oval3
          self.tt4=oval4
      else:
          self.tt=poly
          self.tt1=poly1
          self.tt2=poly2
          self.tt3=poly3
          self.tt4=poly4
       
      print(self.tt)
      print(self.tt1)
      print(self.tt2)
      print(self.tt3)
      print(self.tt4)
      
    
          
      canvas.itemconfig(arc,fill="blue")
      canvas.itemconfig(arc1,fill="blue")
      canvas.itemconfig(arc2,fill="blue")
      canvas.itemconfig(arc3,fill="blue")
      canvas.itemconfig(arc4,fill="blue")
      canvas.itemconfig(rect,fill="red")
      canvas.itemconfig(rect1,fill="red")
      canvas.itemconfig(rect2,fill="red")
      canvas.itemconfig(rect3,fill="red")
      canvas.itemconfig(rect4,fill="red")
      canvas.itemconfig(oval,fill="green")
      canvas.itemconfig(oval1,fill="green")
      canvas.itemconfig(oval2,fill="green")
      canvas.itemconfig(oval3,fill="green")
      canvas.itemconfig(oval4,fill="green")
      canvas.itemconfig(poly,fill="orange")
      canvas.itemconfig(poly1,fill="orange")
      canvas.itemconfig(poly2,fill="orange")
      canvas.itemconfig(poly3,fill="orange")
      canvas.itemconfig(poly4,fill="orange")
      canvas.itemconfig(squr,fill="#ff0066")
      canvas.itemconfig(squr1,fill="#ff0066")
      canvas.itemconfig(squr2,fill="#ff0066")
      canvas.itemconfig(squr3,fill="#ff0066")
      canvas.itemconfig(squr4,fill="#ff0066")
      
      
      
      
  
      

# Get an instance of the MouseMover object
mm = MouseMover()



# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)
canvas.bind("<Double-1>",mm.dbcl)
canvas.pack()

root.mainloop()