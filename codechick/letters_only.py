#  https://codechick.io/challenges/375


def letters_only(txt):
    result: str = ""
    for char in txt:
        if char.isalpha():
            result += char

    return result
