n = int(input())
x = 0
for i in range(1, n+1):
    if n % i == 0:
        x += 1
        print(i, end=' ')
print()
print(x)