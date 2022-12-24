from tkinter import *

class AllTkinterWidgets:
    def __init__(self, master):
        frame = Frame(master, width=800, height=800, bd=0)
        frame.pack()

        iframe5 = Frame(frame)
        iframe5.pack(expand=1, fill=X)
        iframe4 = Frame(frame, bd=2, relief=RAISED)
        iframe4.pack(expand=1, fill=X)
        canvas1 = Canvas(iframe4, bg='skyblue', width=600, height=1700)
        canvas1.pack()
        canvas1.grid(column=0,row=0)
        canvas = Canvas(iframe5, bg='white', width=600, height=1700)
        canvas.pack()
       
        rect=canvas.create_rectangle(60,220,380,360,fill="red")
        squr=canvas.create_rectangle(120,420,320,620,fill="black")

        oval=canvas.create_oval(120,20,280,180,fill="green")
        poly=canvas.create_polygon(200,650,100,850,300,850,fill="orange")
    
        iframe5.pack(expand=1, fill=X,side=LEFT )
        
        


    
root = Tk()
#root.option_add('*font', ('verdana', 10, 'bold'))
all = AllTkinterWidgets(root)
root.title('Tkinter Widgets')
root.mainloop()
           