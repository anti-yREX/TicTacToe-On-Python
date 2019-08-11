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

def check_game(a):
    n = 0
    for i in range(0,2):
        if a[i][0] == a[i][1] == a[i][2] != -1:
            print(str(i)+" a[i][0] == a[i][1] == a[i][2] != -1:")
            n = 1
            break
        if a[0][i] == a[1][i] == a[2][i] != -1:
            print(str(i)+" a[0][i] == a[1][i] == a[2][i] != -1:")
            n = 1
            break
    if a[0][0] == a[1][1] == a[2][2] != -1:
        print("Cross 1")
        n = 1
    if a[2][0] == a[1][1] == a[0][2] != -1:
        print("Cross 2")
        n = 1
    
    if n==0:
        n=2
        for i in range(0,2):
            for j in range(0,2):
                if a[i][j]==-1:
                    return 0
    
    if n==2:
        print("Draw")        
    return n

a = [[-1,-1,-1],
    [-1,-1,-1],
    [-1,-1,-1]]
flag = 0
p = 0
while flag != 1:
    pt = Get_Input_xy(p)
    x,y = process_xy(int(pt.getX()),int(pt.getY()))
    if (x != -1) & (y != -1):
        if(a[y][x] == -1):
            a[y][x] = p
            Put_Output_xy(x,y,p)
            chk = check_game(a)
            if chk!=0:
                Show_Result(p,chk)
                flag = 1
            p += 1
            if(p > 1):
                p = 0
    
print(a[0])
print(a[1])
print(a[2])
Close_window()
