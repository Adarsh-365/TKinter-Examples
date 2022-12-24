from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np



vertex_src = """
# version 330
in vec3 a_position;
in vec3 a_color;
out vec3 v_color;
void main()
{
    gl_Position = vec4(a_position, 1.0);
    v_color = a_color;
}
"""

fragment_src = """
# version 330
in vec3 v_color;
out vec4 out_color;
void main()
{
    out_color = vec4(v_color, 1.0);
}
"""



vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
             0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
             0.0,  0.5, 0.0, 0.0, 0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)





def cube():
    glClear(GL_COLOR_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLES, 0, 3)




class CubeSpinner( OpenGLFrame ):
    def initgl(self):
        
        
        shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))
        
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        
        position = glGetAttribLocation(shader, "a_position")
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        
        color = glGetAttribLocation(shader, "a_color")
        glEnableVertexAttribArray(color)
        glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        
        glUseProgram(shader)
        glClearColor(0, 0.1, 0.1, 1)

    def redraw(self):
        cube()
        
    
        
        




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














