from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 1 and nums[0] == target:
        return 0
    elif len(nums) == 1 and nums[0] != target:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] <= nums[right]:
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        elif nums[left] <= nums[middle]:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return -1
