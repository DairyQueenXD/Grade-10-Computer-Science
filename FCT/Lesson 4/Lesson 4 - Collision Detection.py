from graphics import *

win = GraphWin("Lesson 4",500,500,autoflush = False)

# Game States
# 0: In Game State
# 1: Game Over State
gamestate = 0

# Image Importation
ninja = Image(Point(25,25),"ninja.png")
enemy1 = Image(Point(250,250),"enemy.png")
enemy2 = Image(Point(100,400),"enemy.png")
enemy3 = Image(Point(300,50),"enemy.png")
gameover = Image(Point(250,250),"gameover.png")

enemy1.draw(win)
enemy2.draw(win)
enemy3.draw(win)
ninja.draw(win)

while True:
    update()
    time.sleep(0.02) # 50 FPS
    k = win.checkKey()
    posX = ninja.getAnchor().getX()
    posY = ninja.getAnchor().getY()
    enemy1X = enemy1.getAnchor().getX()
    enemy1Y = enemy1.getAnchor().getY()
    enemy2X = enemy2.getAnchor().getX()
    enemy2Y = enemy2.getAnchor().getY()
    enemy3X = enemy3.getAnchor().getX()
    enemy3Y = enemy3.getAnchor().getY()
    
    if gamestate == 0:
        if k == "w":
            ninja.move(0,-4)
        if k == "a":
            ninja.move(-4,0)
        if k == "s":
            ninja.move(0,4)
        if k == "d":
            ninja.move(4,0)

    ## Collision Detection
        
        if not(posX+25 <= enemy1X-25 or posX-25>=enemy1X+25 or posY+25<=enemy1Y-25 or posY-25>=enemy1Y+25):
            ninja.undraw()
            enemy1.undraw()
            enemy2.undraw()
            enemy3.undraw()
            gameover.draw(win)
            gamestate = 1
        elif not(posX+25 <= enemy2X-25 or posX-25>=enemy2X+25 or posY+25<=enemy2Y-25 or posY-25>=enemy2Y+25):
            ninja.undraw()
            enemy1.undraw()
            enemy2.undraw()
            enemy3.undraw()
            gameover.draw(win)
            gamestate = 1
        elif not(posX+25 <= enemy3X-25 or posX-25>=enemy3X+25 or posY+25<=enemy3Y-25 or posY-25>=enemy3Y+25):
            ninja.undraw()
            enemy1.undraw()
            enemy2.undraw()
            enemy3.undraw()
            gameover.draw(win)
            gamestate = 1
            
    elif gamestate == 1:
        if k!= "":
            gamestate = 0
            gameover.undraw()
            ninja.move(25-posX,25-posY)
            enemy1.draw(win)
            enemy2.draw(win)
            enemy3.draw(win)
            ninja.draw(win)
            
