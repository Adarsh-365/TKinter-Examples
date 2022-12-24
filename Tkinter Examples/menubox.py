from tkinter import *

root=Tk()

root.geometry("330x300")

mbtn=Menubutton(root,text="header",activebackground="red",
                bg="Violet",bd=60,direction=LEFT,disabledforeground="skyblue")

mbtn.grid()
mbtn.menu=Menu(mbtn,tearoff=0)

mbtn["menu"]=mbtn.menu

mayoVar=IntVar()
ketchVar=IntVar()
pythonVar=IntVar()
cVar=IntVar()
cppVar=IntVar()

mbtn.menu.add_command(label="mayo"
                          )

mbtn.menu.add_command(label="Ketchup"
                       )
mbtn.menu.add_command(label="Python")

mbtn.menu.add_command(label="CPP")
mbtn.pack()

root.mainloop()