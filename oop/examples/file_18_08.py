# class Point:
#     pass
#
#
# yellow = Point()
#
# yellow.x = 3.0
# yellow.y = 4.0
#
# print(yellow.x)
# print(yellow.y)
#
# black = Point()
# print(black.x)
# print(black.y)

# ----------------------


class Point:
    #  Свойство(Поле)
    COLOR = "black"

    def __init__(self, x, y):
        # Атрибуты
        self.x = x
        self.y = y


# Объекты (экземпляр)
yellow = Point(3.0, 4.0)
print(yellow.x)
print(yellow.y)

black = Point(6.3, 2.4)
print(black.x)
print(black.y)

red = Point(-1, -2.3)
print(red.x)
print(red.y)

print(yellow.COLOR)
print(black.COLOR)
print(red.COLOR)


class Cat:
    # Свойство(Поле)
    FEET: int = 4

    def __init__(self, nick_name, cat_color):
        # Атрибуты
        self.__name = nick_name
        self.color = cat_color

        #  - public
        # _ - protected
        # __ - private

    # Метод
    def voice(self):
        print('Мяу!')

    def get_name(self):
        return self.__name


# Объекты (экземпляр)
rijik = Cat("Рижик", "рыжий")
tom = Cat("Том", "серый")

rijik.name = "Бла бла"
# print(rijik.__name)
# print(tom.__name)

print(rijik.get_name())
print(tom.get_name())

print(rijik.FEET)
print(tom.FEET)

rijik.voice()
tom.voice()
