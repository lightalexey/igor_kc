n = int(input())
max3 = -301
for i in range(n):
    number = int(input())
    if number % 3 == 0 and number % 10 == 4:
        max3 = max3 + number
print(max3)