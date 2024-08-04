def accept_into_movie(age, is_supervised):
    count = 0
    n = int(input())
    s = input()
    if n >= 15:
        count += 1
    elif s == True:
        count += 1
    if count == 2:
        return True
    else:
        return False

# https://codechick.io/challenges/246
