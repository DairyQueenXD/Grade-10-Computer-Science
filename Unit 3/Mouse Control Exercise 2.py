from graphics import *
import random
win = GraphWin("Mouse Control Exercise", 400, 400)

## Number 2
t = 0
while True:
    time.sleep(0.02)
    m = win.checkMouse()
    if m != None:
        t += 1
        if t % 2 == 1:
            x = m.getX()
            y = m.getY()
        else:
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            rect = Rectangle(Point(x,y),m)
            rect.setFill(color_rgb(r,g,b))
            rect.draw(win)
        
            
