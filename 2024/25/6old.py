for i in range(110203, 110245 + 1):
    k = 0
    for x in range(2, i + 1, 2):
        if i % x == 0:
            k += 1
            if k > 4:
                break
    if k == 4:
        for x in range(2, i + 1, 2):
            if i % x == 0:
                print(x, end=' ')
        print()

