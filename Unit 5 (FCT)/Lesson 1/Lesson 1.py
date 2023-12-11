# This lesson is about game states transition
""" Game states
- Menu Screen -> option button, start button, credits button
- If you press options, you go to another state (Option Screen)
- When press button, erase everything and redraw
- Game state diagram : diagram that shows how game states are related """

from graphics import *

window = GraphWin("Lesson 1 - Game States Transition",500,500)

# Game State Variable
# 0: Menu / Start Screen
# 1: Credit Screen
# 2: In Game Screen
# 3: Game Over Screen
# 4: Win Screen

gamestate = 0

# Image Importation
start = Image(Point(250,250),"start.png")
credit = Image(Point(250,250),"credit.png")
ingame = Image(Point(250,250),"ingame.png")
gameover = Image(Point(250,250),"gameover.png")
win = Image(Point(250,250),"win.png")

# We are in GS 0, so we start the program by drawing the start screen
start.draw(window)
while True:
    time.sleep(0.02) # 50 FPS
    k = window.checkKey()
    m = window.checkMouse()

    if gamestate == 0:
        if m != None:
            x = m.getX()
            y = m.getY()
            if 150 <= x <= 350 and 300 <= y <= 350: # Start Button
                gamestate = 2
                start.undraw()
                ingame.draw(window) 
            if 150 <= x <= 350 and 400 <= y <= 450: # Credit Button
                gamestate = 1
                start.undraw()
                credit.draw(window)
    elif gamestate == 1:
        if k == "space":
            gamestate = 0
            credit.undraw()
            start.draw(window)
    elif gamestate == 2:
        if k == "g":
            gamestate = 3
            ingame.undraw()
            gameover.draw(window)
        if k == "w":
            gamestate = 4
            ingame.undraw()
            win.draw(window)
    elif gamestate == 3:
        if m != None:
            gamestate = 0
            gameover.undraw()
            start.draw(window)
    elif gamestate == 4:
        if m != None:
            gamestate = 0
            win.undraw()
            start.draw(window)
    
