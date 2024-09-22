from typing import List


def min_subarray_sum(target: int, nums: List[int]) -> int:
    left = 0
    right = 0
    maximum_length = (10 ** 5) + 1
    minimum_length = (10 ** 5) + 1
    accumulated_sum = 0
    while left < len(nums) and right < len(nums):
        accumulated_sum += nums[right]
        if accumulated_sum >= target:
            length = (right - left) + 1
            if length == 1:
                print(right)
                print(left)
                return length
            elif length < minimum_length:
                minimum_length = length
            accumulated_sum -= nums[left]
            accumulated_sum -= nums[right]
            left += 1
        else:
            right += 1
    if minimum_length < maximum_length:
        return minimum_length
    else:
        return 0
