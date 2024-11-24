from typing import List


def sum_odd_length_sub_arrays(arr: List[int]) -> int:
    window_length = 1
    total = 0
    while window_length <= len(arr):
        index = 0
        while index + window_length <= len(arr):
            total += sum(arr[index:index + window_length])
            index += 1
        window_length += 2
    return total
