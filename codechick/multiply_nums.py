# https://codechick.io/challenges/448

def multiply_nums(numbers):
    count = 1
    for i in numbers.split(', '):
        count *= int(i)
    return count
