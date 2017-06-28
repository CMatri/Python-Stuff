from PIL import Image, ImageDraw
from colorama import init, deinit, Fore, Back, Style
import requests
from io import BytesIO

init()

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

def getGrayscale(value, invert):
    if invert:
        return toUse[(value * factor) / 255]
    else:
        return toUse[factor - (value * factor) / 255]

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

imi = Image.open("mountains.jpg")
#response = requests.get("https://i.redditmedia.com/-MFLOPiLFGqTt3ntpc5GTyofdxuGhUXwlHvZjhnnxTY.jpg?w=920&s=b92e20bc74aabafcd6711d09f7c13992")
#imi = Image.open(BytesIO(response.content))
im = imi.convert("RGB")
width, height = im.size
x, y = 0, 0

text_file = open("Output.txt", "w")
line = ""

incX = 8
incY = 16

while y < height:
    while x < width:
        r, g, b = im.getpixel((x, y))
        final = getAverage(x, y, incX, incY, width, height, im) #(r + g + b) / 3;
        line += getGrayscale(final, False)
        x = x + incX
    y = y + incY
    x = 0
    text_file.write("%s\n" % line)
    print("    " + line)
    line = ""

im.close()
text_file.close()
deinit()
