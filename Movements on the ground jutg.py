
from easyinput import read

l = read (chr)
x = 0
y = 0
while l is not None :
    if (l == "n"):
        y = (y-1)
    if (l == "s"):
        y = (y+1)
    if (l == "w"):
        x = (x-1)
    if (l == "e"):
        x = (x+1)
    l = read(chr)
    
print("(", x,", ", y, ")")