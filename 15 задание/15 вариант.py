n = int(input())
summa = 0
k = 0
while n != 0:
    if n < 100 and n > 9:
        summa += n
        k += 1
    n = int(input())
if k == 0:
    print("NO")
else:
    print(summa/k)
  