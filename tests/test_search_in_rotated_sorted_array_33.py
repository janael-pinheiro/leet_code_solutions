from leet_code.search_in_rotated_sorted_array_33 import search

from pytest import mark


@mark.parametrize("nums, target, expected", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([1], 0, -1),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([3, 5, 1], 3, 0)
])
def test_search(nums, target, expected):
    output = search(nums, target)
    assert expected == output
