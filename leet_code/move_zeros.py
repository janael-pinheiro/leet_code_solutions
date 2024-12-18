from typing import List


def move_zeros(nums: List[int]) -> None:
    left = 0
    right = len(nums)
    number_zeros = 0
    while left < len(nums):
        while nums[left] == 0 and left < len(nums) - number_zeros:
            nums.insert(right, nums[left])
            nums.pop(left)
            number_zeros += 1
        left += 1
