import math

d = float(input())
square_side: float = float(input())

square_area: float = square_side * 4
circle_area: float = math.pi * ((d / 2) ** 2)

if square_area <= circle_area:
    print('Можно')
else:
    print('Нельзя')
