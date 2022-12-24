from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry("800x800")
canvas= Canvas(root, width= 600, height= 400)


for i in range(8):
    
    for j in range(8):
        color='black'
        n=i+j
        if n%2==0:
            color='white'
        
        
        img= ImageTk.PhotoImage(Image.open("C:\\Users\\BATMAN1\\.spyder-py3\\project5\\2.png"))


        canvas.create_image(10,10,anchor=NW,image=img)
        


root.mainloop()