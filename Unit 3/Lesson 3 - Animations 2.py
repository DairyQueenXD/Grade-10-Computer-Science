from graphics import *

win = GraphWin("Lesson 3 - Animations 2", 400, 400, autoflush = False)
## autoflush means to redraw the entire screen
## when draw() or move() gets called
## autoflush is NOT ideal when multiple objects need to move
## within the same frame. When the graphics card cannot keep up
## with the number of times it needs to redraw the screen within the
## time.sleep duration, flickering will happen
## When we set autoflush to false, we need to tell the computer
## to update using update()
## Otherwise the screen will not redraw until the function
## update() gets called

## Create a green ball with initial radius 10

radius = 10
p = Point(200, 200)
ball = Circle(p, radius)
ball.setFill(color_rgb(0,255,0))
ball.draw(win)
increasing = True
## Animation

while True:
    update()
    time.sleep(0.02) # 50 FPS

    ## Unlike move() function, there is no direct way to change the
    ## radius / length / width / size of any object
    
    ## The only way to change the size, is to undraw the object and
    ## recreate the object with the new size that you want

    ## Process for proportional transformation:
    ## 1. Undraw the object
    ball.undraw()
    ## 2. Adjust the radius/length/width/size
    if increasing:
        radius += 1
    else:
        radius -= 1

    if radius == 200:
        increasing = False
    elif radius == 0:
        increasing = True
        
    ## 3. Recreate the object
    ball = Circle(p, radius)
    ball.setFill(color_rgb(0,255,0))
    ## 4. Draw the object
    ball.draw(win)
    
