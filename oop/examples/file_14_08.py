class Ball:
    TYPE: str = 'круглый'
    INSIDE: str = 'воздух'
    SIZE: int = 4
    WEIGHT: int = 200

    # Магические методы
    def __init__(self, brand: str, color: str):
        """Инициализатор (конструктор) объекта.
        :param brand:
        :param color:
        """
        self.obj_brand = brand
        self.obj_color = color

    def jump(self):
        print('Прыгать!')

    def roll(self):
        print('Катиться!')

    def __str__(self):
        return f'Бренд: {self.obj_brand} Цвет: {self.obj_color}'


class BasketballBall(Ball):
    SIZE: int = 6
    WEIGHT: int = 400


class VolleyballBall(Ball):
    WEIGHT: int = 150


class FootballBall(Ball):
    pass


bb = BasketballBall('adidas', 'оранжевый')
print(bb.__dict__)
print(bb.SIZE)
print(bb)

# bb2 = BasketballBall('demix', 'красный')
# print(bb)
# bb.roll()
# bb2.roll()
#
vb = VolleyballBall('nike', 'желтый')
# vb.jump()
# vb.roll()
print(vb.__dict__)
print(vb.SIZE)
print(vb)
#
# fb = FootballBall()
