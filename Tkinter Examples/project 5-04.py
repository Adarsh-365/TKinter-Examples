from tkinter import *
import pickle
from tkinter import filedialog
root = Tk()
root.geometry("1000x1000")




canvas= Canvas(root)
canvas.config(width=1000,height=1000)
leftside=canvas.create_rectangle(0,0,500,1000,fill="Magenta",tags="leftside")
rightside=canvas.create_rectangle(500,0,1000,1000,fill="#34deeb",tags="rightside")
triangle = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
square=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')
triangle = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
square=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')
canvas.grid(column=0,row=0)

class MouseMover():
  def __init__(self):
    self.tt=0
    self.square=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')
    self.triangle = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
    self.square=canvas.create_rectangle(20,20,120,120,fill="blue", tags=('square','new'))
    self.triangle = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags=('triangle','new'))
  
    self.item = 0; self.previous = (0, 0)
    
    self.expression=[]
  def select(self, event):
 
    
    widget = event.widget                    
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]      
    self.previous = (xc, yc)
   
    
   
    
  def drag(self, event):
  
  
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    if self.item !=1 and self.item != 2:
          canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
          self.previous = (xc, yc)
    
    
  def release(self,event):
    widget = event.widget
      
    
    
    
    self.newi=canvas.gettags(self.item)
    newtag=self.newi[0]
    newt=self.newi[1]
    newi=canvas.coords(self.item)
   
         
     
     
    
    def linearSearch (expression, target):
     for i in range(len(expression)):
       for j in range(len(expression[i])):
           if (expression[i][j] == target):
               return [i, j]
     return [-1, -1]
 
 
    
    o=len(self.expression)
      
    target = self.item
    ans = linearSearch(self.expression, target)
  
    
   
    if(ans == [-1,-1]):  
       array1=[]
       array1.append(self.item)
       array1.append(newtag)
       array1.append(newi) 
       array1.append(newt)
       self.expression.append(array1) 
      
    else: 
         
          [g,h]=ans
          j=int(g)
          k=int(h)
          array2=[]
          array2.append(self.item)
          array2.append(newtag)
          array2.append(newi)  
          array2.append(newt)
          self.expression[j]=array2
          
             
                   
    xc = widget.canvasx(event.x)
    name=self.newi[0]
    
    if xc<500:
        if self.item !=1 and self.item != 2:
            canvas.delete(self.item)
    
        if name=='square':
            
                self.square1=canvas.create_rectangle(20,20,120,120,fill="blue", tags=('square','new'))
        elif name=='triangle':
                self.triangle1 = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags=('triangle','new'))
        else:
                print("")        
            
                 
    elif xc>500:
          
           if name=='square':
                self.square1=canvas.create_rectangle(20,20,120,120,fill="blue", tags=('square','new'))
           elif name=='triangle':
                self.triangle1 = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags=('triangle','new'))
           else:
                print("")
                
            
    
  def savedata(self):
      with open('savedata.pickle','wb') as f:
          pickle.dump(self.expression,f)
  def asktos    
  def retrivedata(self):
     newrange=len(self.expression)
     canvas.delete('new')
     for i in range(newrange):
          data0=self.expression[i][0]
          if data0 !=1 and data0 != 2:
              canvas.delete(data0)
              
      
      
     with open('savedata.pickle','rb') as f:
         self.expression=pickle.load(f)  
        
         n=len(self.expression)
         for i in range(n):
           shapeid=self.expression[i][0]
           shapename=self.expression[i][1]
           
           shapeloc=self.expression[i][2]
           
           x=shapeloc[0]
           y=shapeloc[1]
           x1=shapeloc[2]
           y1=shapeloc[3]
           
           
           if shapename=='square':
              if x>500:
               square=canvas.create_rectangle(x,y,x1,y1,fill="blue", tags=('square','new'))
                  
           if shapename=='triangle':
             if x>500:   
               x2=shapeloc[4]
               y2=shapeloc[5]
               triangle = canvas.create_polygon(x,y,x1,y1,x2,y2,fill="green",tags=('triangle','new'))
       
mm = MouseMover()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Open",command=mm.retrivedata)
filemenu.add_command(label="Save",command= mm.savedata)


menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)
canvas.bind("<ButtonRelease-1>",mm.release)

root.mainloop()