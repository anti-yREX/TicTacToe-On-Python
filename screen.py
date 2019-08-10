from graphics import *
win = GraphWin("GAME",500,500)
#rect = Rectangle(Point(0,100),Point(500,500))
x = 100
y = 150
line = Line(Point(x+100 , 164) , Point(x+100 , y+300))
line.setWidth(5)
line.draw(win)

line = Line(Point(x+200 , 164) , Point(x+200 , y+300))
line.setWidth(5)
line.draw(win)

line = Line(Point(x , y+100) , Point(x+300,y+100))
line.setWidth(5)
line.draw(win)

line = Line(Point(x , y+200) , Point(x+300,y+200))
line.setWidth(5)
line.draw(win)
#182,(164 + 100 + 100)
win.getMouse()
win.close()