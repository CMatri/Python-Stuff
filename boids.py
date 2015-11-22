import pygame
import math
import random

def calc_distance(x1, y1, x2, y2):
	return math.sqrt(((x2 - x1) ** 2.0) + ((y2 - y1) ** 2.0))

def len_vel(x, y):
	return math.sqrt(x ** 2 + y ** 2)

def get_ahead_vec(x, y, x_vel, y_vel, see_ahead):
	vlen = len_vel(x_vel, y_vel)
	nx_vel = x_vel / vlen
	ny_vel = y_vel / vlen
	ax = x + nx_vel * see_ahead
	ay = y + ny_vel * see_ahead
	return (ax, ay)

def lim_vel(boid, max_vel):
	val = math.sqrt(((boid.velX - 0.0) ** 2.0) + ((boid.velY - 0.0) ** 2.0))
	if val > max_vel:
		boid.velX = boid.velX * max_vel / val
		boid.velY = boid.velY * max_vel / val

def boid_line(boid, boid2, color = (0, 255, 0)):
	pygame.draw.line(screen, color, (boid.posX + 5, boid.posY + 5), (boid2.posX + 5, boid2.posY + 5))

class SphereObstacle(object):
	def __init__(self, rad, posX, posY):
		self.rad = rad
		self.posX = posX
		self.posY = posY

	def collides(self, boid):
		dist = math.sqrt(((boid.aheadX - self.posX) ** 2.0) + ((boid.aheadY - self.posY) ** 2.0))
		dist2 = math.sqrt(((boid.aheadX2 - self.posX) ** 2.0) + ((boid.aheadY2 - self.posY) ** 2.0))
		return dist < self.rad or dist2 < self.rad

class Boid(object):
	def __init__(self, posX, posY, velX, velY, rot, bound_rad, zombie):
		self.posX = posX
		self.posY = posY
		self.velX = velX
		self.velY = velY
		self.rot = rot
		self.zombie = zombie
		self.bound_rad = bound_rad
		self.draw_color = (0, 0, 255)

	def distance(self, bb):
		return math.sqrt((self.posX - bb.posX) ** 2 + (self.posY - bb.posY) ** 2)

	def move(self):
		#ahead = get_ahead_vec(self.posX + 5, self.posY + 5, self.velX, self.velY, 50)
		#ahead2 = get_ahead_vec(self.posX + 5, self.posY + 5, self.velX, self.velY, 40)
		self.posX += self.velX
		self.posY += self.velY
		#pygame.draw.line(screen, self.draw_color, (self.posX + 5, self.posY + 5), (self.aheadX, self.aheadY))
		#pygame.draw.line(screen, (0, 255, 0), (self.posX + 5, self.posY + 5), (self.aheadX2, self.aheadY2))


	def move_away(self, boids, min_dist):
		if len(boids) < 1: return

		dist_x = 0
		dist_y = 0
		num_close = 0

		for boid in boids:
			dist = self.distance(boid)
			if dist < min_dist:
				#boid_line(self, boid, (255, 0, 0, 10))
				num_close += 1
				xdiff = (self.posX - boid.posX)
				ydiff = (self.posY - boid.posY)

				if xdiff >= 0: xdiff = math.sqrt(min_dist) - xdiff
				elif xdiff < 0: xdiff = -math.sqrt(min_dist) - xdiff
				if ydiff >= 0: ydiff = math.sqrt(min_dist) - ydiff
				elif ydiff < 0: ydiff = -math.sqrt(min_dist) - ydiff

				dist_x += xdiff
				dist_y += ydiff

		if num_close == 0:
			return

		self.velX -= dist_x / 2
		self.velY -= dist_y / 2

	def move_closer(self, boids):
		if len(boids) < 1: return

		avg_x = 0
		avg_y = 0

		for boid in boids:

			#boid_line(self, boid, (0, 0, 255, 10))
			avg_x += (self.posX - boid.posX)
			avg_y += (self.posY - boid.posY)

		avg_x /= len(boids)
		avg_y /= len(boids)

		distance = math.sqrt((avg_x * avg_x) + (avg_y * avg_y)) * -1.0

		self.velX -= (avg_x / 100)
		self.velY -= (avg_y / 100)

	def move_with(self, boids):
		if len(boids) < 1: return

		avg_x = 0
		avg_y = 0

		for boid in boids:
			#boid_line(self, boid, (0, 255, 255, 10))
			avg_x += boid.velX
			avg_y += boid.velY

		avg_x /= len(boids)
		avg_y /= len(boids)

		self.velX += (avg_x)
		self.velY += (avg_y)

	def avoid_circle(self, circles):
		for circle in circles:
			if calc_distance(circle.posX, circle.posY, self.posX, self.posY) < circle.rad + self.bound_rad:
				self.velX += (self.posX - circle.posX) * 20
				self.velY += (self.posY - circle.posY) * 20

