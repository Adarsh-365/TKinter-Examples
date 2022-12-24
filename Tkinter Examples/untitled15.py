from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x300")

# Define a function to delete the shape
def on_click():
   print (win.winfo_children())

# Create a canvas widget
canvas=Canvas(win, width=500, height=300)
canvas.pack()

# Create a button to delete the button
Button(win, text="Click", command=on_click).pack()

win.mainloop()