s = 'Мама мыла раму'
# найти количество букв а
print(s.count('а'))
# найти количество гласных букв
print(s.count('а') + s.count('ы') + s.count('у'))
k = 0
for i in s:
    if i in ['а', 'о', 'у', 'ы', 'и', 'е', 'я']:
        k += 1
print(k)
# поменять первую букву на заглавную
ss = 'м' + s[1:]
print(ss)
s = s.replace('М', 'м', 1)
print(s)
# поменять слово раму на папу
s = s.replace('раму', 'папу')
print(s)
# найти количество слов
print(s.count(' ') + 1)








