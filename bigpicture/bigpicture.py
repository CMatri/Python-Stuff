import sys
import os
import cv2
import curses
from PIL import Image, ImageDraw

charactersOld = [ "#",
		"#",
		"@",
		"%",
		"=",
		"+",
		"*",
		":",
		"-",
		".",
		" " ]

characters = [
		"@",
		"N",
		"%",
		"Q",
		"&",
		"W",
		"M",
		"g",
		"m",
		"$",
		"0",
		"B",
		"D",
		"R",
		"H",
		"#",
		"8",
		"d",
		"O",
		"b",
		"U",
		"A",
		"q",
		"h",
		"G",
		"w",
		"K",
		"p",
		"X",
		"k",
		"9",
		"V",
		"6",
		"P",
		"]",
		"E",
		"y",
		"u",
		"n",
		"[",
		"4",
		"1",
		"o",
		"j",
		"a",
		"e",
		"2",
        "S",
		"5",
		"Y",
		"f",
		"Z",
		"x",
		"(",
		"l",
		"I",
		")",
		"F",
		"3",
		"{",
		"C",
		"t",
		"J",
		"v",
		"i",
		"T",
		"7",
		"s",
		"r",
		"z",
		"\\",
		"L",
		"c",
		"/",
		"?",
		"*",
		"!",
		"+",
		"<",
		";",
		"^",
		"=",
		"\"",
		".",
		":",
		"_",
		"'",
		".",
		"-",
		"`",
		" "
        ]

toUse = charactersOld
factor = len(toUse) - 1

def createCurses(width, height):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)

    begin_x = 0#20
    begin_y = 0#7
    height = height#5
    width = width#40
    win = curses.newwin(height, width, begin_y, begin_x)
    return stdscr

def getGrayscale(value, invert):
    if invert:
        return toUse[int((value * factor) / 255)]
    else:
        return toUse[int(factor - (value * factor) / 255)]

def getAverage(x, y, amX, amY, width, height, im):
    val = 0
    amt = 0
    for x1 in range(x, x + amX):
        for y1 in range(y, y + amY):
            if x1 < width and y1 < height:
                r, g, b = im.getpixel((x1, y1))
                val += (r + g + b) / 3
                amt += 1
    if amt != 0:
        val = val / amt
        return val
    else:
        return 0

dire = "./";
created_curses = False
vidcap = cv2.VideoCapture(sys.argv[1]);#'vid2.mp4')

if not os.path.isdir("./%s" % dire):
    os.mkdir(dire)

count = 0;

stdscr = None
c = ''

while count < int(sys.argv[2]):
    success,image = vidcap.read()
    cv2_im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im)
    im = pil_im.convert("RGB")

    width, height = im.size
    x, y = 0, 0
    line = ""
    incX = 4
    incY = 8

    if not created_curses:
        created_curses = True
        stdscr = createCurses(int(width / incX), int(height / incY))

    stdscr.refresh()

    while y < height:
        while x < width:
            stdscr.addstr(0,0, "tests! " + str(10), curses.A_STANDOUT)
            stdscr.refresh()
            c = stdscr.getch()
            if c == ord('p'):
                break
            r, g, b = im.getpixel((x, y))
            final = getAverage(x, y, incX, incY, width, height, im) #(r + g + b) / 3;
            line += getGrayscale(final, False)
            x = x + incX
        y = y + incY
        x = 0
        stdscr.addstr(0,0, "RED ALERT!", curses.A_STANDOUT)
        line = ""
        if c == ord('p'):
            break

    im.close()
    count += 1
    if c == ord('p'):
        break

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

# get her back by writing out a story about wishing we could start from the beginning, me trying to 'woo' a girl i didnt know
