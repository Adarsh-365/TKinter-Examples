from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL import GL
from OpenGL import GLU
import numpy as np

verticies = (    (1, -1, 0),    (1, 1, 0),    (-1, 1, 0),    (-1, -1, 0),
             (-1,1,0),(-1,2,0),(-2,2,0),(-2,1,0),
             (1,1,0),(1,2,0),(2,2,0),(2,1,0),
             (1,-1,0),(1,-2,0),(2,-2,0),(2,-1,0),
             (-1,-1,0),(-1,-2,0),(-2,-2,0),(-2,-1,0)
             
                  )


edges = ((0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15),(16,17,18,19))


colors=[1.0, 0.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 0.0, 1.0]

colors=np.array(colors,dtype=np.float32)

def Cube():
    
    
    GL.glBegin(GL.GL_QUADS)
    for edge in edges:
        for vertex in edge:
            GL.glVertex3fv(verticies[vertex])
    
            
    GL.glEnd()

class CubeSpinner( OpenGLFrame ):
    def initgl(self):
        GL.glLoadIdentity()
      
            
        GLU.gluPerspective(400, (self.width/self.height), 0.1, 50.0)
        GL.glTranslatef(.0,0.0, -10)
    def redraw(self):
        
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        Cube()


def red():
    GL.glColor3f(1.0, 0.0, 0.0)

def blue():
    GL.glColor3f(0.0, 0.0, 1.0)
def green():
    GL.glColor3f(0.0, 1.0, 1.0)

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