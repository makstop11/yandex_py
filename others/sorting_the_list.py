nums: list[int] = [23, 42, 4, 16, 8, 15]

length: int = len(nums)

for i in range(length):
    curr_min: int = i
    for j in range(i + 1, length):
        if nums[j] < nums[curr_min]:
            curr_min = j
    if curr_min != i:
        # a, b = b, a
        nums[curr_min], nums[i] = nums[i], nums[curr_min]


def selection_sort(arr: list[int]) -> None:
    pass


if __name__ == "__main__":
    selection_sort(nums)
    print(nums)  # [4, 8, 15, 16, 23, 42]
