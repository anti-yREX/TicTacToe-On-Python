from screen import Close_window , Get_Input_xy , Put_Output_xy , Show_Result , Restart_Game , Initialize
from logic import process_xy , check_game

close = 0
while close != 1:
    Initialize()
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
    close = Restart_Game()
Close_window()