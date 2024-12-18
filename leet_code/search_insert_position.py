from typing import List


def search_insert(nums: List[int], target: int) -> int:
    length = len(nums)
    if length == 0 or target < nums[0]:
        return 0
    left = 0
    right = length - 1
    middle = 0
    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1
    if target > nums[middle]:
        return middle + 1
    else:
        return middle

