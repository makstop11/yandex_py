# https://codechick.io/challenges/318

def XO(s):
    x = []
    o = []
    for i in s.split():
        if i.islower() == 'x':
            x = x.append(i)
        elif i.islower() == 'o':
            o = o.append(i)
    if len(x) == len(o):
        return True
    else:
        return False
