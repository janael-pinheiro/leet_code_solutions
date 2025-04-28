from typing import List


class Solution:
    def __permute_backtracking(self, index, nums, output):
        if index == len(nums):
            output.append(nums)
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.__permute_backtracking(index + 1, list(nums), output)

    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.__permute_backtracking(0, list(nums), output)
        return output
