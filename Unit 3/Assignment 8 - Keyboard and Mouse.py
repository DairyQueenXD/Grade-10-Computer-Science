from graphics import *
import random

win = GraphWin("Assignment 8", 500, 500)
win.setBackground("black")

r = 24
red = 0
green = 0
blue = 0
while True:
    center = win.checkMouse()
    k = win.checkKey()
    if center != None:
        red = random.randint(0,255)
        blue = random.randint(0,255)
        green = random.randint(0,255)
        
        bigC = Circle(center, r)
        bigC.setOutline(color_rgb(red, green, blue))
        bigC.draw(win)

        smallC1 = Circle(Point(center.getX()-r/3, center.getY()-r/3), r/6)
        smallC1.setOutline(color_rgb(red, green, blue))
        smallC1.draw(win)

        smallC2 = Circle(Point(center.getX()+r/3, center.getY()-r/3),r/6)
        smallC2.setOutline(color_rgb(red, green, blue))
        smallC2.draw(win)

        line = Line(Point(center.getX()-r/2,center.getY()+r*3/4),Point(center.getX()+r/2,center.getY()+3*r/4))
        line.setOutline(color_rgb(red, green, blue))
        line.draw(win)
    if k == '1':
        r = 24
    if k == '2':
        r = 48
    if k == '3':
        r = 72
    if k == '4':
        r = 96
    if k == '5':
        win.close()
    

