from leet_code.sort_colors_75 import sort_colors

from pytest import mark


@mark.parametrize("nums, expected", [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([2, 0, 1], [0, 1, 2])
])
def test_sort_colors(nums, expected):
    sort_colors(nums)
    assert nums == expected
