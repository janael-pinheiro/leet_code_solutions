from typing import List


class Solution:
    def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
        output = set([num for num in range(1, len(nums)+1)]).difference(set(nums))
        return list(output)
