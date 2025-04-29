from typing import List


class Solution:
    def find_duplicate(self, nums: List[int]) -> int:
        found_values = [0 for _ in range(len(nums))]
        for num in nums:
            if found_values[num]:
                return num
            found_values[num] = 1
