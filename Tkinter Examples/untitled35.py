import tkinter as tk
import random

COLORS = ["magenta"]

root = tk.Tk()

cv = tk.Canvas(root, width=1000, height=1000, bg='cyan')
cv.pack()

for _ in range(100000):
    ch1=("0","1","2","3","4","5","6", "7", "8", "9", "0", "A", "B", "C", "D", "E",  "F" )      
  
    selt1=random.choice(ch1) 
    selt2=random.choice(ch1) 
    selt3=random.choice(ch1)
    selt4=random.choice(ch1) 
    selt5=random.choice(ch1) 
    selt6=random.choice(ch1)
    
    string = "#"+str(selt1)+str(selt2) +str(selt3)+str(selt4)+str(selt5) +str(selt6)
   
    x = random.randrange(0, 1000)
    y = random.randrange(0, 1000)
    coordinates =(x,y,x+10,y+10)
    cv.create_oval(*coordinates, outline=string,fill=string)

cv.update()
cv.postscript(file="my_drawing.ps")

tk.mainloop()