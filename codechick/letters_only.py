def letters_only(txt):
    s = []
    for i in txt:
        if i.isalpha():
            s.append(i)
    return "".join(s)

#  https://codechick.io/challenges/375
