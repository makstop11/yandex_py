class Line:
    def __init__(self, coords, width, color):
        pass

    def draw(self):
        pass


class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def about_me(self):
        print(
            f"\nПорода: {self.breed}"
            f"\nКличка: {self.name}"
            f"\nВозраст: {self.age}"
        )

    def stand_on_hind_legs(self):
        print(f"Стою на задних лапах! [{self.name}]")


vaska = Cat("Бурма", "Васька", 3)
krasik = Cat("Саванна", "Красик", 5)
rijik = Cat("Русская", "Рыжик", 2)

print(krasik.name)

rijik.about_me()
vaska.about_me()

vaska.stand_on_hind_legs()
krasik.stand_on_hind_legs()
