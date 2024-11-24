from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    numbers_mapping = {}
    index = 0
    while index < len(nums):
        if nums[index] in numbers_mapping:
            if abs(numbers_mapping[nums[index]] - index) <= k:
                return True
        numbers_mapping[nums[index]] = index
        index += 1
    return False
