from PIL import Image, ImageDraw

characters = [ "#", "#", "@", "%", "=", "+", "*", ":", "-", ".", " " ]

def getGrayscale(value, invert):
    if invert:
        return characters[(value * 10) / 255]
    else:
        return characters[10 - (value * 10) / 255]

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

im = Image.open("obama.jpg")
width, height = im.size
x, y = 0, 0

text_file = open("Output.txt", "w")
line = ""

incX = 3
incY = 5

while y < height:
    while x < width:
        r, g, b = im.getpixel((x, y))
        final = getAverage(x, y, incX, incY, width, height, im)#(r + g + b) / 3;
        line += getGrayscale(final, False)
        x = x + incX
    y = y + incY
    x = 0
    text_file.write("%s\n" % line)
    print(line)
    line = ""

im.close()
text_file.close()
