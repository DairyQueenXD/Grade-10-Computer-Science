## Number 3
import random
from graphics import *

win = GraphWin("Exercise 3", 400, 400, autoflush = False)

radius = 50
ball = Circle(Point(200,200), radius)
x = random.randint(0,255)
y = random.randint(0,255)
z = random.randint(0,255)
ball.setFill(color_rgb(x,y,z))
ball.draw(win)

while True:
    update()
    time.sleep(0.02)
    k = win.checkKey()
    if k == 'Up':
        if radius != 200:
            radius += 5
        ball.undraw()
        ball = Circle(Point(200,200),radius)
        ball.setFill(color_rgb(x,y,z))
        ball.draw(win)
    if k == 'Down':
        ball.undraw()
        if radius != 0:
            radius -= 5
        ball = Circle(Point(200,200), radius)
        ball.setFill(color_rgb(x,y,z))
        ball.draw(win)
    if k == 'space':
        ball.undraw()
        x = random.randint(0,255)
        y = random.randint(0,255)
        z = random.randint(0,255)
        ball.setFill(color_rgb(x,y,z))
        ball.draw(win)
        
