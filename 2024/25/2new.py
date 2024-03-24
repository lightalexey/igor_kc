for i in range(0, 10**8, 2622):
    s = str(i)
    if s[0] == '1' and s[2] == '4' and s[-3] == '6' and s[-1] == '8':
        print(s, i//2622)