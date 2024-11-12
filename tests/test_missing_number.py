from leet_code.missing_number import missing_number
from pytest import mark


@mark.parametrize("nums, expected", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
])
def test_missing_number(nums, expected):
    output = missing_number(nums)
    assert expected == output
