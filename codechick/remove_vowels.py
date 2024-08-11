# https://codechick.io/challenges/357


def remove_vowels(txt):
    vowels: str = "aeiou"
    result: str = ""
    for char in txt:
        if char.lower() not in vowels:
            result += char
    return result
