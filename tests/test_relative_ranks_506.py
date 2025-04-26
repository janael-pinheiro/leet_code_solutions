from leet_code.relative_ranks_506 import Solution

from pytest import mark


@mark.parametrize("score, expected", [
    ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
    ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"])
])
def test_find_relative_ranks(score, expected):
    solution = Solution()
    output = solution.find_relative_ranks(score)
    assert expected == output
