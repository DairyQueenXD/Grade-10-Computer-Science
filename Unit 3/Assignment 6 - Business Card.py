from graphics import *

win1 = GraphWin("Business Card Front", 1050, 600)
win1.setBackground(color_rgb(0,43,9))

win2 = GraphWin("Business Card Back", 1050, 600)
win2.setBackground(color_rgb(0,43,9))

p1 = Point(750,162.5)
p2 = Point(800,600)
rec = Rectangle(p1,p2)
rec.setFill(color_rgb(211,167,79))
rec.setOutline(color_rgb(0,43,9))
rec.draw(win1)

p3 = Point(825,162.5)
p4 = Point(875,600)
rec1 = Rectangle(p3,p4)
rec1.setFill(color_rgb(211,167,79))
rec1.setOutline(color_rgb(0,43,9))
rec1.draw(win1)

triangle1 = Polygon(Point(750,162.5),Point(800,162.5),Point(800,212.5))
triangle1.setFill(color_rgb(0,43,9))
triangle1.setOutline(color_rgb(0,43,9))
triangle1.draw(win1)

triangle2 = Polygon(Point(875,162.5),Point(825,162.5),Point(825,212.5))
triangle2.setFill(color_rgb(0,43,9))
triangle2.setOutline(color_rgb(0,43,9))
triangle2.draw(win1)

rec2 = Rectangle(Point(0,535),Point(750,555))
rec2.setFill(color_rgb(211,167,79))
rec2.setOutline(color_rgb(211,167,79))
rec2.draw(win1)

rec3 = Rectangle(Point(875,535),Point(1050,555))
rec3.setFill(color_rgb(211,167,79))
rec3.setOutline(color_rgb(211,167,79))
rec3.draw(win1)

square1 = Rectangle(Point(100,62.5),Point(200,162.5))
square1.setFill(color_rgb(211,167,79))
square1.setOutline(color_rgb(0,43,9))
square1.draw(win1)

square2 = Rectangle(Point(115,77.5),Point(185,147.5))
square2.setFill(color_rgb(0,43,9))
square2.setOutline(color_rgb(0,43,9))
square2.draw(win1)

square3 = Rectangle(Point(185,107.5),Point(200,117.5))
square3.setFill(color_rgb(0,43,9))
square3.setOutline(color_rgb(0,43,9))
square3.draw(win1)

name = Text(Point(810,70),"Dequan Kong")
name.setFill(color_rgb(255,255,255))
name.setStyle("bold")
name.setSize(36)
name.setFace("arial")
name.draw(win1)

position = Text(Point(815,130),"Founder")
position.setFill(color_rgb(255,255,255))
position.setStyle("italic")
position.setSize(24)
position.setFace("helvetica")
position.draw(win1)

c1 = Circle(Point(120,275),15)
c1.setFill(color_rgb(255,255,255))
c1.setOutline(color_rgb(255,255,255))
c1.draw(win1)

c2 = Circle(Point(120,275),5)
c2.setFill(color_rgb(0,43,9))
c2.setOutline(color_rgb(0,43,9))
c2.draw(win1)

triangle3 = Polygon(Point(110,285),Point(130,285),Point(120,302))
triangle3.setFill(color_rgb(255,255,255))
triangle3.setOutline(color_rgb(255,255,255))
triangle3.draw(win1)

location = Text(Point(310,285),"1000 Carlton Rd, Unionville, ON L3P 7P5")
location.setStyle("bold")
location.setFill(color_rgb(255,255,255))
location.draw(win1)

rec4 = Rectangle(Point(107,320),Point(130,367))
rec4.setFill(color_rgb(255,255,255))
rec4.setOutline(color_rgb(255,255,255))
rec4.draw(win1)

rec5 = Rectangle(Point(112,325),Point(125,350))
rec5.setFill(color_rgb(0,43,9))
rec5.setOutline(color_rgb(0,43,9))
rec5.draw(win1)

c3 = Circle(Point(118.25,359),5)
c3.setFill(color_rgb(0,43,9))
c3.setOutline(color_rgb(0,43,9))
c3.draw(win1)

