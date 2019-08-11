from graphics import *

win = GraphWin("GAME",500,550)

blue = "#0099ff"
blue_d = "#0000ff" 

red = "#ff3000"
red_d = "#ff0000"

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

rect  = Rectangle(Point(75,45),Point(425,115))
rect.setFill(blue)
rect.draw(win)

text = Text(Point(250,80),"TEXT")
text.setSize(30)
text.setStyle("bold")
text.setText("X")
text.draw(win)

def Close_window():
    pt = win.getMouse()
    print(str(pt.getX)+"  "+str(pt.getY))
    win.close()
    return pt