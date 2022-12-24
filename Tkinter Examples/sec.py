import time
import tkinter
from OpenGL import GL
from pyopengltk import OpenGLFrame

class AppOgl(OpenGLFrame):

    def initgl(self):
        """Initalize gl states when the frame is created"""
        GL.glViewport(0, 0, self.width, self.height)
        GL.glClearColor(0.0, 1.0, 0.0, 0.0)    
        self.start = time.time()
        self.nframes = 0

    def redraw(self):
        """Render a single frame"""
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        tm = time.time() - self.start
        self.nframes += 1
     #   print("fps",self.nframes / tm, end="\r" )
'''
class CubeSpinner( OpenGLFrame ):
    def initgl(self):
        GL.glLoadIdentity()
        GL.glClearColor(0.0, 1.0, 0.0, 0.0)  
        GLU.gluPerspective(45, (self.width/self.height), 0.1, 50.0)
        GL.glTranslatef(0.0,0.0, -5)
    def redraw(self):
        
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        Cube()
'''       
        
if __name__ == '__main__':
    root = tkinter.Tk()
    app = AppOgl(root, width=820, height=800)
    app.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    app.animate = 1
    app.after(100, app.printContext)
    app.mainloop()