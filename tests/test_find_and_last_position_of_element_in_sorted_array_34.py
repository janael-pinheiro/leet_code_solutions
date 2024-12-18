from pytest import mark

from leet_code.find_first_and_last_position_of_element_in_sorted_array_34 import search_range


@mark.parametrize("nums, target, expected", [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1])
])
def test_search_range(nums, target, expected):
    output = search_range(nums, target)
    assert expected == output
