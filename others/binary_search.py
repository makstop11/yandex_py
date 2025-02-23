nums: list[int] = [12, 19, 21, 36, 47, 75, 77, 84, 92, 95, 97]
target: int = 21

length: int = len(nums)

left: int = 0
right: int = length - 1

middle = (left + right) // 2

if target > nums[middle]:
    left = middle + 1
    middle = (right + left) // 2
    left = middle + 1
elif target < nums[middle]:
    right = middle - 1
    middle = (right + left) // 2
    left = middle - 1
else:
    print(middle)

print(middle)
