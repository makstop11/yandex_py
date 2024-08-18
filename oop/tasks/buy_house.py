# https://smartiqa.ru/courses/python/lesson-6#hometask


class Human:
    default_name: str = "Неизвестный"
    default_age: int = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(
            f"Имя: {self.name} Возраст: {self.age} "
            f"Баланс: {self.__money} Дом: {self.__house}"
        )

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def __make_deal(self, house_obj, price):
        self.__money = self.__money - price
        self.__house = house_obj

    def earn_money(self, amount):
        self.__money = self.__money + amount


Human.default_info()
