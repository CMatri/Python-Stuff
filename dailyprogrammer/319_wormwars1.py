from random import random
import matplotlib.pyplot as plt
import sys

pop = int(sys.argv[1])
infected = int(sys.argv[2])
sI = float(sys.argv[3])
iR = float(sys.argv[4])
sR = float(sys.argv[5])

susceptible, recovered = pop - infected, 0
calc_pop = susceptible + infected

hist = ([pop], [infected], [susceptible], [recovered], [calc_pop])
#plt.plot([], [], [], [], [], '--')

for i in range(int(sys.argv[6])):
	for b in range(susceptible):
		if random() < sI:
			infected += 1
			susceptible -= 1
		if random() < sR:
			recovered += 1
			susceptible -= 1
	for b in range(infected):
		if random() < iR:
			recovered += 1
			infected -=1
	calc_pop = susceptible + recovered + infected
	for j, e in enumerate([pop, infected, susceptible, recovered, calc_pop]):
		hist[j].append(e)

final = range(len(hist[0]))

print susceptible + infected + recovered == pop

plt.plot(final, hist[0], final, hist[1], final, hist[2], final, hist[3], final, hist[4], '--')
plt.legend(["Population", "Infected", "Susceptible", "Recovered", "Calc pop"])
plt.grid()
plt.tight_layout()
plt.show()
