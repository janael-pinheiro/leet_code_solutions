from leet_code.permutations_46 import Solution
from pytest import mark


@mark.parametrize("nums, expected", [
    ([1, 2, 3], [[1, 2, 3],[1, 3, 2],[2, 1, 3],[2, 3, 1],[3, 1, 2],[3, 2, 1]]),
    ([0, 1], [[0, 1],[1, 0]]),
    ([1], [[1]])
])
def test_permute(nums, expected):
    solution = Solution()
    output = solution.permute(nums)
    assert expected == output
