from OpenGL.GL import *
from OpenGL.GLUT import *
import sys


def pressEsc(key, x, y):
    key = int.from_bytes(key, "big")
    if key == 27:
        exit(0)


def draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.4, 0.8, 0.2)
    glutSolidCube(0.8)
    glColor3f(0, 0, 0)
    glutWireCube(0.8)
    glutSwapBuffers()


glutInitWindowSize(400, 400)
glutInitWindowPosition(500, 150)
glutInit(sys.argv)
glutCreateWindow('Lab 1')
glutDisplayFunc(draw)
glutKeyboardFunc(pressEsc)
glutMainLoop()
