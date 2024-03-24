x = '0123456789'
k = 0
for i1 in x:
    for i2 in x:
        for i3 in x:
            if i1 == i2 or i2 == i3 or i1 == i3:
                k += 1
print(k)

