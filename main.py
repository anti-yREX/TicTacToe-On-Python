from screen import Close_window , Get_Input_xy , Put_Output_xy , Show_Result
from math import floor

def process_xy(x,y):
    if(100 < x < 400) & (150 < y < 450):
        x = x - 100
        x = floor(x/100)
        y = y - 150
        y = floor(y/100)
        return x , y
    else:
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
    
print(a[0])
print(a[1])
print(a[2])
Close_window()
