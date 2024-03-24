r = 0
x = 0
for n in range(1, 10**6):
    x = bin(n)
    # if x.count('1') % 2 == 0:
    #     x += '0'
    # else:
    #     x += '1'
    # if x.count('1') % 2 == 0:
    #     x += '0'
    # else:
    #     x += '1'
    x += str(x.count('1') % 2)
    x += str(x.count('1') % 2)
    if int(x, 2) > 77:
        print(n)
        break





