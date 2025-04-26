from typing import List


class Solution:
    def find_relative_ranks(self, score: List[int]) -> List[str]:
        sorted_values = sorted(score, reverse=True)
        rank = {sorted_values[0]: "Gold Medal"}
        number_athletes = len(score)
        if number_athletes > 1:
            rank.update({sorted_values[1]: "Silver Medal"})
        if number_athletes > 2:
            rank.update({sorted_values[2]: "Bronze Medal"})
        if number_athletes > 3:
            rank.update({value: str(index) for index, value in enumerate(sorted_values[3:], start=4)})
        result = []
        for s in score:
            result.append(rank[s])
        return result
