j = 0
for n in range(245690, 245756 + 1):
    j += 1
    k = 0
    for i in range(1, n + 1):
        if n % i == 0:
            k += 1
    if k == 2:
        print(j, n)

