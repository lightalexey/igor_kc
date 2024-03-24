x = 0
for n in range(1, 10**6):
    x = bin(n)
    x += str(x.count('1') % 2)
    x += str(x.count('1') % 2)
    if int(x, 2) > 43:
        print(int(x, 2))
        break