# https://codechick.io/challenges/537

def remove_empty_arrays(arr):
    return [item for item in arr if item != []]


print(remove_empty_arrays(
    ["a", 10, 0, "", "b", [], [], [1, 2, 3]]
))
