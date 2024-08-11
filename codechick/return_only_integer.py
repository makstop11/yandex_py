#  https://codechick.io/challenges/331


def return_only_integer(lst):
    result = []
    for elem in lst:
        if type(elem) == int:
        # if isinstance(elem, int):
            result.append(elem)
    return result
