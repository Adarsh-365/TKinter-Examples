from tkinter import *
import random

root=Tk()
root.geometry("1000x1000")
canvas=Canvas(root)
canvas.configure(width=300,height=300)
canvas.grid(column=0,row=0)
canvas.configure(background="black")

one=canvas.create_rectangle(20,20,80,40,fill="red")
two=canvas.create_rectangle(0,40,20,100,fill="red")
three=canvas.create_rectangle(80,40,100,100,fill="red")
four=canvas.create_rectangle(20,100,80,120,fill="red")
five=canvas.create_rectangle(0,120,20,180,fill="red")
six=canvas.create_rectangle(80,120,100,180,fill="red")
seven=canvas.create_rectangle(20,180,80,200,fill="red")


one=canvas.create_rectangle(200,20,800,40,fill="red")
two=canvas.create_rectangle(0,40,20,100,fill="red")
three=canvas.create_rectangle(80,40,100,100,fill="red")
four=canvas.create_rectangle(20,100,80,120,fill="red")
five=canvas.create_rectangle(0,120,20,180,fill="red")
six=canvas.create_rectangle(80,120,100,180,fill="red")
seven=canvas.create_rectangle(20,180,80,200,fill="red")



def oneon():
   canvas.itemconfigure(one, fill="black")
   
def twoon():
   canvas.itemconfigure(two, fill="black")
   

def threeon():
   canvas.itemconfigure(three, fill="black")
   
def fouron():
   canvas.itemconfigure(four, fill="black")
   
def fiveon():
   canvas.itemconfigure(five, fill="black")
   
def sixon():
   canvas.itemconfigure(six, fill="black")
   
def sevenopn():
   canvas.itemconfigure(seven, fill="black")
   

def cleraall():
    canvas.itemconfigure(one, fill="red")
    canvas.itemconfigure(two, fill="red")
    canvas.itemconfigure(three, fill="red")
    canvas.itemconfigure(four, fill="red")
    canvas.itemconfigure(five, fill="red")
    canvas.itemconfigure(six, fill="red")
    canvas.itemconfigure(seven, fill="red")
    

def click_zero():
      cleraall() 
      fouron()
      

def click_one():
      cleraall() 
      oneon()
      twoon()
      fouron()
      fiveon()
      sevenopn()
      


def click_two():
      cleraall() 
      twoon()
      sixon()


def click_three():
      cleraall() 
      twoon()
      fiveon()
      

def click_four():
      cleraall()
      oneon()
      fiveon()
      sevenopn()
      

def click_five():
      cleraall() 
      threeon()
      fiveon()
      
      

def click_six():
      cleraall() 
      threeon()
      

def click_seven():
      cleraall() 
      fouron()
      twoon()
      fiveon()
      sevenopn()
      

def click_eight():
      cleraall() 
      
      

def click_nine():
      cleraall() 
      fiveon()
      
      
      
      
      
Button(font=("Times",20),text="0",width=3,height=1,relief=RIDGE,command=click_zero).grid(row=1,column=1)
Button(font=("Times",20),text="1",width=3,height=1,relief=RIDGE,command=click_one).grid(row=1,column=2)
Button(font=("Times",20),text="2",width=3,height=1,relief=RIDGE,command=click_two).grid(row=1,column=3)
Button(font=("Times",20),text="3",width=3,height=1,relief=RIDGE,command=click_three).grid(row=1,column=4)
Button(font=("Times",20),text="4",width=3,height=1,relief=RIDGE,command=click_four).grid(row=2,column=1)
Button(font=("Times",20),text="5",width=3,height=1,relief=RIDGE,command=click_five).grid(row=2,column=2)
Button(font=("Times",20),text="6",width=3,height=1,relief=RIDGE,command=click_six).grid(row=2,column=3)
Button(font=("Times",20),text="7",width=3,height=1,relief=RIDGE,command=click_seven).grid(row=2,column=4)
Button(font=("Times",20),text="8",width=3,height=1,relief=RIDGE,command=click_eight).grid(row=3,column=1)
Button(font=("Times",20),text="9",width=3,height=1,relief=RIDGE,command=click_nine).grid(row=3,column=2)




root.mainloop()