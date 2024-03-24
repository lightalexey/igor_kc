for i in range(95632, 95700 + 1):
    k = 0
    delit = []
    for j in range(2, i + 1, 2):
        if i % j == 0:
            k += 1
            delit.append(j)
        if k > 6:
            break
    if k == 6:
        print(*delit)
