import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("Combobox")
root.geometry('500x250')

ttk.Label(root,text="Welcome to Checkbox",background="green",foreground="white").grid(row = 0, column = 1)

ttk.Label(root,text="Select The Month : ",font=10).grid(column=0,row=5,padx = 10, pady = 25)

n = tk.StringVar()

monthchoosen= ttk.Combobox(root,width=27,textvariable=n)

monthchoosen['values']=('january',
                 'february',
                 'march',
                 'april',
                 'may',
                 'june',
                 'jully',
                 'augest',
                 'september',
                 'octomber',
                 'november',
                 'december'
    )


monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
root.mainloop()