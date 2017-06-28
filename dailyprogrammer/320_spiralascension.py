import sys

def enum(**enums):
    return type('Enum', (), enums)

dim = int(sys.argv[1])
entries = [[0 for i in range(0, dim)] for j in range(0, dim)]
posX = 1
posY = 1
lim = 0
maxLength = len(str(dim**2))
Directions = enum(LEFT=(-1, 0), RIGHT=(1, 0), UP=(0, -1), DOWN=(0, 1))
direction = Directions.RIGHT

for i in range(1, dim * dim):
	old = direction

	if direction == Directions.RIGHT:
		if posX == dim - lim:
			direction = Directions.DOWN
	if direction == Directions.DOWN:
		if posY == dim - lim:
			direction = Directions.LEFT
	if direction == Directions.LEFT:
		if posX == 1 + lim:
			direction = Directions.UP
	if direction == Directions.UP:
		if posY == 1 + lim:
			direction = Directions.RIGHT

	if old != direction and direction == Directions.UP:
		lim += 1

	posX += direction[0]
	posY += direction[1]

	entries[posX - 1][posY - 1] = str(i)

for x in range(0, len(entries)):
	for y in range(0, len(entries[x])):
		for i in range(0, maxLength - len(str(entries[x][y]))):
			sys.stdout.write(" ")
		sys.stdout.write(str(entries[x][y]) + " ")
	print ""
