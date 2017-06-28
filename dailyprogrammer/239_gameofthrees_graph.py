import sys
import matplotlib.pyplot as plt

amt = len(sys.argv[1:])
hist = [[] for x in range(amt)]

for i in range(amt):
	inp = int(sys.argv[i + 1])
	while inp != 1:
		op = [0, -1, 1][inp % 3]
		hist[i].append(inp + op)
		print "%d %d" % (inp, op)
		inp = (inp + op ) / 3
		hist[i].append(inp)
	print 1

for i in range(amt): plt.plot(range(len(hist[i])), hist[i])

plt.legend([sys.argv[i + 1] for i in range(amt)])
plt.grid()
plt.show()