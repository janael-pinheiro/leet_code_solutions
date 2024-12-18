from typing import List


def rotate(nums: List[int], k: int) -> None:
    if k == 0:
        return
    length = len(nums)
    count = 0
    i = 0
    already_seen_indexes = {}
    while count < length:
        index = i
        previous = nums[i]
        while index not in already_seen_indexes:
            new_index = (index + k) % length
            temp = nums[new_index]
            nums[new_index] = previous
            previous = temp
            count += 1
            already_seen_indexes[index] = True
            index = new_index
        i += 1
