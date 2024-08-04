# https://codechick.io/challenges/194


def add_odd_to_n(n: int):
    total_sum: int = 0
    for i in range(1, n + 1, 2):
        if i % 2 != 0:
            total_sum += i

    return total_sum


print(add_odd_to_n(1))
print(add_odd_to_n(8))
print(add_odd_to_n(13))
print(add_odd_to_n(47))
