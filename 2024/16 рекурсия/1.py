#F(1) = 1
#F(2) = 3
#F(n) = F(n−1) * F(n−2) + (n−2), при n > 2
#Чему равно значение функции F(5)?
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
        return F(n-1) * F(n-2) + (n-2)
print(F(5))
