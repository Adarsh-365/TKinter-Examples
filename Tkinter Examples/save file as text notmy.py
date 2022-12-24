import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def file1():    
    if not text_zone.edit_modified():      
        text_zone.delete('1.0', tk.END)
    else:        
        savefileas()
          
        text_zone.delete('1.0', tk.END)  
    
    text_zone.edit_modified(0)
       
    ws.title('PYTHON GUIDES')    

def openfile():
    
    if not text_zone.edit_modified():       
        try:            
            path = filedialog.askopenfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
                       
            ws.title('Notepad - ' + path)          
            
            with open(path, 'r') as f:             
                content = f.read()
                text_zone.delete('1.0', tk.END)
                text_zone.insert('1.0', content)
                                
                text_zone.edit_modified(0)
             
        except:
            pass   
    
    else:       
        savefileas()      
        
        text_zone.edit_modified(0)              
        openfile()         

def savefile():    
    try:
        
        path = ws.title().split('-')[1][1:]   
    
    except:
        path = ''
    
    if path != '':
        
        with open(path, 'w') as f:
            content = text_zone.get('1.0', tk.END)
            f.write(content)
      
    else:
        savefileas()    
    
    text_zone.edit_modified(0)
def savefileas():    
    try:
        path = filedialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
        ws.title('Notepad - ' + path)
    
    except:
        return   
    
    with open(path, 'w') as f:
        f.write(text_zone.get('1.0', tk.END))

ws = tk.Tk()

ws.title('Notepad')
ws.geometry('800x600')

menubar = tk.Menu(ws)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=file1)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save as...", command=savefileas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ws.quit)

menubar.add_cascade(label="File", menu=filemenu)

text_zone = tk.Text(ws)
text_zone.pack(expand = tk.YES, fill = tk.BOTH, side = tk.LEFT)

scrollbar = ttk.Scrollbar(ws, orient=tk.VERTICAL, command=text_zone.yview)
scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
text_zone['yscrollcommand'] = scrollbar.set

ws.config(menu=menubar)

ws.mainloop()