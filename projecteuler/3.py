num = 10000001
divisor = 2
largest_divisor = divisor
buf = 0

while num > 1:
    if num % divisor == 0:
        num /= divisor
        print str(divisor) + " : " + str(num)
        if divisor > largest_divisor:
            largest_divisor = divisor
        divisor = 2
    else:
        if divisor % 100000 == 0:
            print str(divisor) + " going to " + str(num)
        divisor += 1
print str(largest_divisor) + " largest divisor "
