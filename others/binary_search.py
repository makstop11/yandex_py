def binary_search(nums: list[int], target: int) -> int:
    length: int = len(nums)

    left: int = 0
    right: int = length - 1
    while left < right:
        middle: int = (left + right) // 2

        if target == nums[middle]:
            return middle

        if target > nums[middle]:
            left = middle + 1
        elif target < nums[middle]:
            right = middle - 1


if __name__ == "__main__":
    nums = [12, 19, 21, 36, 47, 75, 77, 84, 92, 95, 97]
    target = 21
    print(binary_search(nums, target))  # 2
