n = int(input())

count = 1
for i in range(1, n + 1):
    for j in range(i):
        if count > n:
            break
        print(count, end=' ')
        count += 1

    if count > n:
        break
    print()
