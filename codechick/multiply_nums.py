# https://codechick.io/challenges/448


def multiply_nums(numbers):
    summa: int = 1
    for num in numbers.split(', '):
        summa *= int(num)
    return summa
