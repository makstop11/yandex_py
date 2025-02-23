def check_num(number: int) -> None:
    if 37 <= number <= 54 and number % 2 == 0 and number % 2 != 0:
        print('Боковое место')
    elif number % 2 == 0 and number < 37:
        print('Нижнее место')
    elif number % 2 != 0 and number < 37:
        print('Верхнее место')


if __name__ == "__main__":
    number: int = int(input())
    print(check_num(number))
