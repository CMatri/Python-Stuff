import math
from random import randint
from PIL import Image, ImageDraw

def makeImage(width, height):
	im = Image.new('RGBA', (width, height), (0, 0, 0, 255)) # Create a blank image
	return im

def plotPoint(im, draw, x, y):
	final = [0, 0, 0, 0]
	base = (6, 255, 6, 255)
	col = im.getpixel((x, y))
	for i in range(len(base)):
		final[i] = base[i] + col[i]
	draw.line((x, y, x, y), tuple(final), 1)

im = makeImage(300, 300)
draw = ImageDraw.Draw(im)

for x in range(0, 300):
	for y in range(0, 300):
		print(str(x) + " : " + str(y))
		plotPoint(im, draw, x, y)
		for a in range(int(x/10)):
			plotPoint(im, draw, x, y)

im.save('additive.png')