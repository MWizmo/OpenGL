from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


class Scene:
    def __init__(self):
        self.x_angle = 0
        self.y_angle = 0
        self.step = 0.3
        self.ambient = (0.8, 0.8, 0.7, 0.5)
        self.lightpos = (2, 2, 2)

    def pressEsc(self, key, x, y):
        key = int.from_bytes(key, "big")
        if key == 27:
            exit(0)

    def pressKeys(self, key, x, y):
        if key == GLUT_KEY_UP:
            self.x_angle += self.step
        elif key == GLUT_KEY_DOWN:
            self.x_angle -= self.step
        elif key == GLUT_KEY_LEFT:
            self.y_angle += self.step
        elif key == GLUT_KEY_RIGHT:
            self.y_angle -= self.step
        glutPostRedisplay()

    def draw(self):
        glPushMatrix()

        #glLoadIdentity()
        #glTranslatef(-0.5, 0.5, -0.5)
        #light0_position = (0.0, 0.0, 0.0, 1.0)
        # glLightfv(GL_LIGHT0, GL_POSITION, self.lightpos)
        glRotatef(self.x_angle, 1.0, 0.0, 0.0)
        glRotatef(self.y_angle, 0.0, 1.0, 0.0)
        glClearColor(0.2, 0.2, 0.2, 0.2)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        color = (0.4, 0.8, 0.2)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glPopMatrix()
        #glutSwapBuffers()

        glLightfv(GL_LIGHT0, GL_POSITION, self.lightpos)
        glPushMatrix()
        glutSolidSphere(0.5, 50, 50)
        glPopMatrix()
        glFlush()
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # material_diffuse = (1.0, 1.0, 1.0, 1.0)
        # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, material_diffuse)
        # #gluLookAt(self.x_angle,self.y_angle,0, 0,0,0, 0,1,0)
        # light_sample = 2
        #
        # if light_sample == 1:
        #     light0_diffuse = (0.4, 0.7, 0.2)
        #     light0_direction = (0.0, 0.0, 1.0, 0.0)
        #     glEnable(GL_LIGHT0)
        #     glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
        #     glLightfv(GL_LIGHT0, GL_POSITION, light0_direction)
        # if light_sample == 2:
        #     light1_diffuse = (0.4, 0.7, 0.2)
        #     light1_position = (0.0, 0.0, 1.0, 1.0)
        #     glEnable(GL_LIGHT1)
        #     glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
        #     glLightfv(GL_LIGHT1, GL_POSITION, light1_position)
        # if light_sample == 3:
        #     light2_diffuse = (0.4, 0.7, 0.2)
        #     light2_position = (0.0, 0.0, 1.0, 1.0)
        #     glEnable(GL_LIGHT2)
        #     glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_diffuse)
        #     glLightfv(GL_LIGHT2, GL_POSITION, light2_position)
        #     glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.0)
        #     glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.2)
        #     glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 0.4)
        # if light_sample == 4:
        #     light3_diffuse = (0.4, 0.7, 0.2)
        #     light3_position = (0.0, 0.0, 1.0, 1.0)
        #     light3_spot_direction = (0.0, 0.0, -1.0)
        #     glEnable(GL_LIGHT3)
        #     glLightfv(GL_LIGHT3, GL_DIFFUSE, light3_diffuse)
        #     glLightfv(GL_LIGHT3, GL_POSITION, light3_position)
        #     glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 30)
        #     glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, light3_spot_direction)
        # if light_sample == 5:
        #     light4_diffuse = (0.4, 0.7, 0.2)
        #     light4_position = (0.0, 0.0, 1.0, 1.0)
        #     light4_spot_direction = (0.0, 0.0, -1.0)
        #     glEnable(GL_LIGHT4)
        #     glLightfv(GL_LIGHT4, GL_DIFFUSE, light4_diffuse)
        #     glLightfv(GL_LIGHT4, GL_POSITION, light4_position)
        #     glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, 30)
        #     glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, light4_spot_direction)
        #     glLightf(GL_LIGHT4, GL_SPOT_EXPONENT, 15.0)
        # glutSolidSphere(0.5, 500, 100)
        # glRotatef(self.x_angle, 1.0, 0.0, 0.0)
        # glRotatef(self.y_angle, 0.0, 1.0, 0.0)
        # glDisable(GL_LIGHT0)
        # glDisable(GL_LIGHT1)
        # glDisable(GL_LIGHT2)
        # glDisable(GL_LIGHT3)
        # glDisable(GL_LIGHT4)
        # glDisable(GL_LIGHT5)
        # glDisable(GL_LIGHT6)
        # glDisable(GL_LIGHT7)
        glutSwapBuffers()

    def show(self):
        glutInitWindowSize(600, 600)
        glutInitWindowPosition(400, 50)
        glutInit(sys.argv)
        glutCreateWindow('Lab 5')
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glEnable(GL_LIGHTING)
        #glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        glEnable(GL_NORMALIZE)
        glutDisplayFunc(self.draw)
        glutSpecialFunc(self.pressKeys)
        glutKeyboardFunc(self.pressEsc)
        glutMainLoop()


scene = Scene()
scene.show()
