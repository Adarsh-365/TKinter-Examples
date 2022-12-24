import tkinter as tk
from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from random import randint
class MouseMover():
  def __init__(self):
    print("inti")
    
    
  def save_file(self):
      print("saveas")
    
  def newdata1(self):
      print("new")
        
  def retrivedata(self):
      print("retrive")
  def sfile(self):
      print("save")
  
rate=[]


for i in range(10):
    x=randint(0,10)
    rate.append(x)
    
    
data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
         'Random_Rate': rate
        }
df2 = DataFrame(data2,columns=['Year','Random_Rate'])




root= tk.Tk() 
root.geometry("1000x1000")
figure2 = plt.Figure(figsize=(5,4), dpi=100)
plt.savefig("adarsh.jpg")
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().grid(column=0,row=0)
df2 = df2[['Year','Random_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('RANDOM LINE GRAPH')




mm = MouseMover()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=mm.newdata1)

filemenu.add_command(label="Open",command=mm.retrivedata)
filemenu.add_command(label="Save",command= mm.sfile)
filemenu.add_command(label="Saveas",command= mm.save_file)


menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

btn=Button(text="SAVE in XLSX",command=mm.save_file)
btn.grid(column=1,row=1)

root.mainloop()