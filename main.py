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
        x = 3
    
    if y<250:
        y = 1
    elif y<350:
        y = 2
    else:    
        y = 3
    
else:
    print("Invalid")
