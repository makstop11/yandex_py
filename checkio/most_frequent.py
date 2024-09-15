def most_frequent(data: list[str]):
    max_count: int = 0
    max_char: str = ""

    for elem in data:
        temp: int = data.count(elem)
        if temp > max_count:
            max_count = temp
            max_char = elem
    return max_char


if __name__ == "__main__":
    chars = ["a", "b", "c", "a", "b", "a"]
    print(most_frequent(chars))

    # These "asserts" are used for self-checking
    # assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    # assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

    # print("The mission is done! Click 'Check Solution' to earn rewards!")




# №2
# def most_frequent(data: list[str]):
#     frequency: dict[str, int] = {}
#     for char in data:
#         if char in frequency:
#             # frequency[char] += 1
#             frequency[char] = frequency.get(char) + 1
#         else:
#             frequency[char] = 1
#
#     return sorted(frequency.items(), key=lambda elem: elem[1], reverse=True)
