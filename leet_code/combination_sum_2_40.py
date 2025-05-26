from typing import List


class Solution:
    def __backtracking(self, candidates: List[int], target: int, subset, output, index):
        if index == len(candidates):
            return

        for i in range(index, len(candidates)):
            candidate = candidates[i]
            subset2 = list(subset)
            subset2.append(candidate)
            subset_sum = sum(subset2)
            if subset_sum > target:
                return
            elif subset_sum == target:
                output.append(subset2)
                return
            else:
                self.__backtracking(candidates, target, subset2, output, i + 1)

    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        self.__backtracking(candidates, target, [], output, 0)
        return output
