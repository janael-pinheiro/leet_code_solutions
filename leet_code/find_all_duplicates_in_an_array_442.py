from typing import List


class Solution:
    def find_duplicates(self, nums: List[int]) -> List[int]:
        found = set()
        result = []
        for num in nums:
            if num in found:
                result.append(num)
            found.add(num)
        return result
