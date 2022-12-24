from tkinter import *



root=Tk()
root.title("Calculator")
def draw_line(e):
   x, y = e.x, e.y
   if canvas.old_coords:
      x1, y1 = canvas.old_coords
      canvas.create_line(x, y, x1, y1, width=5)
   canvas.old_coords = x, y

canvas = Canvas(root, width=700, height=300)
canvas.grid()
canvas.old_coords = None

# Bind the left button the mouse.
root.bind('<Button-1>', draw_line)


root.geometry("490x540")
root.configure(padx=10,pady=10)
root.resizable(width=FALSE,height=FALSE)
    

Button(text="0",width= 6,height= 1,relief=RIDGE). grid(padx=50,pady=50,row=1,column=1)
Button(text="0",width= 6,height= 1,relief=RIDGE). grid(padx=50,pady=50,row=1,column=2)

Button(text="0",width= 6,height= 1,relief=RIDGE). grid(padx=50,pady=50,row=2,column=0)
Button(text="0",width= 6,height= 1,relief=RIDGE ). grid(padx=50,pady=50,row=2,column=1)
Button(text="0",width= 6,height= 1,relief=RIDGE ). grid(padx=50,pady=50,row=2,column=2)

Button(text="0",width= 6,height= 1,relief=RIDGE ). grid(padx=50,pady=50,row=3,column=0)
Button(text="0",width= 6,height= 1,relief=RIDGE ). grid(padx=50,pady=50,row=3,column=1)
Button(text="0",width= 6,height= 1,relief=RIDGE ). grid(padx=50,pady=50,row=3,column=2)

   
    


root.mainloop()