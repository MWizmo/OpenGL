from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


class Scene:
    def __init__(self):
        self.eyex = 0.6
        self.eyey = 0.8
        self.eyez = 2
        self.mode = 'p'

    def pressEsc(self, key, x, y):
        key = int.from_bytes(key, "big")
        if key == 27:
            exit(0)

    def pressKeys(self, key, x, y):
        if key == GLUT_KEY_UP:
            self.eyex += 0.1
        elif key == GLUT_KEY_DOWN:
            self.eyex -= 0.1
        elif key == GLUT_KEY_LEFT:
            self.eyey += 0.1
        elif key == GLUT_KEY_RIGHT:
            self.eyey -= 0.1
        elif key == GLUT_KEY_F1:
            self.mode = 'p'
        elif key == GLUT_KEY_F2:
            self.mode = 'o'
        glutPostRedisplay()

    def pressMouse(self, key, state, x, y):
        if key == 0 and state == 0:
            self.eyez += 0.1
        if key == 2 and state == 0:
            self.eyez -= 0.1
        glutPostRedisplay()

    def draw(self):
        glPushMatrix()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if self.mode == 'p':
            x, y, width, height = glGetDoublev(GL_VIEWPORT)
            gluPerspective(60, width / height, 1, 20)
        elif self.mode == 'o':
            glOrtho(-2,2,-2,2,0.1,20)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.eyex, self.eyey, self.eyez, 0, 0, 0, 0, 1, 0)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.4, 0.8, 0.2)
        glutSolidCube(0.8)
        glColor3f(0, 0, 0)
        glutWireCube(0.8)
        glPopMatrix()
        glutSwapBuffers()

    def show(self):
        glutInitWindowSize(600, 500)
        glutInitWindowPosition(400, 100)
        glutInit(sys.argv)
        glutCreateWindow('Lab 3')
        glutDisplayFunc(self.draw)
        glutSpecialFunc(self.pressKeys)
        glutKeyboardFunc(self.pressEsc)
        glutMouseFunc(self.pressMouse)
        glutMainLoop()


scene = Scene()
scene.show()
