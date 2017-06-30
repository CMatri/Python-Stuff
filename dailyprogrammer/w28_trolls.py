from Queue import Queue
from random import randint
from getch import getch
import os
import time

m = list("""
#########################################################################
#   #               #               #           #                   #   #
#   #   #########   #   #####   #########   #####   #####   #####   #   #
#               #       #   #           #           #   #   #       #   #
#########   #   #########   #########   #####   #   #   #   #########   #
#       #   #               #           #   #   #   #   #           #   #
#   #   #############   #   #   #########   #####   #   #########   #   #
#   #               #   #   #       #           #           #       #   #
#   #############   #####   #####   #   #####   #########   #   #####   #
#           #       #   #       #   #       #           #   #           #
#   #####   #####   #   #####   #   #########   #   #   #   #############
#       #       #   #   #       #       #       #   #   #       #       #
#############   #   #   #   #########   #   #####   #   #####   #####   #
#           #   #           #       #   #       #   #       #           #
#   #####   #   #########   #####   #   #####   #####   #############   #
#   #       #           #           #       #   #   #               #   #
#   #   #########   #   #####   #########   #   #   #############   #   #
#   #           #   #   #   #   #           #               #   #       #
#   #########   #   #   #   #####   #########   #########   #   #########
#   #       #   #   #           #           #   #       #               #
#   #   #####   #####   #####   #########   #####   #   #########   #   #
# X #                   #           #               #               #   #
#########################################################################""")
mSearch = m[:]

def aStar(current, end):
    openList = [0xFFFFFFFF] * len(mSearch)
    closedList = [False] * len(mSearch)
    path = []
    came_from = [None] * len(mSearch)

    def retracePath(c):
        path.insert(0, c)
        if came_from[c] == None:
            return
        retracePath(came_from[c])
    print current
    openList[current] = 0
    while openList:
        current = openList.index(min(openList))
        print openList[current]
        if current == 0 : exit()
        if current == end:
            return retracePath(current)
        openList[current] = 0xFFFFFFFF
        closedList[current] = True
        for tile in [current + 1, current - 1, current + width, current - width]:
            if closedList[tile] and m[tile] != "#":
                openList[tile] = (abs(end % width - tile % width) + abs(end / width - tile / width)) * 10
                if openList[tile] == None:
                    came_from[tile] = current
                    openList[tile] = (abs(end % width - tile % width) + abs(end / width - tile / width)) * 10
    return path

def path(start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = [None] * len(mSearch)
    came_from[start] = None
    current = start

    while not frontier.empty():
        if current == goal: break
        current = frontier.get()
        for n in [current + 1, current - 1, current + width, current - width]:
            if mSearch[n] != "#" and came_from[n] == None:
                frontier.put(n)
                came_from[n] = current
    current = goal
    path = [current]
    current = frontier.get()
    while current != start:
        current = came_from[current]
        path.append(current)
    return path

def render():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "".join(m)

width = 74
height = 23
pos = [i for i, c in enumerate(m) if c == " "][randint(0, m.count(" ") - 1)]
m[pos] = 'P'
x, y = pos % width, pos / width
trolls = [0] * 2
for j in range(len(trolls)): trolls[j] = [i for i, c in enumerate(m) if c == " "][randint(0, m.count(" ") - 1)]
old = [" "] * (len(trolls) + 1)
render()

while getch() == "\033":
    getch()
    m[y * width + x] = old[0]
    c = map(sum, zip((x, y), {'A': (0, -1), 'B': (0, 1), 'C': (1, 0), 'D': (-1, 0)}.get(getch())))
    aheadI = ((c[1] - y) * 2 + y) * width + ((c[0] - x) * 2 + x)
    n = m[c[1] * width + c[0]]
    if n == "X":
        print "You win!"
        break
    elif n == "#" and aheadI % width < width - 1 and aheadI % width > 1 and aheadI / width > -1 and aheadI / width < height and m[aheadI] != "#":
        m[aheadI], mSearch[aheadI] = "#", "#"
        m[c[1] * width + c[0]], mSearch[c[1] * width + c[0]] = " ", " "
    elif n != "#":
        x, y = c
    i = y * width + x
    old[0] = m[i]
    p = path(i, m.index("X"))
    for aj in p:
        if m[aj] == "X": continue
        m[aj] = "V"
        time.sleep(0.001)
        render()
    #la = aStar(i, m.index("X"))
    #for t in range(len(trolls)):
    #    p = path(i, trolls[t])
    #    m[trolls[t]] = old[t + 1]
    #    trolls[t] = p[1]
    #    old[t + 1] = m[trolls[t]]
    #    m[trolls[t]] = "T"
    m[i] = "P"

    render()
