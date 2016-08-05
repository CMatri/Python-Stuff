lst = [x for x in range(2, 9999)]

toRemove = []

for i in range(0, len(lst)):
    if len(lst) <= i: break
    cur = lst[i]
    for j in range(i, len(lst)):
        if lst[j] % cur != 0: toRemove.append(lst[j])
    for j in range(i, len(toRemove)):
        if toRemove[j] in lst:
            lst.remove(toRemove[j])
for i in range(0, len(lst)):
    print lst[i]
