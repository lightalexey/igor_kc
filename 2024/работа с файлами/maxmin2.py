s = [int(i) for i in open('123.txt')]
print(*s)
maximum, minimum = s[0], s[0]
x, z = 0, 0
for k in range(len(s)):
    if s[k] > maximum:
        maximum = s[k]
        x = k
    if s[k] < minimum:
        minimum = s[k]
        z = k
print(maximum, x, minimum, z)