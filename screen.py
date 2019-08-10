from graphics import *
win = GraphWin()
win.setBackground("White")
r = 50
center = Point(89,90)
center.setFill("White")
cir = Circle(center,r)
cir.setFill("black")
cir.draw(win)

for i in range(0 , 100):
    for j in range(0 , 50):
        pt = Point(39+i , 40+j)
        pt.setFill("White")
        pt.draw(win)
        j += 1
    i += 1

for i in range(0 , 26):
    for j in range(0 , 26):
        pt = Point(50+i , 50+j)
        pt.draw(win)
        j += 1
    i += 1


for i in range(0 , 26):
    for j in range(0 , 26):
        pt = Point(100+i , 50+j)
        pt.draw(win)
        j += 1
    i += 1

win.getMouse()
win.close()