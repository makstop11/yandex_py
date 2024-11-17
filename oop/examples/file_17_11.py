class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    @staticmethod
    def calc_cat_age_by_human(cat_age: int) -> int:
        first_year: int = 15
        second_year: int = 10
        other_year: int = 4

        if cat_age == 1:
            return first_year
        if cat_age == 2:
            return second_year

        return (cat_age - 2) * other_year + (first_year + second_year)


if __name__ == "__main__":
    vaska = Cat("Бурма", "Васька", 3)
    krasik = Cat("Саванна", "Красик", 5)
    rijik = Cat("Русская", "Рыжик", 2)

    print("Возраст:", Cat.calc_cat_age_by_human(vaska.age))
