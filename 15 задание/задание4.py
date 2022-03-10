n = int(input())
min3 = 1000
for i in range(n):
    number = int(input())
    if number < min3 and number % 3 == 0:
        min3 = number
print(min3)