import sys

inp = int(sys.argv[1])

while inp != 1:
	print("%d %d" % (inp, (0, -1, 1)[int(inp % 3)]))
	inp = (inp + [0, -1, 1][inp % 3] ) / 3
print 1