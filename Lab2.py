from OpenGL.GL import *
from OpenGL.GLUT import *
import sys


def pressEsc(key, x, y):
    key = int.from_bytes(key, "big")
    if key == 27:
        exit(0)


def pressMouse(key, state, x, y):
    global angle
    if key == 0 and state == 0:
        angle -= 10.0
    if key == 2 and state == 0:
        angle += 10.0
    glutPostRedisplay()


def pressArrows(key, x, y):
    global x_center
    global y_center
    if key == GLUT_KEY_UP:
        y_center += 0.01
    elif key == GLUT_KEY_DOWN:
        y_center -= 0.01
    elif key == GLUT_KEY_LEFT:
        x_center -= 0.01
    elif key == GLUT_KEY_RIGHT:
        x_center += 0.01
    glutPostRedisplay()


def draw():
    global angle
    global x_center
    global y_center
    glPushMatrix()
    glRotatef(angle, 0.0, 1.0, 0.0)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POLYGON)
    glColor3f(0.8, 0.4, 0.5)
    glVertex2f(0, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0, 0.5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.4, 0.8, 0.2)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0, -0.5)
    glVertex2f(0, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(x_center-0.1, y_center-0.1)
    glVertex2f(x_center+0.1, y_center-0.1)
    glVertex2f(x_center+0.1, y_center+0.1)
    glVertex2f(x_center-0.1, y_center+0.1)
    glEnd()

    glPopMatrix()
    glutSwapBuffers()


global angle
global x_center
global y_center
angle = 0.0
x_center = 0.7
y_center = 0.7
glutInitWindowSize(400, 400)
glutInitWindowPosition(500, 150)
glutInit(sys.argv)
glutCreateWindow('Lab 2')
glutDisplayFunc(draw)
glutSpecialFunc(pressArrows)
glutKeyboardFunc(pressEsc)
glutMouseFunc(pressMouse)
glutMainLoop()
