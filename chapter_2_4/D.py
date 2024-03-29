a = int(input())
b = int(input())

step = 1
if b < a:
    step = -1

for i in range(a, b + step, step):
    print(i, end=' ')

# Option №2
a = int(input())
b = int(input())

while True:
    if a < b:
        print(a, end=' ')
        a += 1
    elif a > b:
        print(a, end=' ')
        a -= 1
    else:
        print(a, end=' ')
        break
