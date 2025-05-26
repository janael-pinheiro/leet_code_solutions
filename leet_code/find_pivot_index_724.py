from typing import List


class Solution:
    def __build_prefix_sum_array(self, nums):
        prefix_sum = []
        current = 0
        index = 0
        while index < len(nums):
            current += nums[index]
            prefix_sum.append(current)
            index += 1
        return prefix_sum

    def pivot_index(self, nums: List[int]) -> int:
        prefix_sum_array = self.__build_prefix_sum_array(nums)
        total_sum = prefix_sum_array[len(nums)-1]
        if total_sum == prefix_sum_array[0]:
            return 0

        index = 0
        while index < len(nums) - 1:
            diff = total_sum - prefix_sum_array[index]
            if diff == prefix_sum_array[index+1]:
                return index + 1
            index += 1
        return -1
