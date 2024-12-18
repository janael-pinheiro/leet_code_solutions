from leet_code.contains_duplicate_217 import contains_duplicate
from pytest import mark


@mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
])
def test_contains_duplicate(nums, expected):
    output = contains_duplicate(nums)
    assert expected == output
