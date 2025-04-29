from typing import List


class Solution:
    def find_duplicate(self, nums: List[int]) -> int:
        found_values = set()
        for num in nums:
            if num in found_values:
                return num
            found_values.add(num)
