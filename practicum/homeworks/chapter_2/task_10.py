def check_num(number: int) -> None:
    if number % 2 != 0:
        print('Невозможно разминять')
    elif number % 500 == 0:
        print('Купюр по 500: ', number / 500)
    elif number % 100 == 0:
        print('Купюр ро 100: ', number / 100)
    elif number % 10 == 0:
        print('Купюр ро 10: ', number / 10)
    elif number % 2 == 0:
        print('Купюр ро 2: ', number / 2)


if __name__ == "__main__":
    number: int = int(input())
    print(check_num(number))
