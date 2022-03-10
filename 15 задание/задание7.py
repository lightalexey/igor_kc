n = int(input())
min6 = 1000
for i in range(n):
    number = int(input())
    if number < min6 and number % 10 == 6:
        min6 = number
print(min6)