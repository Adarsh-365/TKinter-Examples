from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL import GL
from OpenGL import GLU

verticies = [    [1, -1, -1],    [1, 1, -1],    [-1, 1, -1],    [-1, -1, -1],
                 [1, -1, 1],    [1, 1, 1],    [-1, -1, 1],    [-1, 1, 1]    ]

edges = [    [0,1],    [0,3],    [0,4],    [2,1],    [2,3],    [2,7],
    [6,3],    [6,4],    [6,7],    [5,1],    [5,4],    [5,7]    ]


no=0
def Cube():
    global no
    GL.glBegin(GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            no +=1
            print(no)
            if no==2000:
                no=0
            if no>1000:
                verticies[vertex]=[verticies[vertex][0]+0.01,verticies[vertex][1]+0.01,verticies[vertex][2]+0.01]
            if no<1000:
                 verticies[vertex]=[verticies[vertex][0]-0.01,verticies[vertex][1]-0.01,verticies[vertex][2]-0.01]
            GL.glVertex3fv(verticies[vertex])
    GL.glEnd()
    

class CubeSpinner( OpenGLFrame ):
    def initgl(self):
        GL.glLoadIdentity()
        GLU.gluPerspective(45, (self.width/self.height), 0.1, 50.0)
        GL.glTranslatef(0.0,0.0, -5)
    def redraw(self):
       
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        Cube()

def main():
    root = Tk()
    root.geometry('500x500')
    app = CubeSpinner(root, width=500, height=500)
    app.pack(fill=BOTH, expand=YES)
    app.animate = 1
    app.after(100, app.printContext)
    
    app.mainloop()

if __name__=="__main__":
    main()