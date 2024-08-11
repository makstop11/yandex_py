# https://codechick.io/challenges/343


def is_valid_PIN(pin):
    if pin.isdigit():
        # length: int = len(pin)
        # if length == 4 or length == 6:
        if len(pin) in [4, 6]:
            return True
        else:
            return False
    else:
        return False


# После рефакторинга
def is_valid_PIN_2(pin):
    return pin.isdigit() and len(pin) in [4, 6]
