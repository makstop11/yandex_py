n = int(input())
m = int(input())

col_len = len(str(n * m))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        exp = i + (j - 1) * n
        print(f'{exp:<{col_len}}', end=' ')
    print()
