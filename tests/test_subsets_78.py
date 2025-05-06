from pytest import mark

from leet_code.subsets_78 import Solution


@mark.parametrize("nums, expected", [
    ([1, 2, 3], [[], [1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3]]),
    ([0], [[], [0]]),
    ([-1, 1], [[], [-1, 1], [-1], [1]])
])
def test_subsets(nums, expected):
    solution = Solution()
    output = solution.subsets(nums)
    assert expected == output

