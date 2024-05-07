num = int(input())

f = 1

while num > 1:
    f *= num
    num -= 1
print(f)


num = int(input())

if num in (0, 1):
    print(1)
else:
    pass
