from typing import List


class Solution:
    def count_consistent_strings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            unique_characters = set(word)
            if unique_characters.issubset(set(allowed)):
                count += 1
        return count
