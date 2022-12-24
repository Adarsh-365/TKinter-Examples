from tkinter import *
from tkinter import ttk

root =Tk()

root.title("Python Gui")

f=Frame(root)
f.pack()

canvas=Canvas(f)

canvas.config(width=720,height=620)


def onclickred():
    
    
    canvas.itemconfig(oval1,fill="white")
    canvas.itemconfig(oval2,fill="white")
    canvas.itemconfig(oval,fill="red")
    
def onclickyellow():
   canvas.itemconfig(oval1,fill="yellow")
   canvas.itemconfig(oval2,fill="white")
   canvas.itemconfig(oval,fill="white")
    
def onclickgreen():
   canvas.itemconfig(oval1,fill="white")
   canvas.itemconfig(oval2,fill="green")
   canvas.itemconfig(oval,fill="white")

def onclickReset():
    canvas.itemconfig(oval1,fill="white")
    canvas.itemconfig(oval2,fill="white")
    canvas.itemconfig(oval,fill="white")
    
text1=canvas.create_text(380,60,text="Traffic Light",fill="black" ,font=('courier',24,'bold'))
rect=canvas.create_rectangle(300,100,450,530,fill="grey",width=7)
text1=canvas.create_text(375,160,text="RED",fill="black" ,font=('courier',24,'bold'))
text2=canvas.create_text(375,310,text="YELLOW",fill="black" ,font=('courier',24,'bold'))
text3=canvas.create_text(375,450,text="GREEN",fill="black" ,font=('courier',24,'bold'))
oval=canvas.create_oval(310,110,440,240,width=2,fill="white")
oval1=canvas.create_oval(310,250,440,380,width=2,fill="white")
oval2=canvas.create_oval(310,390,440,520,width=2,fill="white")


canvas.lift(text1)
canvas.lift(text2)
canvas.lift(text3)


button= Button(f, text="RED", command= onclickred,width=12,bg="red")
button.pack(pady=20)
button= Button(f, text="Yellow", command= onclickyellow,width=12,bg="yellow")
button.pack(pady=20)
button= Button(f, text="Green", command= onclickgreen,width=12,bg="green")
button.pack(pady=20)
button= Button(f, text="Reset", command= onclickReset,width=12)
button.pack(pady=20)

canvas.pack()

    





root.mainloop()