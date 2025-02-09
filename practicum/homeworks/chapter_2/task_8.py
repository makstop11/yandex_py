import math

square_area = int(input())
r = int(input())
k = int(input())

square_side = math.sqrt(square_area)

if (r * 2 + k) <= square_side:
    print('Можно')
else:
    print('Нельзя')
