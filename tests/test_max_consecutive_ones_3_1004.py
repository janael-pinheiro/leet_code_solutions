from pytest import mark

from leet_code.max_consecutive_ones_3_1004 import longest_ones


@mark.parametrize("nums, k, expected", [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10)
])
def test_longest_ones(nums, k, expected):
    output = longest_ones(nums, k)
    assert expected == output
