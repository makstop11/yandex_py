def is_valid_PIN(pin):
    if pin.isdigit():
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False

# https://codechick.io/challenges/343
