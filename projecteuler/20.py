        ac = 100
final = 1

for x in range(1, fac + 1):
    final *= x
    print final
print "Using " + str(final)

fin_str = str(final)
fin_sum = 0

for x in range(0, len(fin_str)):
    fin_sum += int(fin_str[x])
print fin_sum
