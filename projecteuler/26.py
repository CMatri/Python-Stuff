d = 1.0
longest = 0
sequence = ""

while d < 1000:
    frac = format(1.0 / d, '0.50f')
    last = ""
    for i in range(0, len(frac)):
        if frac[i] != last:
            last = frac[i]
            if i > longest:
                longest = i
                sequence += frac[i]

    d += 1
    print frac
