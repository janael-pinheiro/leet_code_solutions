from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    maximum_average_value = -10 ** 5
    last = 0
    index = 0
    summation = sum(nums[index:index + (k - 1)])
    while index + k <= len(nums):
        summation = (summation - last) + nums[index + (k - 1)]
        print(summation)
        average = summation / k
        if average > maximum_average_value:
            maximum_average_value = average
        last = nums[index]
        index += 1
    return maximum_average_value
