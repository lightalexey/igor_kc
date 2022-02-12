a = int(input('Введи а='))
b = int(input('Введи b='))
c = int(input('Введи c='))
if a < b + c:
    if b < a + c:
        if c < a + b:
            print ('Треугольник существует')
        else:
            print ('Треугольник в небытие') 
    else:
        print ('Треугольник в небытие')           
else:
    print ('Треугольник в небытие')     