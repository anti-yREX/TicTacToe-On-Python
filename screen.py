from graphics import *

win = GraphWin("GAME",500,550)
blue = "#5c9df7"
blue_d = "#0000ff" 

red = "#f7665c"
red_d = "#ff0000"

def Initialize():
    for item in win.items[:]:
        item.undraw()

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

    return

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
    
def Restart_Game():
    
    rect  = Rectangle(Point(25,475),Point(225,525))
    rect.setFill("#525252")
    rect.draw(win)
    text = Text(Point(125,500),"PLAY AGAIN!!")
    text.setSize(20)
    text.setStyle("bold")
    text.draw(win)

    rect  = Rectangle(Point(275,475),Point(475,525))
    rect.setFill("#525252")
    rect.draw(win)
    text = Text(Point(375,500),"CLOSE!!")
    text.setSize(20)
    text.setStyle("bold")
    text.draw(win)

    flag = 0
    while flag != 1:
        pt = win.getMouse()
        if (25 < int(pt.getX()) < 225 & 475 < int(pt.getY()) < 525):
            return 0
        if (275 < int(pt.getX()) < 475 & 475 < int(pt.getY()) <525):
            flag = 1
    return 1

def Close_window():
    win.close()
    return