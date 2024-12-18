from typing import List


def can_jump(nums: List[int]) -> bool:
    length = len(nums) - 1
    count = length
    last_reachable = length
    reachable = False
    while count >= 0:
        if count + nums[count] >= last_reachable:
            reachable = True
            last_reachable = count
        else:
            reachable = False
        count -= 1
    return reachable

