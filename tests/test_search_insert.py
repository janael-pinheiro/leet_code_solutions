from leet_code.search_insert_position import search_insert
from pytest import mark


@mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([], 1, 0),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1, 3], 2, 1)
])
def test_search_insert(nums, target, expected):
    output = search_insert(nums, target)
    assert output == expected
