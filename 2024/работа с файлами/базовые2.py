s = [int(i) for i in open('123.txt')]
print(*s)
summa, b = 0, 0
for k in range(len(s)):
    if s[k] > 0:
        summa += s[k]
        b += 1
print(summa)
print(summa/b)
# отрицательные элементы заменить на 0 и вывести новый список на экран
for k in range(len(s)):
    if s[k] < 0:
        s[k] = 0
print(s)
