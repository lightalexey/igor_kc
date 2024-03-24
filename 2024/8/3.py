k = 0
for i1 in '123':
    for i2 in '0123':
        for i3 in '0123':
            if int(i1) + int(i3) > int(i2):
                k += 1
print(k)
