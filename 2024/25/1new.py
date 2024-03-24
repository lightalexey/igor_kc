for i in range(20240, 10**10, 2024):
    s = str(i)
    if s[0] == '1' and s[2:6] == '2157' and s[-1] == '4':
        print(s, i//2024)

