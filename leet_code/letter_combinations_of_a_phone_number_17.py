from typing import List

class Solution:
    def __init__(self):
        self.__digit_letters_mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                                        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    def __backtracking(self, digits: str, index: int) -> List[str]:
        if index == len(digits) - 1:
            letters = self.__digit_letters_mapping[digits[index]]
            return [letter for letter in letters]
        current_combination = self.__backtracking(digits, index+1)
        letters = self.__digit_letters_mapping[digits[index]]
        new_combination = []
        for letter in letters:
            for combination in current_combination:
                new_combination.append(letter+combination)
        return new_combination

    def letter_combinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return self.__backtracking(digits, 0)
