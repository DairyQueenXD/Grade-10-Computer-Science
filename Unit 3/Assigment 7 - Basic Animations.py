"""
Name: Dequan Kong
Course Code: ICS2O
Assigment 7 - Basic Animations

Title: Soccer
Animation Description:

"""

from graphics import *

win = GraphWin("Assigment 7", 1000, 600, autoflush = False)
win.setBackground("gray")

## Original variables
radius = 10
p1 = Point(800, 500)
p2 = Point(800, 415)
increasing = True
size = 5
### When scoring
goal = False

## Original shapes
score = Circle(p1, radius)
score.setFill(color_rgb(255,255,255))
score.setOutline(color_rgb(255,255,255))
score.draw(win)

text = Text(p1,"0:0")
text.setTextColor("red")
text.setSize(size)
text.setOutline("red")
text.draw(win)

aGoal = Rectangle(Point(450, 50), Point(710, 210))
aGoal.setWidth(3)
aGoal.draw(win)
x = 0
y = 0
for i in range(12):
    l1 = Line(Point(470+x,50),Point(470+x,210))
    l1.draw(win)
    x += 20
for i in range(9):
    l2 = Line(Point(450, 50+y), Point(710,50+y))
    l2.draw(win)
    y += 20
x = 0
y = 0
minusThing = -140
aGoal2 = Rectangle(Point(400+minusThing, 400),Point(660+minusThing, 560))
aGoal2.setWidth(3)
aGoal2.draw(win)
for i in range(12):
    l1 = Line(Point(420+x+minusThing,400),Point(420+x+minusThing,560))
    l1.draw(win)
    x += 20
for i in range(9):
    l2 = Line(Point(400+minusThing,400+y),Point(660+minusThing,400+y))
    l2.draw(win)
    y += 20
    
goalText = Text(p2, "GOAL!")

# Soccer ball
p = Point(200, 400)
radius2 = 20
ball = Circle(p, radius2)
ball.setFill(color_rgb(0,255,0))
ball.draw(win)

# Animation
while True:
    ## Animation stuff
    update()
    time.sleep(0.02)
    score.undraw()
    text.undraw()
    ball.move(2,-1)

    ## Changing variables
    if increasing:
        radius += 1
        size += 1
    else:
        radius -= 1
        size -= 1

    if size == 36:
        increasing = False
    if size == 5:
        increasing = True

    if ball.getCenter().getY() <= 190:
        goal = True
    if goal:

        size = 27
        radius = 42
        
        score = Circle(p1, radius)
        score.setFill(color_rgb(255,255,255))
        score.setOutline(color_rgb(255,255,255))
        score.draw(win)
        
        text = Text(p1, "1:0")
        text.setTextColor("red")
        text.setSize(size)
        text.setOutline("red")
        text.draw(win)

        goalText.setTextColor("red")
        goalText.setSize(36)
        goalText.draw(win)
        break

    ## Redrawing
    score = Circle(p1, radius)
    score.setFill(color_rgb(255,255,255))
    score.setOutline(color_rgb(255,255,255))
    score.draw(win)

    text = Text(p1, "0:0")
    text.setTextColor("red")
    text.setSize(size)
    text.setOutline("red")
    text.draw(win)
    
    
    
