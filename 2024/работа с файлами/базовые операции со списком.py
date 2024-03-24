s = [int(i) for i in open('123.txt')]
print(*s)
summa, pr = 0, 1
for k in range(len(s)):
    summa += s[k]
    if s[k] != 0:
        pr *= s[k]
print(summa)
print(pr)

summa = zero = 0
for k in s:
    summa += k
    if k == 0:
        zero += 1
print(summa)
print(sum(s))
print(zero)
print(summa/len(s))
print(s[0], s[-1])
b = s[0]
s[0] = s[-1]
s[-1] = b
print(*s)
s[0], s[-1] = s[-1], s[0]
print(*s)


