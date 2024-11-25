from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    answer = 0
    left = 0
    right = 0
    number_flips = 0
    count = 0
    while left < len(nums) and right < len(nums):
        if count == 0:
            right = left
        while right < len(nums) and (nums[right] == 1 or number_flips < k):
            if nums[right] == 0:
                number_flips += 1
            right += 1
            count += 1
        if count > answer:
            answer = count
        if nums[left] == 0 and number_flips > 0:
            number_flips -= 1
            count -= 1
        if nums[left] == 1:
            count -= 1
        left += 1

    return answer
