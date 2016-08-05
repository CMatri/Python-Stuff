import pygame

width = 1080
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
done = False

blocks = 10

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	clock.tick(60)
	screen.fill((80, 80, 80))

	for x in range(0, blocks):
		pygame.draw.line(screen, (255, 255, 255), (x * (width / blocks), 0), (x * (width / blocks), height))

	pygame.display.flip()
