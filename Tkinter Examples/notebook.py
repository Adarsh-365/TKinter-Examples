from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame
win = Tk()
win.geometry("750x250")
#Create a Notebook widget
my_notebook= ttk.Notebook(win)
my_notebook.pack(expand=1,fill=BOTH)
#Create Tabs
tab1= ttk.Frame(my_notebook)
my_notebook.add(tab1, text= "Tab 1")
tab2= ttk.Frame(my_notebook)
my_notebook.add(tab2, text= "Tab2")
tab3= ttk.Frame(my_notebook)
my_notebook.add(tab3, text= "Tab3")
tab4= ttk.Frame(my_notebook)
my_notebook.add(tab4, text= "Tab4")
tab5= ttk.Frame(my_notebook)
my_notebook.add(tab5, text= "Tab5")
tab6= ttk.Frame(my_notebook)
my_notebook.add(tab6, text= "Tab6")
tab7= ttk.Frame(my_notebook)
my_notebook.add(tab7, text= "Tab7")
tab8= ttk.Frame(my_notebook)
my_notebook.add(tab8, text= "Tab8")
#Create a Label in Tabs
Label(tab1, text= "Hello, Howdy?", font=('Helvetica', 20 ,'bold')).pack()
Label(tab2, text= """What is Python?
      
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.
What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.
Why Python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way.
Good to know
The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.
Python Syntax compared to other programming languages
Python was designed for readability, and has some similarities to the English language with influence from mathematics.
Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.""", font=('Helvetica', 20, 'bold')).pack()
Label(tab3, text= "Hello, Howdy?3", font=('Helvetica', 20 ,'bold')).pack()
Label(tab4, text= "Hello, Howdy?4", font=('Helvetica', 20 ,'bold')).pack()
Label(tab5, text= "Hello, Howdy?5", font=('Helvetica', 20 ,'bold')).pack()
Label(tab6, text= "Hello, Howdy?6", font=('Helvetica', 20 ,'bold')).pack()
Label(tab7, text= "Hello, Howdy?7", font=('Helvetica', 20 ,'bold')).pack()
Label(tab8, text= "Hello, Howdy?8", font=('Helvetica', 20 ,'bold')).pack()

win.mainloop()