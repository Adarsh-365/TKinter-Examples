from tkinter import *

root = Tk()
root.configure(bg="skyblue")
def changecolor():
    root.configure(bg="red")
def changecolor1():
    root.configure(bg="blue")
def changecolor2():
    root.configure(bg="green")
def changecolor3():
    root.configure(bg="pink")
    
def changecolor4():
    root.configure(bg="violet")
    
def changecolor5():
    root.configure(bg="white")
def changecolor6():
    root.configure(bg="black")
   

menubar=Menu(root,bg="green",title="menubar")
fmenu=Menu(menubar,tearoff=0,activeborderwidth=20,activeforeground="red",title="menubar")
menubar.add_cascade(label="File", menu=fmenu)
fmenu.add_command(label="red",command=changecolor)
fmenu.add_command(label="blue",command=changecolor1)
fmenu.add_command(label="green",command=changecolor2)
fmenu.add_command(label="pink",command=changecolor3)
fmenu.add_command(label="violet",command=changecolor4)
fmenu.add_separator()
fmenu.add_command(label="white",command=changecolor5)
fmenu.add_command(label="black",command=changecolor6)

emenu=Menu(menubar,tearoff=TRUE,bg="pink")
menubar.add_cascade(label="Edit", menu=emenu)

emenu.add_command(label="Copy")
emenu.add_command(label="Copy")
emenu.add_command(label="Copy")
emenu.add_command(label="Copy")
emenu.add_separator()
emenu.add_command(label="Copy")
emenu.add_command(label="Copy")

hmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=hmenu)
hmenu.add_command(label="help")
hmenu.add_separator()
hmenu.add_command(label="help")
hmenu.add_command(label="help")
hmenu.add_command(label="help")


root.config(menu=menubar)
root.mainloop()