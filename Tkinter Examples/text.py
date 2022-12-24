from tkinter import *



root = Tk()

text=Text(root,insertbackground="brown",bg="green",insertborderwidth=80,relief=RIDGE,wrap=WORD )
text.insert(INSERT,"ADARSH.....")
text.insert(END,"Tayde.....")
text.pack()
text.tag_add("first","1.0","1.6")
text.tag_add("last", "1.11", "1.17")

text.tag_config("first",background="red",foreground="blue")
text.tag_config("last",background="pink",foreground="grey")

root.mainloop()
