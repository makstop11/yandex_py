def profitable_gamble(prob, prize, pay):
    prob = int(input())
    prize = int(input())
    pay = int(input())
    if prob * prize > pay:
        return True
    else:
        return False


# https://codechick.io/challenges/35
