n = int(input())

mx = 0
while n > 0:
    last_digit = n % 10
    if last_digit > mx:
        mx = n % 10
    n //= 10

print(mx)