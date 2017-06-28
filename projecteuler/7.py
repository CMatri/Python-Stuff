import primes

a = primes.find_primes(200000, True)
for x in xrange(0, 10001):
    print str(x) + " : " + str(a[x])
