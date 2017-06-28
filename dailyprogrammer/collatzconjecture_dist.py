import matplotlib.pyplot as plt
import sys

floor = int(sys.argv[1])
ceil = int(sys.argv[2])
hist = ([], [])

for i in range(floor, ceil + 1):
	n = i
	steps = 0
	while n != 1:
		steps += 1
		if n % 2:
			n = (n * 3 + 1) / 2
		else:
			n /= 2
	hist[0].append(steps)

final = range(floor, ceil + 1)
plt.xlim([floor , ceil])
plt.plot(final, hist[0])
plt.grid()
plt.show()