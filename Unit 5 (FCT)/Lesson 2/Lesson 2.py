# This lesson is about sprite animation

from graphics import *

win = GraphWin("Lesson 2 - Sprite Animation",500,500,autoflush = False)

## Image Importation

pikachustart = Image(Point(250,250),"pikachustart.png")
pikachubg = Image(Point(250,250),"pikachuBG.png")
gameover = Image(Point(250,250),"gameover.png")

pikachuX = 250
pikachuY = 340
spriteNum = 0
frameNum = 0

pikachu = [Image(Point(pikachuX,pikachuY),"pikachu0.png"),
           Image(Point(pikachuX,pikachuY),"pikachu1.png"),
           Image(Point(pikachuX,pikachuY),"pikachu2.png"),
           Image(Point(pikachuX,pikachuY),"pikachu3.png")]
## Game state variable
# 0 : Start Screen
# 1 : Game State
# 2 : Game Over Screen
gamestate = 0

pikachustart.draw(win)

while True:
    update()
    time.sleep(0.02) # 50 FPS
    k = win.checkKey()
    
    if gamestate == 0: # Start Screen
        if k == "space": # Spacebar detection
            gamestate = 1
            pikachustart.undraw()
            pikachubg.draw(win)
            pikachu[spriteNum].draw(win)
            
    elif gamestate == 1: # Game State
        frameNum += 1
        if frameNum == 4:
            pikachu[spriteNum].undraw()
            spriteNum += 1
            ## Sprite Number Reset
            if spriteNum == 4:
                spriteNum = 0
            pikachu[spriteNum].draw(win)
            frameNum = 0
        if k == "a": # Move pikachu left
            for p in pikachu: # Move all the sprites to left
                p.move(-3,0)
        if k == "d":
            for p in pikachu:
                p.move(3,0)
        if k == "g": # "g" key detection
            gamestate = 2
            pikachubg.undraw()
            pikachu[spriteNum].undraw()
            gameover.draw(win)

    elif gamestate == 2: # Game Over Screen
        if k != "": # Check for any key detectiion
            gamestate = 0
            gameover.undraw()
            pikachustart.draw(win)
        
