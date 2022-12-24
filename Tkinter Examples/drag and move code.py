
from tkinter import * 
root = Tk()
canvas = Canvas(root, width=400, height=200)
canvas.pack()
canvas.create_oval(10, 10, 110, 60, fill="grey")
canvas.create_text(60, 35, text="Oval")
canvas.create_rectangle(10, 100, 110, 150, outline="blue")
canvas.create_text(60, 125, text="Rectangle")
canvas.create_line(60, 60, 60, 100, width=3)


class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
  def select(self, event):
    widget = event.widget                       # Get handle to canvas 
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    print((xc, yc, self.item))
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)


# Get an instance of the MouseMover object
mm = MouseMover()

# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)

root.mainloop()