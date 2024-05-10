from math import gcd

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

curr_gcd = nums[0]
for i in range(1, len(nums)):
    curr_gcd = gcd(curr_gcd, nums[i])

print(curr_gcd)
