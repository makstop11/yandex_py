print(1)
print(2)
print(3)
print(4)
print(5)
print(6)

print('-----\n')

n = 6
for i in range(1, n + 1):
    print(i)

[
    print(i) for i in range(1, n + 1)
]

chars = 'abcdef'
print('|'.join(chars))

nums = [1, 2, 3, 4]
print('-'.join(str(num) for num in nums))
