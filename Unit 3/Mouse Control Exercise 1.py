from graphics import *
import random
win = GraphWin("Mouse Control Exercise", 400, 400)

## Number 1
t = 0

while True:
    time.sleep(0.02)
    m = win.checkMouse()
    
    if m != None:
        t += 1
        if t == 1:
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            a = Line(Point(0,399),m)
            a.setFill(color_rgb(r,g,b))
            a.draw(win)
        else:
            a = Line(a.getP2(),m)
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            a.setFill(color_rgb(r,g,b))
            a.draw(win)
        
            
