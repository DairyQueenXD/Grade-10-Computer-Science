"""
Purpose of the Lesson:
- Draw a ball with random radius from 10 to 50 pixels
- Whenever the user presses on the screen

1) win.getMouse()
    - This stops the entire program and waits until the user presses
      on the mouse

2) win.checkMouse()
    - This does NOT stop the entire program
      When the computer reaches this line, if the mouse has been pressed in
      between framnes, the coordinates of the mouse will be stored as a point
    - If the mouse was NOT pressed in between frames, the computer will
      store the value as None

"""
from graphics import *
import random

win = GraphWin("Lesson 5 - Mouse Control", 400, 400)

while True:
    time.sleep(0.02)
    m = win.checkMouse()
    if m != None:
        radius = random.randint(10,50)
        r = random.randint(0,255)
        b = random.randint(0,255)
        g = random.randint(0,255)
        ball = Circle(m,radius)
        ball.setFill(color_rgb(r,g,b))
        ball.draw(win)
