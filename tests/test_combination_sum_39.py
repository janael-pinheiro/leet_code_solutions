from leet_code.combination_sum_39 import Solution

from pytest import mark


@mark.parametrize("candidates, target, expected", [
    ([3, 5, 8], 11, [[3, 8], [3, 3, 5]]),
    ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
    ([2, 3, 5], 8, [[2, 3, 3], [2, 2, 2, 2], [3, 5]]),
    ([2], 1, [])
])
def test_combination_sum(candidates, target, expected):
    solution = Solution()
    output = solution.combination_sum(candidates, target)
    assert expected == output
