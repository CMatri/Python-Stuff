final = 0

x = 1
y = 2

while x <= 4000000:
    if x % 2 == 0: final += x
    ne = x + y
    x = y
    y = ne
    print final
