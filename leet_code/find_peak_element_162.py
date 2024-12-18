from typing import List, Optional


def _search(nums: List[int], left: int, right: int) -> Optional[int]:
    if left == right and (nums[left - 1] < nums[left] < nums[left + 1]):
        return left
    middle = (left + right) // 2

    if middle == 0 and nums[middle] > nums[middle + 1]:
        return middle
    elif middle == len(nums) - 1 and nums[middle] > nums[middle - 1]:
        return middle

    if nums[middle - 1] < nums[middle] > nums[middle + 1]:
        return middle
    elif nums[middle - 1] > nums[middle]:
        return _search(nums, left, middle)
    elif nums[middle] < nums[middle + 1]:
        return _search(nums, middle + 1, right)


def find_peak_element(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    elif len(nums) == 2:
        if nums[0] > nums[1]:
            return 0
        else:
            return 1
    return _search(nums, 0, len(nums))
