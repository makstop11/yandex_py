# https://codechick.io/challenges/312

def halloween(dt: str) -> str:
    dt: list[str] = dt.split("/")
    day: str = "31"
    month: str = "10"

    if dt[-1] == day and dt[-2] == month:
        return "Bonfire toffee"
    else:
        return "toffee"


if __name__ == '__main__':
    print(halloween("2013/10/31"))
    print(halloween("2012/07/31"))
    print(halloween("2011/10/12"))
