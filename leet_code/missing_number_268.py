from typing import List


def missing_number(nums: List[int]) -> int:
    array_sum = sum(nums)
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    return expected_sum - array_sum
