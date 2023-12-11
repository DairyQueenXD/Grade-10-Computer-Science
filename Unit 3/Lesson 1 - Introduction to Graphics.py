## To gain access to the graphics module, type the following:
from graphics import * 
# the "*" means "everything"

## Next, create a graphics window
win = GraphWin("Lesson 1", 640, 400) # win variable will stand for window
# GraphWin(a,b,c) where a is a string representing the name of the window
# b is width and c is height //// 640 x 400 is kinda default settings

## Setting the background colour
win.setBackground(color_rgb(0, 251, 200))

"""
Goals for today:
1) Coordinate System
2) Creating Points
3) Creating Lines
4) Creating Rectangles
5) Creating Circles

***** 1) Coordinate System ******

In python graphic windows, the LEFT UP corner is (0,0)
NOT the LEFT DOWN corner !!!
Going down is POSITIVE. so for example, if a person jumps up it's negative
And when he falls down it's positive

In our window created (640 x 400), the LEFT UP corner is (0,0)
## the RIGHT UP corner is (639,0) and NOT (640,0)
## The length of the width is 640 and 639 - 0 + 1 = 640
## In the same way, the LEFT DOWN corner is (0,399)
## And the RIGHT DOWN corner is (639,399)
"""

### Creating Points ###
# Suppose we wish to create a line 
# That goes from (30,100) to (500,30)
# We first have to create points

# Also note that you HAVE to write "Point" and "Line" with a upper case
p1 = Point(30,100)
p2 = Point(500,30)
line = Line(p1,p2) # <- just doing this won't work
line.draw(win) # <- use the draw function and specify the window

### Creating a rectangle ###

# Suppose we wish to create a rectangle with 100 length and 50 width 
# The coordinates would be:
# top left coordinate at (400,200)
# bottom right coordinate at (499,249)

# Next, we create the two points and the rectangle
p3 = Point(400,200)
p4 = Point(499,249)
rec = Rectangle(p3,p4) # <- put the two coordinates inside

# If we wish to fill the rectangle with colour, 
# we have to do it BEFORE the draw function
rec.setFill(color_rgb(255, 35, 132)) # <- similar to how we did for background

# Setting width / color of the borders?
# Note that those commands MUST be BEFORE the draw function
rec.setWidth(10)
rec.setOutline(color_rgb(251, 255, 2))

# Drawing
rec.draw(win) # <- same as for lines

### Creating a circle ###

# Suppose we wish to create a circle with radius 50 pixels
# on the bottom left corner of the screen
# We know that the bottom left corner has coordinates (0, 399)
# The coordinates would be (49, 350)

# For circles, you only need one point: the center
p5 = Point(50,349)
cir = Circle(p5, 50) # <- Circle(center, radius)
cir.setFill(color_rgb(100, 244, 15))
cir.draw(win)
