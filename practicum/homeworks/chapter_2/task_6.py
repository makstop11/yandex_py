def check_num(number: int) -> str:
    if number > 0:
        return 'Положительное число'
    elif number < 0:
        return 'Отрицательное число'
    return 'Ноль'


if __name__ == '__main__':
    num: int = int(input())
    print(check_num(num))
