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
    for i in range(0,3):
        if (a[i][0] == a[i][1] == a[i][2] != -1):
            print(str(i)+" (a[i][0] == a[i][1]) and (a[i][1]==a[i][2]) ")
            return 1
        if (a[0][i] == a[1][i] == a[2][i] != -1):
            print("i="+str(i)+" (a[0][i] == a[1][i]) and (a[1][i]==a[2][i]) ")
            return 1
        
    if (a[0][0] == a[1][1] == a[2][2] != -1):
        print("Diagonal")
        return 1
    if (a[2][0] == a[1][1] == a[0][2] != -1):
        print("Anti-Diagonal")
        return 1
    
    for i in range(0,3):
        for j in range(0,3):
                if a[i][j]==-1:
                    return 0
    
    print("Draw")
    return 2