n, max5 = int(input()), 0
for i in range(n):
    number = int(input())
    if number > max5 and number % 5 == 0:
        max5 = number
print(max5)