import math
from random import randint
from PIL import Image, ImageDraw

class vec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def add(self, a):
		return vec2(a.x + self.x, a.y + self.y)
	def sub(self, a):
		return vec2(a.x - self.x, a.y - self.y)
	def length(self):
		return math.sqrt(self.x * self.x + self.y * self.y)

def makeImage(width, height):
	im = Image.new('RGBA', (width, height), (0, 0, 0, 255)) # Create a blank image
	return im

def plotPoint(im, draw, x, y):
	final = [0, 0, 0, 255]
	pos = vec2(x, y)
	center = vec2(150, 150)
	dist = center.sub(pos)
	v = 255 - abs(int(dist.length()))
	final[1] = int(v)
	draw.line((x, y, x, y), tuple(final), 1)

im = makeImage(300, 300)
draw = ImageDraw.Draw(im)

for x in range(0, 300):
	for y in range(0, 300):
		plotPoint(im, draw, y, x)

im.save('fakeShader.png')