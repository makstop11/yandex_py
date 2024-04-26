N = int(input())

count = 0
for _ in range(N):

    num = int(input())
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1

print(count)
