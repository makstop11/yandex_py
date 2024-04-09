s = int(input())

if s in [0, 1]:
    # if s == 1 or s == 0:
    print('NO')
else:
    # for i in range(2, s):
    for i in range(2, int(s**0.5) + 1):
        if s % i == 0:
            print('NO')
            break
    else:
        print('YES')
