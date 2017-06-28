import matplotlib.pyplot as plt
import sys

amt = len(sys.argv[1:])
hist = [[] for x in range(amt)]

for i in range(amt):
	n = int(sys.argv[i + 1])
	while n != 1:
		hist[i].append(n)
		if n % 2:
			n = (n * 3 + 1) / 2
		else:
			n /= 2
	hist[i].append(n)

for i in range(amt): plt.plot(range(len(hist[i])), hist[i])

plt.legend([sys.argv[i + 1] for i in range(amt)])
plt.grid()
plt.show()