highest = 0

for i in range(100, 999):
    for j in range(100, 999):
        tot = i * j
        if (len(str(tot)) & 2) == 0: continue
        a = str(tot)[0 : len(str(tot)) / 2]
        b = str(tot)[len(str(tot)) / 2 : len(str(tot))]
        if a == b[:: -1] and tot > highest:
            highest = tot

print "done"
print highest
