for n in range(174457, 174505 + 1):
    x = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            x += 1
        if x > 2:
            break
    if x == 2:
       for i in range(2, n // 2 + 1):
           if n % i == 0:
               print(i, end=' ')
       print()

        # print(n)




