from leet_code.find_the_duplicate_number_287 import Solution

from pytest import mark


@mark.parametrize("nums, expected", [
    ([3, 1, 3, 4, 2], 3),
    ([1, 3, 4, 2, 2], 2),
    ([3, 3, 3, 3, 3], 3)
])
def test_find_duplicate(nums, expected):
    solution = Solution()
    output = solution.find_duplicate(nums)
    assert expected == output
