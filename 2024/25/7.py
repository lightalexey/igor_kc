for i in range(95632, 95700 + 1):
    k = 0
    for j in range(1, i + 1):
        if i % j == 0 and j % 2 == 0:
            k += 1
    if k == 6:
        #print(i)
        for j in range(1, i + 1):
            if i % j == 0 and j % 2 == 0:
                print(j, end=' ')
        print()
