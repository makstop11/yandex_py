n = int(input())

total = 0
for _ in range(n):
    num = int(input())

    for i in str(num):
        total += int(i)

print(total)
