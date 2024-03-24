for n in range(110203, 110245 + 1):
    s = 0
    for i in range(2, n + 1):
        if n % i == 0 and i % 2 == 0:
            s += 1
        if s > 4:
          break
    if s == 4:
        for i in range(2, n + 1):
            if n % i == 0 and i % 2 == 0:
                print(i, end=' ')
        print()