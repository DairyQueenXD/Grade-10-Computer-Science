from graphics import *
import random
win = GraphWin("Mouse Control Exercise", 600, 400)

## Number 3

happy = Rectangle(Point(430, 70),Point(570,140))
happy.setFill("yellow")
happy.draw(win)

happy_txt = Text(Point(500,105),"Happy")
happy_txt.draw(win)

sad = Rectangle(Point(430, 160),Point(570,230))
sad.setFill("blue")
sad.draw(win)

sad_txt = Text(Point(500,195),"Sad")
sad_txt.draw(win)

angry = Rectangle(Point(430, 250),Point(570,320))
angry.setFill("red")
angry.draw(win)

angry_txt = Text(Point(500,285),"Angry")
angry_txt.draw(win)
x = 0
h = True
s = False
a = False

face = Circle(Point(200,200),150)
face.draw(win)

eyes1 = Circle(Point(150,150),10)
eyes1.setFill("black")
eyes1.draw(win)

eyes2 = Circle(Point(250,150),10)
eyes2.setFill("black")
eyes2.draw(win)

o = Oval(Point(130,250),Point(270,275))
o.setFill("black")
o.draw(win)

while True:
    time.sleep(0.02)
    m = win.checkMouse()
    if m != None:
        if 430 < m.getX() < 570:
            if 70 < m.getY() < 140:
                h = True
                s = False
                a = False
            elif 160 < m.getY() < 230:
                s = True
                h = False
                a = False
            elif 250 < m.getY() < 320:
                a = True
                h = False
                s = False
    break
    #if h == True and s == False and a == False:
