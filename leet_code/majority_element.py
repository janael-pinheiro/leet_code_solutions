from typing import List


def majority_element(nums: List[int]):
    n = len(nums)
    majority_threshold = n / 2
    counter = {}
    index = 0
    response = 0
    while index < n:
        value = nums[index]
        count = counter.get(value, 0)
        counter[value] = count + 1
        if counter[value] > majority_threshold:
            response = value
            break
        index += 1
    return response
