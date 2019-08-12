from screen import Close_window , Get_Input_xy , Put_Output_xy , Show_Result
from math import floor
# ignore the print() are for debugging
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
    for i in range(0,3):
        if ((a[i][0] == a[i][1]) and (a[i][1]==a[i][2]) and (a[i][0] != -1)):
            print(str(i)+" (a[i][0] == a[i][1]) and (a[i][1]==a[i][2]) ")
            return 1
        if ((a[0][i] == a[1][i]) and (a[1][i]==a[2][i]) and (a[0][i] != -1)):
            print("i="+str(i)+" (a[0][i] == a[1][i]) and (a[1][i]==a[2][i]) ")
            return 1
        
    if ((a[0][0] == a[1][1]) and (a[1][1]==a[2][2]) and (a[0][0] != -1)):
        print("Diagonal")
        return 1
    if ((a[0][2] == a[1][1]) and (a[1][1]==a[2][0]) and (a[0][2] != -1)):
        print("Anti-Diagonal")
        return 1
    
    for i in range(0,3):
        for j in range(0,3):
                if a[i][j]==-1:
                    return 0
    
    print("Draw")
    return 2

for i in range(0,2):
    print(i)
a = [[-1,-1,-1],
    [-1,-1,-1],
    [-1,-1,-1]]
flag = 0
p = 0
chk = 0
while flag != 1:
    pt = Get_Input_xy(p)
    x,y = process_xy(int(pt.getX()),int(pt.getY()))
    if (x != -1) & (y != -1):
        if(a[y][x] == -1):
            a[y][x] = p
            Put_Output_xy(x,y,p)
            chk = check_game(a)
            if chk==1 or chk==2:
                Show_Result(p,chk)
                flag = 1
            p += 1
            if(p > 1):
                p = 0
    
print(a[0])
print(a[1])
print(a[2])
Close_window()