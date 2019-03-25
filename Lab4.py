from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image as Image
import sys
import numpy


class Scene:
    def __init__(self):
        self.x = -20
        self.y = 20
        self.step = 3

    def pressEsc(self, key, x, y):
        key = int.from_bytes(key, "big")
        if key == 27:
            exit(0)

    def pressKeys(self, key, x, y):
        if key == GLUT_KEY_UP:
            self.x += self.step
        elif key == GLUT_KEY_DOWN:
            self.x -= self.step
        elif key == GLUT_KEY_LEFT:
            self.y += self.step
        elif key == GLUT_KEY_RIGHT:
            self.y -= self.step
        glutPostRedisplay()

    def draw(self):
        glPushMatrix()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(self.x, 1.0, 0.0, 0.0)
        glRotatef(self.y, 0.0, 1.0, 0.0)
        glClearColor(0.7, 0.9, 0.7, 0.7)
        glClear(GL_COLOR_BUFFER_BIT)
        rad = 0.4
        glColor3f(0, 0, 0)
        glutWireCube(rad * 2 + 0.1)

        glBindTexture(GL_TEXTURE_2D, self.loadTexture("images//one_brick.jpg"))
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0, 0)
        glVertex3f(rad, -rad, -rad)
        glTexCoord2f(5, 0)
        glVertex3f(-rad, -rad, -rad)
        glTexCoord2f(5, 5)
        glVertex3f(-rad, rad, -rad)
        glTexCoord2f(0, 5)
        glVertex3f(rad, rad, -rad)
        glEnd()

        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0, 0)
        glVertex3f(rad, -rad, rad)
        glTexCoord2f(1, 0)
        glVertex3f(-rad, -rad, rad)
        glTexCoord2f(1, 1)
        glVertex3f(-rad, rad, rad)
        glTexCoord2f(0, 1)
        glVertex3f(rad, rad, rad)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, self.loadTexture("images//wood.jpg"))
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0, 0)
        glVertex3f(rad, rad, -rad)
        glTexCoord2f(1, 0)
        glVertex3f(-rad, rad, -rad)
        glTexCoord2f(1, 1)
        glVertex3f(-rad, rad, rad)
        glTexCoord2f(0, 1)
        glVertex3f(rad, rad, rad)
        glEnd()

        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0, 0)
        glVertex3f(rad, -rad, -rad)
        glTexCoord2f(1, 0)
        glVertex3f(-rad, -rad, -rad)
        glTexCoord2f(1, 1)
        glVertex3f(-rad, -rad, rad)
        glTexCoord2f(0, 1)
        glVertex3f(rad, -rad, rad)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, self.loadTexture("images//rock.jpg"))
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0, 0)
        glVertex3f(rad, -rad, -rad)
        glTexCoord2f(1, 0)
        glVertex3f(rad, rad, -rad)
        glTexCoord2f(1, 1)
        glVertex3f(rad, rad, rad)
        glTexCoord2f(0, 1)
        glVertex3f(rad, -rad, rad)
        glEnd()

        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0, 0)
        glVertex3f(-rad, -rad, -rad)
        glTexCoord2f(1, 0)
        glVertex3f(-rad, rad, -rad)
        glTexCoord2f(1, 1)
        glVertex3f(-rad, rad, rad)
        glTexCoord2f(0, 1)
        glVertex3f(-rad, -rad, rad)
        glEnd()
        glPopMatrix()
        glutSwapBuffers()

    def loadTexture(self, fileName):
        image = Image.open(fileName)
        width = image.size[0]
        height = image.size[1]
        image = image.tobytes("raw", "RGBX", 0, -1)
        texture = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, texture)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, width, height, GL_RGBA, GL_UNSIGNED_BYTE, image)
        return texture

    def show(self):
        glutInitWindowSize(600, 600)
        glutInitWindowPosition(400, 50)
        glutInit(sys.argv)
        glutCreateWindow('Lab 4')
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glutDisplayFunc(self.draw)
        glutSpecialFunc(self.pressKeys)
        glutKeyboardFunc(self.pressEsc)
        glutMainLoop()


scene = Scene()
scene.show()
