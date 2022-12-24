from tkinter import *

m1 = PanedWindow(bg="red",borderwidth=100,handlepad=120)
m1.pack(fill=BOTH, expand=1)
m3 = PanedWindow( orient=VERTICAL)
m3.pack(fill=Y,expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL,bg="green")
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

right= Label(m3,text="right")
m3.add(right)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

mainloop()


