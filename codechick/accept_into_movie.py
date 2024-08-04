# https://codechick.io/challenges/246


def accept_into_movie(age: int, is_supervised: bool):
    return age >= 15 or is_supervised


print(accept_into_movie(14, True))
print(accept_into_movie(14, False))
print(accept_into_movie(16, False))
