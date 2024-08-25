from typing import List


def remove_duplicates(nums: List[int]):
    count = 1
    index = 1
    n = len(nums)
    while index < n:
        if nums[index] == nums[index - 1]:
            nums.pop(index)
            n -= 1
        else:
            count += 1
            index += 1
    return count

