n = int(input())
summa6 = 0
for i in range(n):
    number = int(input())
    if number % 6 == 0:
        summa6 = summa6 + number
print(summa6)