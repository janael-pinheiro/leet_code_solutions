from typing import List


def compute_prefix(nums: List[int]) -> List[int]:
    cumulative = 1
    index = 0
    result = []
    while index < len(nums):
        cumulative *= nums[index]
        result.append(cumulative)
        index += 1
    return result


def compute_suffix(nums: List[int]) -> List[int]:
    cumulative = 1
    index = len(nums) - 1
    result = [0 for _ in range(len(nums))]
    while index >= 0:
        cumulative *= nums[index]
        result[index] = cumulative
        index -= 1
    return result


def product_except_self(nums: List[int]) -> List[int]:
    prefix_array = compute_prefix(nums)
    suffix_array = compute_suffix(nums)

    result = []
    index = 0
    while index < len(nums):
        if index == 0:
            result.append(suffix_array[index + 1])
        elif index == len(nums) - 1:
            result.append(prefix_array[len(nums) - 2])
        else:
            result.append(prefix_array[index - 1] * suffix_array[index + 1])
        index += 1
    return result
