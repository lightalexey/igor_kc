s = [int(i) for i in open('123.txt')]
print(*s)
maximum, minimum = s[0], s[0]
for k in range(len(s)):
    if s[k] > maximum:
        maximum = s[k]
    if s[k] < minimum:
        minimum = s[k]
print(maximum, minimum)

maximum, minimum = s[0], s[0]
for k in s:
    if k > maximum:
        maximum = k
    if k < minimum:
        minimum = k
print(maximum, minimum)

print(max(s), min(s))