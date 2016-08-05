def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

final = 0

l = [];

for i in range(1, 1000):
    if is_prime(i): l.append(i)
for i in range(0, len(l)):
    print l[i]
