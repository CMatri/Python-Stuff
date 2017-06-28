from bitarray import bitarray
import time

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def find_primes(max, debug = False):
    if debug: print "Memory needed for sieve bitmap: " + ((str(max / 8.0 / 1024.0 / 1024) + " mb.") if max >= (8 * 1024 * 1024) else (str(max / 8.0 / 1024.0) + " kb."))
    primes = []
    dont_use = bitarray()
    dont_use.extend([False] * max)
    #last = 0
    start = time.clock()
    for x in xrange(3, max, 2):
        if dont_use[x]: continue
        primes.append(x)
        for y in xrange(x, max / x):
            dont_use[y * x] = True

    end = time.clock() - start

    if debug: print "Found primes up to " + str(max) + " in " + str(end) + " second(s), while considering about " + str(int(max / end)) + " numbers per second."
    return primes

# example: primes = find_primes(2000000)
