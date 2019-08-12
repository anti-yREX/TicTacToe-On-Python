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

<<<<<<< HEAD
<<<<<<< HEAD
def Get_Input_xy(n):
    if n==0:
        c = red
        stri = "X"
    if n==1:
        c = blue
        stri = "O"
    rect  = Rectangle(Point(75,45),Point(425,115))
    rect.setFill(c)
    rect.draw(win)
    text = Text(Point(250,80),stri)
    text.setSize(30)
    text.setStyle("bold")
    text.draw(win)
    pt = win.getMouse()
    return pt

def Put_Output_xy(x,y,n):
    x = (100*x)+150
    y = (100*y)+200
    if n == 0:
        c = red_d
        stri = "X"
    if n == 1:
        c = blue_d
        stri = "O"
    text = Text(Point(x,y),stri)
    text.setSize(30)
    text.setStyle("bold")
    text.setTextColor(c)
    text.draw(win)
    return

def Show_Result(n,chk):
    stri = ""
    c = ""
    if chk==1:
        if n == 0:
            c = red
            stri = "X has won!!"
        if n == 1:
            c = blue
            stri = "O has won!!"
    if chk==2:
        c = "#525252"
        stri = "it's a Draw!!"
    rect  = Rectangle(Point(75,45),Point(425,115))
    rect.setFill(c)
    rect.draw(win)
    text = Text(Point(250,80),stri)
    text.setSize(30)
    text.setStyle("bold")
    text.draw(win)
    return
    
=======
>>>>>>> parent of 2961eae... logic is all messed up
=======
>>>>>>> parent of 2961eae... logic is all messed up
def Close_window():
    pt = win.getMouse()
    print(str(pt.getX)+"  "+str(pt.getY))
    win.close()
    return pt