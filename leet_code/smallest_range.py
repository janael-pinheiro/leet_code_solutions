from typing import List


def smallest_range(nums: List[int], k: int) -> int:
    smallest = 10 ** 4 + 1
    biggest = -1
    index = 0
    while index < len(nums):
        if nums[index] < smallest:
            smallest = nums[index]
        if nums[index] > biggest:
            biggest = nums[index]
        index += 1
    difference = biggest - smallest
    if difference > k:
        smallest += k
        new_difference = biggest - smallest
        if new_difference <= k:
            biggest -= new_difference
        else:
            biggest -= k
    else:
        smallest += difference
    return biggest - smallest
