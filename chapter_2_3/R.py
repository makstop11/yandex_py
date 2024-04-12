s = int(input())

prime_number = 2
result = []

while prime_number <= s:
    if s % prime_number == 0:
        result.append(str(prime_number))
        s = s // prime_number
    else:
        prime_number += 1

print(' * '.join(result))
