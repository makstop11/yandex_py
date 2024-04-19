ask = 500
delta = ask // 2

text = ''
while text != 'Угадал!':
    print(ask)

    text = input()

    if text == 'Меньше':
        ask = ask - delta
    if text == 'Больше':
        ask = ask + delta
    if delta >= 2:
        delta = (delta + 1) // 2
