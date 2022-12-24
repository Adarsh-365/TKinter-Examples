from tkinter import *

root = Tk()

canvas=Canvas(root)
canvas.configure(width=500,height=500)
canvas.grid(column=0,row=0)
canvas.create_oval(0,0,500,500,fill="green")
line=canvas.create_line(250,0,250,500,fill="red",width=5)
line=canvas.create_line(0,250,500,250,fill="red",width=5)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root.bind('<Button-1>', motion)
root.mainloop()