from tkinter import *
from tkinter import filedialog


root = Tk()
label=Label(root,text="working-good")
label.pack()
def open_file():
    print("working")
    file=filedialog.askopenfile(mode='r',filetype=[('Python File','*.py')])
    if file is not NONE:
        content=file.read()
        label.configure(text=content)
def save_file():
    print("working")
  
    file=filedialog.asksaveasfile(mode='w',confirmoverwrite=True,filetype=[('Python File','*.py')],defaultextension=('*.py'))
   


btn = Button(root,text="open file",command=open_file,width=10,height=1)
btn.pack()
btn = Button(root,text="Save file",command=save_file,width=10,height=1)
btn.pack()


root.mainloop()