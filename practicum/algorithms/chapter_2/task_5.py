a = int(input('Длина коробки: '))
b = int(input('Ширина коробки: '))
c = int(input('Высота коробки: '))

m = int(input('Длина двери: '))
k = int(input('Ширина двери: '))

volume = a * b * c
door_area = m * k

if volume < door_area:
    print('Коробка пройдёт')
