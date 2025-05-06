from typing import List


class Solution:
    def __backtracking_subsets(self, nums, index, subset, output):
        if index == len(nums):
            return

        for i in range(index, len(nums)):
            current_subset = list(subset)
            current_subset.append(nums[i])
            self.__backtracking_subsets(nums, i+1, current_subset, output)
            output.append(current_subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        self.__backtracking_subsets(nums, 0, [], output)
        return output
