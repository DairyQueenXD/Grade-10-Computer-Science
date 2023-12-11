## Goal of lesson
## 1) Making a red ball move using WASD keys
## 2) Making a red ball move without going pass the borders

## There are 2 commands that allow you to use keyboard control
## 1) win.getKey()
##      - The program will STOP at this line and wait until the user inputs
## 2) win.checkKey()
##      - The program will READ this line and see if the user has pressed a key
##      by the time the computer reads this line
##      - Otherwise, the value is an EMPTY CHARACTER

from graphics import *

win = GraphWin("Lesson 4 - Keyboard Control", 400, 400)

## Creating a red ball with r = 50 pixels
ball = Circle(Point(200,200), 50)
ball.setFill("red")
ball.draw(win)

x = 6
while True:
    time.sleep(0.02)
    
    k = win.checkKey()
        
    if k == 'w':
        if ball.getCenter().getY() - x < 50:
            ball.move(0,50-ball.getCenter().getY())
        else:
            ball.move(0,-x)
    elif k == "a":
        if ball.getCenter().getX() - x < 50:
            ball.move(50-ball.getCenter().getX(),0)
        else:
            ball.move(-x,0)
    elif k == 's':
        if ball.getCenter().getY() + x > 349:
            ball.move(0,349-ball.getCenter().getY())
        else:
            ball.move(0,x)
    elif k == 'd':
        if ball.getCenter().getX() + x > 349:
            ball.move(349-ball.getCenter().getX(),0)
        else:
            ball.move(x,0)
    
    
