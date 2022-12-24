from tkinter import *
from time import strftime

root =Tk()
root.title("remainng Time")
root.configure(bg="black")
root.attributes('-topmost',True)
running = True

def time():
   if running:
  
        string = strftime('%H')
        string1= strftime('%M')
        string2= strftime('%S')
        string=str(18-int(string))
        string1=str(60-int(string1))
        string2=str(60-int(string2))
        if int(string)<10:
            string='0'+str(string)
        if int(string1)<10:
            string1='0'+str(string1)
        if int(string2)<10:
            string2='0'+str(string2)
        string4=string+":"+string1+":"+string2
        
        label2=Label(text=string4,width=10,height=2,font=('calibri', 30, 'bold'),background = 'purple',
    			foreground = 'white')
     
        label2.grid(column=3,row=1)
        label2.after(1000,time)
        

    




label=Label(text="00:00:00",width=10,height=2,font=('calibri', 30, 'bold'),background = 'purple',foreground = 'white')

label.after(0,time)


root.mainloop()

