from typing import List


def max_operations(nums: List[int], k: int) -> int:
    sorted_nums = sorted(nums)
    number_of_operations = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        result = sorted_nums[left] + sorted_nums[right]
        if result > k:
            right -= 1
        elif result < k:
            left += 1
        else:
            number_of_operations += 1
            left += 1
            right -= 1

    return number_of_operations
