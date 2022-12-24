import tkinter
from tkinter import *
from tkinter.messagebox import askyesno, askquestion

root = Tk()

def dest():
    answer = askyesno(title='Confirmation',
                      message='Are you sure that you want to quit?')
    if answer:
        root.destroy()


btn = Button(text="Quite",command=dest)


# Position image
btn.place(x=0, y=0)
root.mainloop()