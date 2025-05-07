from typing import List


class Solution:
    def __backtracking(
            self,
            candidates: List[int],
            target: int,
            index: int,
            subset: List[int],
            output: List[List[int]]):
        if index == len(candidates):
            return

        for i in range(index, len(candidates)):
            candidate = candidates[i]
            repeat = target // candidate
            j = 1
            while j <= repeat:
                subset2 = list(subset)
                subset2.extend([candidate] * j)
                subset_sum = sum(subset2)
                if subset_sum == target:
                    output.append(subset2)
                    break
                elif subset_sum > target:
                    break
                else:
                    self.__backtracking(candidates, target, i+1, subset2, output)
                j += 1

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        self.__backtracking(candidates, target, 0, [], output)
        return output
