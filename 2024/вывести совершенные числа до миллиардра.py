#n = int(input())
for n in range(6, 10 ** 9):
    x = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            x += i
    if x == n:
        print(n, bin(n))




