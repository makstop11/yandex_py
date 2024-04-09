n = int(input())
s = str(n)
result = []

for i in s:
    if i not in '02468':
        result.append(i)

num = ''.join(result)

print(int(num))
