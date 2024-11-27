from typing import List


def longest_subarray(nums: List[int]) -> int:
    response = 0
    left = 0
    right = 0
    zero_count = 0
    count = 0
    n = len(nums)
    while left < n and right < n:
        while right < n and zero_count <= 1:
            if nums[right] == 0 and zero_count == 1:
                break
            count += 1
            if count > response:
                response = count
            if nums[right] == 0:
                zero_count += 1
            right += 1
        if nums[left] == 0 and zero_count > 0:
            zero_count -= 1
            count -= 1
        if nums[left] == 1:
            count -= 1
        left += 1
    return response - 1
