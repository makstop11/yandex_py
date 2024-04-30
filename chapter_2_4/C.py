n = int(input())
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(count + j, end=' ')
    count += 1
    print()
