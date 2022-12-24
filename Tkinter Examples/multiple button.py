from tkinter import *

root=Tk()
root.configure(background="white")
root.resizable(False,False)

root.geometry("700x700")

btn=Button(root,text="Button-1",activeforeground="green",bd=10,bg="orange",font=20,highlightcolor="blue")
btn.pack(side=TOP)
btn=Button(root,text="Button-2",justify=RIGHT,padx=35,pady=35,wraplength=100)
btn.pack(side=BOTTOM)
btn=Button(root,text="Button-3",relief=SUNKEN,activeforeground="green",bd=10,bg="orange",font=20,highlightcolor="blue")
btn.pack(side=LEFT)
btn=Button(root,text="Button-3",relief=RAISED,activeforeground="green",bd=10,bg="orange",font=20,highlightcolor="blue")
btn.pack(side=LEFT)

btn=Button(root,text="Button-3",relief=GROOVE,activeforeground="green",bd=10,bg="orange",font=20,highlightcolor="blue")
btn.pack(side=LEFT)

btn=Button(root,text="Button-3",relief=RIDGE,activeforeground="green",bd=10,bg="orange",font=20,highlightcolor="blue")
btn.pack(side=LEFT)

btn1=Button(root,text="Button-4",wraplength=1)
btn1.pack(side=RIGHT)
btn1.focus()

root.mainloop()