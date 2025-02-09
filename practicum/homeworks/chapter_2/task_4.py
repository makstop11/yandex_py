def check_num(num: int) -> str:
    if num % 10 == 0 and num % 2 == 0:
        return "ДА"
    return "НЕТ"


if __name__ == "__main__":
    number: int = int(input())
    print(check_num(number))
