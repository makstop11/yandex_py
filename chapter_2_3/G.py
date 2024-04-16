a = int(input())
b = int(input())

s = a * b

while b != 0:
    a, b = b, a % b

print(s // a)
