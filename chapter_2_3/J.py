x = 0
y = 0

while (direction := input()) != 'СТОП':
    n = int(input())
    if direction == 'ВОСТОК':
        x += n
    elif direction == 'ЗАПАД':
        x -= n
    elif direction == 'СЕВЕР':
        y += n
    elif direction == 'ЮГ':
        y -= n

print(y)
print(x)
