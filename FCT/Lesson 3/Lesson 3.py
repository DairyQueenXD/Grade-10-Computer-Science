# This lesson is about Jumping Mechanics

from graphics import *

win = GraphWin("Lesson 3 - Jumping Mechanics",500,500,autoflush = False)

## Image Importation
posX = 70
posY = 350
background = Image(Point(250,250),"pikachubg.png")

trex_run = [Image(Point(posX,posY),"trexleft.png"),
            Image(Point(posX,posY),"trexright.png")]

trex_jump = Image(Point(posX,posY),"trexjump.png")

## T-Rex Game stats
trex_run_spriteno = 0
is_jumping = False
initial_velocity = -44
gravity = 4
running_frame_counter = 0

## Initial Setup
background.draw(win)
trex_run[trex_run_spriteno].draw(win)

while True:
    update()
    time.sleep(0.02) # 50 FPS
    k = win.checkKey()

    if is_jumping:# if t-rex is in the middle of a jump
        trex_jump.move(0,initial_velocity)
        initial_velocity += gravity
        if initial_velocity - gravity == 44:
            is_jumping = False
            initial_velocity = -44
            trex_jump.undraw()
            trex_run[trex_run_spriteno].draw(win)
    else: # if t-rex is running
        running_frame_counter += 1
        if running_frame_counter == 8:
            trex_run[trex_run_spriteno].undraw()
            trex_run_spriteno += 1
            if trex_run_spriteno == 2:
                trex_run_spriteno = 0
            trex_run[trex_run_spriteno].draw(win)
            running_frame_counter = 0

        if k == "space":
            is_jumping = True
            trex_run[trex_run_spriteno].undraw()
            trex_jump.draw(win)
