
from tkinter import *

root= Tk()
root.configure(bg="blue")
root.geometry("600x600")

def onclickred():
    root.configure(bg="red")
def onclickgreen():
    root.configure(bg="green")
w = Checkbutton ( root,activeforeground="orange",bg="red" ,command=onclickred,text="red",disabledforeground="pink",underline=3)
w.grid(column=1,row=0)
w = Checkbutton ( root,activeforeground="orange",bg="green" ,command=onclickgreen,text="green",height=4,selectcolor="Purple")
w.grid(column=0,row=0)




root.mainloop()












