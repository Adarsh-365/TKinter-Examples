from tkinter import *

root= Tk()
root.geometry("600x600")
canvas=Canvas(root,bd=3,bg="red",confine=TRUE,cursor="spider",xscrollincrement='4')
canvas.grid(column=0,row=0)
canvas=Canvas(root,bd=3,bg="green",confine=TRUE,cursor="spraycan")
canvas.grid(column=0,row=1)
canvas=Canvas(root,bd=3,bg="pink",confine=TRUE,cursor="star")
canvas.grid(column=1,row=0)
canvas=Canvas(root,bd=3,bg="black",confine=TRUE,cursor="target")
canvas.grid(column=1,row=1)
canvas=Canvas(root,bd=3,bg="grey",confine=TRUE,cursor="tcross")
canvas.grid(column=2,row=0)
canvas=Canvas(root,bd=3,bg="brown",confine=TRUE,cursor="trek")
canvas.grid(column=2,row=1)
canvas=Canvas(root,bd=3,bg="orange",confine=TRUE,cursor="shuttle")
canvas.grid(column=3,row=1)
canvas=Canvas(root,bd=3,bg="yellow",confine=TRUE,cursor="sizing")
canvas.grid(column=3,row=0)



root.mainloop()












