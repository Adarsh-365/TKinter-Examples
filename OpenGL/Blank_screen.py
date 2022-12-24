from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram,  compileShader 
import numpy as np
import pyrr
import time

start = time.time()

vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;

uniform mat4 rotation;

out vec3 v_color;

void main()
{
    gl_Position = rotation * vec4(a_position, 1.0);
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


vertices = [-0.5, -0.5, 0.5, 1.0, 0.0, 0.0,
             0.5, -0.5, 0.5, 0.0, 1.0, 0.0,
             0.5,  0.5, 0.5, 0.0, 0.0, 1.0,
            -0.5,  0.5, 0.5, 1.0, 1.0, 1.0,

            -0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
             0.5, -0.5, -0.5, 0.0, 1.0, 0.0,
             0.5,  0.5, -0.5, 0.0, 0.0, 1.0,
            -0.5,  0.5, -0.5, 1.0, 1.0, 1.0]

indices = [0, 1, 2, 2, 3, 0,
           4, 5, 6, 6, 7, 4,
           4, 5, 1, 1, 0, 4,
           6, 7, 3, 3, 2, 6,
           5, 6, 2, 2, 1, 5,
           7, 4, 0, 0, 3, 7]

vertices = np.array(vertices, dtype=np.float32)
indices = np.array(indices, dtype=np.uint32)

# the main application loop
def cube():
    

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    

    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

class CubeSpinner( OpenGLFrame ):
        def initgl(self):   
                shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))
                
                # Vertex Buffer Object
                VBO = glGenBuffers(1)
                glBindBuffer(GL_ARRAY_BUFFER, VBO)
                glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
                
                # Element Buffer Object
                EBO = glGenBuffers(1)
                glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
                glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)
                
                glEnableVertexAttribArray(0)
                glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
                
                glEnableVertexAttribArray(1)
                glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
                
                glUseProgram(shader)
                glClearColor(0, 0.1, 0.1, 1)
                glEnable(GL_DEPTH_TEST)
                
                rotation_loc = glGetUniformLocation(shader, "rotation")
        def redraw(self):
            glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            cube()

def main():
    root = Tk()
    root.geometry('1000x1000')
    app = CubeSpinner(root, width=1000, height=1000)
    app.pack(fill=BOTH, expand=YES)
    app.animate = 1
    app.after(100, app.printContext)
    
    app.mainloop()

if __name__=="__main__":
    main()

