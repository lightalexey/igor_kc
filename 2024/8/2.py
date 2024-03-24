k = 0
for i1 in '12345':
    for i2 in '12345':
        for i3 in '12345':
            for i4 in '12345':
                for i5 in '12345':
                    s = i1 + i2 + i3 + i4 + i5
                    if s.count('1') == 3:
                        k += 1
print(k)
