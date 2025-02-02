# number: int = int(input())
#
# if number % 5 == 0 and number % 2 != 0:
#     print('Да')
# else:
#     print('Нет')

def check_num(num: int) -> str:
    if num % 5 == 0 and num % 2 != 0:
        return "ДА"
    else:
        return "НЕТ"


if __name__ == "__main__":
    number: int = int(input())
    print(check_num(number))
