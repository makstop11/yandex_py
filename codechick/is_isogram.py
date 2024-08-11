# https://codechick.io/challenges/409


def is_isogram(word):
    word = word.lower()
    length: int = len(word)

    for i in range(length):
        for j in range(i + 1, length):
            if word[i] == word[j]:
                return False
    return True
