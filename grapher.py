import numpy
import matplotlib.pyplot as plt
import sys

def formula(x):
	try:
		return 3 - 4 * x**3
	except:
		return numpy.inf

floor = int(sys.argv[1])
ceil = int(sys.argv[2])
hist = ([], [])

for x in range(floor, ceil + 1):
	hist[0].append(formula(x))

final = range(floor, ceil + 1)
plt.xlim([floor , ceil])
plt.plot(final, hist[0])
plt.grid()
plt.show()