from typing import List
from string import digits


class Solution:
    def __backtracking(self, letters: List[str], index: int, output: List[str]):
        if index == len(letters):
            output.append("".join(letters))
            return

        if letters[index] in digits:
            self.__backtracking(letters, index+1, output)
            return

        upper_letters = list(letters)
        upper_letters[index] = upper_letters[index].upper()

        lower_letters = list(letters)
        lower_letters[index] = lower_letters[index].lower()

        self.__backtracking(upper_letters, index+1, output)
        self.__backtracking(lower_letters, index+1, output)

    def letter_case_permutation(self, s: str) -> List[str]:
        output = []
        letters = [x for x in s]
        self.__backtracking(letters, 0, output)
        return output
