max3 = 0
number = int(input())
while number != 0:
   if number % 3 == 0 and number % 10 == 4:
       max3 = max3 + number
   number = int(input())
print(max3)