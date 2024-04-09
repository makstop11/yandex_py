s = input()
x = 0
y = 0

while s != 'СТОП':
    n = int(input())
    if s == 'ВОСТОК':
        x += n
    elif s == 'ЗАПАД':
        x -= n
    elif s == 'СЕВЕР':
        y += n
    else:
        y -= n
    s = input()

print(y)
print(x)
