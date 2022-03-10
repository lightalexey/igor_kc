n = int(input())
k4 = 0
for i in range(n):
    number = int(input())
    if number % 4 == 0:
        k4 = k4 + 1
print(k4)