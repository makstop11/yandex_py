def check_num(number: int):
    if number > 0:
        print('Положительное число')
    elif number < 0:
        print('Отрицательное число')
    else:
        print('Ноль')


if __name__ == "__main__":
    number: int = int(input())
    print(check_num(number))
