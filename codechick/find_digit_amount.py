# https://codechick.io/challenges/110


def find_digit_amount(num: int):
    # return len(str(num))

    num = abs(num)
    if num == 0:
        return 1

    digits_count: int = 0
    while num != 0:
        num //= 10
        digits_count += 1

    return digits_count


print(find_digit_amount(123))
print(find_digit_amount(56))
print(find_digit_amount(7154))
print(find_digit_amount(61217311514))
print(find_digit_amount(0))
