a = int(input())
b = int(input())
n = 0
for i in range(a,b+1):
    if i % 2 != 0:
        n += 1
print(n)

