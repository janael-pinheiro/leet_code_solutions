from typing import List


class Solution:
    def restore_string(self, s: str, indices: List[int]) -> str:
        shuffled_string = ["" for _ in range(len(s))]
        for index, letter in enumerate(s):
            idx = indices[index]
            shuffled_string[idx] = letter

        return "".join(shuffled_string)
