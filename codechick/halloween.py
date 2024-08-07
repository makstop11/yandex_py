# https://codechick.io/challenges/312

def halloween(dt):
    n = str(dt)
    if n[-1] == 1 and n[-2] == 3:
        return "Bonfire toffee"
    else:
        return "toffee"



print(halloween("2013/10/31"))
print(halloween("2012/07/31"))
print(halloween("2011/10/12"))
