from typing import List


def _search(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            first = middle
            second = middle
            while first >= 0 and target == nums[first]:
                first -= 1
            while second < len(nums) and target == nums[second]:
                second += 1
            return [first + 1, second - 1]
        elif target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return [-1, -1]


def search_range(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]
    elif len(nums) == 1 and nums[0] == target:
        return [0, 0]
    return _search(nums, target)
