""" So far in this course we've seen win.checkKey()
which only takes on ONE KEY that was pressed """

## The "in" "function"
int_list = [4,5,2,3,10,9]

# print(4 in int_list) -> This prints the boolean True
# print(7 in int_list) -> This prints False

from graphics import *

win = GraphWin("Lesson 5 - Multi Key Detection",500,500,autoflush = False)

ball = Circle(Point(250,250),50)
ball.setFill("red")
ball.draw(win)

while True:
    update()
    time.sleep(0.02) # 50 FPS
    k = win.checkAllKeys() # If you need multi key detection you use
                           # win.checkAllKeys()
                           # it stores all the keys that were pressed into
                           # a list
    
    if 'w' in k:
        ball.move(0,-4)
    if 's' in k:
        ball.move(0,4)
    if 'a' in k:
        ball.move(-4,0)
    if 'd' in k:
        ball.move(4,0)
