from screen import Close_window
from math import floor

pt = Close_window()
x = pt.getX()
y = pt.getY()
a = [-1 ,-1]
if(100 < x < 400) & (150 < y < 450):
    if x<200:
        x = 1
    elif x<300:
        x = 2
    else:
<<<<<<< HEAD
        return -1,-1

def check_game(a,p):
    n = 0
    return n
    
a = [[-1,-1,-1],
    [-1,-1,-1],
    [-1,-1,-1]]
flag = 0
p = 0
m = 0
while flag != 1 & m < 9:
    pt = Get_Input_xy(p)
    x,y = process_xy(int(pt.getX()),int(pt.getY()))
    if (x != -1) & (y != -1):
        if(a[y][x] == -1):
            a[y][x] = p
            Put_Output_xy(x,y,p)
            m += 1
            """chk = check_game(a,p)
            if chk!=0:
                print(chk,p)
                Show_Result(p,chk)
                flag = 1"""
            p += 1
            if(p > 1):
                p = 0
=======
        x = 3
    
    if y<250:
        y = 1
    elif y<350:
        y = 2
    else:    
        y = 3
>>>>>>> parent of 2961eae... logic is all messed up
    
else:
    print("Invalid")
