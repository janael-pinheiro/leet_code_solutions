from pytest import mark

from leet_code.binary_search_704 import Solution


@mark.parametrize("nums, target, expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1)
])
def test_search(nums, target, expected):
    solution = Solution()
    output = solution.search(nums, target)
    assert expected == output
