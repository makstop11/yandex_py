a = int(input('длина коробки: '))
b = int(input('ширина коробки: '))
c = int(input('высота коробки: '))

d = int(input('ширина двери: '))
i = int(input('высота двери: '))

if (c <= i and b <= i) or (c <= i and c <= i) or (a <= i and b <= i):
    print('Коробка пройдёт')

else:
    print('Коробка не пройдёт')
