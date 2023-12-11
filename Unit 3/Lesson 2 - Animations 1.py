from graphics import *

win = GraphWin("Lesson 2 - Animations 1",400,200)

## Create a blue ball that moves from the left side
## of the window to the right side of the window
## When the ball completely disappears from the right side
## make the ball reappear from the left side

## Create a blue ball with radius 50

ball = Circle(Point(50,100), 50)
ball.setFill(color_rgb(0,0,255))
ball.draw(win)
ball_frame_counter = 0

## Animation:
## 1) Infinte Loop aka "while True" loop
## 2) Inside the loop you need two things:
##      a) Time Sleep - momentarily stops the program
##      b) Position Update - update any object's position

while True:
    ## Time Sleep (60 FPS / 0.017 SPF in general works for any computer)
    ## In this course, 50 FPS / 0.02 SPF
    ## will often be used for easier calculations
    time.sleep(0.017)
    
    ## Update Blue Ball Position
    ball_frame_counter += 1
    if ball_frame_counter == 1:
        ball.move(1,0) ## <- move(change in x, change in y)
        ball_frame_counter = 0

    ## Getting the x position of the ball when it disappears (same for y)
    if ball.getCenter().getX() >= 449:
        ## Moving the ball back to the left side of the window
        ball.move(-499,0)
