from graphics import *

win = GraphWin("Lesson 6 - Scrolling Background",500,500,)

## Image Importation
bg = Image(Point(500,250),"scrolling_bg.png")
bg.draw(win)
frame_counter = 0

while True:
    time.sleep(0.02) # 50 FPS
    frame_counter += 1
    if frame_counter == 3:
        bg.move(-1,0)
        if bg.getAnchor().getX() == 0:
            bg.move(500,-1)
        frame_counter = 0
