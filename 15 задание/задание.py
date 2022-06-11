n, max6, min6 = int(input()), 0, 10**10
k = 0
summa = 0
summa1 = 0
N = 0
for i in range(n):
    number = int(input())
    if number % 6 == 0:
        k = k + 1
    if number > max6 and number % 6 == 0:
        max6 = number
    if number < min6:
        min6 = number
    summa = summa + number
    if number % 2 == 0:
        summa1 = summa1 + number
        N = N + 1


print(k)
print(max6)
print(min6)
print(summa)
print(summa1)