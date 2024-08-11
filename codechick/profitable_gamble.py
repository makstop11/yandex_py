# https://codechick.io/challenges/35


def profitable_gamble(prob, prize, pay):
    prob = int(input())
    prize = int(input())
    pay = int(input())
    if prob * prize > pay:
        return True
    else:
        return False

# TODO: Неверное решение: переделать.
