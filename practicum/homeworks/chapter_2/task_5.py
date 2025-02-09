a = int(input('длина коробки: '))
b = int(input('ширина коробки: '))
c = int(input('высота коробки: '))

d = int(input('ширина двери: '))
i = int(input('высота двери: '))

sides: list[int] = [a, b, c]
sides.sort()

box_min_side, box_average_side, _ = sides
door_min_side, door_max_side = min(d, i), max(d, i)

if (
    (box_min_side <= door_min_side)
    and (box_average_side <= door_max_side)
):
    print('Коробка пройдёт')
else:
    print('Коробка не пройдёт')
