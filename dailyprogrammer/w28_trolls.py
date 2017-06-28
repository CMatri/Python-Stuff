from random import randint
from getch import getch
import os

m = list("""
#######################################
#######################################
## #       #       #     #         # ##
## # ##### # ### ##### ### ### ### # ##
##       #   # #     #     # # #   # ##
###### # ##### ##### ### # # # ##### ##
##   # #       #     # # # # #     # ##
## # ####### # # ##### ### # ##### # ##
## #       # # #   #     #     #   # ##
## ####### ### ### # ### ##### # ### ##
##     #   # #   # #   #     # #     ##
## ### ### # ### # ##### # # # ########
##   #   # # #   #   #   # # #   #   ##
######## # # # ##### # ### # ### ### ##
##     # #     #   # #   # #   #     ##
## ### # ##### ### # ### ### ####### ##
## #   #     #     #   # # #       # ##
## # ##### # ### ##### # # ####### # ##
## #     # # # # #     #       # #   ##
## ##### # # # ### ##### ##### # ######
## #   # # #     #     # #   #       ##
## # ### ### ### ##### ### # ##### # ##
## #         #     #       #       # ##
##X####################################
#######################################""")

width = 40
height = 25
pos = [i for i, c in enumerate(m) if c == " "][randint(0, m.count(" ") - 1)]
m[pos] = 'P'
x, y = pos % width, pos / width
old = " "
os.system('cls' if os.name == 'nt' else 'clear')
print "".join(m)

while getch() == "\033":
    getch()
    m[y * width + x] = old
    c = map(sum, zip((x, y), {'A': (0, -1), 'B': (0, 1), 'C': (1, 0), 'D': (-1, 0)}.get(getch())))
    n = m[c[1] * width + c[0]]
    if n == "X":
        print "You win!"
        break
    else:
        x, y = c if n == " " else (x, y)
    i = y * width + x
    old = m[i]
    m[i] = "P"
    os.system('cls' if os.name == 'nt' else 'clear')
    print "".join(m)