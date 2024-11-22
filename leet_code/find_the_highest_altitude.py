from typing import List


def largest_altitude(gain: List[int]) -> int:
    prefix_sum = 0
    result = 0
    index = 0
    while index < len(gain):
        prefix_sum += gain[index]
        if prefix_sum > result:
            result = prefix_sum
        index += 1
    return result
