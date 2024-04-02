n = int(input())
count = 0

for i in range(n):
    count += n
    s = count // 100 * 10
    print(s - count)
