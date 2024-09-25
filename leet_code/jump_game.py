from typing import List


def can_jump(nums: List[int]) -> bool:
    if nums[0] == 0 and len(nums) == 1:
        return True
    elif nums[0] == 0:
        return False
    index = 0
    while index < len(nums):
        maximum_jump_length = nums[index]
        next_index = index + maximum_jump_length
        if next_index == len(nums) - 1:
            return True
        while next_index < len(nums) - 1 and nums[next_index] == 0 and maximum_jump_length > 0:
            maximum_jump_length -= 1
            next_index = index + maximum_jump_length
        if maximum_jump_length == 0:
            return False
        index += next_index
    return True
