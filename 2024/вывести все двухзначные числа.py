k = 0
for i in range(10, 99+1):
        print(i, end=' ')
        k += 1 # k = k + 1 k++
print()
print(k)
k = 0
for i in range(10, 99+1):
        if i % 2 == 0:
                k += 1 # k = k + 1 k++
print(k)
k = 0
for _ in range(10, 99+1, 2):
        k += 1
print(k)

# вывести все двухзначные кратные 3 и 5 одновременно
for i in range(10, 99+1):
        if i % 3 == 0 and i % 5 == 0:
                print(i, end=' ')




