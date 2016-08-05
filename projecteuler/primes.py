from bitarray import bitarray
import time

def find_primes(max, debug = False):
    if debug: print "Memory needed for sieve bitmap: " + ((str(max / 8.0 / 1024.0 / 1024) + " mb.") if max >= (8 * 1024 * 1024) else (str(max / 8.0 / 1024.0) + " kb."))
    dont_use = bitarray()
    dont_use.extend([False] * max)
    last = 0
    start = time.clock()
    for x in xrange(2, max):
        if dont_use[x]: continue
        if x % 2 == 0:
            dont_use[x] = True
            continue
        for y in xrange(x, max / x):
            dont_use[y * x] = True

    end = time.clock() - start
    primes = []

    if debug: print "Found primes up to " + str(max) + " in " + str(end) + " second(s), while considering about " + str(int(max / end)) + " numbers per second."

    for x in xrange(2, max):
        if not dont_use[x]:
            primes.append(x)
    return primes

# example: primes = find_primes(2000000)
