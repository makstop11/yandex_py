def say_cat_name(name: str, color: str, age: int) -> str:
    template: str = (f"\nКличка: {name}"
                     f"\nОкраска: {color}"
                     f"\nВозраст: {age}")

    return template


def two_sum(a: int, b: int) -> int:
    return a + b


class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age



if __name__ == "__main__":
    print(two_sum(5, 10))
    print(two_sum(b=5, a=10))

    print(
        say_cat_name(name="Барсик", color="рыжий", age=2)
    )

    vaska = Cat("Бурма", "Васька", 3)
    krasik = Cat("Саванна", "Красик", 5)
    rijik = Cat("Русская", "Рыжик", 2)
