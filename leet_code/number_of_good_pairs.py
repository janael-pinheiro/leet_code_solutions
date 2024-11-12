from typing import List


def num_identical_pairs(nums: List[int]) -> int:
    left = 0
    pairs = 0
    while left < len(nums) - 1:
        right = left + 1
        while right < len(nums):
            if nums[left] == nums[right]:
                pairs += 1
            right += 1
        left += 1
    return pairs
