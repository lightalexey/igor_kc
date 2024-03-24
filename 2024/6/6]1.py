z = 0
for y in range(1, 10):
    for x in range(1, 10):
        if 1 / (3 ** (1 / 2)) * x < y < -((3 ** (1 / 2)) / 3) * x + 10:
            z += 1
print(z)
