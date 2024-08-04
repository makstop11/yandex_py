def add_odd_to_n(n):
    count = 0
    for i in range(n + 1):
        if i % 2 == 0:
            count = count
        else:
            count += i
    return count

# https://codechick.io/challenges/194
