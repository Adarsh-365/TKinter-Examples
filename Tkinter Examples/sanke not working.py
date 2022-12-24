from tkinter import *

root= Tk()
root.geometry("500x500")

root.title("snake")
canvas=Canvas(root)
canvas.configure(width=500,height=500,bg="black")
canvas.grid(column=0,row=0)
ww=0
i=1
x1=0
y1=250
x2=0
y2=250

running=True
snake=canvas.create_line(200,250,300,250,width=5,fill="red")  
def moveline():
    global ww,i,snake,x1,x2,y1,y2,running
    if running:
      ww=ww+10
      i=i*ww
      x1=200-ww
      x2=300-ww 
      canvas.delete(snake)
      print(x1,x2)
    
      snake=canvas.create_line(x1,y1,x2,y2,width=5,fill="red")
      canvas.after(1000,moveline)
    
def uparrow():
    global ww,i,snake,x1,x2,y1,y2
    i=1
    ww=ww+10
    i=i*ww
    x1+=100
    y1=200-ww
    y2=300-ww 
    
    canvas.delete(snake)
    snake=canvas.create_line(x1,y1,x2,y2,width=5,fill="red")
    canvas.after(1000,uparrow)

    
def on_start():
   global running
   running = False
   uparrow()

# Define a function to stop the loop
def on_stop():
   global running
   running = True
   moveline()
   
   
start = Button(root, text="Start", command=on_start)
start.grid(column=1,row=1)

stop = Button(root, text="Stop", command=on_stop)
stop.grid(column=1,row=2)


moveline()

root.mainloop()