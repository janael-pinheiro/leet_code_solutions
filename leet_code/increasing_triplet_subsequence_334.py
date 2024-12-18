import sys
from typing import List


def increasing_triplet(nums: List[int]) -> bool:
    min1 = sys.maxsize
    min2 = sys.maxsize
    index = 0
    while index < len(nums):
        if nums[index] <= min1:
            min1 = nums[index]
        elif nums[index] <= min2:
            min2 = nums[index]
        else:
            return True
        index += 1
    return False
