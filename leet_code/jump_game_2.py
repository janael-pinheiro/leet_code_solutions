from typing import List


def jump(nums: List[int]) -> int:
    length = len(nums)
    if length == 1:
        return 0
    jumps = 0
    index = 0
    while index < length:
        current = nums[index]
        if index + current >= length - 1:
            return jumps + 1

        current_index = 1
        distance = 0
        best_distance = (10 ** 4) + 1
        while current_index <= current:
            current_distance = length - (index + current_index + nums[index + current_index])
            if current_distance <= best_distance:
                best_distance = current_distance
                distance = current_index
            current_index += 1
        index += distance
        jumps += 1

    return jumps
