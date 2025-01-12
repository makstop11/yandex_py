import math

a: int = int(input())
b: int = int(input())
c: int = int(input())

p: float = (a + b + c) / 2
S: float = math.sqrt(
    p * (p - a) * (p - b) * (p - c)
)

print(S)
