# https://codechick.io/challenges/317

def num_of_digits(num):
    if num < 0:
        num = abs(num)
    if num == 0:
        return 1

    count = 0
    while num != 0:
        count += 1
        num = num // 10
    return count


print(num_of_digits(-37))
print(num_of_digits(0))
# -37
