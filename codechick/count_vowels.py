# https://codechick.io/challenges/320


def count_vowels(txt: str):
    vowels: str = 'aeiou'
    count: int = 0
    for char in txt:
        if char.lower() in vowels:
            count += 1

    return count


print(count_vowels("Celebration"))
print(count_vowels("Palm"))
print(count_vowels("Prediction"))
