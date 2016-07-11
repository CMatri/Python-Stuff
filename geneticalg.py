import pygame
import math
from random import randint

class Bar():
    	def __init__(self, xpos, ypos, width, height):
	      	self.x = xpos
	      	self.y = ypos
	      	self.width = width
	      	self.height = height
	      	self.rot = 0

def make_bar(last_y, last_x):
	width = randint(20, 40)
	height = 5
	x = last_x
	y = last_y
	return Bar(x, y, width, height)

pygame.init()
width = 1080
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
done = False
bar_img = pygame.image.load('bar.png').convert()

cars = [make_bar(0, 0)] * 20
bars = [make_bar(100, 200)] * 50


for i in range(0, len(bars)):
	bars[i] = make_bar(randint(10, 900), randint(10, 900))
	bars[i].rot = math.degrees(randint(0, 360))

rot = 0

while not done:
	rot += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
	clock.tick(60)
	screen.fill((60, 60, 60))
	pygame.draw.circle(screen, (0, 0, 255), (20, 20), 5, 1)

	for b in bars:
		#bar_img = pygame.transform.scale(bar_img, (b.width, b.height))
		temp_img = pygame.transform.rotate(bar_img, rot)
		screen.blit(temp_img, (b.x, b.y))
		#screen.blit(pygame.transform.rotate(bar_img, b.rot), (b.x, b.y))
	
	pygame.display.flip()