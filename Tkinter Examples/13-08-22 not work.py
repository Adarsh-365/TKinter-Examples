from tkinter import *

root = Tk()
root.geometry("1000x1000")

def file1():    
    if not text_zone.edit_modified():      
        text_zone.delete('1.0', tk.END)
    else:        
        savefileas()
          
        text_zone.delete('1.0', tk.END)  
    
    text_zone.edit_modified(0)
       
    root.title('PYTHON GUIDES')    

def openfile():
    
    if not text_zone.edit_modified():       
        try:            
            path = filedialog.askopenfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
                       
            root.title('Notepad - ' + path)          
            
            with open(path, 'r') as f:             
                content = f.read()
                text_zone.delete('1.0', tk.END)
                text_zone.insert('1.0', content)
                                
                text_zone.edit_modified(0)
             
        except:
            pass   
    
    else:       
        savefileas()      
        
        text_zone.edit_modified(0)              
        openfile()         

def savefile():    
    try:
        
        path = root.title().split('-')[1][1:]   
    
    except:
        path = ''
    
    if path != '':
        
        with open(path, 'w') as f:
            content = text_zone.get('1.0', tk.END)
            f.write(content)
      
    else:
        savefileas()    
    
    text_zone.edit_modified(0)
def savefileas():    
    try:
        path = filedialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
        root.title('Notepad - ' + path)
    
    except:
        return   
    
    with open(path, 'w') as f:
        f.write(text_zone.get('1.0', tk.END))



menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=file1)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save as...", command=savefileas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

canvas= Canvas(root)
canvas.config(width=1000,height=1000)
leftside=canvas.create_rectangle(0,0,500,1000,fill="red")
rightside=canvas.create_rectangle(500,0,1000,1000,fill="orange")
triangle = canvas.create_polygon(140,120,215,20,290,120,fill="green",tags='triangle')
square=canvas.create_rectangle(20,20,120,120,fill="blue", tags='square')

canvas.pack()


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