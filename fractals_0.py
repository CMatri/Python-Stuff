import time
import pygame
import sys

pygame.init()
dim = (1920, 1080)
screen = pygame.display.set_mode(dim)
running = True

def drawCircle(x, y, radius):
    print (max(min(float(x * y) / float(dim[0] * dim[1]) * 255, 255), 0), max(min(int(y / float(dim[1]) * 255.0), 255), 1), max(min(int(x / float(dim[0]) * 255.0), 255), 1))
    pygame.draw.circle(screen, (max(min(float(x * y) / float(dim[0] * dim[1]) * 255, 255), 1), max(min(int(y / float(dim[1]) * 255.0), 255), 1), max(min(int(x / float(dim[0]) * 255.0), 255), 1)), (int(x), int(y)), int(radius), 1)
    if radius > 1:
        drawCircle(x + radius, y, radius / 2)
        drawCircle(x - radius, y, radius / 2)
        drawCircle(x, y + radius, radius / 2)
        drawCircle(x, y - radius, radius / 2)
        #time.sleep(0.0000001)
        pygame.display.update()

try:
    screen.fill((255, 255, 255))
    drawCircle(dim[0] / 2, dim[1] / 2, 500)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()
except SystemExit:
    pygame.quit()
