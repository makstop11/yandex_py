def remove_vowels(txt):
    n = "AEIOUaeiou"
    s = ""
    for x in txt:
        if x not in n:
            s += x
    return s

# https://codechick.io/challenges/357
