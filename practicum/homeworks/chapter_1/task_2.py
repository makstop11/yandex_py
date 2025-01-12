a: int = int(input())
b: int = int(input())
c: int = int(input())

print(min(a, b, c))
print(max(a, b, c))

# Расширенный пример для функции max().
if a > c and a > b:
    print(a)
elif c > a and c > b:
    print(c)
else:
    print(b)
