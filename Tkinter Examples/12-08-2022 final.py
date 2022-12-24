from tkinter import *

root = Tk()
root.geometry("1000x1000")

canvas= Canvas(root)
canvas.config(width=1000,height=1000)
leftside=canvas.create_rectangle(0,0,500,1000,fill="red")
rightside=canvas.create_rectangle(500,0,1000,1000,fill="orange")
triangle = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
square=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')

canvas.grid(column=0,row=0)


class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
    self.square=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')
    self.triangle = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
    #self.rectangle1=canvas.create_rectangle(20,160,180,260,fill="black",tags='rectangle')
    self.square=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')
    self.triangle = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
   # self.rectangle1=canvas.create_rectangle(20,160,180,260,fill="black",tags='rectangle')
  def select(self, event):
   
    widget = event.widget                       
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]
    if self.item !=1 and self.item != 2:
        canvas.lift(self.item)
    self.previous = (xc, yc)
    
  def drag(self, event):
  
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    if self.item !=1 and self.item != 2:
          canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
          self.previous = (xc, yc)
    self.newi=canvas.gettags(self.item)

      
  def release(self,event):

     widget = event.widget
    
     xc = widget.canvasx(event.x)
     name=self.newi[0]
     if xc<500:
         if self.item !=1 and self.item != 2:
             canvas.delete(self.item)
             
             if name=='square':
                  self.square1=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')
             elif name=='triangle':
                  self.triangle1 = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
            # elif name=='rectangle':
                #  self.rectangle1=canvas.create_rectangle(20,160,180,260,fill="black",tags='rectangle')
             else:
                  print("")
             
                  
     elif xc>500:
         
          if name=='square':
               self.square1=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')
          elif name=='triangle':
               self.triangle1 = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
         # elif name=='rectangle':
               #self.rectangle1=canvas.create_rectangle(20,160,180,260,fill="black",tags='rectangle')
          else:
               print("")
          

mm = MouseMover()

canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)
canvas.bind("<ButtonRelease-1>",mm.release)

root.mainloop()