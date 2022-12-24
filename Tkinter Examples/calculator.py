from tkinter import *
""" global expression
 if num=="0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
     expression=""
 else:
  expression = expression + str(num)

  equation.set(expression)
  
  
  
  """


expression = ""
total=""

def press(num):
    
	
	global expression,total
    
    

	expression = expression + str(num)

	equation.set(expression)

def equalpress():
 
	try:

		global expression,total
		total = str(eval(expression))

		equation.set(total)
		expression = total

	except:

		equation.set(" error ")
		expression = ""
def clear():
	global expression
	expression = ""
	equation.set("")
if __name__ == "__main__":
    root=Tk()
    root.title("Calculator")
    root.geometry("250x325")
    root.configure(padx=10,pady=10)
    root.resizable(width=False,height=False)
    
    equation = StringVar()

    expression_field = Entry(root,text=00, textvariable=equation,width=16,font=("Times",20),)

	
    expression_field.grid(column=0,row=0,columnspan=4)


    Button(font=("Times",20),text="%",width=3,height=1,relief=RIDGE,command=lambda:press("%")).grid(row=1,column=0)
    Button(font=("Times",20),text="CE",width=3,height=1,relief=RIDGE,command=clear).grid(row=1,column=1)
    Button(font=("Times",20),text="C",width=3,height=1,relief=RIDGE,command=clear).grid(row=1,column=2)
    Button(font=("Times",20),text="/",width=3,height=1,relief=RIDGE,command=lambda:press("/")).grid(row=1,column=3)
    Button(font=("Times",20),text="7",width=3,height=1,relief=RIDGE,command=lambda:press(7)).grid(row=2,column=0)
    Button(font=("Times",20),text="8",width=3,height=1,relief=RIDGE,command=lambda:press(8)).grid(row=2,column=1)
    Button(font=("Times",20),text="9",width=3,height=1,relief=RIDGE,command=lambda:press(9)).grid(row=2,column=2)
    Button(font=("Times",20),text="*",width=3,height=1,relief=RIDGE,command=lambda:press("*")).grid(row=2,column=3)
    Button(font=("Times",20),text="4",width=3,height=1,relief=RIDGE,command=lambda:press(4)).grid(row=3,column=0)
    Button(font=("Times",20),text="5",width=3,height=1,relief=RIDGE,command=lambda:press(5)).grid(row=3,column=1)
    Button(font=("Times",20),text="6",width=3,height=1,relief=RIDGE,command=lambda:press(6)).grid(row=3,column=2)
    Button(font=("Times",20),text="-",width=3,height=1,relief=RIDGE,command=lambda:press("-")).grid(row=3,column=3)
    Button(font=("Times",20),text="1",width=3,height=1,relief=RIDGE,command=lambda:press(1)).grid(row=4,column=0)
    Button(font=("Times",20),text="2",width=3,height=1,relief=RIDGE,command=lambda:press(2)).grid(row=4,column=1)
    Button(font=("Times",20),text="3",width=3,height=1,relief=RIDGE,command=lambda:press(3)).grid(row=4,column=2)
    Button(font=("Times",20),text="+",width=3,height=1,relief=RIDGE,command=lambda:press("+")).grid(row=4,column=3)
    Button(font=("Times",20),text="-VE",width=3,height=1,relief=RIDGE,command=lambda:press("-")).grid(row=5,column=0)
    Button(font=("Times",20),text="0",width=3,height=1,relief=RIDGE,command=lambda:press(0)).grid(row=5,column=1)
    Button(font=("Times",20),text=".",width=3,height=1,relief=RIDGE,command=lambda:press(".")).grid(row=5,column=2)
    equal=Button(font=("Times",20),text="=",width=3,height=1,relief=RIDGE,command=equalpress).grid(row=5,column=3)
    


root.mainloop()