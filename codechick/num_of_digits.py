# https://codechick.io/challenges/317

def num_of_digits(num):
    count = 0
    while num != 0:
        count += 1
        num = num // 10
    return count
