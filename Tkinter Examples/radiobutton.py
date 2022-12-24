from tkinter import *

root=Tk()

root.geometry("600x600")
root.resizable(height=FALSE,width=FALSE)
root.configure(background="skyblue")

def func():
    root.configure(background='red')

def ora():
    root.configure(background='orange')

def bl():
    root.configure(background='blue')

def bla():
    root.configure(background='black')
    

R1=Radiobutton(root,text='Red',value=0,command=func,width=12
               ,activebackground="Purple",activeforeground="red").pack(anchor='w')
R1=Radiobutton(root,text='orange',value=1,bg="orange",borderwidth=2,selectcolor="green"
               ,command=ora,width=12).pack(anchor= 'w')
R1=Radiobutton(root,text='blue',value=2,command=bl,width=12).pack(anchor= 'w')
R1=Radiobutton(root,text='black',value=3,command=bla,width=12).pack(anchor= 'w')
root.mainloop()