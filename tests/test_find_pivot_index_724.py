from leet_code.find_pivot_index_724 import Solution

from pytest import mark


@mark.parametrize("nums, expected", [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0)
])
def test_pivot_index(nums, expected):
    solution = Solution()
    output = solution.pivot_index(nums)
    assert output == expected
