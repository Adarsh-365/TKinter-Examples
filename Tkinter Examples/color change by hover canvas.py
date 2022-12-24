from tkinter import *
from tkinter import ttk



root =Tk()
xccs=120
yccs=420
xccc=120
yccc=20
xcco=120
ycco=20
xcca=400
ycca=50
xccr=60
yccr=220
xccp=100
yccp=650

root.title("Python Gui")

root.geometry("900x900")
canvas=Canvas(root)

canvas.config(width=1820,height=920)

coord = 400, 50, 540, 210
arc = canvas.create_arc(coord, start=0, extent=180, fill="blue")
rect=canvas.create_rectangle(60,220,380,360,fill="red")
squr=canvas.create_rectangle(120,420,320,620,fill="black")

oval=canvas.create_oval(120,20,280,180,fill="green")
poly=canvas.create_polygon(200,650,100,850,300,850,fill="yellow")

class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
   
    
    
  def select(self, event):
    widget = event.widget                      
    xc = widget.canvasx(event.x); yc = widget.canvasy(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
   
    canvas.lift(self.item)
    
   
  def drag(self, event):
    global xccs,yccs,xcco,ycco,xcca,ycca,xccr,yccr,xccp,yccp
      
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasy(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)
  
    if self.item==1:
        c=arc
        newi=canvas.coords(c)
        xcca=newi[0]
        ycca=newi[1]
    elif self.item==2:
   
        c=rect
        newi=canvas.coords(c)
        xccr=newi[0]
        yccr=newi[1]
    elif self.item==3:
        c=squr
        newi=canvas.coords(c)
        xccs=newi[0]
        yccs=newi[1]
    elif self.item==4:
        c=oval
        newi=canvas.coords(c)
        xcco=newi[0]
        ycco=newi[1]
    elif self.item==5:
       c=poly
       newi=canvas.coords(c)
       xccp=newi[0]
       yccp=newi[1]
    
   
    
   
    xcc=xccs-xcco
    ycc=yccs-ycco
    xcc1=xccs-xccr
    ycc1=yccs-yccr
    xcc2=xccs-xcca
    ycc2=yccs-ycca
    xcc3=xccs-xccp
    ycc3=yccs-yccp
    
    print(xcc,ycc)
    print(xcc1,ycc1)
    print(xcc3,ycc3)
    
    
    if xcc<100 and xcc>-100 and ycc<100 and ycc>-100:
        color="green"
    elif xcc1<250 and xcc1>-200 and ycc1<135 and ycc1>-200:
            color="red"
    elif xcc2<100 and xcc2>-100 and ycc2<100 and ycc2>-100:
             color="blue"
    elif xcc3<40 and xcc3>-250 and ycc3<150 and ycc3>-100:
              color="yellow"
    else:
               color="black"
               
    print(color)          
    canvas.itemconfig(squr,fill=color)
    
   
    
   
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