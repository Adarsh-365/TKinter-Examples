from tkinter import *

root= Tk()
root.geometry("500x500")

root.title("Analog Clock")
canvas=Canvas(root)
canvas.configure(width=500,height=500,bg="black")
canvas.grid(column=0,row=0)
flag=TRUE

canvas.create_oval(0,0,500,500,fill="green")
canvas.create_text(250,20,text="12",font=("Time",20))
canvas.create_text(480,250,text="3",font=("Time",20))
canvas.create_text(250,480,text="6",font=("Time",20))
canvas.create_text(20,250,text="9",font=("Time",20))
x1=250
y1=250
x2=250
y2=50

line=canvas.create_line(x1,y1,x2,y2,fill="red",width=5)
def second():
    global x1,y1,x2,y2,line,flag
    
    if y2<260:
        if flag:
       
           x2+=10
           y2+=13.334
           flag=0
           print("Flase")
        else:
           x2-=10
           y2-=13.334
           flag=FALSE
           
    if y2>260:
        
        x2-=10
        y2-=13.334
        flag=FALSE
        
   
        
    
    print( x1,y1,x2,y2)
    if x1<440:
        print("wow")
    canvas.delete(line)
    line=canvas.create_line(x1,y1,x2,y2,fill="red",width=5)
    canvas.create_oval(240,240,260,260,fill="black")
    canvas.after(1000,second)


second()

root.mainloop()