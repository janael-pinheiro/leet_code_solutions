import sys
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    elements = set(nums)
    longest = sys.maxsize * -1
    index = 0
    while index < len(nums):
        if nums[index] + 1 in elements and nums[index] - 1 not in elements:
            sequence_length = 0
            current = nums[index]
            while current in elements:
                sequence_length += 1
                current += 1
            if sequence_length > longest:
                longest = sequence_length
        index += 1
    if longest == sys.maxsize * -1:
        return 1
    return longest
