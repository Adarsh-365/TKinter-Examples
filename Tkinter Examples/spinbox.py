from tkinter import *
root=Tk()
root.geometry("300x300")


scrollbar=Scrollbar(root)

scrollbar.pack(side=RIGHT,fill=Y)

mylis = Listbox(root,yscrollcommand=scrollbar.set)
for line in range(1,101):
    mylis.insert(END, "This is line number " + str(line))
    
mylis.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylis.yview)

root.mainloop()