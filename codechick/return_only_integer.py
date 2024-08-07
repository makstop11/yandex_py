def return_only_integer(lst):
    n = []
    for i in lst:
        if type(i) is int:
            n.append(i)
    return n

#  https://codechick.io/challenges/331
