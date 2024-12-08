class BaseCar:
    WHEELS: int = 4


class BigCar(BaseCar):
    WHEELS: int = 6

    @classmethod
    def change_wheels(cls, new_value: int) -> None:
        cls.WHEELS = new_value


if __name__ == "__main__":
    big_1 = BigCar()
    print(big_1.WHEELS)

    big_1.change_wheels(8)
    print(big_1.WHEELS)
