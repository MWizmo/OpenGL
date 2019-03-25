from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Scene:
    def __init__(self):
        self.x_angle = 1
        self.y_angle = 1
        self.distance = 1.0
        self.step = 1

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

    def reshape(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if (w > h):
            glOrtho(-1.5, 1.5, -0.5 * h / w, 0.5 * h / w, - 10.0, 10.0)
        else:
            glOrtho(-1.5 * w / h, 1.5 * w / h, -1.5, 1.5, -10.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def display(self):
        glRotatef(self.x_angle, 1.0, 0.0, 0.0)
        glRotatef(self.y_angle, 0.0, 1.0, 0.0)
        mat_specular = (1.0, 1.0, 1.0, 1.0)
        mat_shininess = (50.0)
        light_position = (1, 1, 1, 0.0)
        white_light = (1.0, 1.0, 1.0, 1.0)
        glClearColor(0.2, 0.2, 0.2, 0.0)
        glShadeModel(GL_SMOOTH)
        color = (0.4, 0.8, 0.2)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, white_light)
        glLightfv(GL_LIGHT0, GL_SPECULAR, white_light)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        light_ambient = (0.2, 0.2, 0.2, 1.0)
        light_diffuse = (1.0, 1.0, 1.0, 1.0)
        light_specular = (1.0, 1.0, 1.0, 1.0)
        light_position = (-2.0, 2.0, 1.0, 1.0)
        spot_direction = (-1.0, -1.0, 0.0)
        glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular)
        glLightfv(GL_LIGHT1, GL_POSITION, light_position)
        glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 1.5)
        glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.5)
        glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.2)
        glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 45.0)
        glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, spot_direction)
        glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 2.0)
        glEnable(GL_LIGHT1)
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glutSolidSphere(1.0, 40, 16)
        glFlush()

    def show(self):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(100, 100)
        glutCreateWindow("Lab 5")
        glutDisplayFunc(self.display)
        glutSpecialFunc(self.pressKeys)
        glutReshapeFunc(self.reshape)
        glutMainLoop()

for i in range(21, 40):
    print(i, (i*31)%40)
scene = Scene()
scene.show()
