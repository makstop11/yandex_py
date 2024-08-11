# https://codechick.io/challenges/58


def check_equals(lst1: list, lst2: list):
    return lst1 == lst2


a = [1, 2, 3]
b = a
print(a is b)
d = [4, 5, 6]
c = [4, 5, 6]
print(d is c)
print(d == c)


print(check_equals([1, 2], [1, 3]))
print(check_equals([1, 2], [1, 2]))
print(check_equals([4, 5, 6], [4, 5, 6]))
print(check_equals([4, 7, 6], [4, 5, 6]))
