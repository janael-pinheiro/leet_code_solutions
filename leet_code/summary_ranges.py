from typing import List


def summary_ranges(nums: List[int]) -> List[str]:
    response = []
    index = 0
    n = len(nums)
    while index < n:
        start = nums[index]
        while index < n - 1 and (nums[index+1] - nums[index]) == 1:
            index += 1
        if start != nums[index]:
            response.append(f"{start}->{nums[index]}")
        else:
            response.append(f"{start}")
        index += 1
    return response
