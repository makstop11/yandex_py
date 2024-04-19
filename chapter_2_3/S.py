ask = 500
delta = ask // 2

str = ''

while str != 'Угадал!':
    print(ask)
    str = input()
    if str == 'Меньше':
        ask = ask - delta
    if str == 'Больше':
        ask = ask + delta
    if delta >= 2:
        delta = (delta + 1) // 2
