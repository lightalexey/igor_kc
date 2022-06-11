N = int(input())
bad = 0
result = 'NO'
for i in range(N):
    x = int(input())
    if x < 5:
        bad = bad + 1
    if x == 10:
        result = 'YES'
print(bad)
print(result)
