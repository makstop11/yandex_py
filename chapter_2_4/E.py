num = int(input())

count = 0
for _ in range(num):

    temp = 0
    line = input()
    while line != 'ВСЁ':
        if line == 'зайка':
            temp += 1

        line = input()

    if temp > 0:
        count += 1

print(count)
