from leet_code.contains_duplicate_2 import contains_nearby_duplicate
from pytest import mark


@mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 1], 3, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False)
])
def test_contains_nearby_duplicate(nums, k, expected):
    output = contains_nearby_duplicate(nums, k)
    assert output == expected
