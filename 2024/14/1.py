for x in '0123456789abcde':
    if (int('123' + x + '5', 15) + int('1' + x + '233', 15)) % 14 == 0:
        print((int('123' + x + '5', 15) + int('1' + x + '233', 15))//14)
        break
for x in range(0, 15):
    if ((5 + x * 15 + 3 * 225 + 2 * 15 ** 3 + 1 * 15 ** 4) + (3 + 3 * 15 + 2 * 225 + x * 15 ** 3 + 1 * 15 ** 4)) % 14 == 0:
        print(((5 + x * 15 + 3 * 225 + 2 * 15 ** 3 + 1 * 15 ** 4) + (3 + 3 * 15 + 2 * 225 + x * 15 ** 3 + 1 * 15 ** 4))//14)
        break
for x in '012345678':
    for y in '012345678':
        if (int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)) % 61 == 0:
            print((int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11))//61)
            break
