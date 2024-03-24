number = int(input('введи целое число:'))
print('количество разрядов равно', len(str(number)))
print(str(number).count('2'))
k = 0
z = 0
while number > 0:
    if number % 10 == 2:
        z += 1
    number = number // 10
    k += 1
print(k, z)


