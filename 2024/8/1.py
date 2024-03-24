k = 0
for i1 in '1234':
    for i2 in '1234':
        for i3 in '1234':
            for i4 in '1234':
                for i5 in '1234':
                    s = i1 + i2 + i3 + i4 + i5
                    if s.count('1') == 2:
                        k += 1
print(k)
