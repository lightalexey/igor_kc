# f = open('123.txt')
# s = f.read().split()
# print(s)
# for i in range(len(s)):
#    s[i] = int(s[i])
# print(s)
# 2 способ
# s = []
# for i in range(10):
#    s.append(int(f.readline()))
# print(s)

s = [int(i) for i in open('123.txt')]
print(s)