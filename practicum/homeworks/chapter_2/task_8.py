import math

s = int(input())
r = int(input())
k = int(input())


l = math.sqrt(s)


c = r - k

if (r * 2 + k) < l:
    print('Можно')
else:
    print('Нельзя')