pygame.init()
width = 1080
height = 720
screen = pygame.display.set_mode((width, height))
done = False
sphere_obs_list = []
boid_list = []
boid_img = pygame.image.load('boid.png').convert()
boidz_img = pygame.image.load('boidz.png').convert()

dist_rule = 20.0
border_rule = 20.0
bound_x_rule = width - border_rule
bound_y_rule = height - border_rule

num_spheres = 40
num_boids = 30
num_zomboids = 0
max_sphere_rad = 20
min_sphere_rad = 5
max_boid_vel = 4
max_zomboid_vel = 3
boid_collision_sphere_rad = 15
debug_circles = False
zomboids_can_kill = True

for i in range(0, num_spheres):
	sphere_obs_list.append(SphereObstacle(random.uniform(min_sphere_rad, max_sphere_rad), random.uniform(border_rule, bound_x_rule), random.uniform(border_rule, bound_x_rule)))

for i in range(0, num_boids):
	boid_list.append(Boid(random.uniform(border_rule, bound_x_rule), random.uniform(border_rule, bound_y_rule), random.uniform(-2, 2), random.uniform(-2, 2), 0, boid_collision_sphere_rad, False))

for i in range(0, num_zomboids):
	boid_list.append(Boid(random.uniform(border_rule, bound_x_rule), random.uniform(border_rule, bound_y_rule), random.uniform(-3, 3), random.uniform(-3, 3), 0, boid_collision_sphere_rad, True))

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	clock.tick(60)
	screen.fill((255, 255, 255))

	for circle in sphere_obs_list:
		pygame.draw.circle(screen, (0, 0, 255), (int(circle.posX), int(circle.posY)), int(circle.rad), 1)

	for boid in boid_list:
		close_boids = []
		close_zomboids = []
		closest_prey = 0
		closest_prey_dist = 1000

		for boid2 in boid_list:
			if boid == boid2: continue
	   		
			dist = boid.distance(boid2)

			if boid.zombie and dist < closest_prey_dist and not boid2.zombie:
	   			closest_prey = boid2
	   			closest_prey_dist = dist
	   			if closest_prey_dist < 10 and zomboids_can_kill: boid_list.remove(closest_prey)

			if dist < 100 and not boid2.zombie:
	   			close_boids.append(boid2)
			if dist < 100 and boid2.zombie:
	   			close_zomboids.append(boid2)
	   		
			if not boid.zombie:
	   			boid.move_closer(close_boids)
	   			boid.move_with(close_boids)
	   			boid.move_away(close_boids, dist_rule)	
	   		elif boid.zombie and boid2.zombie:
	   			boid.move_closer(close_zomboids)
	   			boid.move_with(close_zomboids)
	   			boid.move_away(close_zomboids, dist_rule)	

			for z in close_zomboids:
				if not boid.zombie:
					boid.velX += (boid.posX - z.posX) * 10
					boid.velY += (boid.posY - z.posY) * 10

		boid.avoid_circle(sphere_obs_list)

		if boid.zombie and closest_prey != 0 and closest_prey_dist != 0:
			boid.velX += closest_prey.posX - boid.posX
			boid.velY += closest_prey.posY - boid.posY
			boid_line(boid, closest_prey)

		if boid.posX > bound_x_rule and boid.velX > 0:
			boid.velX = -boid.velX * random.random()
		if boid.posY > bound_y_rule and boid.velY > 0:
			boid.velY = -boid.velY * random.random()

		if boid.posX < border_rule and boid.velX < 0:
			boid.velX = -boid.velX * random.random()
		if boid.posY < border_rule and boid.velY < 0:
			boid.velY = -boid.velY * random.random()

		if boid.zombie: lim_vel(boid, max_zomboid_vel)
		else: lim_vel(boid, max_boid_vel)

		boid.move()

		boid.rot = math.degrees(math.atan2(-boid.velX, -boid.velY))
		if debug_circles: pygame.draw.circle(screen, (0, 255, 0), (int(boid.posX + 5), int(boid.posY + 5)), int(boid.bound_rad), 1)
		screen.blit(pygame.transform.rotate(boidz_img if boid.zombie else boid_img, boid.rot), (boid.posX, boid.posY))

	pygame.display.flip()