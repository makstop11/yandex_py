l: list[int] = [23, 42, 4, 16, 8, 15]

lens = len(l)

for i in range(len(l) - 1):
    m = 0
    for j in range(i + 1):
        if l[j] < l[m]:
            m = j
    if m != i:
        ...
