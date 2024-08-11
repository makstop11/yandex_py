# https://codechick.io/challenges/394


def left_digit(string):
    for i in string:
        if i.isdigit():
            return int(i)