phone = Text(Point(207,345),"666-666-6666")
phone.setStyle("bold")
phone.setFill(color_rgb(255,255,255))
phone.draw(win1)

rec6 = Rectangle(Point(100,385),Point(137,412))
rec6.setFill(color_rgb(255,255,255))
rec6.setOutline(color_rgb(255,255,255))
rec6.draw(win1)

diag1 = Line(Point(100,385),Point(137,412))
diag1.setFill(color_rgb(0,43,9))
diag1.setWidth(1.5)
diag1.draw(win1)

diag2 = Line(Point(137,385),Point(100,412))
diag2.setFill(color_rgb(0,43,9))
diag2.setWidth(2)
diag2.draw(win1)

email = Text(Point(223,400),"email@gmail.com")
email.setFill(color_rgb(255,255,255))
email.setStyle("bold")
email.draw(win1)

x = 5

triangle = Polygon(Point(97,430+x),Point(101,455+x),Point(125,433+x))
triangle.setFill(color_rgb(255,255,255))
triangle.draw(win1)

rec7 = Polygon(Point(107,448+x),Point(118,439+x),Point(140,455+x),Point(132,465+x))
rec7.setFill(color_rgb(255,255,255))
rec7.setOutline(color_rgb(255,255,255))
rec7.draw(win1)

website = Text(Point(261,452),"www.eliteexpeditioners.com")
website.setFill(color_rgb(255,255,255))
website.setStyle("bold")
website.draw(win1)

x = 375
y = 130

square4 = Rectangle(Point(100+x,62.5+y),Point(200+x,162.5+y))
square4.setFill(color_rgb(211,167,79))
square4.setOutline(color_rgb(0,43,9))
square4.draw(win2)

square5 = Rectangle(Point(115+x,77.5+y),Point(185+x,147.5+y))
square5.setFill(color_rgb(0,43,9))
square5.setOutline(color_rgb(0,43,9))
square5.draw(win2)

square6 = Rectangle(Point(185+x,107.5+y),Point(200+x,117.5+y))
square6.setFill(color_rgb(0,43,9))
square6.setOutline(color_rgb(0,43,9))
square6.draw(win2)

x = 375
y = 133

companyName = Text(Point(140+x,225+y),"Elite Expeditioners")
companyName.setStyle("bold")
companyName.setFill(color_rgb(255,255,255))
companyName.setSize(36)
companyName.draw(win2)

x = -288
y = 275
z = 275
p1 = Point(750+x,162.5+y)
p2 = Point(800+x,600+y)
rec = Rectangle(p1,p2)
rec.setFill(color_rgb(211,167,79))
rec.setOutline(color_rgb(0,43,9))
rec.draw(win2)

p3 = Point(825+x,162.5+y)
p4 = Point(875+x,600+y)
rec1 = Rectangle(p3,p4)
rec1.setFill(color_rgb(211,167,79))
rec1.setOutline(color_rgb(0,43,9))
rec1.draw(win2)

triangle1 = Polygon(Point(750+x,162.5+y),Point(800+x,162.5+y),Point(800+x,212.5+y))
triangle1.setFill(color_rgb(0,43,9))
triangle1.setOutline(color_rgb(0,43,9))
triangle1.draw(win2)

triangle2 = Polygon(Point(875+x,162.5+y),Point(825+x,162.5+y),Point(825+x,212.5+y))
triangle2.setFill(color_rgb(0,43,9))
triangle2.setOutline(color_rgb(0,43,9))
triangle2.draw(win2)

y = z + 20
rec10 = Rectangle(Point(0,162.5+25+y),Point(750+x,162.5+40+y))
rec10.setFill(color_rgb(211,167,79))
rec10.setOutline(color_rgb(211,167,79))
rec10.draw(win2)

y = z + 20
rec11 = Rectangle(Point(825+x+5,162.5+25+y),Point(1050,162.5+40+y))
rec11.setFill(color_rgb(211,167,79))
rec11.setOutline(color_rgb(211,167,79))
rec11.draw(win2)
