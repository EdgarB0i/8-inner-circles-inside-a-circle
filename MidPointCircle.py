#Install OpenGL library for python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time

rad=int(input("Enter the radius: "))
rad_half=rad/2
c_x=int(input("Enter center: "))
c_y=int(input("Enter center: "))

#outer circle
def midpointcircle():
    d=1-rad
    x=0
    y=rad
    zoneConversion(x,y,c_x,c_y)
    while(x<y):
        if d<0:
            #East
            d=d+(2*x)+3
            x+=1
        else:
            #SouthEast
            d=d+(2*x)-(2*y)+5
            x+=1
            y-=1
        zoneConversion(x, y, c_x, c_y)

#inner circles
def minions(x1,cx,cy):
    d=1-x1
    x=0
    y=x1
    zoneConversion(x,y,cx,cy)
    while(x<y):
        if d<0:
            #East
            d=d+(2*x)+3
            x+=1
        else:
            #SouthEast
            d=d+(2*x)-(2*y)+5
            x+=1
            y-=1
        zoneConversion(x, y, cx, cy)

#Converting co-ordinates to all different zones
def zoneConversion(x, y, c_x, c_y):
    #Un-comment these lines if you want a trippy circle
    #a=random.randint(0,9)
    #b=random.randint(0,9)
    #c=random.randint(0,9)
    
    glPointSize(2)
    a,b,c=0,0,9
    glColor3d(a, b, c)
    glBegin(GL_POINTS)
    glVertex2f(x + 250 + c_x, y + 250 + c_y)
    glVertex2f(y + 250 + c_x, x + 250 + c_y)
    glVertex2f(y + 250 + c_x, -x + 250 + c_y)
    glVertex2f(x + 250 + c_x, -y + 250 + c_y)
    glVertex2f(-x + 250 + c_x, -y + 250 + c_y)
    glVertex2f(-y + 250 + c_x, -x + 250 + c_y)
    glVertex2f(-y + 250 + c_x, x + 250 + c_y)
    glVertex2f(-x + 250 + c_x, y + 250 + c_y)
    glEnd()

    
def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glutPostRedisplay() 
    time.sleep(0.05)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    #call the draw methods here
    midpointcircle()
    minions(rad_half,-(rad_half)+c_x,0+c_y)
    minions(rad_half,(rad_half)+c_x,0+c_y)
    minions(rad_half,0+c_x,(rad_half)+c_y)
    minions(rad_half,0+c_x,-(rad_half)+c_y)
    
    minions(rad_half,(rad/2.83)+c_x,(rad/2.83)+c_y)
    minions(rad_half,-(rad/2.83)+c_x,-(rad/2.83)+c_y)
    minions(rad_half,-(rad/2.83)+c_x,(rad/2.83)+c_y)
    minions(rad_half,(rad/2.83)+c_x,-(rad/2.83)+c_y)


    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Circle")
glutDisplayFunc(showScreen)
init()
glutMainLoop()
