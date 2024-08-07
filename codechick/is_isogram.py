def is_isogram(word):
    data = word.lower()
    for i in data:
        if data.count(i) > 1:
            return False
    return True

# https://codechick.io/challenges/409
