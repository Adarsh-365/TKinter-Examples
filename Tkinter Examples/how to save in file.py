from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageGrab, PngImagePlugin
from PIL import *

class MyFrame(Frame):
      def __init__(self):
         Frame.__init__(self)
         self.grid()

         self.myCanvas = Canvas(self, width=400, height=175)
         self.myCanvas.grid(row = 1, columnspan = 5)

         self.myCanvas.create_rectangle(10, 10, 50, 50, fill="blue")

         self.button_saveImage = Button(self, text = "Save", command = self.save_image)
         self.button_saveImage.grid(row = 4, column = 4, padx = 5, pady=15)

      def save_image(self):
         x=self.winfo_rootx()+self.myCanvas.winfo_x()
         y=self.winfo_rooty()+self.myCanvas.winfo_y()
         x1=x+self.myCanvas.winfo_width()
         y1=y+self.myCanvas.winfo_height()

         filename = filedialog.asksaveasfilename(initialdir = "C:/Users/desktop.ini",
                                                  title = "Select file",
                                                  filetypes = (("PNG files","*.png"),("All files","*.*")),
                                                  defaultextension=".png")
         ImageGrab.grab().crop((x,y,x1,y1)).save(filename, format="PNG")

frame01 = MyFrame()
frame01.mainloop()
mainloop()