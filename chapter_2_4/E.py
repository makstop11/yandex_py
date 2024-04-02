n = float(input())
total = 0

while n != 0:
    if n >= 500:
        delta = n - (n * 0.1)
        total += delta
    else:
        total += n
    n = float(input())
print(total)
