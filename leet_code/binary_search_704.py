from typing import List


class Solution:
    def __binary_search(self, nums: List[int], target: int, left: int, right: int):
        response = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                response = middle
                break
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return response

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.__binary_search(nums, target, left, right)
