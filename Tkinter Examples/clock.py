from tkinter import *
from time import strftime

root=Tk()

running = True

def time():
   if running:
  
        string = strftime('%H:%M:%S %p')
       
        sec=string[7]
       
        label2=Label(text=string,width=10,height=2,font=('calibri', 30, 'bold'),background = 'purple',
    			foreground = 'white')
        label2.grid(column=1,row=1)
        label2.after(1000,time)
        

    




label=Label(text="00:00:00",width=10,height=2,font=('calibri', 30, 'bold'),background = 'purple',foreground = 'white')

label.after(0,time)




root.mainloop()