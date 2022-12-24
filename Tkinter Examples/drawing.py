from tkinter import *
from tkinter import ttk
import random
lastx, lasty = 0, 0
root = Tk()
canvas =Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
color="black"
def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
def addLine(event):
    global lastx, lasty,color
    canvas.create_line((lastx, lasty, event.x, event.y),fill=color,width=5)
    lastx, lasty = event.x, event.y

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
color = "black"
def setColor(newcolor):
    global color
    color = newcolor
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
    lastx, lasty = event.x, event.y
id = canvas.create_rectangle((10, 10, 30, 30), fill="red")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))




def setgoodcolor():
    global color
    ch1=("1","2","3","4","5","6", "7", "8", "9", "0", "A", "B", "C", "D", "E",  "F", )      

    selt1=random.choice(ch1) 
    selt2=random.choice(ch1) 
    selt3=random.choice(ch1)
    selt4=random.choice(ch1) 
    selt5=random.choice(ch1) 
    selt6=random.choice(ch1)

    string = "#"+str(selt1)+str(selt2) +str(selt3)+str(selt4)+str(selt5) +str(selt6)
    color=string
id = canvas.create_rectangle((10, 85, 30, 105), fill="black")
canvas.tag_bind(id, "<Button-1>", lambda x: setgoodcolor())

root.mainloop()