# https://codechick.io/challenges/300


def sum_recursively(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_recursively(lst[1:])
