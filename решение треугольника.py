a = int(input('Введи а='))
b = int(input('Введи b='))
c = int(input('Введи c='))
if a < b + c and b < a + c and c < a + b:
    print ('Треугольник существует')
else:
    print ('Треугольник в небытие')     